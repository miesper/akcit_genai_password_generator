import pytest
from akcit_genai_password_generator.generator import gerar_senha

@pytest.fixture
def senha_padrao():
    return {
        'tamanho': 12,
        'maiusculas': True,
        'minusculas': True,
        'numeros': True,
        'especiais': True
    }

def test_gera_senha_completa(senha_padrao):
    senha = gerar_senha(**senha_padrao)
    assert len(senha) == senha_padrao['tamanho']
    assert any(c.isupper() for c in senha)
    assert any(c.islower() for c in senha)
    assert any(c.isdigit() for c in senha)
    assert any(c in '!@#$%^&*()_+-=[]{}|;:,.<>?/~' for c in senha)

def test_gera_somente_maiusculas():
    senha = gerar_senha(8, maiusculas=True, minusculas=False, numeros=False, especiais=False)
    assert senha.isupper()
    assert senha.isalpha()
    assert len(senha) == 8

def test_gera_somente_minusculas():
    senha = gerar_senha(10, maiusculas=False, minusculas=True, numeros=False, especiais=False)
    assert senha.islower()
    assert senha.isalpha()
    assert len(senha) == 10

def test_gera_somente_numeros():
    senha = gerar_senha(6, maiusculas=False, minusculas=False, numeros=True, especiais=False)
    assert senha.isdigit()
    assert len(senha) == 6

def test_gera_somente_especiais():
    senha = gerar_senha(5, maiusculas=False, minusculas=False, numeros=False, especiais=True)
    assert all(not c.isalnum() for c in senha)
    assert len(senha) == 5

def test_erro_sem_tipo_caractere():
    with pytest.raises(ValueError, match='Selecione ao menos um tipo de caractere.'):
        gerar_senha(8, maiusculas=False, minusculas=False, numeros=False, especiais=False)

def test_tamanho_zero():
    senha = gerar_senha(0)
    assert senha == ''
