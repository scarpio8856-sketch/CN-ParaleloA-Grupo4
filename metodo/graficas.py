import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from metodo.biseccion import crear_funcion


class LienzoGrafica(FigureCanvasQTAgg):
    def __init__(self, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = self.fig.add_subplot(111)
        super().__init__(self.fig)

    def limpiar(self):
        self.ax.clear()
        self.draw()


def graficar_funcion_previa(lienzo: LienzoGrafica, expr_str: str, xl: float, xu: float, intervalos: list | None = None):
    """Método gráfico previo: grafica f(x) en [xl, xu] y resalta subintervalos con cambio de signo."""
    lienzo.ax.clear()
    f, _ = crear_funcion(expr_str)

    xs = np.linspace(xl, xu, 300)
    ys = [f(float(val)) for val in xs]

    lienzo.ax.axhline(0, color="black", linewidth=1, linestyle="--")
    lienzo.ax.plot(xs, ys, label=f"f(x) = {expr_str}", color="#1f77b4", linewidth=2)

    if intervalos:
        for idx, (a, b) in enumerate(intervalos):
            etiqueta = "Cambio de signo" if idx == 0 else None
            lienzo.ax.axvspan(a, b, color="#2ca02c", alpha=0.25, label=etiqueta)

    lienzo.ax.set_title("Método gráfico previo: f(x) en el intervalo")
    lienzo.ax.set_xlabel("x")
    lienzo.ax.set_ylabel("f(x)")
    lienzo.ax.grid(True, linestyle=":", alpha=0.7)
    lienzo.ax.legend()
    lienzo.fig.tight_layout()
    lienzo.draw()


def graficar_funcion(lienzo: LienzoGrafica, expr_str: str, xl: float, xu: float, tabla: list):
    """Grafica f(x) junto con las aproximaciones xr de cada iteración."""
    lienzo.ax.clear()
    f, _ = crear_funcion(expr_str)

    margen = (xu - xl) * 0.1 if xu > xl else 0.5
    xs = np.linspace(xl - margen, xu + margen, 300)
    ys = [f(float(val)) for val in xs]

    lienzo.ax.axhline(0, color="black", linewidth=1, linestyle="--")
    lienzo.ax.plot(xs, ys, label=f"f(x) = {expr_str}", color="#1f77b4", linewidth=2)

    xrs = [fila["xr"] for fila in tabla]
    yrs = [fila["f_xr"] for fila in tabla]
    if len(xrs) > 1:
        lienzo.ax.scatter(xrs[:-1], yrs[:-1], color="#ff7f0e", zorder=4, label="Iteraciones xr")
    lienzo.ax.scatter(
        [xrs[-1]], [yrs[-1]], color="#d62728", s=80, zorder=5, label=f"Raíz ≈ {xrs[-1]:.6f}"
    )

    lienzo.ax.set_title("Método de Bisección: f(x) y aproximaciones xr")
    lienzo.ax.set_xlabel("x")
    lienzo.ax.set_ylabel("f(x)")
    lienzo.ax.grid(True, linestyle=":", alpha=0.7)
    lienzo.ax.legend()
    lienzo.fig.tight_layout()
    lienzo.draw()


def graficar_error(lienzo: LienzoGrafica, tabla: list, es: float):
    """Grafica el error relativo aproximado εa (%) contra la iteración en escala semilogarítmica."""
    lienzo.ax.clear()
    iters = [fila["i"] for fila in tabla if fila["ea"] is not None]
    eas = [fila["ea"] for fila in tabla if fila["ea"] is not None]

    if eas:
        lienzo.ax.semilogy(iters, eas, marker="o", color="#2ca02c", linewidth=2, label="Error εa (%)")
        lienzo.ax.axhline(es, color="#d62728", linestyle="--", label=f"Tolerancia εs = {es}%")
        lienzo.ax.set_title("Convergencia del Error Relativo Aproximado (escala semilog)")
        lienzo.ax.set_xlabel("Iteración (i)")
        lienzo.ax.set_ylabel("εa (%) [log]")
        lienzo.ax.grid(True, which="both", linestyle=":", alpha=0.7)
        lienzo.ax.legend()
    else:
        lienzo.ax.text(0.5, 0.5, "Se requieren al menos 2 iteraciones para graficar εa", ha="center")

    lienzo.fig.tight_layout()
    lienzo.draw()
