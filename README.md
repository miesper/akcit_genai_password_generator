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
python main.py --length 12 --uppercase --lowercase --digits --specials
```
Parâmetros principais:
- `--length`: tamanho da senha
- `--uppercase`: incluir letras maiúsculas
- `--lowercase`: incluir letras minúsculas
- `--digits`: incluir números
- `--specials`: incluir caracteres especiais

Para mais opções:
```bash
python main.py --help
```

## Documentação
- Escopo: docs/escopo-mvp.md
- Backlog: docs/backlog.md
- Diagrama: docs/diagrama.mmd