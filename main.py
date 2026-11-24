import csv
import sys
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QMessageBox,
    QTableWidgetItem,
    QVBoxLayout,
)
from ui_ventana_principal import Ui_MainWindow
from metodo.biseccion import biseccion, busqueda_incremental
from metodo.graficas import (
    LienzoGrafica,
    graficar_error,
    graficar_funcion,
    graficar_funcion_previa,
)


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ultimo_resultado = None

        # Barra de estado con datos del equipo
        self.ui.statusbar.showMessage(
            "Cálculo Numérico (MECATR24) | Proyecto B: Bisección | Grupo 4 (4 integrantes)"
        )

        # Configurar lienzos de Matplotlib dentro de las pestañas
        self.canvas_func = LienzoGrafica()
        QVBoxLayout(self.ui.widgetGraficaFuncion).addWidget(self.canvas_func)

        self.canvas_err = LienzoGrafica()
        QVBoxLayout(self.ui.widgetGraficaError).addWidget(self.canvas_err)

        # Configurar encabezados de la tabla
        columnas = ["i", "xl", "xu", "xr", "f(xl)", "f(xr)", "f(xl)·f(xr)", "εa (%)", "εt (%)", "Subintervalo"]
        self.ui.tablaResultados.setColumnCount(len(columnas))
        self.ui.tablaResultados.setHorizontalHeaderLabels(columnas)

        # Conectar señales
        self.ui.cmbEjemplos.currentIndexChanged.connect(self.cargar_ejemplo)
        self.ui.btnCalcular.clicked.connect(self.calcular)
        self.ui.btnBuscarIntervalos.clicked.connect(self.buscar_intervalos)
        self.ui.btnLimpiar.clicked.connect(self.limpiar)
        self.ui.btnExportar.clicked.connect(self.exportar_csv)

        # Precargar caso obligatorio del Grupo 4 al iniciar
        self.cargar_ejemplo(0)

    def cargar_ejemplo(self, index: int):
        if index == 0:
            # Caso obligatorio Grupo 4: Punto de operación de un diodo
            self.ui.txtFuncion.setText("1e-12*(exp(x/0.02585) - 1) - (5 - x)/1000")
            self.ui.spnXl.setValue(0.0)
            self.ui.spnXu.setValue(1.0)
            self.ui.spnEs.setValue(0.01)
            self.ui.spnMaxIter.setValue(100)
            self.ui.txtValorVerdadero.setText("0.574147")
            self.ui.txtUnidades.setText("V")
            self.ui.spnPasoDx.setValue(0.1)
        elif index == 1:
            # Ejemplo del libro (Chapra Cap. 5): Paracaidista
            self.ui.txtFuncion.setText("(9.81*68.1/x)*(1 - exp(-(x/68.1)*10)) - 40")
            self.ui.spnXl.setValue(12.0)
            self.ui.spnXu.setValue(20.0)
            self.ui.spnEs.setValue(0.5)
            self.ui.spnMaxIter.setValue(100)
            self.ui.txtValorVerdadero.setText("14.8011")
            self.ui.txtUnidades.setText("kg/s")
            self.ui.spnPasoDx.setValue(1.0)
        else:
            # Ejemplo clásico: f(x) = exp(-x) - x
            self.ui.txtFuncion.setText("exp(-x) - x")
            self.ui.spnXl.setValue(0.0)
            self.ui.spnXu.setValue(1.0)
            self.ui.spnEs.setValue(0.5)
            self.ui.spnMaxIter.setValue(100)
            self.ui.txtValorVerdadero.setText("0.567143")
            self.ui.txtUnidades.setText("")
            self.ui.spnPasoDx.setValue(0.1)

    def buscar_intervalos(self):
        try:
            expr = self.ui.txtFuncion.text().strip()
            xl = self.ui.spnXl.value()
            xu = self.ui.spnXu.value()
            dx = self.ui.spnPasoDx.value()

            intervalos = busqueda_incremental(expr, xl, xu, dx)
            graficar_funcion_previa(self.canvas_func, expr, xl, xu, intervalos)
            self.ui.tabGraficas.setCurrentIndex(0)

            if not intervalos:
                QMessageBox.information(
                    self,
                    "Búsqueda incremental",
                    f"No se detectaron cambios de signo en [{xl}, {xu}] con paso Δx = {dx}.",
                )
                return

            lista_str = "\n".join(f"• [{a:.6f}, {b:.6f}]" for a, b in intervalos)
            QMessageBox.information(
                self,
                "Intervalos sugeridos",
                f"Se encontraron cambios de signo en:\n{lista_str}\n\nSe cargará el primer subintervalo encontrado.",
            )
            self.ui.spnXl.setValue(intervalos[0][0])
            self.ui.spnXu.setValue(intervalos[0][1])
        except Exception as exc:
            QMessageBox.warning(self, "Error en búsqueda incremental", str(exc))

    def calcular(self):
        try:
            expr = self.ui.txtFuncion.text().strip()
            xl = self.ui.spnXl.value()
            xu = self.ui.spnXu.value()
            es = self.ui.spnEs.value()
            max_iter = self.ui.spnMaxIter.value()
            unidades = self.ui.txtUnidades.text().strip()

            vv_texto = self.ui.txtValorVerdadero.text().strip()
            valor_verdadero = float(vv_texto) if vv_texto else None

            res = biseccion(expr, xl, xu, es, max_iter, valor_verdadero)
            self.ultimo_resultado = res

            # Llenar tabla (6 a 9 decimales y errores en %)
            tabla = res["tabla"]
            self.ui.tablaResultados.setRowCount(len(tabla))
            for row_idx, fila in enumerate(tabla):
                ea_txt = f"{fila['ea']:.6f}%" if fila["ea"] is not None else "---"
                et_txt = f"{fila['et']:.6f}%" if fila["et"] is not None else "---"
                valores = [
                    str(fila["i"]),
                    f"{fila['xl']:.6f}",
                    f"{fila['xu']:.6f}",
                    f"{fila['xr']:.6f}",
                    f"{fila['f_xl']:.6e}",
                    f"{fila['f_xr']:.6e}",
                    f"{fila['producto']:.6e}",
                    ea_txt,
                    et_txt,
                    fila["subintervalo"],
                ]
                for col_idx, texto in enumerate(valores):
                    self.ui.tablaResultados.setItem(row_idx, col_idx, QTableWidgetItem(texto))

            self.ui.tablaResultados.resizeColumnsToContents()

            # Mostrar resumen
            ea_final = f"{res['ea_final']:.6f}%" if res["ea_final"] is not None else "N/A"
            et_final = f"{res['et_final']:.6f}%" if res["et_final"] is not None else "N/A"
            unidad_str = f" {unidades}" if unidades else ""

            resumen = (
                f"Raíz aproximada: {res['raiz']:.6f}{unidad_str}\n"
                f"Iteraciones realizadas: {res['iteraciones']} "
                f"(Estimación teórica n = log2(Δx0/Ea,d) = {res['n_teorico_exacto']:.2f} → {res['n_teorico']})\n"
                f"Error aproximado final (εa): {ea_final} | Error verdadero (εt): {et_final}\n"
                f"Criterio de parada: {res['criterio']}"
            )
            if self.ui.cmbEjemplos.currentIndex() == 0:
                resumen += (
                    "\n\nInterpretación física (Grupo 4): El voltaje Vd ≈ 0.574127 V representa el punto de "
                    "operación (punto Q) donde la corriente exponencial del diodo iguala a la corriente "
                    "de la recta de carga de la fuente Vs = 5 V y resistencia R = 1 kΩ."
                )
            self.ui.txtResultado.setPlainText(resumen)

            # Actualizar gráficas
            graficar_funcion(self.canvas_func, expr, xl, xu, tabla)
            graficar_error(self.canvas_err, tabla, es)

        except Exception as exc:
            QMessageBox.warning(self, "Error de cálculo", str(exc))

    def limpiar(self):
        self.ultimo_resultado = None
        self.ui.tablaResultados.setRowCount(0)
        self.ui.txtResultado.clear()
        self.canvas_func.limpiar()
        self.canvas_err.limpiar()

    def exportar_csv(self):
        if not self.ultimo_resultado:
            QMessageBox.information(self, "Exportar CSV", "Primero ejecuta un cálculo para exportar los resultados.")
            return

        ruta, _ = QFileDialog.getSaveFileName(self, "Guardar resultados", "resultados_biseccion.csv", "CSV (*.csv)")
        if not ruta:
            return

        with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["i", "xl", "xu", "xr", "f(xl)", "f(xr)", "f(xl)*f(xr)", "ea (%)", "et (%)", "Subintervalo"])
            for fila in self.ultimo_resultado["tabla"]:
                writer.writerow([
                    fila["i"],
                    f"{fila['xl']:.9f}",
                    f"{fila['xu']:.9f}",
                    f"{fila['xr']:.9f}",
                    f"{fila['f_xl']:.9e}",
                    f"{fila['f_xr']:.9e}",
                    f"{fila['producto']:.9e}",
                    f"{fila['ea']:.6f}" if fila["ea"] is not None else "",
                    f"{fila['et']:.6f}" if fila["et"] is not None else "",
                    fila["subintervalo"],
                ])
        QMessageBox.information(self, "Exportar CSV", "Archivo exportado correctamente.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
