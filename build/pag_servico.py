# -*- coding: utf-8 -*-
"""Páginas de serviço. Conteúdo técnico baseado no material da própria SPS."""

from base import (pagina, hero, sec_head, blocos, foto, cta, relacionados, bullets)

# chave: (titulo_aba, descricao, sobrelinha, h1, lead, imagem, alt, blocos, relacionados)
SERVICOS = {

# ------------------------------------------------------------------ DOCUMENTOS
"pgr": dict(
  title="PGR · Programa de Gerenciamento de Riscos | SPS Segurança do Trabalho",
  desc="Elaboração de PGR conforme a NR 1: inventário de riscos, plano de ação e integração com o eSocial. SPS Segurança do Trabalho, litoral catarinense.",
  eyebrow="Documentos legais", h1="PGR",
  sub="Programa de Gerenciamento de Riscos",
  lead="Mais do que uma exigência da NR 1, o PGR é a planta baixa da segurança da sua empresa. "
       "É dele que saem o inventário de riscos, o plano de ação e boa parte do que você declara ao eSocial.",
  img="risco-equipe", alt="Equipe de segurança do trabalho analisando riscos em obra com prancheta",
  blocos=[
    ("O que é o PGR",
     "<p>O PGR (Programa de Gerenciamento de Riscos) é um documento obrigatório exigido pela Norma "
     "Regulamentadora nº 1. Seu objetivo é garantir a saúde e a integridade física dos trabalhadores "
     "por meio da identificação, avaliação e controle dos riscos presentes no ambiente de trabalho.</p>"
     "<p>Na prática, ele deixa de ser papel quando vira rotina: cada risco mapeado ganha um responsável, "
     "um prazo e uma medida de controle que a SPS acompanha junto com você.</p>", None),
    ("Para que serve",
     "", ["Identificar todos os riscos ocupacionais do ambiente de trabalho",
          "Avaliar o nível de exposição dos colaboradores a cada risco",
          "Propor e acompanhar medidas de controle eficazes",
          "Reduzir a ocorrência de acidentes e doenças ocupacionais",
          "Cumprir exigências legais e fiscais, inclusive no eSocial"]),
    ("A estrutura obrigatória",
     "<p>O PGR precisa conter, no mínimo, dois documentos:</p>"
     "<p><strong>1. Inventário de Riscos Ocupacionais</strong>, com as atividades da empresa, os perigos "
     "identificados, a avaliação dos riscos e as medidas preventivas já existentes.</p>"
     "<p><strong>2. Plano de Ação</strong>, onde se definem as ações para eliminar, reduzir ou controlar "
     "cada risco, com responsável e prazo.</p>", None),
    ("Quando precisa ser atualizado",
     "<p>O PGR deve ser revisto sempre que houver:</p>",
     ["Mudança no layout ou no processo de trabalho",
      "Inclusão de novos equipamentos ou substâncias",
      "Ocorrência de acidentes ou incidentes",
      "Alterações nas condições ambientais",
      "No mínimo uma vez por ano, como boa prática preventiva"]),
    ("Quem precisa ter",
     "<p>Toda empresa com empregados sob regime CLT. Micro e pequenas empresas com grau de risco 1 ou 2, "
     "que não expõem trabalhadores a riscos químicos, físicos ou biológicos, podem ser dispensadas desde "
     "que cumpram os critérios do modelo simplificado.</p>"
     "<p>Na dúvida sobre o seu enquadramento, a SPS avalia sem custo antes de propor qualquer escopo.</p>", None),
    ("Como o PGR conversa com os outros documentos",
     "<p>Nenhum documento de SST vive sozinho. O PGR é a base de onde os outros puxam informação:</p>",
     ["<strong>PGR</strong> identifica e gerencia os riscos do ambiente",
      "<strong>PCMSO</strong> monitora a saúde dos trabalhadores com base nesses riscos",
      "<strong>LTCAT</strong> avalia a exposição a agentes nocivos para fins previdenciários",
      "<strong>PPP</strong> registra, individualmente, o histórico de exposição e função"]),
  ],
  rel=[("PCMSO", "O programa médico que nasce dos riscos mapeados no seu PGR.", "pcmso.html"),
       ("LTCAT", "O laudo que comprova exposição a agentes nocivos para a Previdência.", "ltcat.html"),
       ("Engenharia de segurança", "Projetos e PGR específico para canteiro de obra.", "engenharia.html")],
),

"pcmso": dict(
  title="PCMSO · Programa de Controle Médico de Saúde Ocupacional | SPS",
  desc="PCMSO conforme a NR 7: exames admissional, periódico, mudança de função, retorno ao trabalho e demissional, com ASO e envio ao eSocial.",
  eyebrow="Documentos legais", h1="PCMSO",
  sub="Programa de Controle Médico de Saúde Ocupacional",
  lead="Cuidar da saúde do trabalhador é proteger o futuro da sua empresa. O PCMSO é o programa que "
       "transforma os riscos do PGR em exames, prazos e acompanhamento clínico de verdade.",
  img="medico", alt="Médico do trabalho com estetoscópio",
  blocos=[
    ("O que é o PCMSO",
     "<p>O PCMSO é um programa obrigatório previsto pela Norma Regulamentadora nº 7. Seu objetivo é "
     "monitorar e preservar a saúde dos colaboradores por meio de exames clínicos ocupacionais "
     "realizados em diferentes momentos da relação de trabalho.</p>"
     "<p>Ele é planejado, coordenado e executado por um médico do trabalho, e precisa refletir os riscos "
     "reais que o PGR levantou.</p>", None),
    ("Para que serve",
     "<p>O PCMSO é muito mais do que uma exigência legal. Ele permite:</p>",
     ["Acompanhamento clínico contínuo dos colaboradores",
      "Diagnóstico precoce de doenças relacionadas ao trabalho",
      "Adoção de medidas preventivas e corretivas",
      "Redução de afastamentos e acidentes",
      "Suporte à gestão de SST e ao PGR"]),
    ("Os exames previstos",
     "<p>Todos geram o Atestado de Saúde Ocupacional (ASO) e devem ser conduzidos por médico do trabalho "
     "ou profissional habilitado.</p>",
     ["<strong>Admissional</strong> · antes do início das atividades",
      "<strong>Periódico</strong> · conforme função, idade e grau de risco",
      "<strong>Mudança de função</strong> · ao alterar atividades com riscos diferentes",
      "<strong>Retorno ao trabalho</strong> · após afastamentos superiores a 30 dias",
      "<strong>Demissional</strong> · no encerramento do contrato"]),
    ("Vantagens para a sua empresa",
     "", ["Prevenção de passivos trabalhistas e previdenciários",
          "Redução de custos com afastamentos e acidentes",
          "Conformidade com a legislação trabalhista",
          "Valorização da saúde e do bem-estar da equipe",
          "Integração com o PGR, fortalecendo a cultura de segurança"]),
    ("É obrigatório?",
     "<p>Sim. Toda empresa com colaboradores contratados pelo regime CLT deve implementar o PCMSO, "
     "com planejamento, coordenação e execução por um médico do trabalho.</p>", None),
    ("PCMSO e PGR andam juntos",
     "<p>Os dois programas são complementares. O PGR mapeia o risco do ambiente; o PCMSO define qual "
     "exame cada colaborador exposto àquele risco precisa fazer, e com que frequência. Contratar os "
     "dois com a mesma equipe evita a incoerência clássica entre laudo e exame, que é onde a "
     "fiscalização costuma bater.</p>", None),
  ],
  rel=[("Exames ocupacionais", "Admissional, periódico, demissional e ASO na própria unidade.", "exames.html"),
       ("PGR", "O inventário de riscos que dá origem ao seu programa médico.", "pgr.html"),
       ("eSocial", "Envio dos eventos S-2220 sem redigitar informação.", "esocial.html")],
),

"ltcat": dict(
  title="LTCAT · Laudo Técnico das Condições Ambientais do Trabalho | SPS",
  desc="LTCAT elaborado por engenheiro de segurança ou médico do trabalho, para comprovar exposição a agentes nocivos e alimentar o evento S-2240 do eSocial.",
  eyebrow="Documentos legais", h1="LTCAT",
  sub="Laudo Técnico das Condições Ambientais do Trabalho",
  lead="O laudo que a Previdência Social usa para decidir se existe direito à aposentadoria especial. "
       "É medição de campo, não estimativa de escritório.",
  img="ambiente-obra", alt="Trabalhador em frente a equipamento pesado em área de extração",
  blocos=[
    ("O que é o LTCAT",
     "<p>O LTCAT é um documento exigido pela Previdência Social, com base na Lei nº 8.213/91 e no "
     "Decreto nº 3.048/99, utilizado para comprovar a exposição de trabalhadores a agentes nocivos "
     "no ambiente de trabalho.</p>"
     "<p>É a partir dele que se verifica se o trabalhador tem direito à Aposentadoria Especial.</p>", None),
    ("Para que serve",
     "<p>Documentar tecnicamente a presença de agentes físicos, químicos ou biológicos, avaliando se a "
     "exposição está dentro dos limites de tolerância. Com ele é possível:</p>",
     ["Comprovar ou descartar exposição a agentes nocivos",
      "Auxiliar nos processos de aposentadoria especial",
      "Prevenir autuações em fiscalizações previdenciárias",
      "Integrar os dados ao evento S-2240 do eSocial",
      "Complementar o PGR e demais documentos de SST"]),
    ("O que o laudo avalia",
     "<p>O LTCAT é elaborado com base em avaliações ambientais técnicas e deve conter:</p>",
     ["Descrição detalhada das atividades realizadas",
      "Identificação dos agentes nocivos presentes",
      "Avaliação quantitativa e qualitativa da exposição",
      "Equipamentos de proteção utilizados",
      "Conclusão técnica quanto ao direito à aposentadoria especial"]),
    ("Quem pode assinar",
     "<p>O LTCAT deve ser elaborado e assinado por um <strong>Engenheiro de Segurança do Trabalho</strong> "
     "ou <strong>Médico do Trabalho</strong>, devidamente registrados em seus conselhos profissionais "
     "(CREA ou CRM). A SPS mantém os dois perfis em quadro próprio.</p>", None),
    ("Qual a validade",
     "<p>O LTCAT não tem prazo de validade fixo, mas deve ser atualizado sempre que houver mudanças no "
     "ambiente de trabalho, nos processos produtivos ou nas condições de exposição. Recomenda-se revisão "
     "anual para garantir que o laudo reflita a realidade da empresa.</p>", None),
  ],
  rel=[("PPP", "O documento individual que se alimenta do seu LTCAT.", "ppp.html"),
       ("PGR", "Inventário de riscos e plano de ação conforme a NR 1.", "pgr.html"),
       ("eSocial", "S-2240 e os demais eventos de SST enviados sem intermediário.", "esocial.html")],
),

"ppp": dict(
  title="PPP · Perfil Profissiográfico Previdenciário | SPS Segurança do Trabalho",
  desc="PPP digital pelo evento S-2240 do eSocial: histórico individual de exposição a agentes nocivos para fins de aposentadoria especial.",
  eyebrow="Documentos legais", h1="PPP",
  sub="Perfil Profissiográfico Previdenciário",
  lead="O histórico de vida laboral de cada colaborador, exigido pela Previdência. Desde 2023 ele nasce "
       "digital, dentro do eSocial, e só fica correto se o LTCAT por trás estiver em dia.",
  img="documentos", alt="Formulário de registro ocupacional sobre a mesa, com estetoscópio e laptop",
  blocos=[
    ("O que é o PPP",
     "<p>O Perfil Profissiográfico Previdenciário é um documento obrigatório que reúne informações sobre "
     "as condições de trabalho de cada colaborador ao longo do vínculo empregatício, especialmente quanto "
     "à exposição a agentes nocivos à saúde.</p>"
     "<p>É exigido pela Previdência Social conforme o Decreto nº 3.048/99, e serve para comprovar, quando "
     "necessário, o direito à Aposentadoria Especial.</p>", None),
    ("O que consta no documento",
     "", ["Dados da empresa e do trabalhador",
          "Descrição das atividades exercidas",
          "Registros da exposição a agentes físicos, químicos e biológicos",
          "Responsáveis técnicos pelas avaliações ambientais",
          "Informações sobre uso de EPIs e EPCs",
          "Resultados de exames médicos ocupacionais (ASOs)",
          "Assinatura do responsável legal e do profissional de SST"]),
    ("A relação com o LTCAT",
     "<p>O PPP é elaborado com base nas informações contidas no LTCAT. O laudo fornece os dados técnicos "
     "de exposição; o PPP formaliza e individualiza essas informações para cada colaborador.</p>"
     "<p>Por isso, LTCAT desatualizado significa PPP incorreto, e PPP incorreto significa problema na "
     "hora da aposentadoria ou da perícia.</p>", None),
    ("PPP e eSocial",
     "<p>Desde janeiro de 2023 o PPP passou a ser emitido exclusivamente em meio digital, por meio do "
     "evento S-2240 do eSocial. Isso reforça a importância de manter PGR e LTCAT atualizados e "
     "integrados.</p>", None),
    ("Quando deve ser emitido",
     "<p>Todas as empresas com empregados sob regime CLT são obrigadas a manter o PPP atualizado, "
     "especialmente para trabalhadores expostos a riscos. O documento deve ser emitido:</p>",
     ["Durante a vigência do contrato, para fins previdenciários e fiscalizações",
      "Na rescisão contratual, para ser entregue ao colaborador",
      "Em requerimentos de aposentadoria especial ou perícias médicas"]),
  ],
  rel=[("LTCAT", "A base técnica de onde o PPP puxa a exposição.", "ltcat.html"),
       ("eSocial", "Mensageria dos eventos de SST direto da nossa plataforma.", "esocial.html"),
       ("Consultoria técnica", "Assistente de perito e auditoria quando o caso vira processo.", "consultoria.html")],
),

"esocial": dict(
  title="eSocial · Mensageria dos eventos de SST | SPS Segurança do Trabalho",
  desc="Envio dos eventos S-2210, S-2220 e S-2240 ao eSocial a partir da mesma base que gera seus documentos, com acompanhamento de recibo e de rejeição.",
  eyebrow="Documentos legais", h1="eSocial",
  sub="Mensageria dos eventos de SST",
  lead="Seus laudos e exames já vivem na nossa plataforma. O envio ao eSocial sai da mesma base, sem "
       "redigitar informação e sem software intermediário no meio do caminho.",
  img="esocial", alt="Profissional de saúde preenchendo formulário e digitando no laptop",
  blocos=[
    ("O que é o eSocial",
     "<p>O eSocial é um sistema integrado do Governo Federal que unifica o envio de informações fiscais, "
     "previdenciárias e trabalhistas das empresas. Ao substituir diversos formulários e declarações "
     "isoladas, traz mais transparência, segurança jurídica e eficiência na relação entre empresas e "
     "órgãos governamentais.</p>", None),
    ("Por que a SST pesa tanto aqui",
     "<p>A área de Segurança e Saúde no Trabalho ganhou papel de destaque no eSocial. As empresas "
     "precisam enviar informações específicas sobre condições de trabalho, exposição a riscos, exames "
     "ocupacionais e acidentes. Esses dados contribuem para:</p>",
     ["Prevenção de acidentes e doenças ocupacionais",
      "Promoção de ambientes mais seguros e saudáveis",
      "Cumprimento rigoroso da legislação trabalhista e previdenciária"]),
    ("Os três eventos que importam",
     "", ["<strong>S-2210 · CAT</strong> registra os acidentes ocorridos durante o exercício da função, "
          "com data, hora, local e descrição da ocorrência",
          "<strong>S-2220 · Monitoramento da saúde</strong> relaciona todos os exames ocupacionais, "
          "com resultado, data e identificação do profissional responsável",
          "<strong>S-2240 · Condições ambientais</strong> registra a exposição a agentes físicos, "
          "químicos ou biológicos conforme a Tabela 24, base da aposentadoria especial"]),
    ("O que acontece se atrasar",
     "<p>O envio incorreto, fora do prazo, ou a omissão de informações expõe a empresa a multas, "
     "autuações e questionamentos em fiscalização. Pior: costuma aparecer justamente quando existe um "
     "acidente ou um pedido de benefício em análise, no momento de menor margem para corrigir.</p>", None),
    ("Como a SPS resolve",
     "", ["Envio integrado, a partir da mesma base que gera os seus documentos",
          "Acompanhamento de recibo e de rejeição dentro da plataforma",
          "Alerta de pendência antes de o prazo fechar",
          "Sem software de RH intermediário no processo de envio"]),
  ],
  rel=[("Plataforma SPS", "Onde tudo isso é acompanhado, em tempo real.", "plataforma.html"),
       ("PCMSO", "A origem dos eventos S-2220 da sua empresa.", "pcmso.html"),
       ("LTCAT", "A origem técnica do evento S-2240.", "ltcat.html")],
),

# ------------------------------------------------------------------- EXAMES
"exames": dict(
  title="Exames ocupacionais e ASO | SPS Segurança do Trabalho",
  desc="Admissional, periódico, mudança de risco, retorno ao trabalho e demissional. Coleta de sangue, audiometria e ASO nas unidades da SPS ou na sua empresa.",
  eyebrow="Medicina ocupacional", h1="Exames ocupacionais",
  sub="Do admissional ao demissional, com ASO assinado digitalmente",
  lead="Cinco unidades no litoral norte catarinense, unidade móvel para atender dentro da sua operação, "
       "e o ASO disponível na plataforma no mesmo dia.",
  img="consulta", alt="Médico do trabalho realizando consulta e avaliando exames",
  blocos=[
    ("O que é o ASO",
     "<p>O Atestado de Saúde Ocupacional é o documento legal, assinado pelo médico examinador, que "
     "mostra se o trabalhador está apto ou não para exercer suas atividades. Ele é emitido depois de cada "
     "exame clínico ocupacional e é o que a fiscalização pede primeiro.</p>"
     "<p>Na SPS o ASO nasce assinado digitalmente e vai direto para a plataforma, sem impressão e sem "
     "risco de extravio.</p>", None),
    ("Exame admissional <span id=\"admissional\"></span>",
     "<p>Realizado antes do início das atividades. Define se o candidato está apto para a função "
     "pretendida, considerando os riscos que o PGR mapeou para aquele posto de trabalho. É o exame que "
     "protege a empresa de assumir um passivo que já existia.</p>", None),
    ("Exame periódico <span id=\"periodico\"></span>",
     "<p>A frequência depende da função, da idade do colaborador e do grau de risco da atividade. "
     "É no periódico que doenças ocupacionais aparecem cedo, quando ainda dá para agir sem afastamento. "
     "A plataforma avisa o RH antes de cada vencimento.</p>", None),
    ("Mudança de risco <span id=\"mudanca\"></span>",
     "<p>Obrigatório quando o colaborador passa a exercer atividade com riscos diferentes dos anteriores. "
     "Trocar de setor sem refazer o exame é uma das falhas mais comuns e mais caras em auditoria.</p>", None),
    ("Retorno ao trabalho e demissional <span id=\"demissional\"></span>",
     "<p>O retorno é exigido após afastamentos superiores a 30 dias. O demissional encerra o ciclo e "
     "registra o estado de saúde do colaborador na saída, o que costuma ser decisivo em reclamatória "
     "trabalhista.</p>", None),
    ("Exames complementares na própria unidade",
     "<p>Boa parte do que o PCMSO pede é feito sem você precisar mandar o colaborador para outro lugar:</p>",
     ["Coleta de sangue e exames laboratoriais",
      "Audiometria em cabine",
      "Acuidade visual",
      "Exames específicos conforme o risco da função"]),
  ],
  rel=[("PCMSO", "O programa que define quais exames e com que frequência.", "pcmso.html"),
       ("Unidade móvel", "Consultório completo estacionado no seu pátio.", "unidade-movel.html"),
       ("Unidades", "Onde a SPS atende no litoral norte catarinense.", "unidades.html")],
),

"treinamentos": dict(
  title="Treinamentos de NRs | SPS Segurança do Trabalho",
  desc="Turmas de NR 12, NR 18, NR 35 e demais normas regulamentadoras, presenciais ou in company, com instrutores registrados e certificado digital.",
  eyebrow="Capacitação", h1="Treinamentos de NRs",
  sub="Turmas presenciais e in company, com certificado digital",
  lead="Mais de 220 mil certificados emitidos em treze anos. Instrutores registrados, turma montada no "
       "seu cronograma e certificado disponível na plataforma assim que a turma encerra.",
  img="capacete", alt="Trabalhador segurando capacete de segurança",
  blocos=[
    ("Como funciona",
     "<p>Você escolhe entre trazer a equipe até uma das nossas unidades ou receber o instrutor na sua "
     "obra ou fábrica. Nos dois casos a turma é montada conforme a sua escala, não a nossa.</p>"
     "<p>O certificado é emitido digitalmente e fica arquivado por colaborador na plataforma, com "
     "rastreabilidade de quem participou e quando vence a reciclagem.</p>", None),
    ("NR 12 · Máquinas e equipamentos <span id=\"nr12\"></span>",
     "<p>Capacitação para operação segura de máquinas e equipamentos, com foco em proteções, "
     "dispositivos de parada de emergência e procedimentos de manutenção. Indispensável para indústria, "
     "marcenaria, metalurgia e qualquer operação com maquinário.</p>", None),
    ("NR 18 · Construção civil <span id=\"nr18\"></span>",
     "<p>Treinamento admissional e periódico exigido em canteiro de obra, cobrindo os riscos "
     "específicos da atividade e as medidas de proteção coletiva e individual. Anda junto com o PGR de "
     "obra e com os projetos de proteção que a nossa engenharia elabora.</p>", None),
    ("NR 35 · Trabalho em altura <span id=\"nr35\"></span>",
     "<p>Obrigatório para toda atividade executada acima de dois metros do nível inferior com risco de "
     "queda. Inclui parte prática com equipamentos, análise de risco e procedimentos de resgate. É o "
     "treinamento que mais evita fatalidade em obra.</p>", None),
    ("Outras normas atendidas",
     "<p>A SPS monta turma para as demais NRs conforme a necessidade do seu setor, entre elas:</p>",
     ["NR 5 · CIPA", "NR 6 · EPI", "NR 10 · Segurança em eletricidade",
      "NR 17 · Ergonomia", "NR 23 · Brigada de incêndio", "NR 33 · Espaço confinado"]),
  ],
  faixa=("epi-bancada",
         "Capacete, abafador de ruído, óculos de proteção e luvas sobre bancada",
         "Cada turma sai com o EPI certo para o risco que o PGR mapeou, e o registro de entrega "
         "fica na plataforma, como a NR 6 exige."),
  rel=[("Engenharia de segurança", "Projetos de proteção coletiva para trabalho em altura.", "engenharia.html"),
       ("PGR", "O inventário de riscos que define quais treinamentos são obrigatórios.", "pgr.html"),
       ("Consultoria técnica", "Auditoria e acompanhamento de obra.", "consultoria.html")],
),

# --------------------------------------------------------------- ENGENHARIA
"engenharia": dict(
  title="Engenharia de segurança do trabalho | SPS Segurança do Trabalho",
  desc="PGR de obra, projeto de linha de vida, sistemas de ancoragem e projeto elétrico provisório, com ART do engenheiro responsável.",
  eyebrow="Engenharia", h1="Engenharia de segurança",
  sub="Projetos com ART para a sua obra",
  lead="Mais de 350 obras em execução acompanhadas. Quando a proteção precisa de cálculo, memorial e "
       "responsabilidade técnica registrada, o serviço sai daqui.",
  img="altura", alt="Trabalhadores executando serviço em altura sobre estrutura",
  blocos=[
    ("PGR e projetos para a sua obra <span id=\"obra\"></span>",
     "<p>Canteiro de obra tem risco que muda toda semana. O PGR de obra é elaborado considerando as "
     "fases da execução, e revisado conforme o cronograma avança, junto com os projetos de proteção "
     "coletiva que cada etapa exige.</p>", None),
    ("Projeto de linha de vida <span id=\"linha-de-vida\"></span>",
     "<p>Dimensionamento e memorial de cálculo do sistema de linha de vida, horizontal ou vertical, "
     "com definição de pontos, cabos, absorvedores e carga admissível. Entregue com ART do engenheiro "
     "responsável, que é o que a fiscalização pede quando encontra alguém trabalhando em altura.</p>", None),
    ("Sistemas de ancoragem <span id=\"ancoragem\"></span>",
     "<p>Projeto dos pontos de ancoragem estruturais, com verificação da estrutura existente e "
     "especificação dos elementos de fixação. Sem projeto, o ponto de ancoragem é uma aposta, e a "
     "aposta é a vida do trabalhador.</p>", None),
    ("Projeto elétrico provisório <span id=\"eletrico\"></span>",
     "<p>Projeto das instalações elétricas provisórias do canteiro conforme a NR 10 e a NR 18, "
     "incluindo quadros, aterramento, proteção contra choque e dimensionamento de circuitos. "
     "Documento exigido para liberação e para ligação junto à concessionária.</p>", None),
    ("Proteções coletivas",
     "<p>Especificação e detalhamento das proteções que protegem todo mundo ao mesmo tempo, antes de "
     "recorrer ao EPI:</p>",
     ["Guarda-corpo e rodapé em periferia e vãos",
      "Plataformas de proteção",
      "Fechamento de aberturas em laje",
      "Proteção de poço de elevador e escadas"]),
  ],
  rel=[("Treinamento NR 35", "Trabalho em altura, teoria e prática com equipamentos.", "treinamentos.html"),
       ("Consultoria técnica", "Desembargo de obra e assistência em perícia.", "consultoria.html"),
       ("PGR", "O programa de gerenciamento de riscos que ampara o projeto.", "pgr.html")],
),

"consultoria": dict(
  title="Consultoria técnica em SST | SPS Segurança do Trabalho",
  desc="Pacotes Básico, Plus e Premium, auditorias técnicas, assistente de perito e desembargo de obras com a SPS Segurança do Trabalho.",
  eyebrow="Consultoria", h1="Consultoria técnica",
  sub="Acompanhamento contínuo, auditoria e perícia",
  lead="Mais de 365 consultorias simultâneas. Do acompanhamento mensal de rotina ao dia em que a obra "
       "foi embargada e alguém precisa resolver.",
  img="reuniao", alt="Três profissionais discutindo plano de segurança dentro de fábrica",
  blocos=[
    ("Pacotes de acompanhamento",
     "<p>Três níveis de consultoria, definidos pelo porte da empresa e pelo grau de risco da atividade. "
     "O escopo é fechado antes de começar, sem serviço avulso aparecendo na fatura.</p>",
     ["<strong>Básico</strong> · documentação legal em dia e suporte técnico sob demanda",
      "<strong>Plus</strong> · visitas periódicas, acompanhamento de indicadores e treinamentos inclusos",
      "<strong>Premium</strong> · técnico dedicado, gestão completa de SST e resposta prioritária"]),
    ("Auditorias técnicas <span id=\"auditoria\"></span>",
     "<p>Avaliação independente do seu sistema de gestão de SST: o que está documentado, o que está "
     "sendo praticado, e a distância entre as duas coisas. O relatório sai com não conformidades "
     "classificadas por gravidade e um plano de correção com prazo.</p>", None),
    ("Assistente de perito <span id=\"pericia\"></span>",
     "<p>Atuação como assistente técnico da empresa em perícias trabalhistas e previdenciárias. "
     "Acompanhamento da diligência, elaboração de quesitos, análise do laudo pericial e parecer "
     "técnico contrário quando o caso exige.</p>"
     "<p>Ter um assistente na diligência costuma ser a diferença entre um laudo que reflete a realidade "
     "e um que não.</p>", None),
    ("Desembargo de obras <span id=\"desembargo\"></span>",
     "<p>Obra embargada é dinheiro parado todo dia. A SPS levanta os itens que motivaram o embargo, "
     "executa as correções técnicas, monta a documentação comprobatória e acompanha o processo de "
     "liberação junto ao órgão fiscalizador.</p>", None),
    ("Quando faz sentido contratar",
     "", ["A empresa cresceu e a documentação parou no tempo",
          "Houve acidente e existe risco de reclamatória",
          "A fiscalização apareceu e deixou notificação",
          "Existe obra parada ou em vias de ser embargada",
          "O RH não tem a quem perguntar quando a dúvida é técnica"]),
  ],
  rel=[("Engenharia de segurança", "Projetos com ART para regularizar a obra.", "engenharia.html"),
       ("Auditoria documental", "PGR, PCMSO, LTCAT e PPP revisados.", "pgr.html"),
       ("Plataforma SPS", "Indicadores e histórico para sustentar a defesa.", "plataforma.html")],
),

"unidade-movel": dict(
  title="Unidade móvel de exames | SPS Segurança do Trabalho",
  desc="Consultório completo estacionado no seu pátio: exames ocupacionais e treinamentos in company, sem deslocar a equipe nem parar a operação.",
  eyebrow="Atendimento in company", h1="Unidade móvel",
  sub="A SPS vai até a sua operação",
  lead="Um consultório inteiro sobre rodas, estacionado no seu pátio. A equipe não perde o dia de "
       "trabalho no deslocamento e a operação não para para ficar em dia.",
  img="un-itapema", alt="Unidade móvel de exames da SPS estacionada na unidade de Itapema",
  blocos=[
    ("Como funciona",
     "<p>A SPS leva até a sua empresa a estrutura necessária para realizar os exames ocupacionais no "
     "local: consultório, equipamentos e equipe técnica. Você define a data, nós organizamos a fila por "
     "turno para não travar a produção.</p>", None),
    ("Quando compensa",
     "", ["Equipes grandes, em que o deslocamento custa mais que o exame",
          "Obras e operações com turnos que não podem parar",
          "Empresas fora do raio das nossas cinco unidades",
          "Campanhas de periódico concentradas em poucos dias",
          "Admissão em volume, como abertura de obra ou safra"]),
    ("O que é feito no local",
     "", ["Exames clínicos ocupacionais com médico do trabalho",
          "Coleta de sangue e exames laboratoriais",
          "Audiometria em cabine",
          "Acuidade visual",
          "Emissão de ASO assinado digitalmente"]),
    ("Treinamento in company",
     "<p>O mesmo raciocínio vale para as turmas de NR. O instrutor vai até a obra ou a fábrica, monta a "
     "parte prática no ambiente real de trabalho, e o certificado sai pela plataforma no fim da turma.</p>", None),
  ],
  rel=[("Exames ocupacionais", "Todos os tipos de exame e o que cada um resolve.", "exames.html"),
       ("Treinamentos de NRs", "Turmas in company na sua obra ou fábrica.", "treinamentos.html"),
       ("Solicite uma proposta", "Diga o volume e a região, e receba o escopo.", "proposta.html")],
),
}


def gerar():
    saida = []
    for slug, d in SERVICOS.items():
        h1 = '%s<span class="ph__sub">%s</span>' % (d["h1"], d["sub"])
        # foto opcional entre o conteúdo e os relacionados
        faixa = ""
        if d.get("faixa"):
            fslug, falt, fleg = d["faixa"]
            faixa = ('<section class="faixa"><div class="wrap">%s</div></section>'
                     % foto(fslug, falt, fleg, cls="foto--larga",
                            sizes="(max-width:940px) 100vw, 1200px"))
        corpo = "".join([
            hero(d["eyebrow"], h1, d["lead"], d["img"], d["alt"], botoes=[
                '<a class="btn btn--primary" href="proposta.html">Solicitar proposta'
                '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8h11m0 0L9 4m4 4-4 4" fill="none" '
                'stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></a>',
                '<a class="btn btn--ghost" href="solucoes.html">Ver todas as soluções</a>',
            ]),
            '<section class="conteudo"><div class="wrap">%s</div></section>' % blocos(d["blocos"]),
            faixa,
            relacionados(d["rel"]),
            cta(),
        ])
        saida.append(pagina(slug + ".html", d["title"], d["desc"], corpo, active="solucoes"))
    return saida
