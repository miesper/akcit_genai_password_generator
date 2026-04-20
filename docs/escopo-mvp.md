# Escopo do MVP – Gerador de Senhas CLI

## Objetivo
Desenvolver uma aplicação de linha de comando (CLI) em Python para geração de senhas aleatórias e seguras, permitindo ao usuário definir critérios como tamanho, inclusão de caracteres especiais, números, letras maiúsculas e minúsculas.

## Requisitos Funcionais
- Permitir ao usuário definir o tamanho da senha a ser gerada (inteiro positivo, máximo 1.000.000).
- Permitir a escolha de inclusão/exclusão de:
  - Letras maiúsculas
  - Letras minúsculas
  - Números (--numbers)
  - Caracteres especiais
- Gerar senhas aleatórias de acordo com os critérios definidos.
- Exibir a senha gerada diretamente no terminal e copiá-la para a área de transferência.
- Disponibilizar ajuda e documentação dos comandos via `--help`.
- Utilizar biblioteca padrão (argparse) ou Click para o parsing dos argumentos.

## Requisitos Não Funcionais
- Implementação em Python 3.8 ou superior.
- Código limpo, modular e documentado.
- Interface de linha de comando amigável e robusta a erros de entrada, incluindo rejeição de valores fora do intervalo permitido para o tamanho.
- Não armazenar senhas geradas em disco ou memória após exibição.
- Compatibilidade com sistemas operacionais Windows, Linux e macOS.
- Utilização de gerador de números aleatórios seguro (ex: `secrets` do Python).

## Fora de Escopo
- Interface gráfica (GUI).
- Integração com gerenciadores de senhas ou serviços externos.
- Armazenamento ou exportação de senhas.
- Geração de frases-senha (passphrases).
- Customização avançada de regras (ex: padrões de repetição, blacklist de caracteres).
- Suporte a múltiplos idiomas na CLI.

---

*Documento gerado automaticamente para definição do escopo do MVP do Gerador de Senhas CLI.*
# Escopo do MVP – Gerador de Senhas CLI

## Objetivo
Desenvolver uma aplicação de linha de comando (CLI) em Python para geração de senhas aleatórias e seguras, permitindo ao usuário definir critérios como tamanho, inclusão de caracteres especiais, números, letras maiúsculas e minúsculas.

## Requisitos Funcionais
- Permitir ao usuário definir o tamanho da senha a ser gerada.
- Permitir a escolha de inclusão/exclusão de:
  - Letras maiúsculas
  - Letras minúsculas
  - Números
  - Caracteres especiais
- Gerar senhas aleatórias de acordo com os critérios definidos.
- Exibir a senha gerada diretamente no terminal.
- Disponibilizar ajuda e documentação dos comandos via `--help`.
- Utilizar biblioteca padrão (argparse) ou Click para o parsing dos argumentos.

## Requisitos Não Funcionais
- Implementação em Python 3.8 ou superior.
- Código limpo, modular e documentado.
- Interface de linha de comando amigável e robusta a erros de entrada.
- Não armazenar senhas geradas em disco ou memória após exibição.
- Compatibilidade com sistemas operacionais Windows, Linux e macOS.
- Utilização de gerador de números aleatórios seguro (ex: `secrets` do Python).

## Fora de Escopo
- Interface gráfica (GUI).
- Integração com gerenciadores de senhas ou serviços externos.
- Armazenamento ou exportação de senhas.
- Geração de frases-senha (passphrases).
- Customização avançada de regras (ex: padrões de repetição, blacklist de caracteres).
- Suporte a múltiplos idiomas na CLI.

---

*Documento gerado automaticamente para definição do escopo do MVP do Gerador de Senhas CLI.*
