"""Funções auxiliares para validação e suporte."""


def validar_tamanho(tamanho):
    """Valida se o tamanho é positivo."""
    if not isinstance(tamanho, int) or tamanho < 1:
        raise ValueError('O tamanho deve ser inteiro positivo.')
    return True
