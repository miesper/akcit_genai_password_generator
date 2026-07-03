# Identificação de Riscos — Gerador de Senhas CLI (GenAI)

Análise de riscos baseada no contexto do projeto salvo em `docs/project_management.md`.

---

## 1. Riscos Técnicos

### 1.1 Incompatibilidade Cross-Platform
**Severidade:** Alta | **Probabilidade:** Alta

**Descrição Breve:**  
A integração com clipboard e funcionalidades específicas do SO podem falhar ou se comportar diferentemente em Windows, Linux e macOS, comprometendo a confiabilidade do produto final.

**Contexto:**  
O projeto depende criticamente de compatibilidade cross-platform para o MVP. Diferentes bibliotecas de clipboard têm suporte inconsistente em cada SO. Testes automatizados para múltiplos SO demandam infraestrutura e tempo.

**Impacto Potencial:**  
- Produto não funciona em um ou mais SO
- Necessidade de refatoração em fase avançada
- Retrabalho significativo no código de integração

---

### 1.2 Cobertura de Testes Inadequada
**Severidade:** Alta | **Probabilidade:** Alta

**Descrição Breve:**  
A cobertura de testes abaixo de 80% deixa gaps em casos extremos (senhas muito grandes, combinações vazias, valores inválidos), permitindo bugs em produção.

**Contexto:**  
Validações de entrada com tamanho máximo de 1.000.000 e múltiplas combinações de caracteres criam casos extremos complexos. A equipe pequena (2 desenvolvedores) tem dificuldade em manter cobertura adequada enquanto implementa novas funcionalidades.

**Impacto Potencial:**  
- Falhas não previstas em produção
- Necessidade de patches urgentes
- Perda de confiança do usuário na ferramenta

---

### 1.3 Dificuldades com Integração de Clipboard
**Severidade:** Média | **Probabilidade:** Média

**Descrição Breve:**  
A funcionalidade de copiar a senha para clipboard pode falhar silenciosamente ou depender de bibliotecas externas com suporte inconsistente, afetando a usabilidade.

**Contexto:**  
Clipboard é uma dependência crítica que varia bastante entre SO. Bibliotecas como `pyperclip` têm limitações e requerem fallbacks. Testes unitários para clipboard são complexos.

**Impacto Potencial:**  
- Usuários não conseguem copiar senhas geradas
- Degradação da experiência do usuário
- Aumento de tickets de suporte

---

## 2. Riscos de Requisitos

### 2.1 Mudanças de Requisitos (Scope Creep)
**Severidade:** Alta | **Probabilidade:** Média

**Descrição Breve:**  
Stakeholders solicitam novos requisitos de validação e regras de negócio enquanto o desenvolvimento está em andamento, expandindo o escopo original do MVP.

**Contexto:**  
Requisitos relacionados a critérios de força mínima, validações avançadas e regras de negócio foram solicitados depois do planejamento inicial. Equipe pequena não tem buffer para absorver mudanças sem impactar o prazo.

**Impacto Potencial:**  
- Atraso no cronograma do MVP
- Necessidade de renegociar prazos
- Desalinhamento entre expectativas de stakeholders e capacidade da equipe

---

### 2.2 Complexidade Crescente de Validações
**Severidade:** Média | **Probabilidade:** Alta

**Descrição Breve:**  
Novos critérios de validação e regras de negócio podem introduzir lógica complexa e difícil de testar, aumentando o acoplamento do código.

**Contexto:**  
Validações como "tamanho máximo de 1.000.000", "rejeição de combinações vazias" e "critérios de força" criam branches complexas na lógica. Sem design adequado, isso leva a código monolítico e difícil de manter.

**Impacto Potencial:**  
- Código mais difícil de manter e estender
- Maior tempo de implementação de mudanças futuras
- Risco de regressões

---

## 3. Riscos de Equipe e Recursos

### 3.1 Equipe Pequena Sobrecarregada
**Severidade:** Alta | **Probabilidade:** Alta

**Descrição Breve:**  
Com apenas 2 desenvolvedores e 1 tester, a equipe pode ficar sobrecarregada com a demanda de testes, validações e ajustes, impactando qualidade e prazos.

**Contexto:**  
Gaps em cobertura de testes, novos requisitos de validação e dificuldades em manutenção do código aumentam a carga. Equipes pequenas têm menos flexibilidade para redistribuir trabalho em caso de emergências.

**Impacto Potencial:**  
- Atraso em entregas
- Redução de qualidade por pressa
- Risco de burnout da equipe
- Impossibilidade de lidar com emergências

---

### 3.2 Falta de Documentação de Código
**Severidade:** Média | **Probabilidade:** Média

**Descrição Breve:**  
Documentação inadequada do código torna difícil para novos membros (ou mesmo a equipe atual) entender a lógica, aumentando o tempo de onboarding e correção de bugs.

**Contexto:**  
Projeto em fase intermediária com acoplamento crescente entre CLI e lógica de geração. Sem documentação clara, a manutenção e testes se tornam mais lentos.

**Impacto Potencial:**  
- Tempo maior para correção de bugs
- Dificuldade em escalar a equipe
- Mais tempo gasto em reuniões de alinhamento

---

## 4. Riscos de Qualidade

### 4.1 Casos Extremos Não Cobertos
**Severidade:** Alta | **Probabilidade:** Alta

**Descrição Breve:**  
Senhas muito grandes (próximas ao máximo de 1.000.000), combinações vazias de caracteres e valores inválidos podem não estar cobertos por testes, levando a falhas imprevistas.

**Contexto:**  
A cobertura abaixo de 80% indica gaps em testes. Casos extremos são frequentemente negligenciados em testes unitários iniciais. Com apenas 1 tester para 2 desenvolvedores, validação manual é limitada.

**Impacto Potencial:**  
- Crashes em produção
- Comportamento inesperado para usuários avançados
- Necessidade de patches urgentes

---

### 4.2 Acoplamento Crescente Entre CLI e Lógica de Geração
**Severidade:** Média | **Probabilidade:** Alta

**Descrição Breve:**  
Falta de separação clara entre a interface CLI (Click) e a lógica de geração dificulta testes unitários e reutilização do código.

**Contexto:**  
Projeto em fase intermediária com sinais de acoplamento crescente. Sem refatoração, futuras mudanças na lógica de negócio podem impactar a CLI e vice-versa.

**Impacto Potencial:**  
- Testes unitários mais frágeis
- Dificuldade em reutilizar a lógica de geração em outros contextos
- Maior tempo para implementar mudanças
- Regressões frequentes

---

## 5. Riscos de Cronograma

### 5.1 Atraso na Entrega do MVP
**Severidade:** Alta | **Probabilidade:** Média

**Descrição Breve:**  
Combinação de novos requisitos, gaps em testes e dificuldades de manutenção pode levar a atrasos na entrega do MVP.

**Contexto:**  
Equipe pequena (2 devs + 1 tester), requisitos em mudança, cobertura inadequada de testes e acoplamento de código criam múltiplas fontes de atraso. Sem buffers de tempo, qualquer complicação impacta o cronograma.

**Impacto Potencial:**  
- Atraso na data de lançamento
- Renegociação de prazos com stakeholders
- Possibilidade de perda de mercado ou relevância do produto
- Impacto na reputação do projeto

---

## Resumo de Riscos por Prioridade

| # | Risco | Severidade | Probabilidade | Score |
|---|-------|-----------|--------------|-------|
| 1.1 | Incompatibilidade Cross-Platform | Alta | Alta | 🔴 Crítico |
| 1.2 | Cobertura de Testes Inadequada | Alta | Alta | 🔴 Crítico |
| 2.1 | Mudanças de Requisitos | Alta | Média | 🟠 Alto |
| 3.1 | Equipe Sobrecarregada | Alta | Alta | 🔴 Crítico |
| 1.3 | Integração de Clipboard | Média | Média | 🟡 Médio |
| 2.2 | Complexidade de Validações | Média | Alta | 🟠 Alto |
| 5.1 | Atraso na Entrega | Alta | Média | 🟠 Alto |
| 4.1 | Casos Extremos | Alta | Alta | 🔴 Crítico |
| 4.2 | Acoplamento de Código | Média | Alta | 🟠 Alto |
| 3.2 | Falta de Documentação | Média | Média | 🟡 Médio |

---

**Data de Identificação:** 2026-07-03  
**Responsável:** Análise LLM — GitHub Copilot
