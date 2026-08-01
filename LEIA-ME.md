# Site SPS Segurança do Trabalho

## Pastas

- `site/` é o **site pronto**. HTML estático puro, sobe em qualquer hospedagem.
- `build/` é o **gerador**. As 17 páginas saem daqui para não haver header,
  rodapé ou menu fora de sincronia entre elas.
- `backup01-site/` é o **BACKUP01SPS**, versão congelada de página única.
  Não editar.

## Como mexer no conteúdo

Os arquivos `.html` dentro de `site/` são **saída** e são sobrescritos.
Para alterar texto, menu, rodapé ou criar página nova, edite:

| Arquivo | O que tem dentro |
|---|---|
| `build/base.py` | casca comum: head, header, menu, rodapé, popups de login, componentes |
| `build/pag_geral.py` | home, sobre, soluções, diferenciais, unidades, proposta, trabalhe conosco |
| `build/pag_servico.py` | as 10 páginas de serviço (PGR, PCMSO, LTCAT, PPP, eSocial, exames, treinamentos, engenharia, consultoria, unidade móvel) |

Depois de editar, rode:

    cd build && python3 gerar.py

CSS e JS não passam pelo gerador. Ficam direto em `site/css/style.css` e
`site/js/main.js`.

## Login

Os popups apontam para o sistema da ASAP (carlos-ti.com) e as URLs estão em
`build/base.py`, no dicionário `PAINEL`. **Não alterar sem falar com a SPS**,
é sistema de terceiro.

## Formulários

Proposta e Trabalhe Conosco não têm back-end. Eles validam os campos e abrem
o WhatsApp da SPS com a mensagem montada. Nada é armazenado no site. Se um dia
houver servidor, o ponto de troca é a seção 7 de `site/js/main.js`.

## Mapa

`site/js/map-data.js` tem a geometria real de Santa Catarina (malha IBGE,
projeção Mercator). É gerado uma vez e não precisa ser refeito. A lista de
unidades e as coordenadas dos alfinetes ficam em `site/js/main.js`, na
seção 5.

## Imagens

Duas origens, ambas fora da pasta servida:

- `banco/` são as fotos de banco de imagem (obra, indústria, medicina).
- `banco/sps/` são as fotos reais da SPS, tiradas do site atual deles.
- `site/img/linha/` tem os treze marcos da linha do tempo, que já vêm com ano
  e legenda na arte.

O site **não** serve esses originais. Quem prepara tudo é:

    cd build && python3 imagens.py

O script recorta em 16:9 respeitando um ponto de foco vertical, gera WebP e
JPEG em três larguras (1600, 1000 e 640) e escreve `site/img/manifesto.json`.
O gerador lê esse manifesto e monta `<picture>` com `srcset`, então o navegador
baixa só o tamanho que precisa. Rodar de novo apaga o que ficou obsoleto.

Para trocar uma foto ou mexer no enquadramento, edite os dicionários
`BANCO_MAPA` e `SPS_MAPA` em `build/imagens.py`. O terceiro valor é o foco
vertical: 0 corta pelo topo, 1 pelo rodapé. Depois rode `imagens.py` e
`gerar.py`.

### Foto de fundo de seção

`fundo("slug", "força")` em `build/base.py` põe uma foto atrás de um véu
escuro. A seção precisa ter a classe `tem-foto`. Quatro intensidades:

| força | opacidade | quando usar |
|---|---|---|
| `sutil` | 0.22 | seções com grade de cards, onde a foto só dá textura |
| `leve`  | 0.42 | padrão |
| `media` | 0.55 | seções de destaque, com pouco texto |
| `forte` | 0.70 | uso pontual |

O véu fecha nas bordas com a cor da seção, então uma seção emenda na outra
sem costura. Se quiser mais ou menos presença, mexa na opacidade em
`site/css/style.css`, no bloco "FOTO DE FUNDO DE SEÇÃO". Conferi o contraste
depois de calibrar: 15:1 no texto e 8:1 no verde, no ponto mais claro da foto.
