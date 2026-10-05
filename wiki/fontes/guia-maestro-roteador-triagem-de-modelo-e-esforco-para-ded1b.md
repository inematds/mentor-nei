# maestro-roteador — triagem de modelo e esforço para Claude Code

- Tipo: guia
- Origem: https://inematds.github.io/maestro-roteador/guia/
- Arquivo: raw/guia/maestro-roteador-triagem-de-modelo-e-esforco-para--ded1bc.md

## Resumo
Guia de uma skill de Claude Code que, antes de despachar trabalho, decide qual modelo e qual esforço cada parte merece. Separa dois eixos: modelo = repertório (o menor que resolve o pior passo) e esforço = deliberação (ambiguidade + custo do erro). Segue quatro passos fixos, com regras anti-overhead, "risco nomeado = high" e escada de esforço baseada em evidência. Dedica uma seção ao custo escondido do prompt cache (troca de modelo só em fronteira; subagente não toca o cache principal) e outra a "harness > esforço": spec clara e boas ferramentas rendem mais que subir o slider. A skill foi validada contra um baseline medido (sem ela, tudo vira "sonnet + medium"). Conclusão: o meio-termo genérico paga demais no mecânico e de menos no arriscado.

## Ideias centrais
- "O menor modelo que resolve bem esse passo é o escolhido" — nunca por garantia; modelo pelo pior passo.
- Esforço = "Soma ambiguidade + custo do erro."
- "Quando o risco é de correção, não há opção barata."
- Anti-overhead: "Tarefa mais barata que a própria triagem não recebe triagem."
- Escada: "comece baixo e suba só com evidência" — e ela não vale para risco irreversível.
- Cache: "Trocar o /model do turno principal joga fora o cache acumulado." Subagente tem contexto próprio e é o caminho preferido.
- Spec clara vence esforço alto: "Esforço não compensa especificação vaga."
- "Investir no harness rende mais que subir esforço."
- Validação: "sem ela, agentes colapsam qualquer tarefa em" sonnet + medium.

## Como ele ensina aqui
- Ensina com regra + contraexemplo: cada regra vem com a armadilha que evita ("Medium com cuidado" não existe; nada de keepalive artificial).
- Mede antes de afirmar: a skill foi escrita contra baseline (TDD de skill) e o guia ensina o leitor a repetir o teste com e sem a skill.
- Traz números de custo concretos (cache ~12,5× mais caro ao perder 100k de contexto) e dados de terceiros sobre esforço, marcando o que é referência e o que é opinião dele (medium por padrão).
- Entrega saída padronizada (YAML com pior passo e risco por parte) para a decisão ficar auditável.

## Ligações
- Temas: [[orquestracao-de-modelos]], [[custo-de-tokens]], [[skills]], [[subagentes]], [[claude-code]]
- Princípios: [[menor-custo-que-resolve]], [[medir-antes-de-acreditar]], [[criterio-de-pronto-explicito]]
- Métodos: [[triagem-de-modelo-e-esforco]], [[guia-de-projeto-landing]]
