# inemaSEO — seu site em destaque no Google, no Bing e nas IAs

- Tipo: guia
- Origem: https://inematds.github.io/inemaseo-metodo/guia/
- Arquivo: raw/guia/inemaseo-seu-site-em-destaque-no-google-no-bing-e--daa22e.md

## Resumo
Guia do repositório `inemaseo-metodo`: um método de SEO em 10 etapas para ser encontrado no Google, no Bing e nas IAs (ChatGPT, Copilot, Perplexity). Vai da auditoria do HTML entregue pelo servidor até a fundação técnica (um canônico só, sitemaps, robots que libera os robôs das IAs, llms.txt, content-index.json), medição sem a marca, entidade com @id fixo, território por site, conteúdo próprio, hubs e links internos, links de volta, notícias com página e aviso aos buscadores (IndexNow/Bing). Cada etapa tem script pronto (auditoria.sh, gsc_semanal.py, validar_extracao.mjs, link_de_volta.py, avisar_buscadores.sh, gsc_inspecionar.py) e tudo é gratuito. Conta o que foi aplicado no ecossistema INEMA (portal, notícias, eventos) entre setembro e outubro de 2026, a cadência (semana 0, a cada página, semanal, mensal, dia 30–60) e os projetos ligados (WebMCP, AIV 2026, claude-seo).

## Ideias centrais
- Fundação técnica antes de conteúdo: "Sem isso, nenhum conteúdo rende."
- Só dado real, com trava anti-invenção: "O LLM extrai e reescreve; um validador descarta o que não está na fonte."
- A métrica certa é a busca sem a marca: "O número que importa é o de buscas que não têm o seu nome"
- Auditar o HTML real: "Página sem link é página que quase não existe."
- Pauta escolhida por score, sem ferramenta paga: "GO com 6 pontos ou mais, e só se houver um ativo real para citar."
- Mudança em lote com ensaio antes: "Dry-run primeiro; depois --apply --commit ."
- Avisar só o que responde: "Só URLs que respondem 200. O script confere antes e envia ao IndexNow"
- Bing importa para as IAs: "IndexNow e Bing a cada publicação (o ChatGPT e o Copilot usam o índice do Bing)"
- Rotina vence truque: "O SEO paga em semanas e meses, não em dias. A rotina é que faz o resultado."
- Testar se as IAs citam: "Dez perguntas-alvo no ChatGPT e no Perplexity: o seu site é citado?"

## Como ele ensina aqui
- Entrega o método já como ferramenta: cada etapa tem um comando real e a saída esperada no comentário (ex.: `{ apoiada: true, numerosNaFonte: false, ... } → descartar`).
- Fecha o ciclo com verificação: auditoria de novo depois de publicar, inspeção de URL no Search Console, checklist de qualidade antes de publicar.
- Mostra o caso aplicado no próprio ecossistema (fichas de curso, links de volta em lote, páginas por notícia em PT/EN/ES), não um exemplo inventado.
- Plano B por sintoma (sem indexação, sem impressão, sem clique) em vez de esperar melhorar.

## Ligações
- Temas: [[seo-e-sites-para-agentes]], [[git-e-deploy]]
- Princípios: [[medir-antes-de-acreditar]], [[verificar-antes-de-afirmar]], [[menor-custo-que-resolve]], [[automatizar-o-repetitivo]]
- Métodos: [[metodo-seo-10-etapas]], [[guia-de-projeto-landing]]
