"""Funções para geração de senhas seguras."""
import string
import secrets


def gerar_senha(tamanho, maiusculas=True, minusculas=True, numeros=True, especiais=True):
    """Gera uma senha aleatória conforme os critérios."""
    caracteres = ''
    if maiusculas:
        caracteres += string.ascii_uppercase
    if minusculas:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if especiais:
        caracteres += string.punctuation
    if not caracteres:
        raise ValueError('Selecione ao menos um tipo de caractere.')
    return ''.join(secrets.choice(caracteres) for _ in range(tamanho))
