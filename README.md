# SPS Segurança do Trabalho · site

Site institucional de 17 páginas para a SPS Segurança do Trabalho, empresa de
medicina ocupacional, engenharia de segurança e treinamentos de NRs, com cinco
unidades no litoral norte de Santa Catarina.

HTML estático puro, sem framework e sem dependência em tempo de execução.
Sobe em qualquer hospedagem.

## Rodar localmente

```bash
cd site
python3 -m http.server 4173
```

E abrir <http://localhost:4173>.

## Estrutura

| Pasta | O que é |
|---|---|
| `site/` | o site pronto. É isso que vai para a hospedagem |
| `build/` | o gerador em Python que produz as 17 páginas |
| `backup01-site/` | primeira versão, de página única. Congelada |
| `backup02-site/` + `backup02-build/` | segunda versão. Congelada |

Os arquivos `.html` dentro de `site/` são **saída** e são sobrescritos a cada
build. Para mudar conteúdo, menu ou rodapé, edite o gerador:

```bash
cd build && python3 gerar.py
```

| Arquivo | Conteúdo |
|---|---|
| `build/base.py` | casca comum: head, header, menu, rodapé, popups de login, componentes |
| `build/pag_geral.py` | home, sobre, soluções, diferenciais, unidades, proposta, trabalhe conosco |
| `build/pag_servico.py` | as 10 páginas de serviço |
| `build/imagens.py` | prepara as imagens (recorte, WebP, srcset) |

CSS e JS não passam pelo gerador: ficam direto em `site/css/style.css` e
`site/js/main.js`.

## O que tem de interessante aqui

**Mapa animado de Santa Catarina.** Geometria real, malha do IBGE em projeção
Mercator, com as 295 divisas municipais. A animação traça o contorno do estado,
preenche, dá zoom no litoral norte e solta os cinco alfinetes. Os alfinetes
ficam dentro do grupo da câmera e só compensam a escala, de modo que a posição
não tem como sair do lugar. Código na seção 5 de `site/js/main.js`, geometria
em `site/js/map-data.js`.

**Imagens responsivas.** `build/imagens.py` recorta em 16:9 respeitando um
ponto de foco vertical, gera WebP e JPEG em três larguras e escreve um
manifesto que o gerador usa para montar `<picture>` com `srcset`.

**Formulários sem back-end.** Proposta e Trabalhe Conosco validam os campos e
abrem o WhatsApp com a mensagem montada. Nada é armazenado.

## Imagens

Os originais não estão versionados: são 129 MB de fotos de banco licenciadas,
mais as fotos da própria SPS. O repositório carrega apenas as versões
processadas, em `site/img/`.

Consequência prática: `build/imagens.py` só roda em quem tiver a pasta `banco/`
localmente. `build/gerar.py` roda normalmente, porque lê o manifesto já pronto.

## Área de login

Os dois popups apontam para o sistema da ASAP (`carlos-ti.com`), fornecedor da
SPS. As URLs estão em `build/base.py`, no dicionário `PAINEL`, e são as mesmas
já publicadas no site atual deles. **Não alterar sem falar com a SPS**: é
sistema de terceiro.

## Documentação

`LEIA-ME.md` tem o detalhe de manutenção: como trocar foto, ajustar
enquadramento, calibrar as fotos de fundo de seção e mexer no mapa.
