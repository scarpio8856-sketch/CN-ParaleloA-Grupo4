# Proyecto de Aula: Método de Bisección (Grupo 4 - Diodo)

Aplicación de escritorio desarrollada en **Python** con **PySide6 (Qt Designer)**, **SymPy**, **NumPy** y **Matplotlib** para la asignatura **Cálculo Numérico (MECATR24)** (Quinto Nivel, Ingeniería Mecatrónica).

## Integrantes y Roles (Equipo de 4)
- **Integrante 1 — Lógica numérica (`metodo/biseccion.py`):** JOSÉ STEVEN NAVARRETE RIVAS
- **Integrante 2 — Interfaz gráfica (`ui/ventana_principal.ui`):** JUNIOR ALEXANDER HERRERA CHÁVEZ
- **Integrante 3 — Controlador y gráficas (`main.py`, `metodo/graficas.py`):** STEVEN JOSUÉ CARPIO FRANCO
- **Integrante 4 — Pruebas y documentación (`tests/test_metodo.py`, `README.md`):** ALAN FLAUBERT FIERRO YANZA

## Descripción del Caso de Aplicación (Grupo 4)
Determinación del **punto de operación ($V_d$)** de un diodo semiconductor en serie con una fuente $V_S = 5\text{ V}$ y una resistencia $R = 1\text{ k}\Omega$, con corriente de saturación $I_s = 1\times 10^{-12}\text{ A}$ y voltaje térmico $V_T = 25.85\text{ mV}$:

$$f(V_d) = 1\times 10^{-12}\left(e^{V_d / 0.02585} - 1\right) - \frac{5 - V_d}{1000} = 0$$

En el intervalo $[0, 1]\text{ V}$ con tolerancia $\varepsilon_s = 0.01\%$, el método converge en **15 iteraciones** a $V_d = 0.574127\text{ V}$ (error verdadero $\varepsilon_t \approx 0.0034\%$ respecto a la raíz exacta $0.574147\text{ V}$).

## Instalación y Ejecución

```bash
python -m venv .venv
# En Windows:
.venv\Scripts\activate
# En Linux/macOS:
# source .venv/bin/activate

pip install -r requirements.txt
python main.py
```

### Compilar interfaz desde Qt Designer (si se edita `.ui`)
```bash
pyside6-uic ui/ventana_principal.ui -o ui_ventana_principal.py
```

### Ejecutar pruebas unitarias
```bash
pytest -v
```

## Capturas de la Interfaz
*(Agregar aquí al menos 3 capturas guardadas en la carpeta `capturas/`)*
1. `capturas/01_ventana_principal.png`
2. `capturas/02_tabla_resultados.png`
3. `capturas/03_graficas_convergencia.png`
