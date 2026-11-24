# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtWidgets import (QComboBox, QDoubleSpinBox, QFormLayout,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem, QSpinBox, QStatusBar,
    QTabWidget, QTableWidget, QTextEdit, QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1220, 780)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutMain = QHBoxLayout(self.centralwidget)
        self.horizontalLayoutMain.setObjectName("horizontalLayoutMain")
        self.grpEntrada = QGroupBox(self.centralwidget)
        self.grpEntrada.setObjectName("grpEntrada")
        self.verticalLayoutEntrada = QVBoxLayout(self.grpEntrada)
        self.verticalLayoutEntrada.setObjectName("verticalLayoutEntrada")
        self.formLayoutParametros = QFormLayout()
        self.formLayoutParametros.setObjectName("formLayoutParametros")
        self.lblEjemplos = QLabel(self.grpEntrada)
        self.lblEjemplos.setObjectName("lblEjemplos")
        self.formLayoutParametros.setWidget(0, QFormLayout.LabelRole, self.lblEjemplos)

        self.cmbEjemplos = QComboBox(self.grpEntrada)
        self.cmbEjemplos.addItem("")
        self.cmbEjemplos.addItem("")
        self.cmbEjemplos.addItem("")
        self.cmbEjemplos.setObjectName("cmbEjemplos")
        self.formLayoutParametros.setWidget(0, QFormLayout.FieldRole, self.cmbEjemplos)

        self.lblFuncion = QLabel(self.grpEntrada)
        self.lblFuncion.setObjectName("lblFuncion")
        self.formLayoutParametros.setWidget(1, QFormLayout.LabelRole, self.lblFuncion)

        self.txtFuncion = QLineEdit(self.grpEntrada)
        self.txtFuncion.setObjectName("txtFuncion")
        self.formLayoutParametros.setWidget(1, QFormLayout.FieldRole, self.txtFuncion)

        self.lblXl = QLabel(self.grpEntrada)
        self.lblXl.setObjectName("lblXl")
        self.formLayoutParametros.setWidget(2, QFormLayout.LabelRole, self.lblXl)

        self.spnXl = QDoubleSpinBox(self.grpEntrada)
        self.spnXl.setObjectName("spnXl")
        self.spnXl.setDecimals(6)
        self.spnXl.setMinimum(-100000.000000)
        self.spnXl.setMaximum(100000.000000)
        self.spnXl.setSingleStep(0.100000)
        self.formLayoutParametros.setWidget(2, QFormLayout.FieldRole, self.spnXl)

        self.lblXu = QLabel(self.grpEntrada)
        self.lblXu.setObjectName("lblXu")
        self.formLayoutParametros.setWidget(3, QFormLayout.LabelRole, self.lblXu)

        self.spnXu = QDoubleSpinBox(self.grpEntrada)
        self.spnXu.setObjectName("spnXu")
        self.spnXu.setDecimals(6)
        self.spnXu.setMinimum(-100000.000000)
        self.spnXu.setMaximum(100000.000000)
        self.spnXu.setSingleStep(0.100000)
        self.spnXu.setValue(1.000000)
        self.formLayoutParametros.setWidget(3, QFormLayout.FieldRole, self.spnXu)

        self.lblEs = QLabel(self.grpEntrada)
        self.lblEs.setObjectName("lblEs")
        self.formLayoutParametros.setWidget(4, QFormLayout.LabelRole, self.lblEs)

        self.spnEs = QDoubleSpinBox(self.grpEntrada)
        self.spnEs.setObjectName("spnEs")
        self.spnEs.setDecimals(6)
        self.spnEs.setMinimum(0.000001)
        self.spnEs.setMaximum(100.000000)
        self.spnEs.setSingleStep(0.010000)
        self.spnEs.setValue(0.010000)
        self.formLayoutParametros.setWidget(4, QFormLayout.FieldRole, self.spnEs)

        self.lblMaxIter = QLabel(self.grpEntrada)
        self.lblMaxIter.setObjectName("lblMaxIter")
        self.formLayoutParametros.setWidget(5, QFormLayout.LabelRole, self.lblMaxIter)

        self.spnMaxIter = QSpinBox(self.grpEntrada)
        self.spnMaxIter.setObjectName("spnMaxIter")
        self.spnMaxIter.setMinimum(1)
        self.spnMaxIter.setMaximum(1000)
        self.spnMaxIter.setValue(100)
        self.formLayoutParametros.setWidget(5, QFormLayout.FieldRole, self.spnMaxIter)

        self.lblValorVerdadero = QLabel(self.grpEntrada)
        self.lblValorVerdadero.setObjectName("lblValorVerdadero")
        self.formLayoutParametros.setWidget(6, QFormLayout.LabelRole, self.lblValorVerdadero)

        self.txtValorVerdadero = QLineEdit(self.grpEntrada)
        self.txtValorVerdadero.setObjectName("txtValorVerdadero")
        self.formLayoutParametros.setWidget(6, QFormLayout.FieldRole, self.txtValorVerdadero)

        self.lblUnidades = QLabel(self.grpEntrada)
        self.lblUnidades.setObjectName("lblUnidades")
        self.formLayoutParametros.setWidget(7, QFormLayout.LabelRole, self.lblUnidades)

        self.txtUnidades = QLineEdit(self.grpEntrada)
        self.txtUnidades.setObjectName("txtUnidades")
        self.formLayoutParametros.setWidget(7, QFormLayout.FieldRole, self.txtUnidades)

        self.lblPasoDx = QLabel(self.grpEntrada)
        self.lblPasoDx.setObjectName("lblPasoDx")
        self.formLayoutParametros.setWidget(8, QFormLayout.LabelRole, self.lblPasoDx)

        self.spnPasoDx = QDoubleSpinBox(self.grpEntrada)
        self.spnPasoDx.setObjectName("spnPasoDx")
        self.spnPasoDx.setDecimals(4)
        self.spnPasoDx.setMinimum(0.000100)
        self.spnPasoDx.setMaximum(1000.000000)
        self.spnPasoDx.setSingleStep(0.050000)
        self.spnPasoDx.setValue(0.100000)
        self.formLayoutParametros.setWidget(8, QFormLayout.FieldRole, self.spnPasoDx)

        self.verticalLayoutEntrada.addLayout(self.formLayoutParametros)

        self.gridLayoutBotones = QGridLayout()
        self.gridLayoutBotones.setObjectName("gridLayoutBotones")
        self.btnCalcular = QPushButton(self.grpEntrada)
        self.btnCalcular.setObjectName("btnCalcular")
        self.gridLayoutBotones.addWidget(self.btnCalcular, 0, 0, 1, 1)

        self.btnBuscarIntervalos = QPushButton(self.grpEntrada)
        self.btnBuscarIntervalos.setObjectName("btnBuscarIntervalos")
        self.gridLayoutBotones.addWidget(self.btnBuscarIntervalos, 0, 1, 1, 1)

        self.btnLimpiar = QPushButton(self.grpEntrada)
        self.btnLimpiar.setObjectName("btnLimpiar")
        self.gridLayoutBotones.addWidget(self.btnLimpiar, 1, 0, 1, 1)

        self.btnExportar = QPushButton(self.grpEntrada)
        self.btnExportar.setObjectName("btnExportar")
        self.gridLayoutBotones.addWidget(self.btnExportar, 1, 1, 1, 1)

        self.verticalLayoutEntrada.addLayout(self.gridLayoutBotones)

        self.verticalSpacerEntrada = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.verticalLayoutEntrada.addItem(self.verticalSpacerEntrada)

        self.horizontalLayoutMain.addWidget(self.grpEntrada)

        self.grpResultados = QGroupBox(self.centralwidget)
        self.grpResultados.setObjectName("grpResultados")
        self.verticalLayoutResultados = QVBoxLayout(self.grpResultados)
        self.verticalLayoutResultados.setObjectName("verticalLayoutResultados")
        self.tabGraficas = QTabWidget(self.grpResultados)
        self.tabGraficas.setObjectName("tabGraficas")
        self.tabFuncion = QWidget()
        self.tabFuncion.setObjectName("tabFuncion")
        self.layoutTabFunc = QVBoxLayout(self.tabFuncion)
        self.layoutTabFunc.setObjectName("layoutTabFunc")
        self.widgetGraficaFuncion = QWidget(self.tabFuncion)
        self.widgetGraficaFuncion.setObjectName("widgetGraficaFuncion")
        self.layoutTabFunc.addWidget(self.widgetGraficaFuncion)
        self.tabGraficas.addTab(self.tabFuncion, "")

        self.tabError = QWidget()
        self.tabError.setObjectName("tabError")
        self.layoutTabError = QVBoxLayout(self.tabError)
        self.layoutTabError.setObjectName("layoutTabError")
        self.widgetGraficaError = QWidget(self.tabError)
        self.widgetGraficaError.setObjectName("widgetGraficaError")
        self.layoutTabError.addWidget(self.widgetGraficaError)
        self.tabGraficas.addTab(self.tabError, "")

        self.tabAcercaDe = QWidget()
        self.tabAcercaDe.setObjectName("tabAcercaDe")
        self.layoutTabAcerca = QVBoxLayout(self.tabAcercaDe)
        self.layoutTabAcerca.setObjectName("layoutTabAcerca")
        self.lblAcercaDe = QLabel(self.tabAcercaDe)
        self.lblAcercaDe.setObjectName("lblAcercaDe")
        self.lblAcercaDe.setAlignment(Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.lblAcercaDe.setWordWrap(True)
        self.layoutTabAcerca.addWidget(self.lblAcercaDe)
        self.tabGraficas.addTab(self.tabAcercaDe, "")

        self.verticalLayoutResultados.addWidget(self.tabGraficas)

        self.tablaResultados = QTableWidget(self.grpResultados)
        self.tablaResultados.setObjectName("tablaResultados")
        self.verticalLayoutResultados.addWidget(self.tablaResultados)

        self.txtResultado = QTextEdit(self.grpResultados)
        self.txtResultado.setObjectName("txtResultado")
        self.txtResultado.setMaximumSize(QSize(16777215, 140))
        self.txtResultado.setReadOnly(True)
        self.verticalLayoutResultados.addWidget(self.txtResultado)

        self.verticalLayoutResultados.setStretch(0, 3)
        self.verticalLayoutResultados.setStretch(1, 2)
        self.verticalLayoutResultados.setStretch(2, 1)

        self.horizontalLayoutMain.addWidget(self.grpResultados)
        self.horizontalLayoutMain.setStretch(0, 1)
        self.horizontalLayoutMain.setStretch(1, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabGraficas.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "Cálculo Numérico - Método de Bisección (Grupo 4: Diodo)", None))
        self.grpEntrada.setTitle(QCoreApplication.translate("MainWindow", "Parámetros de entrada", None))
        self.lblEjemplos.setText(QCoreApplication.translate("MainWindow", "Caso / Ejemplo:", None))
        self.cmbEjemplos.setItemText(0, QCoreApplication.translate("MainWindow", "Caso Grupo 4: Punto de operación de un diodo", None))
        self.cmbEjemplos.setItemText(1, QCoreApplication.translate("MainWindow", "Ejemplo libro (Chapra): Paracaidista", None))
        self.cmbEjemplos.setItemText(2, QCoreApplication.translate("MainWindow", "Ejemplo libro: exp(-x) - x", None))

        self.lblFuncion.setText(QCoreApplication.translate("MainWindow", "Función f(x):", None))
        self.txtFuncion.setPlaceholderText(QCoreApplication.translate("MainWindow", "Ej: exp(-x) - x", None))
        self.lblXl.setText(QCoreApplication.translate("MainWindow", "Límite inferior (xl):", None))
        self.lblXu.setText(QCoreApplication.translate("MainWindow", "Límite superior (xu):", None))
        self.lblEs.setText(QCoreApplication.translate("MainWindow", "Tolerancia εs (%):", None))
        self.lblMaxIter.setText(QCoreApplication.translate("MainWindow", "Máx. iteraciones:", None))
        self.lblValorVerdadero.setText(QCoreApplication.translate("MainWindow", "Valor verdadero (opc.):", None))
        self.txtValorVerdadero.setPlaceholderText(QCoreApplication.translate("MainWindow", "Opcional para calcular εt (%)", None))
        self.lblUnidades.setText(QCoreApplication.translate("MainWindow", "Unidades físicas:", None))
        self.txtUnidades.setText(QCoreApplication.translate("MainWindow", "V", None))
        self.lblPasoDx.setText(QCoreApplication.translate("MainWindow", "Paso búsqueda Δx:", None))
        self.btnCalcular.setText(QCoreApplication.translate("MainWindow", "Calcular", None))
        self.btnBuscarIntervalos.setText(QCoreApplication.translate("MainWindow", "Buscar intervalos (Δx)", None))
        self.btnLimpiar.setText(QCoreApplication.translate("MainWindow", "Limpiar", None))
        self.btnExportar.setText(QCoreApplication.translate("MainWindow", "Exportar CSV", None))
        self.grpResultados.setTitle(QCoreApplication.translate("MainWindow", "Resultados, Tabla y Gráficas", None))
        self.tabGraficas.setTabText(self.tabGraficas.indexOf(self.tabFuncion), QCoreApplication.translate("MainWindow", "Gráfica f(x)", None))
        self.tabGraficas.setTabText(self.tabGraficas.indexOf(self.tabError), QCoreApplication.translate("MainWindow", "Convergencia εa", None))
        self.lblAcercaDe.setText(QCoreApplication.translate("MainWindow", "<html><head/><body><h3>Proyecto de Aula: Método de Bisección (Proyecto B - Grupo 4)</h3><p><b>Asignatura:</b> Cálculo Numérico (MECATR24) — Quinto Nivel, Ingeniería Mecatrónica</p><p><b>Caso de aplicación obligatorio:</b> Punto de operación de un diodo semiconductor (Vs = 5 V, R = 1 kΩ, Is = 1×10⁻¹² A, VT = 25.85 mV)</p><p><b>Paralelo:</b> [Colocar Paralelo A o B]</p><p><b>Integrantes del Equipo (4):</b></p><ul><li>Integrante 1 (Lógica numérica): [Nombre Apellido]</li><li>Integrante 2 (Interfaz Qt Designer): [Nombre Apellido]</li><li>Integrante 3 (Controlador y gráficas): [Nombre Apellido]</li><li>Integrante 4 (Pruebas y documentación): [Nombre Apellido]</li></ul></body></html>", None))
        self.tabGraficas.setTabText(self.tabGraficas.indexOf(self.tabAcercaDe), QCoreApplication.translate("MainWindow", "Acerca de", None))
