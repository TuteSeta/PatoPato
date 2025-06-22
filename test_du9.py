import pytest
from main import obtener_ficha_especie

def test_ficha_existente():
    ficha = obtener_ficha_especie("Pato criollo")
    assert ficha["habitat"] == "laguna"

def test_ficha_inexistente():
    assert obtener_ficha_especie("Pingüino") is None

def test_ficha_nombre_mayusculas():
    ficha = obtener_ficha_especie("PATO COLORADO")
    assert ficha["vuelo"] == "corto"

def test_ficha_nombre_con_espacios_extra():
    ficha = obtener_ficha_especie("  Pato picazo  ".strip())
    assert ficha["vuelo"] == "largo"
