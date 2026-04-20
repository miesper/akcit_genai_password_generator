"""Módulo principal da CLI do gerador de senhas."""
import click
from akcit_genai_password_generator.generator import gerar_senha
from akcit_genai_password_generator.utils import validar_criterios, validar_tamanho

@click.command()
@click.option('--length', '-l', default=12, show_default=True, help='Tamanho da senha')
@click.option('--uppercase/--no-uppercase', default=True, show_default=True, help='Incluir letras maiúsculas')
@click.option('--lowercase/--no-lowercase', default=True, show_default=True, help='Incluir letras minúsculas')
@click.option('--numbers/--no-numbers', default=True, show_default=True, help='Incluir números')
@click.option('--specials/--no-specials', default=True, show_default=True, help='Incluir caracteres especiais')
def cli(length, uppercase, lowercase, numbers, specials):
    """Executa a geração de senha conforme opções."""
    try:
        validar_tamanho(length)
        validar_criterios(uppercase, lowercase, numbers, specials)
    except ValueError as e:
        click.secho(str(e), fg='red')
        return
    senha = gerar_senha(length, uppercase, lowercase, numbers, specials)
    confs = []
    if uppercase:
        confs.append('maiúsculas')
    if lowercase:
        confs.append('minúsculas')
    if numbers:
        confs.append('números')
    if specials:
        confs.append('caracteres especiais')
    confs_str = ', '.join(confs)
    import subprocess
    import sys
    click.echo(f"Senha segura de {length} caracteres e configurações selecionadas: {confs_str}")
    click.echo(senha)

    # Copiar para área de transferência
    try:
        if sys.platform == 'win32':
            subprocess.run('clip', universal_newlines=True, input=senha, check=True)
        elif sys.platform == 'darwin':
            subprocess.run('pbcopy', universal_newlines=True, input=senha, check=True)
        else:
            subprocess.run('xclip -selection clipboard', universal_newlines=True, input=senha, shell=True, check=True)
        click.secho('Senha copiada para a área de transferência!', fg='green')
    except Exception:
        click.secho('Não foi possível copiar para a área de transferência.', fg='yellow')
