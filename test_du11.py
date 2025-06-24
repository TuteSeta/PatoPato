import pytest  
from main import filtrar_por_tipo_de_vuelo

def test_filtrar_vuelo_corto():
    res = filtrar_por_tipo_de_vuelo("corto")
    assert "Pato criollo" in res

def test_filtrar_vuelo_inexistente():
    assert filtrar_por_tipo_de_vuelo("planeado") == []
