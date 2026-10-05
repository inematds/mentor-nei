# MakeShorts — Fábrica de Shorts com IA

Origem: https://inematds.github.io/makeshorts/guia/

O que é

## Uma fábrica de shorts dentro do Claude Code

MakeShorts é uma skill ( /makeshorts ) com scripts de apoio. Você entrega um tema, um link ou um clipe gravado; ela devolve o short editado, conferido e pronto para agendar.

### 🧩 Orquestra, não reinventa

Chama o que já funciona: HyperFrames para editar, inemavox para voz e transcrição, HeyGen para avatar, Metricool para agendar.

### 📐 Fórmula fixa, tema variável

Todo short segue gancho → gancho secundário → 3 passos → CTA. Três versões de roteiro para você escolher.

### ✅ Qualidade medida

Nada sai sem passar pelo qa_short.py : duração, formato 1080x1920, loudness, gancho visual, hashtags e CTA.

Como funciona

## Sete etapas, um pedido

Cada etapa pode ser feita sozinha (os 5 modos) ou em sequência. As que custam dinheiro ou publicam sempre pedem sua confirmação.

Roteiro → Voz ou avatar → B-roll real → Edição 9:16 → QA → Agendar → Funil de DM

1

### Roteiro

~75 palavras, gancho em 3 s, fatos só de fonte oficial, 3 versões.

2

### Voz / rosto

Gravação humana, voz sintética (local ou API) ou avatar HeyGen.

3

### Edição

Visual em cima, rosto embaixo, legenda palavra a palavra, punch-in e SFX.

4

### Publicação

Legenda com benefício, até 5 hashtags, rótulo de IA, Metricool.

Pré-requisitos

## O que precisa estar na máquina

O básico roda em qualquer Linux ou Mac. GPU e inemavox são opcionais: sem eles, troque os backends por API (veja VPS ).

### Claude Code

Pela assinatura. É onde a skill roda.

```
npm i -g @anthropic-ai/claude-code
```

### ffmpeg + Python + Node

Edição, QA e o motor HyperFrames.

```
sudo apt install -y ffmpeg python3 nodejs
```

### HyperFrames

Motor de edição em HTML → MP4, roda em CPU.

```
npx hyperframes skills update general-video
```

Guia de uso · passo a passo

## Do clone ao primeiro short

Cinco passos. Os comandos são os do repositório, prontos para copiar.

1

### Clone e instale

O instalador confere dependências, liga a skill em ~/.claude/skills/makeshorts (symlink) e cria o .env .

```
git clone https://github.com/inematds/makeshorts.git && cd makeshorts
bash scripts/instalar.sh --check   # só confere
bash scripts/instalar.sh           # instala a skill + cria .env
```

2

### Escolha os backends no .env

Uma linha por etapa. Na máquina com GPU fica tudo local; em outro lugar, troque por API.

```
MS_VOZ=inemavox          # inemavox | edge | openai | elevenlabs
MS_TRANSCRICAO=inemavox  # inemavox | groq | openai
MS_IMAGEM=flux-local     # flux-local | nenhuma
MS_AVATAR=nenhum         # heygen | nenhum
MS_PUBLICAR=metricool   # metricool | manual
```

3

### Peça o short

No Claude Code, chame a skill ou fale naturalmente. Ela descobre o modo pelo pedido.

```
/makeshorts 3 roteiros sobre o Claude Code no celular        # modo roteiro
/makeshorts edita ~/Downloads/clip.mp4                        # modo humano
/makeshorts short sobre https://site-da-ferramenta, sem gravar # modo IA
/makeshorts 5 shorts de IA grátis da semana, um por dia às 18h # modo lote
```

4

### Passe pelo portão de QA

A skill roda sozinha, mas você pode rodar à mão. Exit 1 reprova e diz o que corrigir.

```
python3 .claude/skills/makeshorts/scripts/qa_short.py final.mp4 --caption legenda.txt
✅ duração        31.2s
✅ formato        1080x1920
✅ loudness       -14.1 LUFS
✅ gancho visual  sem tela preta no início
✅ hashtags       4: #claudecode #ia #automacao #shorts
RESULTADO: APROVADO
```

5

### Agende e ligue o funil

A skill monta legenda e hashtags, mostra tudo e só agenda no Metricool depois do seu "pode". O CTA "Comenta IA" vira DM automática com o link (ManyChat, configurado uma vez).

```
/makeshorts publica final.mp4 no Instagram, TikTok e Shorts no melhor horário
```

Rodar numa VPS

## Sem GPU, sem voz local: só muda o .env

Nenhum código muda. Os scripts voz.py e transcreve.py leem o backend do .env e chamam a API certa.

### 🖥️ Máquina com GPU

Voz: inemavox (chatterbox, voz clonada local) · Transcrição: inemavox (Whisper large-v3) · Imagem: flux-local .

### ☁️ VPS

Voz: edge (grátis), openai ou elevenlabs (sua voz clonada) · Transcrição: groq ou openai · Imagem: nenhuma (b-roll real).

```
# .env típico de VPS
MS_VOZ=edge
EDGE_VOZ=pt-BR-AntonioNeural
MS_TRANSCRICAO=groq
GROQ_API_KEY=gsk_...
MS_IMAGEM=nenhuma

# testar cada peça
python3 scripts/voz.py --texto "Teste de voz." --out /tmp/t.mp3
python3 scripts/transcreve.py --in /tmp/t.mp3 --outdir /tmp/tr
```

Instalação completa no Ubuntu, custos de referência e uso com tmux: docs/vps.md .

Exemplos

## A fórmula do roteiro

Um short de 30 segundos, ato por ato. Mesma espinha, qualquer tema.

0–3s

### Gancho

"Tem uma IA nova que edita teus vídeos sozinha."

3–8s

### Gancho secundário

"E não é o CapCut. Nem o Premiere."

8–28s

### Entrega

"Passo 1… passo 2… passo 3…" — direto, sem enrolação.

28s+

### CTA

"Comenta IA que eu te mando o passo a passo."

Roadmap

## O que já existe e o que vem

Descrevemos só o que está no repositório; o resto é plano.

v1 ✅

Skill + QA + backends Skill orquestradora, fórmula de roteiro, spec visual, qa_short.py, voz.py e transcreve.py com backends local/API, guia de VPS.

Próximo

Captura de b-roll automatizada Script próprio para gravar rolagem de site e GitHub em 1080x960, pronto para a metade de cima.

Depois

Painel de métricas Relatório semanal a partir do Metricool: quais ganchos e temas trouxeram mais views e comentários.
