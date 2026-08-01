# -*- coding: utf-8 -*-
"""Casca comum e componentes de todas as páginas do site da SPS."""

import json
import os

_MANIFESTO = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          "..", "site", "img", "manifesto.json")
try:
    with open(_MANIFESTO) as _f:
        FOTOS = json.load(_f)
except IOError:
    FOTOS = {}


def imagem(slug, alt, sizes="100vw", prioridade=False, classe=""):
    """<picture> com WebP + JPEG e srcset, a partir do manifesto de imagens.

    Rode build/imagens.py depois de acrescentar qualquer foto nova.
    """
    d = FOTOS.get(slug)
    if not d:
        return '<img src="img/foto/%s.jpg" alt="%s"%s>' % (slug, alt,
                                                           ' class="%s"' % classe if classe else "")
    larguras = d["larguras"]

    def srcset(ext):
        partes = []
        for i, lg in enumerate(larguras):
            sufixo = "" if i == 0 else "-%d" % lg
            partes.append("img/foto/%s%s.%s %dw" % (slug, sufixo, ext, lg))
        return ", ".join(partes)

    carga = ' fetchpriority="high"' if prioridade else ' loading="lazy" decoding="async"'
    return (
        '<picture>'
        '<source type="image/webp" srcset="%s" sizes="%s">'
        '<img src="img/foto/%s.jpg" srcset="%s" sizes="%s" alt="%s" '
        'width="%d" height="%d"%s%s>'
        '</picture>'
        % (srcset("webp"), sizes, slug, srcset("jpg"), sizes, alt,
           d["w"], d["h"], carga, ' class="%s"' % classe if classe else "")
    )


SITE = "SPS Segurança do Trabalho"
TEL = "(47) 3368-8130"
TEL_RAW = "+554733688130"
WPP = "https://web.whatsapp.com/send?phone=554792398519"
MAIL = "qualidade@spsseguranca.com.br"

# Sistema de terceiro (ASAP / carlos-ti). Não alterar estas URLs.
PAINEL = {
    "cliente": "https://carlos-ti.com/cw3/osmapCERT/painelC2/acesso/index.php?destroy=",
    "inspecoes": "https://carlos-ti.com/cw3/osmapSEG/painel2.0/acesso/index.php?destroy=",
    "treinamentos": "https://carlos-ti.com/cw3/osmapCERT/painel2.0/acesso/index.php?destroy=",
    "instrutores": "https://carlos-ti.com/cw3/osmapCERT/painelP/acesso/index.php?destroy=",
    "medicos": "https://carlos-ti.com/cw3/osmapCERT/painelM/acesso/index.php?destroy=",
}

MENU_SOLUCOES = [
    ("Documentos legais", [
        ("PGR", "pgr.html"), ("PCMSO", "pcmso.html"), ("LTCAT", "ltcat.html"),
        ("PPP", "ppp.html"), ("eSocial", "esocial.html"),
    ]),
    ("Exames ocupacionais", [
        ("Visão geral e ASO", "exames.html"), ("Admissional", "exames.html#admissional"),
        ("Periódico", "exames.html#periodico"), ("Mudança de risco", "exames.html#mudanca"),
        ("Demissional", "exames.html#demissional"),
    ]),
    ("Treinamentos", [
        ("Todas as NRs", "treinamentos.html"), ("NR 12 · Máquinas", "treinamentos.html#nr12"),
        ("NR 18 · Construção civil", "treinamentos.html#nr18"),
        ("NR 35 · Trabalho em altura", "treinamentos.html#nr35"),
    ]),
    ("Engenharia", [
        ("Visão geral", "engenharia.html"), ("PGR de obra", "engenharia.html#obra"),
        ("Linha de vida", "engenharia.html#linha-de-vida"),
        ("Ancoragem", "engenharia.html#ancoragem"),
        ("Elétrico provisório", "engenharia.html#eletrico"),
    ]),
    ("Consultoria", [
        ("Pacotes e escopo", "consultoria.html"), ("Auditorias técnicas", "consultoria.html#auditoria"),
        ("Assistente de perito", "consultoria.html#pericia"),
        ("Desembargo de obras", "consultoria.html#desembargo"),
        ("Unidade móvel", "unidade-movel.html"),
    ]),
]

NAV = [
    ("solucoes", "Soluções", "solucoes.html"),
    ("sobre", "Sobre Nós", "sobre.html"),
    ("plataforma", "Diferenciais", "plataforma.html"),
    ("unidades", "Unidades", "unidades.html"),
    ("proposta", "Solicite uma Proposta", "proposta.html"),
    ("trabalhe", "Trabalhe Conosco", "trabalhe.html"),
]


def _drop():
    cols = []
    for titulo, itens in MENU_SOLUCOES:
        links = "".join('<a href="%s">%s</a>' % (h, t) for t, h in itens)
        cols.append('<div class="drop__col"><span class="drop__title">%s</span>%s</div>'
                    % (titulo, links))
    return '<div class="drop" id="drop-solucoes"><div class="drop__grid">%s</div></div>' % "".join(cols)


def _nav(active):
    out = []
    for key, rotulo, href in NAV:
        cls = "nav__link" + (" is-active" if key == active else "")
        if key == "solucoes":
            aopen = ' aria-current="page"' if active == "solucoes" else ""
            out.append(
                '<li class="nav__item nav__item--has-drop">'
                '<a class="%s" href="%s"%s>Soluções</a>'
                '<button class="nav__toggle" aria-expanded="false" aria-controls="drop-solucoes" '
                'aria-label="Abrir submenu de soluções">'
                '<svg class="nav__caret" viewBox="0 0 12 8" aria-hidden="true"><path d="M1 1.5 6 6.5l5-5" '
                'fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" '
                'stroke-linejoin="round"/></svg></button>%s</li>' % (cls, href, aopen, _drop()))
        else:
            aria = ' aria-current="page"' if key == active else ""
            out.append('<li class="nav__item"><a class="%s" href="%s"%s>%s</a></li>'
                       % (cls, href, aria, rotulo))
    out.append('<li class="nav__item nav__item--cta">'
               '<button class="btn btn--login js-open-login">Login</button></li>')
    return "".join(out)


HEADER = """<header class="hdr" id="hdr">
  <div class="hdr__inner">
    <a class="hdr__logo" href="index.html" aria-label="%s, ir para a página inicial">
      <img src="img/logo-sps.png" alt="%s" width="850" height="215">
    </a>
    <nav class="nav" id="nav" aria-label="Menu principal"><ul class="nav__list">%s</ul></nav>
    <button class="burger" id="burger" aria-label="Abrir menu" aria-expanded="false" aria-controls="nav">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>"""


FOOTER = """<footer class="ft">
  <div class="wrap ft__grid">
    <div class="ft__brand">
      <img class="ft__logo" src="img/logo-sps.png" alt="%(site)s" width="850" height="215">
      <p>Há treze anos cuidando de quem faz a sua empresa acontecer. Medicina ocupacional,
         engenharia de segurança do trabalho e treinamentos no litoral catarinense.</p>
      <picture>
        <source type="image/webp" srcset="img/selo-13anos.webp">
        <img class="ft__selo" src="img/selo-13anos.png" alt="Selo comemorativo de treze anos da SPS"
             width="240" height="240" loading="lazy" decoding="async">
      </picture>
    </div>
    <div class="ft__col">
      <h4>Institucional</h4>
      <a href="sobre.html">Sobre nós</a>
      <a href="plataforma.html">Diferenciais</a>
      <a href="unidades.html">Unidades</a>
      <a href="proposta.html">Solicite uma proposta</a>
      <a href="trabalhe.html">Trabalhe conosco</a>
    </div>
    <div class="ft__col">
      <h4>Soluções</h4>
      <a href="pgr.html">PGR</a>
      <a href="pcmso.html">PCMSO</a>
      <a href="exames.html">Exames ocupacionais</a>
      <a href="treinamentos.html">Treinamentos de NRs</a>
      <a href="engenharia.html">Engenharia de segurança</a>
      <a href="consultoria.html">Consultoria técnica</a>
    </div>
    <div class="ft__col ft__col--contato">
      <h4>Contato</h4>
      <a href="https://maps.google.com/?q=Rua+406B,+883,+Morretes,+Itapema/SC" target="_blank" rel="noopener">
        Rua 406B, 883 &middot; Morretes<br>Itapema/SC &middot; 88.220-000</a>
      <a href="mailto:%(mail)s">%(mail)s</a>
      <a href="tel:%(telraw)s">%(tel)s</a>
      <p class="ft__hora">Segunda a sexta<br>07h às 12h &middot; 13h às 17h</p>
      <div class="ft__social">
        <a href="https://www.instagram.com/spssegurancadotrabalho" target="_blank" rel="noopener" aria-label="Instagram da SPS">
          <svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r="1.2" fill="currentColor" stroke="none"/></svg></a>
        <a href="https://www.facebook.com/people/SPS-Seguran%%C3%%A7a-do-Trabalho/61577307736137/" target="_blank" rel="noopener" aria-label="Facebook da SPS">
          <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14.5 8.5h2.5V5h-2.5c-2 0-3.5 1.5-3.5 3.5V11H8v3.5h3V21h3.5v-6.5H17l.5-3.5h-3V9c0-.3.2-.5.5-.5Z"/></svg></a>
        <a href="https://www.linkedin.com/in/sps-segu-95296b287" target="_blank" rel="noopener" aria-label="LinkedIn da SPS">
          <svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="3"/><path d="M7.5 10v7M7.5 7.2v.1M11.5 17v-4a2.5 2.5 0 0 1 5 0v4"/></svg></a>
      </div>
    </div>
  </div>
  <div class="wrap ft__bar">
    <span>&copy; <span id="ano">2026</span> %(site)s. Todos os direitos reservados.</span>
    <span class="ft__cnpj">Itapema &middot; Porto Belo &middot; Itajaí &middot; Balneário Piçarras &middot; SC</span>
  </div>
</footer>""" % {"site": SITE, "mail": MAIL, "tel": TEL, "telraw": TEL_RAW}


FLOATS = """<div class="floats">
  <a class="float float--wa" href="%s" target="_blank" rel="noopener" aria-label="Falar no WhatsApp">
    <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Z" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="M8.8 7.6c.2-.4.4-.4.7-.4h.5c.2 0 .4 0 .6.5l.8 1.9c.1.2 0 .4-.1.6l-.4.5c-.2.2-.3.4-.1.7a7 7 0 0 0 3.3 2.9c.3.1.5.1.7-.1l.6-.7c.2-.2.3-.2.6-.1l1.9.9c.3.1.4.3.4.5a2 2 0 0 1-1.4 1.7c-.5.2-1.2.3-3.5-.7a10 10 0 0 1-4.7-4.6c-.9-1.9-.6-2.9-.4-3.4Z" fill="currentColor" stroke="none"/></svg>
  </a>
  <button class="float float--top" id="toTop" aria-label="Voltar ao topo">
    <svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 13V3m0 0L3.5 7.5M8 3l4.5 4.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
  </button>
</div>""" % WPP


def _painel_link(rotulo, href):
    return ('<a class="pn" href="%s" target="_blank" rel="noopener"><span>%s</span>'
            '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8h11m0 0L9 4m4 4-4 4" fill="none" '
            'stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/>'
            '</svg></a>' % (href, rotulo))


MODAIS = """<div class="modal" id="mdLogin" role="dialog" aria-modal="true" aria-labelledby="mdLoginTitle" hidden>
  <div class="modal__backdrop" data-close></div>
  <div class="modal__box modal__box--lg" role="document">
    <div class="modal__head">
      <h2 class="modal__title" id="mdLoginTitle">Acesso Rápido</h2>
      <button class="modal__x" data-close aria-label="Fechar">
        <svg viewBox="0 0 16 16" aria-hidden="true"><path d="m4 4 8 8M12 4l-8 8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
      </button>
    </div>
    <div class="modal__body">
      <div class="acc__grid">
        <button class="acc js-open-painel" type="button">
          <span class="acc__ico"><svg viewBox="0 0 32 32" aria-hidden="true"><path d="M4 28V9l10-5 10 5v19"/><path d="M2 28h28"/><path d="M11 15h6M11 20h6"/></svg></span>
          <span class="acc__txt"><strong>Acesso Empresa</strong><small>Área de login exclusiva para colaboradores SPS.</small></span>
          <svg class="acc__arrow" viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8h11m0 0L9 4m4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </button>
        <a class="acc" href="%(cliente)s" target="_blank" rel="noopener">
          <span class="acc__ico"><svg viewBox="0 0 32 32" aria-hidden="true"><circle cx="16" cy="11" r="5.5"/><path d="M5 28c0-5.5 4.9-9 11-9s11 3.5 11 9"/></svg></span>
          <span class="acc__txt"><strong>Acesso Cliente</strong><small>Gestão de medicina, segurança do trabalho e eSocial da sua empresa.</small></span>
          <svg class="acc__arrow" viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8h11m0 0L9 4m4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </a>
      </div>
    </div>
  </div>
</div>

<div class="modal" id="mdPainel" role="dialog" aria-modal="true" aria-labelledby="mdPainelTitle" hidden>
  <div class="modal__backdrop" data-close></div>
  <div class="modal__box" role="document">
    <div class="modal__head">
      <button class="modal__back js-back-login" aria-label="Voltar para Acesso Rápido">
        <svg viewBox="0 0 16 16" aria-hidden="true"><path d="M14 8H3m0 0 4.5-4.5M3 8l4.5 4.5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </button>
      <h2 class="modal__title" id="mdPainelTitle">Painel</h2>
      <button class="modal__x" data-close aria-label="Fechar">
        <svg viewBox="0 0 16 16" aria-hidden="true"><path d="m4 4 8 8M12 4l-8 8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
      </button>
    </div>
    <div class="modal__body"><div class="pn__list">%(links)s</div></div>
  </div>
</div>""" % {
    "cliente": PAINEL["cliente"],
    "links": "".join([
        _painel_link("Inspeções", PAINEL["inspecoes"]),
        _painel_link("Treinamentos", PAINEL["treinamentos"]),
        _painel_link("Instrutores", PAINEL["instrutores"]),
        _painel_link("Médicos", PAINEL["medicos"]),
        _painel_link("Clientes", PAINEL["cliente"]),
    ]),
}


SHELL = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<meta name="theme-color" content="#052D15">
<link rel="icon" href="img/logo-sps.png">
<meta property="og:type" content="website">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:image" content="img/un-corporativo.jpg">
<meta property="og:locale" content="pt_BR">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800;900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
<script>document.documentElement.className+=' js';</script>
</head>
<body%(bodyattr)s>

<a class="skip-link" href="#conteudo">Pular para o conteúdo</a>

%(header)s

<main id="conteudo">
%(body)s
</main>

%(footer)s
%(floats)s
%(modais)s

%(scripts)s
<script src="js/main.js"></script>
</body>
</html>
"""


def pagina(nome, title, desc, body, active="", scripts="", bodyattr=""):
    """Monta o HTML final de uma página."""
    html = SHELL % {
        "title": title, "desc": desc, "body": body,
        "header": HEADER % (SITE, SITE, _nav(active)),
        "footer": FOOTER, "floats": FLOATS, "modais": MODAIS,
        "scripts": scripts, "bodyattr": bodyattr,
    }
    return nome, html


# ---------------------------------------------------------------- componentes

def hero(eyebrow, titulo, texto, slug, alt, botoes=None, alto=False):
    b = ""
    if botoes:
        b = '<div class="ph__actions">%s</div>' % "".join(botoes)
    return """<section class="ph%(alto)s">
  <div class="ph__bg">%(img)s</div>
  <div class="ph__veil"></div>
  <div class="wrap ph__inner">
    <span class="eyebrow"><i class="dot"></i>%(eyebrow)s</span>
    <h1>%(titulo)s</h1>
    <p>%(texto)s</p>
    %(b)s
  </div>
</section>""" % {"eyebrow": eyebrow, "titulo": titulo, "texto": texto,
                 "img": imagem(slug, alt, "100vw", prioridade=True),
                 "b": b, "alto": " ph--alto" if alto else ""}


def fundo(slug, forca="media"):
    """Foto de fundo de seção, atrás de um véu escuro.

    O véu mantém o contraste do texto: a imagem entra como textura, não
    como concorrente da leitura. forca: leve | media | forte.
    """
    return ('<div class="sec-bg sec-bg--%s" aria-hidden="true">%s'
            '<span class="sec-bg__veil"></span></div>'
            % (forca, imagem(slug, "", "100vw")))


def sec_head(eyebrow, titulo, sub="", center=False):
    s = '<p class="sec-head__sub">%s</p>' % sub if sub else ""
    return ('<header class="sec-head%s reveal"><span class="eyebrow"><i class="dot"></i>%s</span>'
            '<h2>%s</h2>%s</header>' % (" sec-head--center" if center else "", eyebrow, titulo, s))


def bullets(itens, cls="lista"):
    return '<ul class="%s">%s</ul>' % (cls, "".join("<li>%s</li>" % i for i in itens))


def bloco(titulo, corpo, itens=None, i=0):
    li = bullets(itens) if itens else ""
    return ('<article class="bloco reveal" style="--d:%.2fs"><h3>%s</h3>%s%s</article>'
            % (i * 0.05, titulo, corpo, li))


def blocos(lista):
    """lista de (titulo, corpo_html, itens|None)"""
    out = [bloco(t, c, it, i) for i, (t, c, it) in enumerate(lista)]
    return '<div class="blocos">%s</div>' % "".join(out)


def foto(slug, alt, legenda="", cls="", sizes="(max-width:940px) 100vw, 50vw"):
    # o <span> existe para limitar a largura do texto sem cortar o gradiente
    cap = '<figcaption><span>%s</span></figcaption>' % legenda if legenda else ""
    return ('<figure class="foto %s reveal">%s%s</figure>'
            % (cls, imagem(slug, alt, sizes), cap))


def cta(titulo="Peça uma proposta para a sua empresa",
        texto="Conte quantos colaboradores você tem e qual o ramo da empresa. A SPS monta o escopo "
              "de documentos, exames e treinamentos que a sua operação realmente precisa."):
    return """<section class="cta tem-foto">
  %(fundo)s
  <div class="wrap cta__inner cta__inner--simples">
    <div class="cta__txt reveal">
      <span class="eyebrow"><i class="dot"></i>Vamos conversar</span>
      <h2>%(titulo)s</h2>
      <p>%(texto)s</p>
      <div class="cta__actions">
        <a class="btn btn--primary" href="proposta.html">Solicitar proposta
          <svg viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8h11m0 0L9 4m4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
        <a class="btn btn--ghost" href="%(wpp)s" target="_blank" rel="noopener">Chamar no WhatsApp</a>
      </div>
    </div>
  </div>
</section>""" % {"fundo": fundo("reuniao", "leve"), "titulo": titulo, "texto": texto, "wpp": WPP}


def relacionados(itens):
    """itens: lista de (titulo, texto, href)"""
    cards = "".join(
        '<a class="rel reveal" style="--d:%.2fs" href="%s"><h3>%s</h3><p>%s</p>'
        '<span class="rel__go">Ver detalhes<svg viewBox="0 0 16 16" aria-hidden="true">'
        '<path d="M2 8h11m0 0L9 4m4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.7" '
        'stroke-linecap="round" stroke-linejoin="round"/></svg></span></a>'
        % (i * 0.06, h, t, x) for i, (t, x, h) in enumerate(itens))
    return ('<section class="relacionados tem-foto">%s<div class="wrap">%s'
            '<div class="rel__grid">%s</div></div></section>'
            % (fundo("engenheiro", "sutil"),
               sec_head("Continue por aqui", "Serviços relacionados", center=True), cards))
