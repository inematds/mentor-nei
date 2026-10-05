# INEMA  VibeCode do Zero - Dia 1 - Infra Git e Vercel

- Tipo: video
- Origem: https://www.youtube.com/watch?v=0UeW1P--sqc
- Arquivo: raw/videos/inema-vibecode-do-zero-dia-1-infra-git-e-vercel.txt

## Resumo
Primeiro dia do curso "VibeCode do Zero", em aula ao vivo (~3 h) com alunos interagindo. Nei apresenta o fluxo completo: ideia → contexto (uma pasta `doc` com material de referência) → plano validado por outro modelo → implementação → testes → commit no GitHub → publicação (GitHub Pages ou Vercel, com Supabase no dia seguinte). Mostra a estrutura de pastas do usuário (`.claude`, `.codex`, `.ssh`, `projetos/`) na máquina local e numa VPS, explica `.gitignore` e `.env`, chave SSH, tokens finos do GitHub, 2FA, Git vs `gh`, GitHub Pages (main + root, inversão da URL para `usuario.github.io/repo`), e no Vercel as três coisas que importam: variáveis de ambiente (com import de `.env`), diretório raiz e domínio. Os alunos criam uma landing page, sobem no GitHub e publicam; ele depura ao vivo um bloqueio de sandbox do Codex ao fazer push via SSH e usa a skill impeccable para criticar um site de aluna. Fecha discutindo custo: Vercel/Supabase dão grátis e cobram na escala, e assinatura sai ~20× mais barata que pagar API no uso pleno.

## Ideias centrais
- Vibe code começa por contexto, não por prompt: "tua intenção, mas ela não pode ser num" (@00:41:08) prompt — "Entrega uma pasta cheia de informações" (@00:41:17).
- A pasta `doc` (privada, fora do git) é a fonte de referência, para a IA não chutar: "informação. Ele não vai chutar buscando" (@00:36:23).
- Com contexto pronto, a instrução fica simples: "simples levou ele a atingir o resultado" (@00:59:53).
- Validar custa mais que criar: "Geralmente o custo maior não é criar, o" (@00:08:40); teste mal especificado queima tokens: "ele vai gastar muitos tokens indo e" (@00:42:25).
- Planejar com esforço alto, implementar com esforço baixo: "e a implementação pode ser na menor, na" (@02:50:41); "dá para alguém que seja operacional, não" (@02:51:55) criativo.
- Segredos não vão pro git; no Vercel as variáveis são configuradas à mão (ou importadas do `.env`): "Como não vai o ponto ENV para o Git, eu" (@01:02:49).
- Plataformas dão grátis e cobram quando escala: "de graça e se teu negócio crescer você" (@01:15:13) tem que bancar.
- Repetir mil vezes justifica transformar raciocínio em script: "certo? E isso tem vantagem se eu repetir" (@02:54:47).
- Assinatura vs API: um modelo aberto "ele teria que ser 20 vezes mais barato" (@03:04:22) para empatar.
- Referências valem mais que templates: "importante de tudo é as referências que" (@02:58:43) tu vai dar para a IA.

## Como ele ensina aqui
- Constrói junto ao vivo: passa o exercício (criar página, jogar pro git, publicar) e acompanha os alunos um a um, abrindo os sites deles e corrigindo o erro na hora (URL invertida, Pages em "none").
- Prefere fundamento a ferramenta: ensina pelo terminal, não pela IDE, para não distrair — "dar camada, eu quero dar fundamento." (@01:55:39).
- Depura ao vivo sem esconder o erro: o push falha por sandbox do Codex, ele pergunta ao próprio agente, entende a causa (workspace-write + never) e cria um `cx2.bat` com acesso total.
- Usa exemplos reais do próprio acervo (INEMA Pro, Lib, promo avatar, painel de uso do Vercel) e mede custo com números (créditos jogados fora, limites do plano, estudo de assinatura vs API).
- Usa IA como revisor duro: pede à skill impeccable "Seja duro. Não quero elogio," (@02:40:44).

## Ligações
- Temas: [[git-e-deploy]], [[infraestrutura-basica]], [[contexto-e-memoria]], [[custo-de-tokens]], [[orquestracao-de-modelos]], [[claude-code]]
- Princípios: [[construir-junto-ao-vivo]], [[menor-custo-que-resolve]], [[verificar-antes-de-afirmar]], [[automatizar-o-repetitivo]], [[criterio-de-pronto-explicito]], [[orquestrar-nao-reinventar]]
- Métodos: [[vibe-code-do-zero]], [[depurar-ao-vivo]], [[live-construindo-ao-vivo]]
