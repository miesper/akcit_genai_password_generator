"""Módulo principal da CLI do gerador de senhas."""
import click
from akcit_genai_password_generator.generator import gerar_senha

@click.command()
@click.option('--length', '-l', default=12, show_default=True, help='Tamanho da senha')
@click.option('--uppercase/--no-uppercase', default=True, show_default=True, help='Incluir letras maiúsculas')
@click.option('--lowercase/--no-lowercase', default=True, show_default=True, help='Incluir letras minúsculas')
@click.option('--digits/--no-digits', default=True, show_default=True, help='Incluir números')
@click.option('--specials/--no-specials', default=True, show_default=True, help='Incluir caracteres especiais')
def cli(length, uppercase, lowercase, digits, specials):
    """Executa a geração de senha conforme opções."""
    senha = gerar_senha(length, uppercase, lowercase, digits, specials)
    click.echo(senha)
