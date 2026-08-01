# -*- coding: utf-8 -*-
"""Gera o site estático da SPS em ../site/.

Uso:  python3 gerar.py
Os arquivos .html em site/ são SAÍDA. Edite o conteúdo aqui, não lá.
"""

import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
SAIDA = os.path.normpath(os.path.join(AQUI, "..", "site"))
sys.path.insert(0, AQUI)

import pag_geral
import pag_servico


def main():
    paginas = pag_geral.gerar() + pag_servico.gerar()
    if not os.path.isdir(SAIDA):
        raise SystemExit("pasta de saída não encontrada: %s" % SAIDA)

    escritos = []
    for nome, html in paginas:
        caminho = os.path.join(SAIDA, nome)
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(html)
        escritos.append((nome, len(html)))

    escritos.sort()
    print("gerado em %s" % SAIDA)
    for nome, n in escritos:
        print("  %-22s %6.1f KB" % (nome, n / 1024.0))
    print("  %d páginas" % len(escritos))


if __name__ == "__main__":
    main()
