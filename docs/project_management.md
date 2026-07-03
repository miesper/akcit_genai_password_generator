# CENÁRIO ADAPTADO: Gerador de Senhas CLI (GenAI)

**Papel:** Você atua como gerente de projetos responsável pelo desenvolvimento de uma **ferramenta CLI de geração de senhas seguras com recursos avançados de personalização**. O sistema inclui funcionalidades como geração de senhas com critérios customizáveis, validação de critérios de força, integração com clipboard, interface CLI amigável e testes automatizados.

**Status do Projeto:** O projeto encontra-se em **fase intermediária de desenvolvimento**, com parte das funcionalidades já implementadas (geração básica, CLI com Click, testes unitários) e outras ainda em progresso (melhorias de UX, validações avançadas, documentação completa).

---

## DESAFIOS IDENTIFICADOS

● **Qualidade e Cobertura de Testes:** A cobertura de testes não atende aos padrões esperados (abaixo de 80%), com gaps identificados na validação de casos extremos (senhas muito grandes, combinações vazias de caracteres, valores inválidos);

● **Requisitos de Validação e Regras de Negócio:** Stakeholders (usuários finais e leads técnicos) solicitaram alterações nos requisitos relacionados a critérios de força mínima de senha, novas regras de validação de entrada e melhorias na robustez do tratamento de erros;

● **Escalabilidade e Manutenibilidade:** A equipe relatou dificuldades em manter a modularidade do código, com acoplamento crescente entre a CLI e a lógica de geração, impactando a capacidade de reutilização e testes unitários.

---

## CONTEXTO ADICIONAL

● **Composição da Equipe:** 
  - 2 desenvolvedores Python
  - 1 QA/Tester
  - Você (gerente de projetos)

● **Dependências Críticas:** 
  - A compatibilidade cross-platform (Windows, Linux, macOS) é crítica para a entrega do MVP
  - A integração com clipboard deve funcionar de forma confiável em todos os SO
