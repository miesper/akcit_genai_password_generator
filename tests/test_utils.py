import pytest
from akcit_genai_password_generator.utils import validar_tamanho, validar_criterios

# Testes para validar_tamanho

def test_validar_tamanho_valido():
    assert validar_tamanho(10) is True
    assert validar_tamanho(1_000_000) is True

def test_validar_tamanho_zero():
    with pytest.raises(ValueError, match='O tamanho deve ser inteiro positivo.'):
        validar_tamanho(0)

def test_validar_tamanho_negativo():
    with pytest.raises(ValueError, match='O tamanho deve ser inteiro positivo.'):
        validar_tamanho(-5)

def test_validar_tamanho_decimal():
    with pytest.raises(ValueError, match='O tamanho deve ser inteiro positivo.'):
        validar_tamanho(12.5)

def test_validar_tamanho_acima_limite():
    with pytest.raises(ValueError, match='O tamanho máximo permitido é 1.000.000 de caracteres.'):
        validar_tamanho(1_000_001)

# Testes para validar_criterios

def test_validar_criterios_valido():
    assert validar_criterios(True, False, False, False) is True
    assert validar_criterios(False, True, True, False) is True

def test_validar_criterios_todos_false():
    with pytest.raises(ValueError, match='Selecione ao menos um tipo de caractere'):
        validar_criterios(False, False, False, False)
