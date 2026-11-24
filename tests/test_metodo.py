import pytest
from metodo.biseccion import biseccion, busqueda_incremental


def test_caso_grupo4_diodo():
    """Valida el caso obligatorio del Grupo 4: Vd = 0.574127 V en 15 iteraciones."""
    expr = "1e-12*(exp(x/0.02585) - 1) - (5 - x)/1000"
    res = biseccion(expr, xl=0.0, xu=1.0, es=0.01, max_iter=100, valor_verdadero=0.574147)
    assert res["iteraciones"] == 15
    assert pytest.approx(res["raiz"], abs=1e-6) == 0.574127
    assert res["ea_final"] < 0.01


def test_caso_grupo5_paracaidista():
    """Valida el caso del paracaidista (Sección 8): c = 14.8125 kg/s en 7 iteraciones."""
    expr = "(9.81*68.1/x)*(1 - exp(-(x/68.1)*10)) - 40"
    res = biseccion(expr, xl=12.0, xu=20.0, es=0.5, max_iter=100, valor_verdadero=14.8011)
    assert res["iteraciones"] == 7
    assert pytest.approx(res["raiz"], abs=1e-4) == 14.8125


def test_caso_grupo6_rlc():
    """Valida el caso del circuito RLC (Sección 8): R = 328.2227 ohm en 12 iteraciones."""
    expr = "exp(-x*0.05/(2*5))*cos(sqrt(1/(5*1e-4) - (x/(2*5))**2)*0.05) - 0.01"
    res = biseccion(expr, xl=0.0, xu=400.0, es=0.05, max_iter=100, valor_verdadero=328.1514)
    assert res["iteraciones"] == 12
    assert pytest.approx(res["raiz"], abs=1e-4) == 328.2227


def test_error_sin_cambio_signo():
    """Verifica que bisección lance ValueError si f(xl)*f(xu) > 0."""
    with pytest.raises(ValueError, match="cambio de signo"):
        biseccion("x**2 + 1", xl=-1.0, xu=1.0, es=0.01)


def test_busqueda_incremental():
    """Verifica la detección automática de intervalos con cambio de signo."""
    expr = "1e-12*(exp(x/0.02585) - 1) - (5 - x)/1000"
    intervalos = busqueda_incremental(expr, x_inicio=0.0, x_fin=1.0, dx=0.1)
    assert len(intervalos) == 1
    a, b = intervalos[0]
    assert a <= 0.574147 <= b
