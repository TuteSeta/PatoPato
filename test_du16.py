import pytest
from main import autenticar_usuario

def test_login_correcto():
    assert autenticar_usuario("pato@correo.com", "1234")

def test_login_incorrecto():
    assert not autenticar_usuario("pato@correo.com", "mal")

def test_usuario_inexistente():
    assert not autenticar_usuario("otro@correo.com", "1234")
