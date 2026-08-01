# BACKUP2 · congelado em 01/08/2026

Segunda versão do site da SPS. Não editar: esta pasta é referência.

O que tem aqui:
- 17 páginas geradas (institucionais, 10 de serviço, 2 de formulário)
- fotos de banco distribuídas por tema, WebP + srcset
- fotos de fundo de seção (6 na home)
- mapa animado de Santa Catarina com as 5 unidades
- contraste do botão principal corrigido para WCAG AA
- correção de telas abaixo de 420px

O gerador correspondente está em `backup02-build/`.

Restaurar:

    rm -rf SPS/site SPS/build
    cp -R SPS/backup02-site SPS/site
    cp -R SPS/backup02-build SPS/build
