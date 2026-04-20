# Gerador de Senhas CLI

Aplicação de linha de comando (CLI) em Python para geração de senhas aleatórias e seguras, com critérios personalizáveis pelo usuário.

## Escopo
Gera senhas seguras conforme critérios definidos pelo usuário:
- Tamanho da senha
- Inclusão/exclusão de letras maiúsculas, minúsculas, números e caracteres especiais
- Interface amigável e robusta a erros

## Requisitos
- Python 3.8+
- Dependências: ver `requirements.txt`

## Instalação
```bash
pip install -r requirements.txt
```

## Uso Básico

```bash
python main.py --length 12 --uppercase --lowercase --numbers --specials
```

Parâmetros principais:
- `--length`: tamanho da senha (inteiro positivo, máximo 1.000.000)
- `--uppercase`: incluir letras maiúsculas
- `--lowercase`: incluir letras minúsculas
- `--numbers`: incluir números
- `--specials`: incluir caracteres especiais

**Limites:**
- O tamanho deve ser um inteiro positivo e no máximo 1.000.000. Valores decimais ou acima desse limite geram erro amigável.

**Exemplo de erro:**
```bash
python main.py --length 2000000
# Saída: O tamanho máximo permitido é 1.000.000 de caracteres.
```

Ao gerar a senha, ela será copiada automaticamente para a área de transferência e uma mensagem será exibida ao usuário.

Para mais opções:
```bash
python main.py --help
```

## Documentação
- Escopo: docs/escopo-mvp.md
- Backlog: docs/backlog.md
- Diagrama: docs/diagrama.mmd