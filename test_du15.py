import pytest
from main import filtrar_especies_por_habitat

def test_filtrar_laguna():
    resultado = filtrar_especies_por_habitat("laguna")
    assert set(resultado) == {"Pato criollo", "Pato colorado", "Pato cuchara"}

def test_filtrar_rio():
    resultado = filtrar_especies_por_habitat("río")
    assert set(resultado) == {"Pato picazo", "Pato barcino", "Pato overo"}

def test_filtrar_inexistente():
    resultado = filtrar_especies_por_habitat("desierto")
    assert resultado == []
