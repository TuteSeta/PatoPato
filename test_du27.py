import pytest
from main import obtener_datos_comportamiento

def test_datos_comportamiento_picazo():
    datos = obtener_datos_comportamiento("Pato picazo")
    assert any(tipo == "vuelo" for tipo, _ in datos)

def test_datos_comportamiento_inexistente():
    assert obtener_datos_comportamiento("Flamenco") == []
