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


## Uso Avançado

#### Gerar senha apenas com números e minúsculas, tamanho 20
```bash
python main.py --length 20 --no-uppercase --lowercase --numbers --no-specials
```
Saída: senha de 20 caracteres, apenas números e letras minúsculas.

#### Gerar senha só com caracteres especiais, tamanho 8
```bash
python main.py --length 8 --no-uppercase --no-lowercase --no-numbers --specials
```
Saída: senha de 8 caracteres, apenas símbolos.

#### Gerar senha longa (1000 caracteres) com todos os tipos
```bash
python main.py --length 1000 --uppercase --lowercase --numbers --specials
```
Saída: senha de 1000 caracteres, misturando todos os tipos.

#### Gerar senha e redirecionar para arquivo
```bash
python main.py --length 16 > senha.txt
```
A senha será salva no arquivo senha.txt.

#### Exibir ajuda detalhada
```bash
python main.py --help
```

## Cobertura de Testes

Para gerar o relatório de cobertura de testes, execute:

```bash
python -m pytest --cov=akcit_genai_password_generator --cov-report=html:docs/cov_html
```

O relatório em HTML estará disponível em `docs/cov_html/index.html` após a execução.

> **Nota:** Recomenda-se não versionar a pasta `docs/cov_html` (adicione ao `.gitignore`).

## Documentação
- Escopo: docs/escopo-mvp.md
- Backlog: docs/backlog.md
- Diagrama: docs/diagrama.mmd