/* =========================================================
   SPS Segurança do Trabalho
   ========================================================= */
(function () {
'use strict';

var $  = function (s, c) { return (c || document).querySelector(s); };
var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
var REDUCED = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

/* =========================================================
   1. HEADER
   ========================================================= */
(function header () {
  var hdr = $('#hdr'), last = 0;
  window.addEventListener('scroll', function () {
    var y = window.scrollY;
    hdr.classList.toggle('stuck', y > 30);
    hdr.classList.toggle('hide', y > 460 && y > last && !$('#nav').classList.contains('open'));
    last = y;
  }, { passive: true });

  /* menu mobile */
  var burger = $('#burger'), nav = $('#nav');
  burger.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    burger.setAttribute('aria-expanded', String(open));
    burger.setAttribute('aria-label', open ? 'Fechar menu' : 'Abrir menu');
  });
  $$('#nav a').forEach(function (a) {
    a.addEventListener('click', function () {
      nav.classList.remove('open');
      burger.setAttribute('aria-expanded', 'false');
    });
  });

  /* dropdown Soluções */
  var item = $('.nav__item--has-drop'), tgl = $('.nav__toggle', item), t;
  function setOpen (v) {
    item.setAttribute('aria-open', String(v));
    tgl.setAttribute('aria-expanded', String(v));
  }
  tgl.addEventListener('click', function (e) {
    e.preventDefault();
    setOpen(item.getAttribute('aria-open') !== 'true');
  });
  item.addEventListener('mouseenter', function () {
    if (window.innerWidth <= 940) return;
    clearTimeout(t); setOpen(true);
  });
  item.addEventListener('mouseleave', function () {
    if (window.innerWidth <= 940) return;
    t = setTimeout(function () { setOpen(false); }, 180);
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setOpen(false); });
  document.addEventListener('click', function (e) { if (!item.contains(e.target)) setOpen(false); });
})();

/* =========================================================
   2. REVEAL ON SCROLL
   ========================================================= */
(function reveal () {
  var els = $$('.reveal');
  if (REDUCED || !('IntersectionObserver' in window)) {
    els.forEach(function (el) { el.classList.add('in'); });
    return;
  }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
  els.forEach(function (el) { io.observe(el); });

  /* rede de segurança: nenhum conteúdo pode ficar preso invisível se o
     observer não disparar (aba em segundo plano, navegador exótico) */
  setTimeout(function () {
    els.forEach(function (el) {
      if (el.getBoundingClientRect().top < window.innerHeight) el.classList.add('in');
    });
  }, 2500);
})();

/* =========================================================
   3. CONTADORES
   ========================================================= */
(function counters () {
  var nodes = $$('[data-count]');
  var fmt = function (n) { return n.toLocaleString('pt-BR'); };

  function run (el) {
    var target = parseInt(el.dataset.count, 10);
    var prefix = el.dataset.prefix || '';
    /* o valor final já vem no HTML: sem JS, com JS travado ou com
       movimento reduzido, o número correto continua na tela */
    if (REDUCED) return;

    var dur = 1800, t0 = null;
    function step (ts) {
      if (t0 === null) t0 = ts;
      var p = Math.min((ts - t0) / dur, 1);
      var e = 1 - Math.pow(1 - p, 3);             /* easeOutCubic */
      el.textContent = prefix + fmt(Math.round(target * e));
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  if (!('IntersectionObserver' in window)) { nodes.forEach(run); return; }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (en.isIntersecting) { run(en.target); io.unobserve(en.target); }
    });
  }, { threshold: 0.5 });
  nodes.forEach(function (el) { io.observe(el); });
})();

/* =========================================================
   4. TABS DA PLATAFORMA
   ========================================================= */
(function tabs () {
  var btns = $$('.plat__tab');
  btns.forEach(function (btn, i) {
    btn.addEventListener('click', function () {
      btns.forEach(function (b) {
        b.classList.remove('is-active');
        b.setAttribute('aria-selected', 'false');
        $('#' + b.getAttribute('aria-controls')).hidden = true;
      });
      btn.classList.add('is-active');
      btn.setAttribute('aria-selected', 'true');
      $('#' + btn.getAttribute('aria-controls')).hidden = false;
    });
    btn.addEventListener('keydown', function (e) {
      var d = e.key === 'ArrowRight' || e.key === 'ArrowDown' ? 1
            : e.key === 'ArrowLeft'  || e.key === 'ArrowUp'   ? -1 : 0;
      if (!d) return;
      e.preventDefault();
      var n = btns[(i + d + btns.length) % btns.length];
      n.focus(); n.click();
    });
  });
})();

/* =========================================================
   5. MAPA DE SANTA CATARINA
   ========================================================= */
var Mapa = (function () {

  var VB_W = 1000, VB_H = 640;

  /* enquadramentos da câmera */
  var VIEW_STATE = { cx: 500, cy: 320, z: 1 };
  var VIEW_ZOOM  = { cx: 898, cy: 192, z: 5.4 };

  /* Cada alfinete fica exatamente sobre a coordenada da unidade. Corporativo e
     Itapema distam ~700 m, então nesse zoom eles quase coincidem: quem estiver
     selecionado vem para a frente. */
  var UNIDADES = [
    { id:'corporativo', nome:'Corporativo', curto:'ITAPEMA (Corporativo)',
      x:904.3, y:217.8,
      end:'Rua 406B, nº 883 &middot; Morretes, Itapema/SC &middot; CEP 88.220-000',
      maps:'https://www.google.com/maps/place/SPS+Seguran%C3%A7a+do+Trabalho+-+Corporativo/@-27.1207719,-48.6263447,16z/data=!4m7!3m6!1s0x2f2fb178b66c50bb:0xce917bdd12d11132!8m2!3d-27.1207719!4d-48.61759!16s%2Fg%2F11xkr3jfw7' },

    { id:'itapema', nome:'Itapema', curto:'ITAPEMA',
      x:905.4, y:218.3,
      end:'Rua 434, nº 88 &middot; Morretes, Itapema/SC &middot; CEP 88.220-000',
      maps:'https://www.google.com/maps/place/SPS+Seguran%C3%A7a+do+Trabalho+-+Unidade+Itapema/@-27.1235166,-48.6132515,17z/data=!3m1!4b1!4m6!3m5!1s0x94d8b1dbb90e5693:0x871ea7c78721fa99!8m2!3d-27.1235214!4d-48.6106766!16s%2Fg%2F11c0r5hg6n' },

    { id:'portobelo', nome:'Porto Belo', curto:'PORTO BELO',
      x:912.7, y:224.3,
      end:'Av. Atílio Fontana, nº 387 &middot; Perequê, Porto Belo/SC &middot; CEP 88.210-000',
      maps:'https://www.google.com/maps/place/SPS+treinamentos+e+exames/@-27.1559858,-48.5657683,17z/data=!3m1!4b1!4m6!3m5!1s0x94d8af0008ae7eb7:0x3e6eb8d7434ef5db!8m2!3d-27.1559858!4d-48.5657683!16s%2Fg%2F11x7mf1j3r' },

    { id:'itajai', nome:'Itajaí', curto:'ITAJAÍ',
      x:893.3, y:182.9,
      end:'Av. Ver. Abrahão João Francisco, nº 3820 &middot; Ressacada, Itajaí/SC &middot; CEP 88.301-335',
      maps:'https://www.google.com/maps/place/SPS+SEGURAN%C3%87A+DO+TRABALHO+UN.+ITAJA%C3%8D%2FSC/@-26.9293605,-48.6851534,17z/data=!3m1!4b1!4m6!3m5!1s0x94d8cd917c4d134b:0x9593293af264a630!8m2!3d-26.9293605!4d-48.6851534!16s%2Fg%2F11rw_vfxnt' },

    { id:'picarras', nome:'Balneário Piçarras', curto:'B. PIÇARRAS',
      x:894.8, y:152.5,
      end:'Rua 1240, nº 153 &middot; Centro, Balneário Piçarras/SC &middot; CEP 88.380-000',
      maps:'https://www.google.com/maps/place/SPS+SEGURAN%C3%87A+DO+TRABALHO+UN.+BALNE%C3%81RIO+PI%C3%87ARRAS/@-26.7624756,-48.6761676,17z/data=!3m1!4b1!4m6!3m5!1s0x94d8d58a3c8ae211:0x9fcb10d1471dbdb6!8m2!3d-26.7624756!4d-48.6761676!16s%2Fg%2F11smdybq43' }
  ];

  var NS = 'http://www.w3.org/2000/svg';
  var stage, svg, cam, pinsG, clusterG, badge;
  var view = VIEW_STATE, played = false, active = null;
  var ps = 1;   /* escala dos alfinetes: mantém ~30px na tela em qualquer viewport */

  function el (tag, attrs) {
    var n = document.createElementNS(NS, tag);
    for (var k in attrs) n.setAttribute(k, attrs[k]);
    return n;
  }

  /* posição de tela de um ponto do mapa, dado o enquadramento atual.
     Usada só para conferência: os alfinetes herdam a câmera. */
  function screenX (x) { return (x - view.cx) * view.z + VB_W / 2; }
  function screenY (y) { return (y - view.cy) * view.z + VB_H / 2; }

  function applyCam () {
    var tx = VB_W / 2 - view.cx * view.z;
    var ty = VB_H / 2 - view.cy * view.z;
    cam.setAttribute('transform', 'translate(' + tx.toFixed(2) + ',' + ty.toFixed(2) + ') scale(' + view.z + ')');
    layoutPins();
  }

  /* O SVG usa preserveAspectRatio padrão (meet), então a escala de renderização
     é o menor dos dois fatores. Os alfinetes compensam essa escala para ter
     sempre o mesmo tamanho em pixels, do desktop ao celular. */
  function measure () {
    var r = svg.getBoundingClientRect();
    if (!r.width || !r.height) return;
    var render = Math.min(r.width / VB_W, r.height / VB_H);
    ps = Math.max(0.8, Math.min(3.4, 0.9375 / render));
  }

  /* Os alfinetes estão dentro de #cam, então a posição é a coordenada
     geográfica pura e nunca muda: quem move é a câmera. Só compensamos a
     escala (ps/z) para o alfinete ter o mesmo tamanho na tela em qualquer
     zoom. Dentro do alfinete, 1 unidade equivale a ps unidades do viewBox. */
  function layoutPins () {
    var k = (ps / view.z).toFixed(4);
    UNIDADES.forEach(function (u) {
      u.node.setAttribute('transform',
        'translate(' + u.x + ',' + u.y + ') scale(' + k + ')');

      u.label.setAttribute('x', 0);
      u.label.setAttribute('y', 16);
    });
    ajustaRotulos();
    clusterG.setAttribute('transform',
      'translate(' + SC_MAP.cluster.cx + ',' + SC_MAP.cluster.cy + ') scale(' + k + ')');
  }

  /* Corporativo e Itapema caem sobre o mesmo ponto neste zoom, e dois rótulos
     no mesmo lugar viram borrão. Em vez de empurrar o alfinete para fora da
     coordenada real, escondemos o rótulo que colidiria: o nome continua
     disponível no selo do mapa e no card, e ao selecionar ele reaparece. */
  function ajustaRotulos () {
    var r = svg.getBoundingClientRect();
    var render = Math.min(r.width / VB_W, r.height / VB_H);
    if (!render) return;

    function bateEm (a, lista) {
      return lista.some(function (b) {
        return a.x1 < b.x2 && a.x2 > b.x1 && a.y1 < b.y2 && a.y2 > b.y1;
      });
    }

    /* os corpos dos alfinetes são obstáculos fixos: o rótulo desvia deles */
    var ocupado = UNIDADES.map(function (u) {
      var px = screenX(u.x) * render, py = screenY(u.y) * render;
      return { x1: px - 12, x2: px + 12, y1: py - 32, y2: py + 2 };
    });

    /* o selecionado escolhe posição primeiro e sempre aparece */
    var ordem = UNIDADES.slice().sort(function (a, b) {
      return (b.id === active ? 1 : 0) - (a.id === active ? 1 : 0);
    });

    ordem.forEach(function (u) {
      var px = screenX(u.x) * render, py = screenY(u.y) * render;
      var mw = u.curto.length * 3.7;                  /* ~7.3px por caractere */
      var abaixo = { x1: px - mw, x2: px + mw, y1: py + 6,  y2: py + 22 };
      var acima  = { x1: px - mw, x2: px + mw, y1: py - 52, y2: py - 36 };

      var pos = !bateEm(abaixo, ocupado) ? abaixo
              : !bateEm(acima, ocupado)  ? acima : null;

      if (!pos && u.id === active) pos = acima;       /* selecionado nunca some */
      u.label.style.display = pos ? '' : 'none';
      if (pos) {
        u.label.setAttribute('y', pos === abaixo ? 16 : -42);
        ocupado.push(pos);
      }
    });
  }

  function buildPin (u, i) {
    var anchor = el('g', { class: 'pin-anchor' });
    var g = el('g', { class: 'pin', tabindex: '0', role: 'button',
                      'aria-label': 'Unidade ' + u.nome });
    g.style.setProperty('--pd', (i * 0.13) + 's');

    var body = el('g', { class: 'pin__body' });
    body.appendChild(el('circle', { class: 'pin__ping', cx: 0, cy: -20, r: 12 }));
    body.appendChild(el('path', { class: 'pin__shape',
      d: 'M0,0 C-4.5,-7 -12,-13 -12,-20 a12,12 0 1,1 24,0 C12,-13 4.5,-7 0,0 Z' }));
    body.appendChild(el('circle', { class: 'pin__core', cx: 0, cy: -20, r: 5 }));
    g.appendChild(body);
    u.body = body;

    /* la = rótulo acima do alfinete, usado quando dois pontos ficam lado a lado */
    var label = el('text', { class: 'pin__label' });
    label.textContent = u.curto;
    g.appendChild(label);
    u.label = label;

    function pick () { select(u.id, true); }
    g.addEventListener('click', pick);
    g.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); pick(); }
    });

    anchor.appendChild(g);
    u.pin = g;
    return anchor;
  }

  function buildCluster () {
    var g = el('g', { class: 'cluster' });
    g.appendChild(el('circle', { class: 'cluster__ring', cx: 0, cy: 0, r: 26 }));
    g.appendChild(el('circle', { class: 'cluster__dot',  cx: 0, cy: 0, r: 15 }));
    var n = el('text', { class: 'cluster__n', x: 0, y: 5 });
    n.textContent = '5';
    g.appendChild(n);
    var t = el('text', { class: 'cluster__t', x: 0, y: 44 });
    t.textContent = 'UNIDADES';
    g.appendChild(t);
    return g;
  }

  function buildCards () {
    var ul = $('#ucards');
    UNIDADES.forEach(function (u) {
      var li = document.createElement('li');
      li.innerHTML =
        '<div class="ucard" data-id="' + u.id + '" role="button" tabindex="0">' +
          '<span class="ucard__dot"></span>' +
          '<span><span class="ucard__nome">' + u.curto + '</span>' +
          '<span class="ucard__end">' + u.end + '</span></span>' +
          '<a class="ucard__go" href="' + u.maps + '" target="_blank" rel="noopener" ' +
             'aria-label="Abrir ' + u.nome + ' no Google Maps" title="Traçar rota">' +
            '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M6 3h7v7M13 3 3.5 12.5" ' +
            'fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" ' +
            'stroke-linejoin="round"/></svg>' +
          '</a>' +
        '</div>';
      ul.appendChild(li);

      var card = $('.ucard', li);
      u.card = card;
      function pick (e) {
        if (e.target.closest('.ucard__go')) return;   /* o link segue para o Maps */
        select(u.id, true);
      }
      card.addEventListener('click', pick);
      card.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); pick(e); }
      });
    });
  }

  function select (id, focusMap) {
    active = id;
    UNIDADES.forEach(function (u) {
      var on = u.id === id;
      u.pin.classList.toggle('is-active', on);
      u.card.classList.toggle('is-active', on);
      if (on) {
        badge.textContent = u.nome;
        /* SVG não tem z-index: quem vem por último fica por cima. Corporativo
           e Itapema ficam praticamente no mesmo ponto, então o selecionado
           precisa ir para o fim da lista para ser visto e clicado. */
        pinsG.appendChild(u.node);
      }
    });
    ajustaRotulos();   /* o selecionado tem prioridade de rótulo */
    if (focusMap && !stage.classList.contains('is-zoomed')) zoomIn();
  }

  function setView (v) {
    view = v;
    applyCam();
  }

  /* a queda dura no máximo 0.75s + 0.52s de escalonamento; depois disso os
     alfinetes têm que estar em repouso, tenham os frames rodado ou não */
  var travaFinal;
  function garanteAlfinetes () {
    clearTimeout(travaFinal);
    travaFinal = setTimeout(function () { stage.classList.add('pin-final'); }, 1800);
  }

  function zoomIn () {
    setView(VIEW_ZOOM);
    stage.classList.add('is-zoomed', 'is-pinned');
    garanteAlfinetes();
    badge.textContent = active
      ? (UNIDADES.filter(function (u) { return u.id === active; })[0] || {}).nome
      : 'Litoral Norte · SC';
  }

  function zoomOut () {
    setView(VIEW_STATE);
    stage.classList.remove('is-zoomed');
    badge.textContent = 'Santa Catarina';
    active = null;
    UNIDADES.forEach(function (u) {
      u.pin.classList.remove('is-active');
      u.card.classList.remove('is-active');
    });
  }

  function play () {
    clearTimeout(travaFinal);
    stage.classList.remove('is-drawn', 'is-zoomed', 'is-pinned', 'pin-final');
    setView(VIEW_STATE);
    badge.textContent = 'Santa Catarina';

    if (REDUCED) {
      stage.classList.add('is-drawn');
      zoomIn();
      return;
    }
    /* força reflow para reiniciar a animação de traçado */
    void $('#scStroke').getBoundingClientRect();

    setTimeout(function () { stage.classList.add('is-drawn'); }, 60);
    setTimeout(function () { setView(VIEW_ZOOM); stage.classList.add('is-zoomed');
                             badge.textContent = 'Litoral Norte · SC'; }, 1600);
    setTimeout(function () { stage.classList.add('is-pinned'); garanteAlfinetes(); }, 2700);
  }

  function init () {
    /* o mapa só existe na home e em unidades.html */
    if (typeof SC_MAP === 'undefined') return;
    if (!$('#mapaStage') || $('#mapaStage').dataset.ready) return;
    stage    = $('#mapaStage');
    stage.dataset.ready = '1';
    svg      = $('#scmap');
    cam      = $('#cam');
    pinsG    = $('#scPins');
    clusterG = $('#scCluster');
    badge    = $('#mapaBadge');

    $('#scFill').setAttribute('d', SC_MAP.state);
    $('#scMuni').setAttribute('d', SC_MAP.muni);

    var stroke = $('#scStroke');
    stroke.setAttribute('d', SC_MAP.state);
    var len = stroke.getTotalLength();
    stroke.style.setProperty('--len', len);

    var hl = $('#scHl');
    Object.keys(SC_MAP.hl).forEach(function (k) {
      hl.appendChild(el('path', { d: SC_MAP.hl[k] }));
    });

    clusterG.appendChild(buildCluster());
    UNIDADES.forEach(function (u, i) {
      u.node = buildPin(u, i);
      pinsG.appendChild(u.node);
    });

    buildCards();
    measure();
    applyCam();

    /* A transição de 1.7s só vale para movimento de câmera. Sem esta trava,
       o primeiro posicionamento animava a partir da origem e os alfinetes
       ficavam empilhados no canto até a transição terminar, ou para sempre
       se a aba estivesse em segundo plano e os frames não rodassem. */
    requestAnimationFrame(function () {
      requestAnimationFrame(function () { stage.classList.add('is-pronto'); });
    });

    var rt;
    window.addEventListener('resize', function () {
      clearTimeout(rt);
      rt = setTimeout(function () {
        stage.classList.remove('is-pronto');   /* reposiciona sem deslizar */
        measure(); layoutPins();
        requestAnimationFrame(function () { stage.classList.add('is-pronto'); });
      }, 150);
    }, { passive: true });

    $('#btnZoomOut').addEventListener('click', function () {
      if (stage.classList.contains('is-zoomed')) zoomOut();
      else { zoomIn(); }
      this.textContent = stage.classList.contains('is-zoomed') ? 'Ver o estado' : 'Ver as unidades';
    });
    $('#btnReplay').addEventListener('click', play);

    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (en) {
        if (en[0].isIntersecting && !played) { played = true; play(); io.disconnect(); }
      }, { threshold: 0.28 });
      io.observe(stage);
    } else { play(); }
  }

  return { init: init };
})();

/* =========================================================
   6. MODAIS
   ========================================================= */
(function modais () {
  var open = null, lastFocus = null;
  var SEL = 'a[href], button:not([disabled]), [tabindex]:not([tabindex="-1"])';

  function show (id) {
    var m = $('#' + id);
    if (!m) return;
    if (open) open.hidden = true; else lastFocus = document.activeElement;
    m.hidden = false;
    open = m;
    document.body.style.overflow = 'hidden';
    /* foca a primeira ação, não o botão de fechar */
    var f = $('.acc, .pn', m) || $(SEL, m);
    if (f) f.focus();
  }

  function hide () {
    if (!open) return;
    open.hidden = true;
    open = null;
    document.body.style.overflow = '';
    if (lastFocus) { lastFocus.focus(); lastFocus = null; }
  }

  $$('.js-open-login').forEach(function (b) {
    b.addEventListener('click', function () { show('mdLogin'); });
  });
  $$('.js-open-painel').forEach(function (b) {
    b.addEventListener('click', function () { show('mdPainel'); });
  });
  $$('.js-back-login').forEach(function (b) {
    b.addEventListener('click', function () { show('mdLogin'); });
  });
  $$('[data-close]').forEach(function (b) {
    b.addEventListener('click', hide);
  });

  document.addEventListener('keydown', function (e) {
    if (!open) return;
    if (e.key === 'Escape') { hide(); return; }
    if (e.key !== 'Tab') return;

    /* foco preso dentro do modal */
    var f = $$(SEL, open).filter(function (n) { return n.offsetParent !== null; });
    if (!f.length) return;
    var first = f[0], last = f[f.length - 1];
    if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
  });
})();

/* =========================================================
   7. FORMULÁRIOS
   Sem back-end: o formulário valida e monta uma mensagem de
   WhatsApp já preenchida. Nada é armazenado no site.
   ========================================================= */
(function formularios () {
  var WPP = '5547992398519';

  var TEXTOS = {
    formProposta: function (v) {
      return 'Olá! Quero uma proposta de SST para a minha empresa.\n\n' +
             'Empresa: ' + v.empresa + '\n' +
             'Contato: ' + v.nome + '\n' +
             'E-mail: ' + v.email + '\n' +
             'Telefone: ' + v.fone + '\n' +
             'Cidade: ' + v.cidade + '\n' +
             'Colaboradores: ' + v.func +
             (v.msg ? '\n\nNecessidade:\n' + v.msg : '');
    },
    formVaga: function (v) {
      return 'Olá! Gostaria de trabalhar na SPS.\n\n' +
             'Nome: ' + v.nome + '\n' +
             'E-mail: ' + v.email + '\n' +
             'Telefone: ' + v.fone + '\n' +
             'Cidade: ' + v.cidade + '\n' +
             'Área: ' + v.area +
             (v.msg ? '\n\nExperiência:\n' + v.msg : '');
    }
  };

  function erro (campo, texto) {
    campo.classList.add('is-erro');
    if (!$('.campo__erro', campo)) {
      var s = document.createElement('span');
      s.className = 'campo__erro';
      s.textContent = texto;
      campo.appendChild(s);
    }
  }

  function limpa (campo) {
    campo.classList.remove('is-erro');
    var e = $('.campo__erro', campo);
    if (e) e.remove();
  }

  function valida (form) {
    var ok = true, primeiro = null;
    $$('.campo', form).forEach(function (campo) {
      var el = $('input, select, textarea', campo);
      if (!el) return;
      limpa(campo);
      var v = (el.value || '').trim();

      if (el.hasAttribute('required') && !v) {
        erro(campo, 'Preencha este campo.');
        ok = false; primeiro = primeiro || el;
        return;
      }
      if (el.type === 'email' && v && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v)) {
        erro(campo, 'Confira o e-mail.');
        ok = false; primeiro = primeiro || el;
        return;
      }
      if (el.type === 'tel' && v && v.replace(/\D/g, '').length < 10) {
        erro(campo, 'Informe o DDD e o número.');
        ok = false; primeiro = primeiro || el;
      }
    });
    if (primeiro) primeiro.focus();
    return ok;
  }

  Object.keys(TEXTOS).forEach(function (id) {
    var form = $('#' + id);
    if (!form) return;

    $$('input, select, textarea', form).forEach(function (el) {
      el.addEventListener('input', function () {
        var c = el.closest('.campo');
        if (c && c.classList.contains('is-erro')) limpa(c);
      });
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!valida(form)) return;

      var v = {};
      $$('input, select, textarea', form).forEach(function (el) {
        v[el.name] = (el.value || '').trim();
      });
      window.open('https://wa.me/' + WPP + '?text=' + encodeURIComponent(TEXTOS[id](v)),
                  '_blank', 'noopener');
    });
  });
})();

/* =========================================================
   8. MISCELÂNEA
   ========================================================= */
(function misc () {
  $('#ano').textContent = new Date().getFullYear();

  var top = $('#toTop');
  window.addEventListener('scroll', function () {
    top.classList.toggle('show', window.scrollY > 700);
  }, { passive: true });
  top.addEventListener('click', function () {
    window.scrollTo({ top: 0, behavior: REDUCED ? 'auto' : 'smooth' });
  });

  /* brilho que segue o cursor nos cards de solução */
  if (!REDUCED && window.matchMedia('(hover:hover)').matches) {
    $$('.sol').forEach(function (c) {
      c.addEventListener('pointermove', function (e) {
        var r = c.getBoundingClientRect();
        c.style.setProperty('--mx', ((e.clientX - r.left) / r.width * 100) + '%');
        c.style.setProperty('--my', ((e.clientY - r.top) / r.height * 100) + '%');
      });
    });
  }
})();

document.addEventListener('DOMContentLoaded', Mapa.init);
if (document.readyState !== 'loading') Mapa.init();

})();
