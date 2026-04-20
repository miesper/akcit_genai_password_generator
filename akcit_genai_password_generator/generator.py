"""Funções para geração de senhas seguras."""

import string
import secrets
from .utils import validar_tamanho


def gerar_senha(tamanho, maiusculas=True, minusculas=True, numeros=True, especiais=True):
    """Gera uma senha aleatória conforme os critérios."""
    validar_tamanho(tamanho)
    pools = []
    if maiusculas:
        pools.append(string.ascii_uppercase)
    if minusculas:
        pools.append(string.ascii_lowercase)
    if numeros:
        pools.append(string.digits)
    if especiais:
        pools.append(string.punctuation)
    if not pools:
        raise ValueError('Selecione ao menos um tipo de caractere.')

    # Garante pelo menos um caractere de cada tipo solicitado
    senha = [secrets.choice(pool) for pool in pools]
    restantes = tamanho - len(senha)
    todos_caracteres = ''.join(pools)
    senha += [secrets.choice(todos_caracteres) for _ in range(restantes)]
    secrets.SystemRandom().shuffle(senha)
    return ''.join(senha)
