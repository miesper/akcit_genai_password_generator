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
