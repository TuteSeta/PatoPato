import pytest
from main import comparar_especies

def test_comparar_dos_existentes():
    e1, e2 = comparar_especies("Pato picazo", "Pato criollo")
    assert e1 and e2
    assert e1["nombre"] == "Pato picazo"
    assert e2["nombre"] == "Pato criollo"

def test_comparar_uno_inexistente():
    e1, e2 = comparar_especies("Pingüino", "Pato criollo")
    assert e1 is None
    assert e2
