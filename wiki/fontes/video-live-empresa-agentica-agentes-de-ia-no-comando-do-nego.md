# LIVE： Empresa Agêntica - Agentes de IA no Comando do Negócio

- Tipo: video
- Origem: https://www.youtube.com/watch?v=U1pEPovZyfY
- Arquivo: raw/videos/live-empresa-agentica-agentes-de-ia-no-comando-do-negocio.txt

## Resumo
Live em duas partes. Na primeira, a partir de um vídeo do presidente da Vercel, ele apresenta a "empresa agêntica": um agente central que tem o cérebro da empresa, gerencia subagentes, skills e ferramentas, roda por eventos e gatilhos, tem segurança e permissões e passa por melhoria contínua. O líder vira arquiteto, curador de contexto, gestor de autonomia e risco, gestor de skills e treinador de agentes. A segurança vem da identidade (autenticação → identidade → permissões), da classificação dos dados, do human-in-the-loop, de logs e auditoria e de zero confiança, com checagem na ida e na volta. Cita o eve.dev (estrutura de pastas por agente). Na segunda parte, instala ao vivo o Inema CCBot (filas + workers + skills, SQLite, Telegram/BotFather, `.env`) numa VPS limpa e quebra em vários erros (Ubuntu 26 incompatível com dependência, token apagado, chat ID não liberado). Conserta um por um, mostra o fluxo Promo Avatar 3 gerando 36 vídeos com portões de aprovação e promete organizar a instalação.

## Ideias centrais
- Agente central que orquestra a empresa: "um um agente central e esse agente" (@00:01:59)
- Checagem dupla na segurança: "tu tem duas checagens, né, na ida para" (@00:04:45)
- Não depender de um só modelo: "multimodelos, ou seja, eu não dependo da" (@00:07:01)
- Autonomia aos poucos, com mais harness: "esse agente aos poucos ele vai ter mais" (@00:07:28)
- O líder vira curador de contexto: "ser um curador do contexto. É o que que" (@00:09:06)
- Processos viram regras que os agentes acionam: "vão começando virar regras, certo? E os" (@00:12:29)
- Zero confiança: "não deve ter acesso a nada que não tiver" (@00:16:29)
- Instalar com o agente em vez de tentativa e erro: "link para ele e ele instalou tudo para" (@00:27:33)
- Erro ao vivo assumido: "É fácil quando tudo dá certo." (@00:55:27)
- Ambientes de teste separados: "Por isso é bom ter duas, três VPS é pra" (@00:55:51)

## Como ele ensina aqui
- Leva o conceito para a analogia da empresa real (estagiário não recebe acesso a tudo; caixinha de sugestões do 5S) antes de falar de arquitetura.
- Instala do zero numa VPS limpa, na frente da turma, em vez de mostrar uma instalação pronta; quando quebra, lê a mensagem de erro, consulta o agente e vai testando hipóteses (caminhos, comentário no `.env`, token apagado, chat ID).
- Escolhe instalar na mão "para mim identificar os erros", sabendo que o agente resolveria sozinho: usa a falha como material da aula.
- Compara ambientes para achar a causa (Ubuntu 24.04 funcionou, 26 quebrou) e transforma o erro em tarefa de melhoria: criar um arquivo de instalação.
- Mostra o fluxo pronto rodando (36 vídeos com aprovação C53) para provar que o sistema funciona, mesmo com a instalação ao vivo travada.

## Ligações
- Temas: [[agentes-de-ia]], [[subagentes]], [[skills]], [[filas-e-workers]], [[orquestracao-de-modelos]], [[infraestrutura-basica]], [[producao-de-video-com-ia]], [[governanca-e-seguranca-de-agentes]]
- Princípios: [[orquestrar-nao-reinventar]], [[construir-junto-ao-vivo]], [[verificar-antes-de-afirmar]]
- Métodos: [[depurar-ao-vivo]], [[arquitetura-bot-fila-worker-skill]], [[live-construindo-ao-vivo]], [[pipeline-de-video-por-assunto]]
