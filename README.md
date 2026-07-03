# Gerador de Senhas CLI

## Problema e Solução

### Problema
A criação de senhas seguras é uma necessidade constante para proteger contas e dados, mas muitos usuários têm dificuldade em gerar senhas fortes, únicas e que atendam a critérios específicos de segurança.

### Solução
Este projeto oferece uma ferramenta de linha de comando (CLI) em Python que gera senhas aleatórias, seguras e personalizáveis, permitindo ao usuário definir tamanho, tipos de caracteres e garantindo robustez por meio de validações e testes automatizados.

## Arquitetura
O projeto segue uma arquitetura modular:
- **CLI:** Interface de linha de comando baseada em Click.
- **Core:** Lógica de geração e validação de senhas.
- **Testes:** Cobertura automatizada com pytest.
- **Documentação:** Diagramas e escopo em docs/.

Veja o diagrama detalhado em [docs/diagrama.mmd](docs/diagrama.mmd).

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

## Uso da IA no Desenvolvimento

O desenvolvimento deste projeto contou com o apoio do GitHub Copilot (modelo Claude Haiku 4.5), utilizado para:
- Sugerir e revisar código Python.
- Gerar testes automatizados.
- Refatorar funções e melhorar validações.
- Criar e atualizar documentação.
- Apoiar análise e gerenciamento de riscos de projetos.
- Estruturar comunicação para stakeholders.
- Manter histórico e rastreabilidade das decisões via chat, garantindo granularidade nos commits e transparência no processo.

---

## Organização do Repositório

```
akcit_genai_password_generator/
├── main.py                                    # Ponto de entrada da CLI
├── pyproject.toml                             # Configuração do pacote Python
├── requirements.txt                           # Dependências do projeto
├── Makefile                                   # Comandos úteis
├── LICENSE                                    # Licença
├── README.md                                  # Este arquivo
│
├── akcit_genai_password_generator/            # Código-fonte
│   ├── __init__.py
│   ├── cli.py                                 # Interface CLI (Click)
│   ├── generator.py                           # Lógica de geração de senhas
│   └── utils.py                               # Funções utilitárias
│
├── tests/                                     # Testes automatizados
│   ├── test_cli.py
│   ├── test_generator.py
│   └── test_utils.py
│
└── docs/                                      # Documentação
    ├── escopo-mvp.md                          # Escopo funcional do MVP
    ├── backlog.md                             # Backlog de funcionalidades
    ├── diagrama.mmd                           # Arquitetura (Mermaid)
    ├── project_management.md                  # Cenário para gerenciamento
    ├── roteiro_apresentacao.md                # Roteiro de apresentação
    ├── forum.md                               # Tópicos de discussão
    ├── risks/                                 # Análise de riscos
    │   ├── identification.md                  # Identificação de riscos
    │   ├── analysis.md                        # Análise qualitativa
    │   └── reply.md                           # Estratégias de resposta
    └── comunication/                          # Comunicação com stakeholders
        └── stackholders.md                    # Documento para stakeholders
```

---

## Exercício de Gerenciamento de Projetos — Módulo 9

Este projeto serve como **estudo de caso prático** para o exercício de **Gerenciamento de Riscos** do módulo 9 de Gerenciamento de Projetos.

### Objetivo do Exercício

Aplicar as **5 etapas de gerenciamento de riscos** em um cenário real de desenvolvimento de software:

1. **Etapa 1 — Identificação de Riscos**  
   Documento: `docs/risks/identification.md`
   - Identificação de 10 riscos em 5 categorias
   - Análise de severidade e probabilidade
   - Matriz de priorização

2. **Etapa 2 — Análise Qualitativa de Riscos**  
   Documento: `docs/risks/analysis.md`
   - Análise estruturada dos riscos
   - Impactos potenciais (funcional, comercial, temporal, reputacional)
   - Fatores condicionantes e interdependências
   - Cenários de impacto com sequências

3. **Etapa 3 — Definição de Estratégias de Resposta**  
   Documento: `docs/risks/reply.md`
   - Estratégias para cada risco (Evitar, Mitigar, Aceitar, Transferir)
   - Ações concretas com prazos e benefícios
   - Plano de implementação por horizonte de tempo
   - Indicadores de sucesso

4. **Etapa 4 — Comunicação para Stakeholders**  
   Documento: `docs/comunication/stackholders.md`
   - Resumo executivo do projeto
   - Desafios em linguagem acessível
   - 4 decisões necessárias de stakeholders
   - Cenários de sucesso e seu impacto
   - Calendário de reuniões e próximos passos

5. **Contexto do Projeto**  
   Documento: `docs/project_management.md`
   - Cenário adaptado do projeto
   - Desafios iniciais
   - Contexto da equipe e dependências críticas

### Metodologia Aplicada

A análise segue as melhores práticas de **PMBOK (Project Management Body of Knowledge)**:

- ✅ **Identificação qualitativa** de riscos através de brainstorm e análise
- ✅ **Análise qualitativa** considerando probabilidade, impacto e interdependências
- ✅ **Estratégias de resposta** estruturadas e acionáveis
- ✅ **Comunicação clara** adaptada para diferentes públicos
- ✅ **Monitoramento contínuo** com indicadores de sucesso

### Cenário do Projeto

**Papel:** Gerente de projetos responsável pelo desenvolvimento de uma **ferramenta CLI de geração de senhas seguras**.

**Status:** Projeto em fase intermediária com **4 riscos críticos** identificados:
- Incompatibilidade cross-platform (Windows, Linux, macOS)
- Cobertura de testes inadequada (<80%)
- Equipe sobrecarregada (2 devs + 1 tester)
- Casos extremos não cobertos em validações

**Equipe:** 2 desenvolvedores Python + 1 QA/Tester + você (gerente)

**Desafios:** Requisitos em mudança, pressão por prazos, qualidade de testes abaixo do esperado.

### Como Usar Este Material

1. **Para Aprender a Identificar Riscos:**  
   Leia `docs/risks/identification.md` — veja como 10 riscos foram estruturados em categorias com severidade e probabilidade.

2. **Para Entender Análise Qualitativa:**  
   Estude `docs/risks/analysis.md` — análise de impactos, fatores condicionantes e como riscos se amplificam.

3. **Para Aprender a Responder Riscos:**  
   Consulte `docs/risks/reply.md` — estratégias específicas, ações concretas e plano de implementação.

4. **Para Comunicar com Stakeholders:**  
   Use `docs/comunication/stackholders.md` — modelo de comunicação clara com decisões estruturadas.