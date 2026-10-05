# inemaSEO — seu site em destaque no Google, no Bing e nas IAs

Origem: https://inematds.github.io/inemaseo-metodo/guia/

O que é

## Um método, não um truque

Dez etapas que vão do raio-x do site até o aviso aos buscadores, com scripts prontos e modelos que você adapta ao seu site.

### 🧱 Fundação primeiro

Canônico único, sitemaps com idioma, robots que libera as IAs, llms.txt e páginas rasas fora do índice. Sem isso, nenhum conteúdo rende.

### 🧾 Só dado real

Cada página se apoia num curso, projeto, evento ou experimento que existe. O LLM extrai e reescreve; um validador descarta o que não está na fonte.

### 📏 Medido sem a marca

O número que importa é o de buscas que não têm o seu nome: gente que não te conhecia e te achou. O export semanal separa isso.

O método

## As 10 etapas

Na ordem em que aplicamos. O detalhe de cada uma está em docs/METODO.md .

1 Auditoria → 2 Fundação técnica → 3 Medição sem marca → 4 Entidade → 5 Território por site → 6 Conteúdo próprio → 7 Hubs e links internos → 8 Links de volta → 9 Notícias com página → 10 Avisar e acompanhar

### 1 · Auditoria real

Olhe o HTML que o servidor entrega: canônico, hreflang, JSON-LD e quantos links internos existem. Página sem link é página que quase não existe.

### 2 · Fundação técnica

Um canônico só (www ou não), sitemap com lastModified real, robots liberando os robôs das IAs, llms.txt e um manifesto content-index.json por site.

### 3 · Medição sem marca

Export semanal do Search Console separando as buscas pela marca, inspeção de URL e uma meta de conversão no analytics.

### 4 · Entidade

Uma Person e uma Organization com @id fixo, citadas por todas as páginas e por todos os subdomínios.

### 5 · Território por site

Guia evergreen no site principal, novidade no site de notícias, evento no site de eventos. Uma página dona para cada intenção de busca.

### 6 · Conteúdo próprio

Pilares, páginas de pergunta com resposta direta de 40–60 palavras e fichas com dado extraído da página real. Palavra-chave validada por score, sem ferramenta paga.

### 7 · Hubs e links internos

Escada de links a cada página nova e páginas-hub que leem o manifesto dos outros sites. Página de busca mantém um índice de links no HTML.

### 8 · Links de volta

Cada satélite (curso, landing, README) linka a página certa do site principal, em lote e com dry-run.

### 9 · Notícias com página

Uma URL por notícia e idioma, NewsArticle , arquivo que nunca é podado e corpo mínimo escrito só com fatos da fonte.

### 10 · Avisar e acompanhar

IndexNow e Bing a cada publicação (o ChatGPT e o Copilot usam o índice do Bing), sitemap no Search Console e leitura semanal.

Pré-requisitos

## O que você precisa

Tudo gratuito. As contas de busca precisam do site verificado.

### Google Search Console

Propriedade de domínio verificada e o gcloud com credenciais de aplicação, para os scripts de medição.

```
gcloud auth application-default login \
  --scopes=https://www.googleapis.com/auth/webmasters.readonly,\
https://www.googleapis.com/auth/cloud-platform
```

### Bing Webmaster + IndexNow

Site verificado no Bing (pode importar do Search Console) e uma chave IndexNow publicada na raiz do site.

```
# chave pública: https://seusite.com/<chave>.txt
openssl rand -hex 16
```

### Ferramentas locais

git, curl, Python 3 e Node 18+. Um agente de IA (Claude Code ou Codex CLI) para as etapas de extração e redação.

```
git clone https://github.com/inematds/inemaseo-metodo
```

Passo a passo

## Aplicando no seu site

Os comandos são os scripts deste repositório. Troque seusite.com pelo seu domínio.

1

### Faça o raio-x

Redirecionamentos, robots, sitemaps, llms.txt e, por página, título, canônico, hreflang, JSON-LD e links internos no HTML.

```
bash tools/auditoria.sh https://www.seusite.com /catalogo/ /sobre/  # relatório no terminal
```

2

### Corrija a fundação

Use os modelos: templates/robots.txt , templates/llms.txt , templates/content-index.json e templates/jsonld-entidade.json . Canônico, sitemap e JSON-LD com o mesmo host.

```
# depois de publicar, confirme
bash tools/auditoria.sh https://www.seusite.com
```

3

### Comece a medir sem a marca

Rode toda semana. Gera um CSV com as consultas sem a marca e uma linha de resumo por semana e site.

```
export GSC_SITES="sc-domain:seusite.com" GSC_MARCA="seusite|seu nome" GSC_QUOTA_PROJ="seu-projeto-gcp"
python3 tools/gsc_semanal.py --dias 7  # dados/gsc/resumo.csv
```

4

### Escolha as páginas pelo score

Autocomplete, Google Trends, impressões que você já tem e a força do top 10. GO com 6 pontos ou mais, e só se houver um ativo real para citar. Tabela em docs/METODO.md .

```
# consultas com impressão e sem página dedicada = pauta validada
sort -t, -k4 -nr dados/gsc/*_sem-marca.csv | head -30
```

5

### Escreva com trava anti-invenção

O LLM extrai da página real ( templates/prompt-ficha-extrativa.md , templates/prompt-texto-noticia.md ); o validador descarta frase sem apoio na fonte e número que não aparece nela.

```
node tools/validar_extracao.mjs fonte.txt "Curso com 5 módulos e 12 horas"
# { apoiada: true, numerosNaFonte: false, ... }  → descartar
```

6

### Ligue os satélites ao site principal

Um JSON com repo e página de destino. Dry-run primeiro; depois --apply --commit .

```
python3 tools/link_de_volta.py mapa.json --guia https://www.seusite.com/aprender/ --guia-rotulo "Guia completo"
python3 tools/link_de_volta.py mapa.json --apply --commit
```

7

### Publique e avise os buscadores

Só URLs que respondem 200. O script confere antes e envia ao IndexNow e, se houver chave, ao Bing.

```
INDEXNOW_KEY=<chave> BING_API_KEY=<chave> bash tools/avisar_buscadores.sh urls.txt
# IndexNow: HTTP 200 · Bing SubmitUrlBatch: HTTP 200
```

8

### Confira a indexação e repita

Pergunte ao Google o estado de cada página nova; as que não aparecem ganham links internos e um pedido de indexação no painel. Antes de publicar, passe o checklist de qualidade .

```
python3 tools/gsc_inspecionar.py sc-domain:seusite.com https://www.seusite.com/nova-pagina/
# Enviada e indexada | rastreio 2026-10-01 | canônico Google ...
```

Aplicado no INEMA

## O que fizemos no ecossistema

O método rodou no portal (inema.club), no site de notícias e no de eventos entre setembro e outubro de 2026.

### 📚 Fichas com ementa real

Uma página por curso no catálogo; dezenas enriquecidas com módulos extraídos da página de cada curso e validadas contra a fonte.

### 🔗 Links de volta em lote

Os cursos publicados no GitHub Pages passaram a linkar a sua ficha e o guia no site principal.

### 🧭 Pilares e perguntas

Guia "aprender inteligência artificial" em PT, EN e ES, pilares de agentes e de comunidade e páginas de pergunta com resposta direta.

### 🗂️ Hubs de eventos e notícias

Páginas /eventos/ e /noticias/ no site principal, lendo o manifesto de cada subdomínio.

### 📰 Uma página por notícia

Arquivo permanente, NewsArticle , versões PT/EN/ES e corpo escrito só com fatos da fonte; sem texto, noindex .

### 🪪 Uma entidade só

Autor e organização com @id fixo, citados pelo portal, pela base de conhecimento e pelo site de notícias.

Projetos relacionados

## Para ir além: agentes e buscas de IA

O SEO deixa o site ser encontrado. O WebMCP deixa os agentes de IA usarem o site. Os projetos abaixo completam o caminho.

### 🧪 WebMCP Readiness

Teste se o seu site está pronto para agentes de IA: descoberta, manifestos, ferramentas e boas práticas.

webmcp.inema.pro

### 🎓 Formação WebMCP

Cinco cursos, do zero ao expert: sites que conversam com agentes, integração e desenvolvimento de agentes.

Começar pela Formação WebMCP

### 📡 AIV 2026 — AI Visibility

Playbook de AEO/GEO: como ser citado pelas IAs, com o case do INEMA.

Ver o guia do AIV 2026

### 📅 WebMCP nos eventos

A área de WebMCP do Eventos INEMA: prepare seu site para conversar com agentes.

eventos.inema.pro/webmcp

### 🛠️ claude-seo

Skill de análise de SEO para o Claude Code: SEO técnico, conteúdo (E-E-A-T), schema, sitemaps e busca por IA (GEO). Complementa a auditoria da etapa 1.

github.com/inematds/claude-seo

### 🧭 Aprender IA

O guia pilar do INEMA.CLUB, em três idiomas, com trilhas e cursos abertos.

inema.club/aprender-inteligencia-artificial

Cadência

## Quando fazer cada coisa

O SEO paga em semanas e meses, não em dias. A rotina é que faz o resultado.

Semana 0

Auditoria e fundação Raio-x, canônico, sitemaps, robots, llms.txt, entidade e medição ligada.

A cada página

Checklist + escada + aviso Checklist de qualidade, 2–3 páginas antigas apontando para a nova e aviso aos buscadores.

Semanal

Leitura do Search Console Consultas sem marca, páginas com impressão e sem clique, consultas sem página dedicada.

Mensal

Teste nas IAs Dez perguntas-alvo no ChatGPT e no Perplexity: o seu site é citado?

Dia 30–60

Plano B Sem indexação, sem impressão ou sem clique: cada sintoma tem uma resposta (tabela em docs/METODO.md).
