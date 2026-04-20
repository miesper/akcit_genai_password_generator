def test_cli_copia_clipboard_falha(monkeypatch):
    runner = CliRunner()

    # Simula erro no subprocess.run para forçar o except
    def fake_run(*args, **kwargs):
        raise Exception("Erro simulado")
    monkeypatch.setattr("subprocess.run", fake_run)

    result = runner.invoke(cli, ['--length', '12'])
    assert "Não foi possível copiar para a área de transferência." in result.output

def test_cli_copia_clipboard_sucesso_win32(monkeypatch):
    runner = CliRunner()

    # Simula sucesso no subprocess.run e sys.platform como win32
    monkeypatch.setattr("sys.platform", "win32")
    monkeypatch.setattr("subprocess.run", lambda *a, **k: None)

    result = runner.invoke(cli, ['--length', '12'])
    assert "Senha copiada para a área de transferência!" in result.output
import pytest
from click.testing import CliRunner
from akcit_genai_password_generator.cli import cli

def test_cli_gera_senha_valida():
    runner = CliRunner()
    result = runner.invoke(cli, ['--length', '12', '--uppercase', '--lowercase', '--numbers', '--specials'])
    assert result.exit_code == 0
    assert "Senha segura de 12 caracteres" in result.output

def test_cli_erro_tamanho_zero():
    runner = CliRunner()
    result = runner.invoke(cli, ['--length', '0'])
    assert result.exit_code == 0
    assert "O tamanho deve ser inteiro positivo." in result.output

def test_cli_erro_tamanho_maximo():
    runner = CliRunner()
    result = runner.invoke(cli, ['--length', '1000001'])
    assert result.exit_code == 0
    assert "O tamanho máximo permitido é 1.000.000 de caracteres." in result.output

def test_cli_erro_sem_criterios():
    runner = CliRunner()
    result = runner.invoke(cli, ['--length', '12', '--no-uppercase', '--no-lowercase', '--no-numbers', '--no-specials'])
    assert result.exit_code == 0
    assert "Selecione ao menos um tipo de caractere" in result.output
