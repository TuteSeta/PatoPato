import pytest
from main import buscar_especie_por_nombre

def test_busqueda_exacta():
    resultado = buscar_especie_por_nombre("Pato criollo")
    assert resultado == ["Pato criollo"]

def test_busqueda_parcial():
    resultado = buscar_especie_por_nombre("cutirí")
    assert resultado == ["Pato cutirí"]

def test_busqueda_inexistente():
    resultado = buscar_especie_por_nombre("pingüino")
    assert resultado == []