import pytest
from seleccionar_palabras_largas import seleccionar_palabras_largas


# 1. Selección correcta de palabras largas
def test_seleccionar_palabras_largas_correcto():
    palabras = ["hola", "adiós", "sol", "informática"]
    resultado = seleccionar_palabras_largas(palabras, 5)
    assert resultado == ["adiós", "informática"]


# 2. Lista sin palabras que cumplan la condición
def test_seleccionar_palabras_largas_sin_resultados():
    palabras = ["sol", "pez", "u"]
    resultado = seleccionar_palabras_largas(palabras, 4)
    assert resultado == []


# 3. Lista vacía
def test_seleccionar_palabras_largas_lista_vacia():
    palabras = []
    resultado = seleccionar_palabras_largas(palabras, 3)
    assert resultado == []


# 4. Palabras que alcanzan exactamente la longitud mínima
def test_seleccionar_palabras_largas_longitud_exacta():
    palabras = ["casa", "ola", "mundo"]
    resultado = seleccionar_palabras_largas(palabras, 4)
    assert resultado == ["casa", "mundo"]


# 5. Error si algún elemento no es cadena
def test_seleccionar_palabras_largas_tipo_invalido_elemento():
    palabras = ["hola", 5, "adiós"]
    with pytest.raises(TypeError):
        seleccionar_palabras_largas(palabras, 4)


# 6. Error si longitud_minima no es un entero
def test_seleccionar_palabras_largas_tipo_invalido_longitud():
    palabras = ["hola", "adiós"]
    with pytest.raises(TypeError):
        seleccionar_palabras_largas(palabras, "4")
