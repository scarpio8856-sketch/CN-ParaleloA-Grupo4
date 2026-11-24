import math
import numpy as np
import sympy as sp


def crear_funcion(expr_str: str):
    """Convierte una cadena de texto en una función evaluable f(x) usando SymPy."""
    if not expr_str or not expr_str.strip():
        raise ValueError("La función f(x) no puede estar vacía.")

    # Permite usar '^' como potencia
    expr_limpia = expr_str.replace("^", "**")
    x = sp.Symbol("x")
    try:
        expr_sym = sp.sympify(expr_limpia)
    except Exception as exc:
        raise ValueError(f"Expresión matemática inválida: {exc}")

    simbolos_extra = expr_sym.free_symbols - {x}
    if simbolos_extra:
        nombres = ", ".join(str(s) for s in simbolos_extra)
        raise ValueError(f"Variables no reconocidas ({nombres}). Escribe la función en términos de 'x'.")

    f_num = sp.lambdify(x, expr_sym, modules=["numpy", "math"])

    def f(val: float) -> float:
        resultado = float(f_num(val))
        if math.isnan(resultado) or math.isinf(resultado):
            raise ValueError(f"La función produjo un valor indefinido en x = {val}.")
        return resultado

    return f, expr_sym


def busqueda_incremental(expr_str: str, x_inicio: float, x_fin: float, dx: float):
    """Explora [x_inicio, x_fin] con paso Δx y devuelve subintervalos con cambio de signo."""
    if dx <= 0:
        raise ValueError("El paso Δx debe ser mayor que cero.")
    if x_inicio >= x_fin:
        raise ValueError("El límite inferior debe ser menor que el superior.")

    f, _ = crear_funcion(expr_str)
    puntos = np.arange(x_inicio, x_fin + dx * 0.5, dx)
    if puntos[-1] < x_fin:
        puntos = np.append(puntos, x_fin)

    intervalos = []
    for i in range(len(puntos) - 1):
        a, b = float(puntos[i]), float(puntos[i + 1])
        fa, fb = f(a), f(b)
        if fa == 0.0:
            intervalos.append((a, a))
        elif fa * fb < 0:
            intervalos.append((a, b))

    return intervalos


def biseccion(
    expr_str: str,
    xl: float,
    xu: float,
    es: float = 0.01,
    max_iter: int = 100,
    valor_verdadero: float | None = None,
):
    """Ejecuta el método de bisección programado a mano paso a paso."""
    if xl >= xu:
        raise ValueError("El extremo inferior xl debe ser menor que xu.")
    if es <= 0:
        raise ValueError("La tolerancia εs (%) debe ser mayor que cero.")
    if max_iter < 1:
        raise ValueError("El máximo de iteraciones debe ser al menos 1.")

    f, _ = crear_funcion(expr_str)
    fl = f(xl)
    fu = f(xu)

    if fl * fu > 0:
        raise ValueError(
            f"No hay cambio de signo en [{xl}, {xu}]: f(xl) = {fl:.6e}, f(xu) = {fu:.6e}.\n"
            "Usa 'Buscar intervalos (Δx)' para localizar un intervalo válido."
        )

    delta_x0 = xu - xl
    filas = []
    xr_anterior = None
    criterio_parada = "Máximo de iteraciones alcanzado"
    xl_actual, xu_actual = float(xl), float(xu)

    for i in range(1, max_iter + 1):
        fl = f(xl_actual)
        xr = (xl_actual + xu_actual) / 2.0
        fr = f(xr)
        producto = fl * fr

        ea = abs((xr - xr_anterior) / xr) * 100.0 if (xr_anterior is not None and xr != 0) else None
        et = (
            abs((valor_verdadero - xr) / valor_verdadero) * 100.0
            if (valor_verdadero is not None and valor_verdadero != 0)
            else None
        )

        if producto < 0:
            subintervalo = f"[{xl_actual:.6f}, {xr:.6f}]"
        elif producto > 0:
            subintervalo = f"[{xr:.6f}, {xu_actual:.6f}]"
        else:
            subintervalo = "Raíz exacta"

        filas.append(
            {
                "i": i,
                "xl": xl_actual,
                "xu": xu_actual,
                "xr": xr,
                "f_xl": fl,
                "f_xr": fr,
                "producto": producto,
                "ea": ea,
                "et": et,
                "subintervalo": subintervalo,
            }
        )

        if producto == 0.0:
            criterio_parada = "Raíz exacta encontrada (f(xr) = 0)"
            break

        if ea is not None and ea < es:
            criterio_parada = f"Tolerancia alcanzada (εa = {ea:.6f}% < εs = {es}%)"
            break

        if producto < 0:
            xu_actual = xr
        else:
            xl_actual = xr

        xr_anterior = xr

    raiz = filas[-1]["xr"]
    iteraciones_obtenidas = len(filas)

    # Número teórico de iteraciones: n = log2(Δx0 / Ea,d)
    ead = (es / 100.0) * abs(raiz) if raiz != 0 else (es / 100.0) * delta_x0
    n_teorico_exacto = math.log2(delta_x0 / ead) if ead > 0 else float(iteraciones_obtenidas)
    n_teorico = math.ceil(n_teorico_exacto)

    return {
        "raiz": raiz,
        "iteraciones": iteraciones_obtenidas,
        "n_teorico": n_teorico,
        "n_teorico_exacto": n_teorico_exacto,
        "ea_final": filas[-1]["ea"],
        "et_final": filas[-1]["et"],
        "criterio": criterio_parada,
        "tabla": filas,
    }
