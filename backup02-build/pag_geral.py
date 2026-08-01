# -*- coding: utf-8 -*-
"""Home, institucionais, unidades e formulários."""

from base import (pagina, hero, sec_head, blocos, foto, cta, relacionados,
                  bullets, imagem, fundo, WPP, TEL, TEL_RAW, MAIL, MENU_SOLUCOES)

# Setores atendidos: ajuda o visitante a se reconhecer antes de ler qualquer
# especificação técnica. Cada item aponta para a solução mais provável.
SETORES = [
  ("Construção civil", "altura",
   "Canteiro com risco que muda a cada etapa. PGR de obra, NR 18, NR 35 e projetos de proteção coletiva "
   "com ART.", "engenharia.html"),
  ("Indústria e metalurgia", "industria",
   "Maquinário, ruído e agentes químicos. NR 12, audiometria, LTCAT e monitoramento contínuo da "
   "exposição.", "ltcat.html"),
  ("Obras e terraplenagem", "ambiente-obra",
   "Equipamento pesado e frente de serviço espalhada. Unidade móvel no canteiro e turmas in company.",
   "unidade-movel.html"),
  ("Comércio e serviços", "esocial",
   "Grau de risco menor, obrigação igual. PCMSO, admissional e periódico sem burocracia para o RH.",
   "exames.html"),
]


def _setores():
    cards = "".join(
        '<a class="setor reveal" style="--d:%.2fs" href="%s">'
        '<div class="setor__foto">%s</div>'
        '<div class="setor__txt"><h3>%s</h3><p>%s</p>'
        '<span class="rel__go">Ver a solução<svg viewBox="0 0 16 16" aria-hidden="true">'
        '<path d="M2 8h11m0 0L9 4m4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.7" '
        'stroke-linecap="round" stroke-linejoin="round"/></svg></span></div></a>'
        % (i * 0.07, href,
           imagem(slug, "", "(max-width:940px) 100vw, 25vw"),
           nome, txt)
        for i, (nome, slug, txt, href) in enumerate(SETORES))
    return '<div class="setor__grid">%s</div>' % cards

MAPA_JS = '<script src="js/map-data.js"></script>'

SOL = [
  ("documentos", "Documentos legais", "pgr.html",
   "PGR, PCMSO, LTCAT, PPP e mensageria eSocial. Documentação elaborada, revisada e entregue no prazo.",
   ["PGR", "PCMSO", "LTCAT", "PPP", "eSocial"],
   '<path d="M8 3h11l6 6v20a1 1 0 0 1-1 1H8a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1Z"/><path d="M19 3v6h6"/><path d="M11 17h10M11 22h7"/>'),
  ("exames", "Exames ocupacionais", "exames.html",
   "Admissional, periódico, mudança de risco e demissional. Coleta de sangue e audiometria na própria unidade.",
   ["Admissional", "Periódico", "Demissional", "ASO"],
   '<path d="M16 28s-11-6.5-11-14a6 6 0 0 1 11-3.3A6 6 0 0 1 27 14c0 7.5-11 14-11 14Z"/><path d="M16 13v6M13 16h6"/>'),
  ("treinamentos", "Treinamentos de NRs", "treinamentos.html",
   "Turmas presenciais e in company com instrutores registrados. Certificado digital direto na plataforma.",
   ["NR 12", "NR 18", "NR 35"],
   '<path d="M16 4 5 9v7c0 6.6 4.5 11.9 11 13 6.5-1.1 11-6.4 11-13V9L16 4Z"/><path d="m11.5 16 3 3 6-6"/>'),
  ("movel", "Unidade móvel", "unidade-movel.html",
   "Consultório completo estacionado no seu pátio. Atendimento na empresa, sem parar a operação.",
   ["In company", "Exames no local"],
   '<path d="M3 21V12h14v9"/><path d="M17 15h5l4 4v2h-9"/><circle cx="9" cy="24" r="2.6"/><circle cx="22" cy="24" r="2.6"/><path d="M6 12V9a2 2 0 0 1 2-2h5"/>'),
  ("engenharia", "Engenharia", "engenharia.html",
   "Linha de vida, ancoragem, elétrico provisório e PGR de obra, com ART do engenheiro responsável.",
   ["Linha de vida", "Ancoragem", "Elétrico"],
   '<path d="M4 27h24"/><path d="M7 27V13l9-8 9 8v14"/><path d="M13 27v-7h6v7"/><path d="M2 15 16 3l14 12"/>'),
  ("consultoria", "Consultoria técnica", "consultoria.html",
   "Auditorias, assistente de perito e desembargo de obras. Pacotes Básico, Plus e Premium.",
   ["Auditoria", "Perícia", "Desembargo"],
   '<circle cx="13" cy="13" r="9"/><path d="m20 20 8 8"/><path d="M9.5 13h7M13 9.5v7"/>'),
]


def _sol_cards():
    out = []
    for i, (_id, tit, href, txt, tags, ico) in enumerate(SOL):
        t = "".join("<li>%s</li>" % x for x in tags)
        out.append(
            '<a class="sol reveal" style="--d:%.2fs" href="%s">'
            '<div class="sol__ico"><svg viewBox="0 0 32 32" aria-hidden="true">%s</svg></div>'
            '<h3>%s</h3><p>%s</p><ul class="sol__tags">%s</ul>'
            '<span class="sol__go">Ver detalhes<svg viewBox="0 0 16 16" aria-hidden="true">'
            '<path d="M2 8h11m0 0L9 4m4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.7" '
            'stroke-linecap="round" stroke-linejoin="round"/></svg></span></a>'
            % (i * 0.07, href, ico, tit, txt, t))
    return '<div class="sol__grid">%s</div>' % "".join(out)


PLATAFORMA_TABS = [
  ("Plataforma web", "Todos os seus documentos, um login",
   "PGR, PCMSO, LTCAT, ASO e certificados ficam organizados por empresa e por colaborador. Consulta em "
   "tempo real, histórico completo e download imediato quando a fiscalização bater na porta.",
   ["Programas e laudos sempre na versão vigente", "Histórico por colaborador e por setor",
    "Acesso separado para cliente, médico e instrutor"]),
  ("Agendamento online", "Marque exames e turmas sem telefonema",
   "O RH agenda exames e treinamentos direto pela plataforma, escolhe a unidade mais próxima e acompanha "
   "as confirmações. Menos e-mail de ida e volta, mais previsibilidade na escala.",
   ["Escolha de unidade e horário pelo próprio RH", "Confirmação e lembrete automáticos",
    "Turmas in company organizadas pelo mesmo painel"]),
  ("Assinatura digital", "Assinou, valeu. Sem impressora.",
   "Assinatura digital em ASO, certificados e ordens de serviço. O documento nasce válido, chega ao "
   "destinatário na hora e fica arquivado sem custo de papel nem risco de extravio.",
   ["ASO e certificados assinados digitalmente", "Zero impressão e zero arquivo morto",
    "Rastreabilidade de quem assinou e quando"]),
  ("Mensageria eSocial", "Eventos de SST no eSocial sem susto",
   "S-2210, S-2220 e S-2240 enviados a partir da mesma base que gera seus documentos. Você acompanha cada "
   "retorno pela plataforma e descobre a inconsistência antes que ela vire multa.",
   ["Envio integrado, sem redigitar informação", "Acompanhamento de recibo e de rejeição",
    "Alerta de pendência antes do prazo fechar"]),
  ("Atendimento in company", "A SPS vai até a sua operação",
   "Unidade móvel de exames e turmas de NR realizadas dentro da sua empresa. Sua equipe não perde o dia "
   "de trabalho no deslocamento e a obra não para para ficar em dia.",
   ["Consultório móvel completo no seu pátio", "Treinamentos de NR na sua obra ou fábrica",
    "Cronograma alinhado com a sua produção"]),
]


def _plataforma():
    tabs, panels = [], []
    for i, (rot, tit, txt, itens) in enumerate(PLATAFORMA_TABS):
        act = " is-active" if i == 0 else ""
        tabs.append('<button class="plat__tab%s" role="tab" aria-selected="%s" aria-controls="p%d" id="t%d">'
                    '<span class="plat__tab-n">%02d</span><span class="plat__tab-t">%s</span></button>'
                    % (act, "true" if i == 0 else "false", i, i, i + 1, rot))
        panels.append('<div class="plat__panel%s" role="tabpanel" id="p%d" aria-labelledby="t%d"%s>'
                      '<h3>%s</h3><p>%s</p>%s</div>'
                      % (act, i, i, "" if i == 0 else " hidden", tit, txt,
                         bullets(itens, "plat__list")))
    return ('<div class="plat"><div class="plat__tabs reveal" role="tablist" '
            'aria-label="Recursos da plataforma">%s</div>'
            '<div class="plat__panels reveal" style="--d:.1s">%s</div></div>'
            % ("".join(tabs), "".join(panels)))


MAPA = """<div class="mapa">
  <div class="mapa__stage" id="mapaStage">
    <div class="mapa__glow" aria-hidden="true"></div>
    <svg class="mapa__svg" id="scmap" viewBox="0 0 1000 640" role="img"
         aria-label="Mapa de Santa Catarina com as cinco unidades da SPS no litoral norte">
      <defs>
        <linearGradient id="gFill" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0" stop-color="#1c7a4b"/><stop offset=".55" stop-color="#14603a"/><stop offset="1" stop-color="#0d4429"/>
        </linearGradient>
        <linearGradient id="gHl" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0" stop-color="#00d068"/><stop offset="1" stop-color="#00a550"/>
        </linearGradient>
        <filter id="fGlow" x="-60%" y="-60%" width="220%" height="220%">
          <feGaussianBlur stdDeviation="7" result="b"/>
          <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
        </filter>
        <filter id="fPin" x="-70%" y="-70%" width="240%" height="240%">
          <feDropShadow dx="0" dy="3" stdDeviation="3.4" flood-color="#001b0d" flood-opacity=".55"/>
        </filter>
      </defs>
      <g id="cam">
        <path id="scFill" class="m-fill" d=""/>
        <path id="scMuni" class="m-muni" d=""/>
        <g id="scHl" class="m-hl"></g>
        <path id="scStroke" class="m-stroke" d=""/>
      </g>
      <g id="scCluster"></g>
      <g id="scPins"></g>
    </svg>
    <div class="mapa__hud">
      <span class="mapa__badge" id="mapaBadge">Santa Catarina</span>
      <div class="mapa__ctrls">
        <button class="mapa__btn" id="btnZoomOut" type="button">Ver o estado</button>
        <button class="mapa__btn" id="btnReplay" type="button" aria-label="Repetir animação do mapa">
          <svg viewBox="0 0 16 16" aria-hidden="true"><path d="M13.5 8a5.5 5.5 0 1 1-1.9-4.2M13.5 1.5V5H10" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </button>
      </div>
    </div>
  </div>
  <aside class="mapa__side">
    <ul class="ucards" id="ucards"></ul>
    <div class="mapa__note">
      <strong>Não achou a sua cidade?</strong>
      <p>A SPS atende toda a região com unidade móvel e equipe in company. Fale com a unidade mais
         próxima e leve o atendimento até a sua empresa.</p>
    </div>
  </aside>
</div>"""


NUMEROS = [
  ("150000", "+", "Exames realizados"), ("220000", "+", "Certificados emitidos"),
  ("100000", "+", "Pessoas atendidas"), ("8000", "+", "Clientes protegidos"),
  ("365", "+", "Consultorias simultâneas"), ("350", "", "Obras em execução"),
]


def _fmt(n):
    return "{:,}".format(int(n)).replace(",", ".")


def _numeros():
    cards = "".join(
        '<article class="ncard reveal" style="--d:%.2fs"><span class="ncard__n" data-count="%s" '
        'data-prefix="%s">%s%s</span><span class="ncard__l">%s</span></article>'
        % (i * 0.06, n, p, p, _fmt(n), rot) for i, (n, p, rot) in enumerate(NUMEROS))
    return '<div class="numeros__grid">%s</div>' % cards


# ------------------------------------------------------------------------ HOME

def home():
    corpo = """
<section class="hero" id="topo">
  <div class="hero__bg">%(hero_img)s</div>
  <div class="hero__veil"></div>
  <div class="hero__grid-lines" aria-hidden="true"></div>
  <div class="wrap hero__inner">
    <div class="hero__card reveal">
      <span class="eyebrow"><i class="dot"></i>Treze anos de litoral catarinense</span>
      <h1>Sua parceira em <em>saúde e segurança</em> do trabalho</h1>
      <p>Medicina ocupacional, engenharia de segurança e treinamentos de NRs em um só lugar. Da
         documentação legal ao exame do colaborador, a SPS cuida de tudo, com plataforma própria e
         envio ao eSocial.</p>
      <div class="hero__actions">
        <a class="btn btn--primary" href="proposta.html">Solicite uma proposta
          <svg viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8h11m0 0L9 4m4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
        <button class="btn btn--ghost js-open-login">Área do cliente</button>
      </div>
    </div>
    <div class="hero__stats">
      <article class="stat reveal" style="--d:.05s">
        <span class="stat__num" data-count="13" data-prefix="">13</span>
        <span class="stat__lbl">Anos protegendo<br>quem trabalha</span></article>
      <article class="stat reveal" style="--d:.15s">
        <span class="stat__num" data-count="5500" data-prefix="+">+5.500</span>
        <span class="stat__lbl">Empresas<br>atendidas</span></article>
      <article class="stat reveal" style="--d:.25s">
        <span class="stat__num" data-count="82000" data-prefix="">82.000</span>
        <span class="stat__lbl">Trabalhadores<br>sob nossos cuidados</span></article>
    </div>
  </div>
  <a class="hero__scroll" href="#numeros" aria-label="Rolar para baixo"><span></span></a>
</section>

<section class="numeros tem-foto" id="numeros">
  %(bg_num)s
  <div class="wrap">
  %(sh_num)s
  %(numeros)s
  </div>
</section>

<section class="setores tem-foto">
  %(bg_set)s
  <div class="wrap">
  %(sh_set)s
  %(setores)s
  </div>
</section>

<section class="solucoes tem-foto" id="solucoes">
  %(bg_sol)s
  <div class="wrap">
  %(sh_sol)s
  %(sol)s
  </div>
</section>

<section class="destaque tem-foto">
  %(bg_des)s
  <div class="wrap destaque__grid">
  <div class="destaque__txt reveal">
    <span class="eyebrow"><i class="dot"></i>Estrutura própria</span>
    <h2>Cinco unidades, frota própria e um consultório sobre rodas</h2>
    <p>A SPS não terceiriza o que é essencial. São cinco unidades no litoral norte catarinense, equipe
       clínica e de engenharia em quadro próprio, frota para atender obra e indústria onde elas estão,
       e uma unidade móvel de exames que estaciona no seu pátio.</p>
    <p>É o que permite fechar um admissional no mesmo dia e resolver uma exigência de fiscalização sem
       depender da agenda de ninguém de fora.</p>
    <a class="btn btn--ghost" href="unidades.html">Conhecer as unidades</a>
  </div>
  <div class="destaque__fotos">
    %(f1)s
    %(f2)s
  </div>
  </div>
</section>

<section class="plataforma tem-foto" id="plataforma">
  %(bg_plat)s
  <div class="wrap">
  %(sh_plat)s
  %(plat)s
  </div>
</section>

<section class="unidades" id="unidades">
  <div class="wrap">
  %(sh_uni)s
  %(mapa)s
  </div>
</section>

<section class="cta tem-foto" id="proposta">
  %(bg_cta)s
  <div class="wrap cta__inner">
  <div class="cta__txt reveal">
    <span class="eyebrow"><i class="dot"></i>Vamos conversar</span>
    <h2>Peça uma proposta e descubra o custo real de estar em dia</h2>
    <p>Conte quantos colaboradores você tem e qual o ramo da empresa. A SPS monta o escopo de documentos,
       exames e treinamentos que a sua operação realmente precisa, sem pacote inflado.</p>
    <div class="cta__actions">
      <a class="btn btn--primary" href="proposta.html">Solicitar proposta
        <svg viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8h11m0 0L9 4m4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
      <a class="btn btn--ghost" href="tel:%(telraw)s">%(tel)s</a>
    </div>
  </div>
  <ul class="cta__list reveal" style="--d:.1s">
    <li><span>01</span>Você conta o cenário da empresa</li>
    <li><span>02</span>A SPS monta o escopo técnico</li>
    <li><span>03</span>Você recebe a proposta fechada</li>
    <li><span>04</span>A equipe assume tudo e você acompanha pela plataforma</li>
  </ul>
</div></section>
""" % {
        "bg_set": fundo("epi-bancada", "sutil"),
        "bg_des": fundo("industria", "sutil"),
        "bg_num": fundo("capacete", "media"),
        "bg_plat": fundo("documentos", "leve"),
        "bg_cta": fundo("executivo", "leve"),
        "bg_sol": fundo("risco-equipe", "sutil"),
        "hero_img": imagem("un-corporativo", "Sede corporativa da SPS em Itapema com a frota",
                           "100vw", prioridade=True),
        "sh_set": sec_head("Quem a SPS protege", "Cada setor tem um risco, e uma obrigação diferente",
                           "Se a sua operação está aqui, já sabemos por onde começar.", center=True),
        "setores": _setores(),
        "sh_num": sec_head("Treze anos em números", "Segurança que se mede",
                           "Cada número aqui é uma empresa em conformidade, uma obra liberada e um "
                           "trabalhador que voltou para casa.", center=True),
        "numeros": _numeros(),
        "sh_sol": sec_head("Conheça nossas soluções", "Tudo o que a sua empresa precisa em SST",
                           "Seis frentes que se conversam. Você contrata uma equipe inteira, não um "
                           "serviço avulso."),
        "sol": _sol_cards(),
        "f1": foto("frota", "Frota de veículos da SPS em frente a uma das unidades", cls="foto--a"),
        "f2": foto("un-itapema", "Unidade móvel de exames da SPS estacionada em Itapema", cls="foto--b"),
        "sh_plat": sec_head("Eficiência e tecnologia em SST",
                            "A sua empresa em conformidade, em tempo real",
                            "Programas, laudos e certificados dentro de uma plataforma só. Agende exames "
                            "e treinamentos, assine digitalmente e acompanhe cada envio ao eSocial, sem "
                            "imprimir uma folha."),
        "plat": _plataforma(),
        "sh_uni": sec_head("Unidades Grupo SPS", "Descubra a SPS mais próxima de você",
                           "Cinco unidades no litoral norte catarinense, de Balneário Piçarras a Porto "
                           "Belo. Escolha um ponto no mapa para ver o endereço e traçar a rota.",
                           center=True),
        "mapa": MAPA, "tel": TEL, "telraw": TEL_RAW,
    }
    return pagina("index.html",
                  "SPS Segurança do Trabalho | Medicina Ocupacional, Engenharia e Treinamentos em SST",
                  "Há 13 anos cuidando de quem faz sua empresa acontecer. Medicina ocupacional, "
                  "engenharia de segurança do trabalho e treinamentos de NRs no litoral catarinense. "
                  "5 unidades, +5.500 empresas atendidas.",
                  corpo, active="", scripts=MAPA_JS)


# ----------------------------------------------------------------------- SOBRE

LINHA = [
  ("2013", "Primeira unidade em Itapema"), ("2014", "Segunda unidade em Itapema"),
  ("2016", "Terceira unidade em Itapema"), ("2018", "Quarta unidade em Itapema"),
  ("2019", "Unidade em Itajaí"), ("Pandemia", "Tenda de treinamentos"),
  ("2020", "Ampliação da unidade em Itapema"), ("2020", "Corporativo 226"),
  ("2021", "Unidade em Balneário Piçarras"), ("2023", "Nova unidade em Itajaí"),
  ("2024", "Nova unidade em Balneário Piçarras"), ("2025", "Unidade em Porto Belo"),
  ("2025", "Novo Corporativo"),
]

PILARES = [
  ("missao", "Missão",
   "Promover um ambiente de trabalho seguro, através de soluções em Segurança, Medicina e Engenharia "
   "do Trabalho de forma contínua e dedicada, identificando riscos, implementando soluções e treinando "
   "equipes, contribuindo assim para um ambiente mais seguro e produtivo."),
  ("visao", "Visão",
   "Ser referência na prestação dos serviços de Segurança e Medicina do Trabalho, oferecendo soluções "
   "inovadoras e personalizadas, buscando ser a principal escolha de nossos clientes pela competência, "
   "eficiência, agilidade e qualidade de nossos serviços e produtos."),
  ("valores", "Valores",
   "Responsabilidade, ética, qualidade, valorização das pessoas, credibilidade e agilidade no "
   "atendimento, garantindo os melhores serviços e produtos para a melhoria da qualidade de vida dos "
   "colaboradores e a satisfação dos nossos clientes."),
  ("proposito", "Propósito",
   "Transformar ambientes de trabalho em espaços seguros e saudáveis. Acreditamos que promover a saúde "
   "e a segurança contribui diretamente para o bem-estar dos trabalhadores e o sucesso das empresas, "
   "gerando resultados no âmbito profissional e humano."),
]

ICO_PILAR = {
  "missao": '<path d="M16 4v24M4 16h24"/><circle cx="16" cy="16" r="11"/><circle cx="16" cy="16" r="4"/>',
  "visao": '<path d="M2 16s5-8 14-8 14 8 14 8-5 8-14 8-14-8-14-8Z"/><circle cx="16" cy="16" r="4.5"/>',
  "valores": '<path d="m16 4 3.7 7.6 8.3 1.2-6 5.9 1.4 8.3-7.4-4-7.4 4 1.4-8.3-6-5.9 8.3-1.2Z"/>',
  "proposito": '<path d="M16 28s-11-6.5-11-14a6 6 0 0 1 11-3.3A6 6 0 0 1 27 14c0 7.5-11 14-11 14Z"/>',
}


def sobre():
    marcos = "".join(
        '<li class="tl__item reveal" style="--d:%.2fs"><picture>'
        '<source type="image/webp" srcset="img/linha/m%02d.webp">'
        '<img src="img/linha/m%02d.jpg" alt="%s, %s" loading="lazy" decoding="async" '
        'width="600" height="450"></picture></li>'
        % ((i % 4) * 0.06, i + 1, i + 1, ano, txt)
        for i, (ano, txt) in enumerate(LINHA))

    pilares = "".join(
        '<article class="pilar reveal" style="--d:%.2fs">'
        '<div class="pilar__ico"><svg viewBox="0 0 32 32" aria-hidden="true">%s</svg></div>'
        '<h3>%s</h3><p>%s</p></article>'
        % (i * 0.07, ICO_PILAR[k], t, x) for i, (k, t, x) in enumerate(PILARES))

    corpo = "".join([
        hero("Sobre nós", 'Treze anos construindo segurança<span class="ph__sub">A história da SPS, de 2013 até aqui</span>',
             "O que começou como uma sala em Itapema em 2013 hoje são cinco unidades, frota própria e "
             "mais de 82 mil trabalhadores sob cuidado.",
             "engenheiro", "Engenheiro de segurança do trabalho com capacete em canteiro de obra"),

        '<section class="conteudo"><div class="wrap">%s</div></section>' % blocos([
            ("Como a SPS começou",
             "<p>A SPS nasceu em 2013, em Itapema, com uma ideia simples e nada modesta: fazer segurança "
             "do trabalho de um jeito que a empresa cliente conseguisse acompanhar. Naquela época, o "
             "normal do setor era entregar um calhamaço de laudo uma vez por ano e sumir.</p>"
             "<p>A primeira unidade era pequena. A segunda veio em 2014, a terceira em 2016 e a quarta em "
             "2018, todas ainda em Itapema, porque a demanda crescia mais rápido que o espaço.</p>", None),
            ("O salto para a região",
             "<p>Em 2019 a SPS cruzou a fronteira da cidade e abriu em Itajaí. Veio a pandemia, e com ela "
             "a tenda de treinamentos montada para não parar as turmas obrigatórias em plena crise "
             "sanitária. Em 2020 a unidade de Itapema foi ampliada e nasceu o Corporativo 226.</p>"
             "<p>De 2021 a 2025 vieram Balneário Piçarras, a nova unidade de Itajaí, a nova de Piçarras, "
             "Porto Belo e o novo Corporativo. Cinco cidades, cinco estruturas, uma equipe.</p>", None),
            ("O que mudou e o que não mudou",
             "<p>Mudou a escala: são mais de 150 mil exames, 220 mil certificados e 8 mil clientes "
             "protegidos. Mudou a tecnologia: hoje o cliente acompanha tudo por plataforma, assina "
             "digitalmente e envia ao eSocial sem intermediário.</p>"
             "<p>Não mudou o motivo. Cada laudo aqui existe para que alguém volte inteiro para casa no "
             "fim do turno.</p>", None),
        ]),

        '<section class="linha"><div class="wrap">%s<ul class="tl">%s</ul></div></section>'
        % (sec_head("Linha do tempo", "Treze anos, treze marcos",
                    "De uma sala em Itapema ao novo corporativo, sem pular nenhuma etapa.", center=True),
           marcos),

        '<section class="pilares tem-foto">%s<div class="wrap">%s<div class="pilares__grid">%s</div></div></section>'
        % (fundo("engenheiro", "sutil"),
           sec_head("O que nos guia", "Missão, visão, valores e propósito", center=True), pilares),

        '<section class="numeros tem-foto">%s<div class="wrap">%s%s</div></section>'
        % (fundo("capacete", "media"),
           sec_head("Treze anos em números", "Segurança que se mede", center=True), _numeros()),

        cta("Quer conhecer a SPS de perto?",
            "Agende uma visita a uma das nossas unidades ou peça uma proposta para a sua empresa. "
            "A conversa começa entendendo a sua operação, não vendendo pacote."),
    ])
    return pagina("sobre.html", "Sobre nós | SPS Segurança do Trabalho",
                  "A história da SPS Segurança do Trabalho: treze anos, cinco unidades no litoral norte "
                  "catarinense, missão, visão, valores e propósito.",
                  corpo, active="sobre")


# -------------------------------------------------------------------- SOLUÇÕES

def solucoes():
    listas = "".join(
        '<div class="idx__col reveal" style="--d:%.2fs"><h3>%s</h3><ul>%s</ul></div>'
        % (i * 0.06, titulo, "".join('<li><a href="%s">%s</a></li>' % (h, t) for t, h in itens))
        for i, (titulo, itens) in enumerate(MENU_SOLUCOES))

    corpo = "".join([
        hero("Soluções", 'Soluções completas em SST<span class="ph__sub">Uma equipe para tudo, não um serviço avulso</span>',
             "Documentos legais, medicina ocupacional, treinamentos, engenharia e consultoria. Tudo com a "
             "mesma equipe, o que evita a incoerência clássica entre o laudo e o exame.",
             "epi", "Capacete, abafador e colete de segurança do trabalho",
             botoes=['<a class="btn btn--primary" href="proposta.html">Solicitar proposta</a>',
                     '<a class="btn btn--ghost" href="%s" target="_blank" rel="noopener">Chamar no WhatsApp</a>' % WPP]),

        '<section class="solucoes"><div class="wrap">%s%s</div></section>'
        % (sec_head("Seis frentes", "Escolha por onde começar",
                    "Cada frente tem uma página com o detalhe técnico, a obrigatoriedade legal e o que "
                    "a SPS entrega na prática.", center=True), _sol_cards()),

        '<section class="indice tem-foto">%s<div class="wrap">%s<div class="idx__grid">%s</div></div></section>'
        % (fundo("documentos", "sutil"),
           sec_head("Índice completo", "Todos os serviços, um a um", center=True), listas),

        cta(),
    ])
    return pagina("solucoes.html", "Soluções em SST | SPS Segurança do Trabalho",
                  "Documentos legais, exames ocupacionais, treinamentos de NRs, engenharia de segurança "
                  "e consultoria técnica com a SPS Segurança do Trabalho.",
                  corpo, active="solucoes")


# ------------------------------------------------------------------ PLATAFORMA

def plataforma():
    corpo = "".join([
        hero("Diferenciais", 'Tecnologia que vira tempo livre<span class="ph__sub">Da agenda do RH ao recibo do eSocial, em um lugar só</span>',
             "Plataforma própria, assinatura digital, mensageria direta ao eSocial e uma equipe que "
             "atende dentro da sua operação quando é preciso.",
             "industria", "Engenheira de segurança em ambiente industrial automatizado"),

        '<section class="plataforma"><div class="wrap">%s%s</div></section>'
        % (sec_head("Eficiência e tecnologia em SST", "A sua empresa em conformidade, em tempo real",
                    "Programas, laudos e certificados dentro de uma plataforma só."), _plataforma()),

        '<section class="conteudo"><div class="wrap">%s</div></section>' % blocos([
            ("Acesso separado por perfil",
             "<p>Cliente, médico, instrutor e equipe de inspeção entram por painéis diferentes, cada um "
             "vendo apenas o que lhe compete. O RH da sua empresa não navega em prontuário, e o médico "
             "não mexe em contrato.</p>", None),
            ("Área do colaborador",
             "<p>O item 1.4.1 da NR 1 obriga o empregador a informar ao trabalhador os riscos do posto, "
             "as medidas de prevenção adotadas e os resultados dos seus próprios exames.</p>"
             "<p>Em vez de imprimir e colher assinatura em papel, o colaborador consulta pela própria "
             "plataforma, e fica registrado que ele consultou.</p>", None),
            ("Segurança e LGPD",
             "<p>Dado de saúde é dado sensível pela Lei Geral de Proteção de Dados. O acesso é "
             "segmentado por perfil, cada consulta fica registrada, e os documentos carregam validação "
             "que permite conferir autenticidade sem expor o conteúdo.</p>", None),
            ("Indicadores que servem para decidir",
             "<p>Absenteísmo, exames vencendo, treinamentos a reciclar, pendências de eSocial. O painel "
             "mostra o que está para vencer antes de virar problema, que é a única hora em que esse tipo "
             "de informação vale alguma coisa.</p>", None),
        ]),

        relacionados([
            ("eSocial", "Como funciona a mensageria dos eventos de SST.", "esocial.html"),
            ("Exames ocupacionais", "Agendamento, ASO digital e histórico por colaborador.", "exames.html"),
            ("Unidades", "Onde a SPS atende, com mapa e rotas.", "unidades.html"),
        ]),
        cta(),
    ])
    return pagina("plataforma.html", "Diferenciais e plataforma | SPS Segurança do Trabalho",
                  "Plataforma web própria, área do colaborador conforme a NR 1, assinatura digital, "
                  "mensageria eSocial e conformidade com a LGPD.",
                  corpo, active="plataforma")


# -------------------------------------------------------------------- UNIDADES

UNIDADES_INFO = [
  ("Corporativo", "un-corporativo", "Rua 406B, nº 883", "Morretes, Itapema/SC", "88.220-000",
   "Sede administrativa e comercial. É daqui que saem as propostas, os contratos e a coordenação técnica "
   "das cinco unidades.",
   "https://www.google.com/maps/place/SPS+Seguran%C3%A7a+do+Trabalho+-+Corporativo/@-27.1207719,-48.6263447,16z"),
  ("Itapema", "un-itapema", "Rua 434, nº 88", "Morretes, Itapema/SC", "88.220-000",
   "Unidade de exames e treinamentos, base da unidade móvel e da frota que atende obra e indústria na "
   "região.",
   "https://www.google.com/maps/place/SPS+Seguran%C3%A7a+do+Trabalho+-+Unidade+Itapema/@-27.1235166,-48.6132515,17z"),
  ("Porto Belo", "un-portobelo", "Av. Atílio Fontana, nº 387", "Perequê, Porto Belo/SC", "88.210-000",
   "Inaugurada em 2025, atende exames e treinamentos de toda a península de Porto Belo e Bombinhas.",
   "https://www.google.com/maps/place/SPS+treinamentos+e+exames/@-27.1559858,-48.5657683,17z"),
  ("Itajaí", "un-itajai", "Av. Ver. Abrahão João Francisco, nº 3820", "Ressacada, Itajaí/SC", "88.301-335",
   "Atende o polo portuário e industrial de Itajaí e Navegantes, com estrutura completa de exames "
   "ocupacionais.",
   "https://www.google.com/maps/place/SPS+SEGURAN%C3%87A+DO+TRABALHO+UN.+ITAJA%C3%8D%2FSC/@-26.9293605,-48.6851534,17z"),
  ("Balneário Piçarras", "un-picarras", "Rua 1240, nº 153", "Centro, Balneário Piçarras/SC", "88.380-000",
   "A unidade mais ao norte da rede, atendendo Piçarras, Penha e Barra Velha.",
   "https://www.google.com/maps/place/SPS+SEGURAN%C3%87A+DO+TRABALHO+UN.+BALNE%C3%81RIO+PI%C3%87ARRAS/@-26.7624756,-48.6761676,17z"),
]


def unidades():
    cards = "".join(
        '<article class="uni reveal" style="--d:%.2fs">'
        '<div class="uni__foto">%s</div>'
        '<div class="uni__txt"><h3>%s</h3><p class="uni__desc">%s</p>'
        '<dl class="uni__dados">'
        '<div><dt>Endereço</dt><dd>%s<br>%s<br>CEP %s</dd></div>'
        '<div><dt>Telefone</dt><dd><a href="tel:%s">%s</a><br><a href="%s" target="_blank" rel="noopener">(47) 99239-8519</a></dd></div>'
        '<div><dt>Atendimento</dt><dd>Segunda a sexta<br>07h às 12h &middot; 13h às 17h</dd></div>'
        '</dl>'
        '<a class="btn btn--ghost" href="%s" target="_blank" rel="noopener">Traçar rota'
        '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M6 3h7v7M13 3 3.5 12.5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></a>'
        '</div></article>'
        % (i * 0.05, imagem(img, "Fachada da unidade da SPS em %s" % nome,
                            "(max-width:940px) 100vw, 45vw"),
           nome, desc, end, bairro, cep, TEL_RAW, TEL, WPP, maps)
        for i, (nome, img, end, bairro, cep, desc, maps) in enumerate(UNIDADES_INFO))

    corpo = "".join([
        hero("Unidades Grupo SPS", 'Onde a SPS atende<span class="ph__sub">De Balneário Piçarras a Porto Belo</span>',
             "Cinco unidades no litoral norte catarinense, de Balneário Piçarras a Porto Belo, mais "
             "unidade móvel para atender dentro da sua empresa.",
             "un-picarras", "Fachada da unidade da SPS em Balneário Piçarras"),

        '<section class="unidades tem-foto">%s<div class="wrap">%s%s</div></section>'
        % (fundo("engenheiro", "leve"),
           sec_head("No mapa", "Onde a SPS atende",
                    "Escolha um ponto no mapa ou um card ao lado para ver o endereço e traçar a rota.",
                    center=True), MAPA),

        '<section class="unilista"><div class="wrap">%s<div class="uni__grid">%s</div></div></section>'
        % (sec_head("Uma a uma", "Endereço, telefone e horário",
                    "Todas as unidades atendem de segunda a sexta, das 07h às 12h e das 13h às 17h.",
                    center=True), cards),

        relacionados([
            ("Unidade móvel", "Quando compensa levar o consultório até você.", "unidade-movel.html"),
            ("Exames ocupacionais", "O que é feito em cada unidade.", "exames.html"),
            ("Solicite uma proposta", "Diga a região e o volume, receba o escopo.", "proposta.html"),
        ]),
        cta(),
    ])
    return pagina("unidades.html", "Unidades | SPS Segurança do Trabalho",
                  "Cinco unidades da SPS no litoral norte de Santa Catarina: Itapema, Porto Belo, "
                  "Itajaí e Balneário Piçarras. Endereços, telefones e rotas.",
                  corpo, active="unidades", scripts=MAPA_JS)


# ----------------------------------------------------------------- FORMULÁRIOS

def _campo(id_, rot, tipo="text", req=True, ph="", opcoes=None, linhas=0):
    r = ' required' if req else ''
    marca = ' <span class="req" aria-hidden="true">*</span>' if req else ' <small>(opcional)</small>'
    if opcoes:
        op = "".join('<option value="%s">%s</option>' % (o, o) for o in opcoes)
        campo = '<select id="%s" name="%s"%s><option value="" disabled selected>Selecione</option>%s</select>' % (id_, id_, r, op)
    elif linhas:
        campo = '<textarea id="%s" name="%s" rows="%d" placeholder="%s"%s></textarea>' % (id_, id_, linhas, ph, r)
    else:
        campo = '<input type="%s" id="%s" name="%s" placeholder="%s"%s>' % (tipo, id_, id_, ph, r)
    return '<div class="campo"><label for="%s">%s%s</label>%s</div>' % (id_, rot, marca, campo)


def proposta():
    form = """<form class="form reveal" id="formProposta" novalidate>
      <div class="form__grid">
        %s %s %s %s %s %s
      </div>
      %s
      <div class="form__acoes">
        <button class="btn btn--primary" type="submit">Enviar pelo WhatsApp
          <svg viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8h11m0 0L9 4m4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
        <p class="form__nota">Ao enviar, abrimos o WhatsApp da SPS com os dados já preenchidos.
           Nada é armazenado neste site.</p>
      </div>
    </form>""" % (
        _campo("empresa", "Empresa"),
        _campo("nome", "Seu nome"),
        _campo("email", "E-mail", "email", ph="voce@empresa.com.br"),
        _campo("fone", "Telefone ou WhatsApp", "tel", ph="(47) 90000-0000"),
        _campo("cidade", "Cidade"),
        _campo("func", "Nº de colaboradores", opcoes=["1 a 10", "11 a 50", "51 a 100",
                                                      "101 a 300", "Mais de 300"]),
        _campo("msg", "O que a sua empresa precisa?", req=False, linhas=4,
               ph="Ex.: somos uma construtora com 40 funcionários, precisamos de PGR, PCMSO e NR 35."),
    )

    corpo = "".join([
        hero("Solicite uma proposta", 'Vamos entender a sua operação<span class="ph__sub">A conversa começa pelo seu cenário, não pelo preço</span>',
             "Sem pacote pronto. A SPS monta o escopo a partir do seu ramo, do número de colaboradores "
             "e do grau de risco da atividade.",
             "executivo", "Executivo do setor da construção com colete de segurança"),

        '<section class="formsec tem-foto">%s<div class="wrap form__grid-out">'
        '<div class="form__lado reveal">%s%s%s</div><div class="form__box">%s</div>'
        '</div></section>' % (
            fundo("executivo", "sutil"),
            '<span class="eyebrow"><i class="dot"></i>Como funciona</span>'
            '<h2>Da conversa à proposta em quatro passos</h2>',
            '<ol class="passos">'
            '<li><span>01</span><div><strong>Você conta o cenário</strong>'
            '<p>Ramo, número de colaboradores, cidade e o que já existe de documentação.</p></div></li>'
            '<li><span>02</span><div><strong>A SPS monta o escopo</strong>'
            '<p>Definimos quais documentos, exames e treinamentos são obrigatórios para o seu caso.</p></div></li>'
            '<li><span>03</span><div><strong>Você recebe a proposta fechada</strong>'
            '<p>Valor por item e valor do pacote, sem surpresa depois.</p></div></li>'
            '<li><span>04</span><div><strong>A equipe assume</strong>'
            '<p>Você acompanha tudo pela plataforma, inclusive os envios ao eSocial.</p></div></li>'
            '</ol>',
            '<div class="form__contato"><p>Prefere falar direto?</p>'
            '<a class="btn btn--ghost" href="tel:%s">%s</a> '
            '<a class="btn btn--ghost" href="mailto:%s">%s</a></div>' % (TEL_RAW, TEL, MAIL, MAIL),
            form),
    ])
    return pagina("proposta.html", "Solicite uma proposta | SPS Segurança do Trabalho",
                  "Peça uma proposta de SST para a sua empresa. A SPS monta o escopo conforme o ramo, "
                  "o número de colaboradores e o grau de risco.",
                  corpo, active="proposta")


def trabalhe():
    form = """<form class="form reveal" id="formVaga" novalidate>
      <div class="form__grid">
        %s %s %s %s
      </div>
      %s %s
      <div class="form__acoes">
        <button class="btn btn--primary" type="submit">Enviar pelo WhatsApp
          <svg viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8h11m0 0L9 4m4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
        <p class="form__nota">Para anexar currículo, envie para
           <a href="mailto:%s">%s</a>.</p>
      </div>
    </form>""" % (
        _campo("nome", "Seu nome"),
        _campo("email", "E-mail", "email", ph="voce@email.com"),
        _campo("fone", "Telefone ou WhatsApp", "tel", ph="(47) 90000-0000"),
        _campo("cidade", "Cidade onde mora"),
        _campo("area", "Área de interesse", opcoes=[
            "Medicina do trabalho", "Enfermagem do trabalho", "Técnico em segurança do trabalho",
            "Engenharia de segurança", "Instrutor de treinamentos", "Administrativo e comercial",
            "Outra área"]),
        _campo("msg", "Conte um pouco da sua experiência", req=False, linhas=4,
               ph="Formação, tempo de atuação e o que você procura."),
        MAIL, MAIL,
    )

    corpo = "".join([
        hero("Trabalhe conosco", 'Venha construir segurança com a gente<span class="ph__sub">Vagas em medicina, segurança e engenharia do trabalho</span>',
             "A SPS cresceu de uma sala em Itapema para cinco unidades em treze anos. Quem entra aqui "
             "entra numa equipe que atende obra, indústria e consultório no mesmo dia.",
             "risco-equipe", "Equipe de segurança do trabalho em campo"),

        '<section class="formsec tem-foto">%s<div class="wrap form__grid-out">'
        '<div class="form__lado reveal">%s</div><div class="form__box">%s</div>'
        '</div></section>' % (
            fundo("risco-equipe", "sutil"),
            '<span class="eyebrow"><i class="dot"></i>Por que a SPS</span>'
            '<h2>Uma equipe que resolve, não que empurra</h2>'
            '<p>Aqui o técnico vai a campo, o médico atende de verdade e o engenheiro assina o que '
            'projetou. Não existe laudo feito de escritório sobre obra que ninguém visitou.</p>'
            '<ul class="lista">'
            '<li>Cinco unidades no litoral norte catarinense</li>'
            '<li>Equipe clínica e de engenharia em quadro próprio</li>'
            '<li>Estrutura e frota para atender in company</li>'
            '<li>Plataforma própria, sem depender de sistema de terceiro no dia a dia</li>'
            '</ul>', form),
    ])
    return pagina("trabalhe.html", "Trabalhe conosco | SPS Segurança do Trabalho",
                  "Faça parte da equipe da SPS Segurança do Trabalho. Vagas em medicina ocupacional, "
                  "segurança do trabalho, engenharia e administrativo no litoral norte de SC.",
                  corpo, active="trabalhe")


def gerar():
    return [home(), sobre(), solucoes(), plataforma(), unidades(), proposta(), trabalhe()]
