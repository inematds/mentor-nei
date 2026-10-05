# musicavideo — música, capa e clipe a partir de uma frase

Origem: https://inematds.github.io/musicavideo/guia/

PT EN ES

O que é

## Planejar é barato. Executar é caro.

Pedir "faz uma música sobre X" pra um agente genérico entrega uma faixa qualquer, uma capa que não conversa com ela e nenhum clipe. Os três saem desconexos porque nunca houve um plano comum. Aqui o plano é o produto.

### 📋 O plano vem primeiro

Um plano.json de esquema fechado decide junto a estrutura da música, o conceito da capa e a decupagem do clipe — olhando um banco de estilos medido de material real (BPM, tom, instrumentação, tipo de voz).

### 🚦 Portão por parte

Cada parte tem seu próprio ciclo: ver → ajusta → ok → faz . Dá pra parar depois de aprovar a capa e voltar três dias depois — o estado.json retoma de onde parou.

### 🔌 Motor é dado, não código

Provedor plugável no padrão adapter + models.json declarativo. Sem chave, ele aparece indisponível com o motivo — nunca estoura na hora de gerar. Trocar é uma flag.

Como funciona

## Quatro fases, e só uma delas gasta

A pesquisa é opt-in. O plano é grátis. A execução é por parte, com o custo estimado na tela antes de qualquer chamada. A entrega é automática quando as três ficam prontas.

pesquisa (opt-in) → plano → ok → faz → PACOTE.md

### 🔎 Fase 0 — pesquisa

Só com --pesquisa . Vai à web ver referências do nicho e se o tema tem tração; vira pesquisa.md e entra como contexto do planejador. Nunca sobrescreve o que você pediu.

### 📝 Fase 1 — plano

Custo zero de API de mídia. Sai plano.json (o contrato) e PLANO.md (pra você ler). Letra pode vir sua: como rascunho , ele termina e mostra o diff; como final , é lei e nem o ajusta mexe.

### 🎛️ Fase 2 — execução

faz só roda o que foi aprovado. Falha de um provedor não derruba a corrida: aquela parte vira erro com a mensagem e as outras seguem (exit 2).

planejado → ok → aprovado → faz → gerando → pronto | erro

Pré-requisitos

## Python da distro e ffmpeg. Só.

Zero dependência pip: tudo em stdlib. As chaves são lidas em runtime dos .env autorizados e nunca copiadas pro repo.

### Sistema

python3 (3.10+) e ffmpeg , usado pra concatenar os shots do clipe.

```
# Debian/Ubuntu
sudo apt install ffmpeg
```

### Capa e clipe — de graça

AGNES_API_KEY dá imagem e vídeo a custo zero. É o default das duas partes, e o motivo de rodar em qualquer VPS.

```
# lida em runtime de:
~/projetos/openpcbotv2/.env
```

### Música — a parte paga

KIE_API_KEY (Suno v4.5), ~US$ 0,08 por geração — que já traz duas faixas.

```
# lida em runtime de:
~/projetos/wifi/.env
```

Guia de uso · passo a passo

## Do texto solto ao pacote pronto

Comandos reais. O caminho normal é com portão; no fim tem o atalho sem portão pra quando você confia no plano.

1

### Instalar

Clone e pronto — não há build nem pip install .

```
git clone https://github.com/inematds/musicavideo.git && cd musicavideo
```

2

### Planejar (não gasta nada)

Solicitação em texto livre. O plano das três partes sai junto, e o PLANO.md aparece na tela.

```
bash musicavideo.sh plano "música de virada, rock feminino, sobre quem constrói em silêncio e agora cobra"
```

3

### Ler cada parte

Sem argumento, mostra o plano inteiro. Com a parte, só a seção dela — estilo e letra, conceito e prompt da capa, ou a decupagem shot a shot.

```
bash musicavideo.sh ver agora-eu-cobro           # o plano inteiro
bash musicavideo.sh ver agora-eu-cobro clipe     # só a decupagem
```

4

### Ajustar o que não ficou bom

Replaneja só aquela parte e imprime o diff do que mudou. Quantas vezes você quiser — nada foi gerado ainda.

```
bash musicavideo.sh ajusta agora-eu-cobro musica "mais lento, e o refrão sobe uma oitava"
```

5

### Aprovar — o portão

Parte sem ok não gera. Aprovar uma não aprova as outras.

```
bash musicavideo.sh ok agora-eu-cobro musica
```

6

### Gerar (aqui gasta)

Mostra o custo estimado por parte e o total antes de chamar qualquer API. Sem a parte, roda tudo que estiver aprovado. --sim pula a confirmação.

```
bash musicavideo.sh faz agora-eu-cobro musica
# custo estimado:
#   musica   US$ 0.0800  (kie:suno-v4.5)
#   total    US$ 0.0800
# confirmar? [s/N]
```

7

### Trazer sua própria letra

Como rascunho, o planejador termina e mostra o diff. Com --letra-final , a letra vai verbatim e ninguém altera — nem o ajusta .

```
bash musicavideo.sh plano "sertanejo" --letra rascunho.txt
bash musicavideo.sh plano "sertanejo" --letra final.txt --letra-final
```

8

### Sem portão, com trava de gasto

Planeja, aprova as três e executa. O teto para antes de estourar: o que coube fica pronto, o resto continua aprovado e retoma com faz .

```
bash musicavideo.sh tudo "balada pop sobre recomeço" --teto 2 --sim
```

9

### Trocar de motor

O motor mora no plano, nunca no código. A flag sobrescreve em plano , ajusta ou faz .

```
bash musicavideo.sh faz agora-eu-cobro clipe --motor clipe=kling:kling-2.5
```

10

### Consultar o acervo

Cada slug vira uma linha no index.jsonl , reescrita a cada mudança de estado. O acervo engorda a cada uso e alimenta o próprio planejador.

```
bash musicavideo.sh lista 10
bash musicavideo.sh busca "rock"
bash musicavideo.sh custo agora-eu-cobro   # estimado vs gasto
```

Do disco para a web

## O clipe pronto não termina na sua máquina

São dois painéis, e é de propósito. O painel local é a bancada: é onde se ouve, se compara, se manda para a lixeira — e onde se aprova o que sai da máquina . A vitrine é o que o público vê. Subir não é consequência de ficar pronto: produção pronta é material de trabalho.

### 🎛️ O painel, sempre de pé

Um serviço do systemd mantém a bancada no ar desde o boot, na rede local. Ficar fora do ar por esquecer de rodar o comando é o defeito, não a economia.

```
systemctl --user enable --now musicavideo-painel
```

### ☁️ Um clique aprova, um comando publica

O publica-hf sobe só o que mudou , escreve o manifesto no repo da vitrine e commita — publicar termina no push, não no meio.

```
bash musicavideo.sh publica-hf
# 0 produções se nada mudou
```

### 📺 Hospedagem que não custa

Os arquivos moram num dataset público no Hugging Face, que serve range request — a barra do vídeo navega direto, sem proxy e sem storage pago. A vitrine só lê o manifesto.

```
bash musicavideo.sh likes   # o ♥ do público volta
```

Motores

## Grátis por padrão, pago por escolha

Os defaults de capa e clipe custam US$ 0 de propósito — é o que faz o projeto rodar em qualquer VPS sem conta em lugar nenhum.

### 🎵 Música

kie:suno-v4.5 — ~US$ 0,08 por geração, traz 2 faixas. A única parte paga hoje.

### 🖼️ Capa

agnes:agnes-image-2.1-flash — US$ 0 . Alternativa: inemaimg:flux2-klein , servidor local no DGX.

### 🎬 Clipe

agnes:agnes-video-v2.0 — US$ 0 , shots concatenados com ffmpeg. Alternativas pagas: kling:kling-2.5 e fal:kling-video-v2.5-turbo-pro .

Adicionar um provedor são dois arquivos: providers/<nome>.py implementando disponivel / estimar_custo / gerar , e providers/<nome>.models.json declarando modelos, custo e params aceitos. Nada mais no projeto muda.

```
# saída de um slug
~/projetos/output/musicavideo/<slug>/
├── plano.json      # o contrato
├── PLANO.md        # o mesmo plano, pra ler e aprovar
├── estado.json     # fonte de verdade: fases, custo, erros, histórico
├── faixa.mp3  capa.png  clipe.mp4
├── PACOTE.md       # entrega (completa ou parcial, com o que falta)
└── raw/            # respostas cruas dos provedores
```

Roadmap

## Onde está e o que vem

O núcleo está fechado e testado. O que falta é largura de provedores e acabamento do clipe.

pronto

Núcleo completo Portão por parte, máquina de estados com retomada, contrato fechado, custo antes de gastar, teto, acervo pesquisável e entrega em PACOTE.md.

pronto

Agnes e Kie exercitados Capa e clipe gerando de graça pelo Agnes; música pelo Suno via Kie.

a testar

Kling e fal Adapters escritos e cobertos por teste de contrato, ainda não exercitados contra a API real.

depois

Pós-edição do clipe Hoje os shots são concatenados sem grading nem mixagem com a faixa. Casar clipe e música no beat é o próximo passo natural.

depois

Acoplar como skill O plano.json é contrato fechado justamente pra outros projetos consumirem sem saber como ele foi feito.
