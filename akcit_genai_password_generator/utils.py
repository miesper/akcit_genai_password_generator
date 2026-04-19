"""Funções auxiliares para validação e suporte."""


def validar_tamanho(tamanho):
    """Valida se o tamanho é positivo."""
    if not isinstance(tamanho, int) or tamanho < 1:
        raise ValueError('O tamanho deve ser inteiro positivo.')
    return True


def validar_criterios(uppercase, lowercase, numbers, specials):
    """Valida se ao menos um critério está selecionado."""
    if not (uppercase or lowercase or numbers or specials):
        raise ValueError('Selecione ao menos um tipo de caractere para gerar a senha.')
    return True
