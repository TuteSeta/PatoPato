import pytest
from main import simular_comportamiento

def test_swim_in_cold_water():
    resultado = simular_comportamiento("fría", "invierno", "premium")
    assert resultado == "El pato está nadando para entrar en calor."

def test_quack_in_temperate_water():
    resultado = simular_comportamiento("templada", "otoño", "premium")
    assert resultado == "El pato emite su sonido característico."

def test_fly_in_hot_water_and_summer():
    resultado = simular_comportamiento("caliente", "verano", "premium")
    assert resultado == "El pato vuela alto en verano."

def test_fly_in_hot_water_and_winter():
    resultado = simular_comportamiento("caliente", "invierno", "premium")
    assert resultado == "El pato vuela bajo."

def test_block_access_for_non_premium_user():
    resultado = simular_comportamiento("fría", "invierno", "gratis")
    assert resultado == "Funcionalidad exclusiva para usuarios gratis"
