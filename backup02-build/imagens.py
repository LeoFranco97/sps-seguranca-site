# -*- coding: utf-8 -*-
"""Prepara as imagens do site: recorta, redimensiona e gera WebP + JPEG.

Uso:  python3 imagens.py

Lê de SPS/banco/ (fotos de banco) e das fotos originais da SPS já em site/img/,
escreve tudo em site/img/foto/ com larguras responsivas, e grava
site/img/manifesto.json para o gerador saber quais larguras existem.
"""

import json
import os
from PIL import Image, ImageOps

AQUI = os.path.dirname(os.path.abspath(__file__))
SPS = os.path.normpath(os.path.join(AQUI, ".."))
BANCO = os.path.join(SPS, "banco")
BANCO_SPS = os.path.join(BANCO, "sps")   # fotos originais da própria SPS
IMG = os.path.join(SPS, "site", "img")
FOTO = os.path.join(IMG, "foto")

LARGURAS = {"hero": [1600, 1000, 640], "card": [900, 560]}

# slug -> (origem, foco vertical 0..1, uso)
BANCO_MAPA = {
    "risco-equipe":  ("colleagues-with-safety-equipment-working-with-blueprints.jpg", .40, "hero"),
    "medico":        ("young-handsome-physician-medical-robe-with-stethoscope.jpg", .35, "hero"),
    "ambiente-obra": ("male-worker-with-bulldozer-sand-quarry.jpg", .42, "hero"),
    "documentos":    ("form-records-desk-pen-information.jpg", .50, "hero"),
    "esocial":       ("hands-unrecognizable-female-doctor-writing-form-typing-laptop-keyboard.jpg", .45, "hero"),
    # retrato alto: o recorte 16:9 precisa cair embaixo, onde estão a mão,
    # o estetoscópio e os documentos. Mais acima só pega parede desfocada.
    "consulta":      ("general-practitioner-consulting-patient-reviewing-x-ray-test-results.jpg", .72, "hero"),
    "capacete":      ("closeup-construction-worker-holding-hard-hat-his-hands.jpg", .45, "hero"),
    "altura":        ("workers-examining-work.jpg", .45, "hero"),
    "reuniao":       ("three-people-discussing-plan-factory.jpg", .40, "hero"),
    "engenheiro":    ("engineer-holding-hard-hat-construction-worker-professional-safety-work-industry-building-person-manager-service.jpg", .42, "hero"),
    "industria":     ("portrait-asian-female-engineer-wearing-uniform-saftey-helmet-standing-confident-cheerful-automation-robot-arm-machine-factory-background.jpg", .38, "hero"),
    "executivo":     ("unrecognizable-male-construction-industry-executive-posing-safety-vest-with-hardhat.jpg", .42, "hero"),
    "epi":           ("closeup-safety-measures-precautions.jpg", .45, "hero"),
    "epi-bancada":   ("front-view-protective-glasses-with-hard-hat-headphones.jpg", .50, "card"),
}

# fotos reais da SPS (originais ficam em banco/sps/, fora da pasta servida)
SPS_MAPA = {
    "un-corporativo": ("un-corporativo.jpg", .42, "hero"),
    "un-picarras":    ("un-picarras.jpg", .45, "hero"),
    "un-portobelo":   ("un-portobelo.jpg", .45, "hero"),
    "un-itapema":     ("un-itapema.jpg", .45, "card"),
    "un-itajai":      ("un-itajai.jpg", .50, "card"),
    "frota":          ("frota.jpg", .50, "card"),
}


def recorta_169(im, foco):
    alvo = 16 / 9.0
    w, h = im.size
    if w / float(h) > alvo:
        nw = int(h * alvo)
        return im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
    nh = int(w / alvo)
    y = int((h - nh) * foco)
    return im.crop((0, y, w, y + nh))


def processa(origem, slug, foco, uso, manifesto):
    im = Image.open(origem)
    im.draft("RGB", (3200, 3200))
    im = ImageOps.exif_transpose(im).convert("RGB")
    im = recorta_169(im, foco)

    larguras = [l for l in LARGURAS[uso] if l <= im.width] or [im.width]
    for i, lg in enumerate(larguras):
        r = im.resize((lg, int(round(lg * im.height / float(im.width)))), Image.LANCZOS)
        sufixo = "" if i == 0 else "-%d" % lg
        r.save(os.path.join(FOTO, "%s%s.webp" % (slug, sufixo)), quality=76, method=6)
        r.save(os.path.join(FOTO, "%s%s.jpg" % (slug, sufixo)), quality=80,
               optimize=True, progressive=True)
    manifesto[slug] = {"larguras": larguras,
                       "w": larguras[0],
                       "h": int(round(larguras[0] * 9 / 16.0))}


def main():
    if not os.path.isdir(FOTO):
        os.makedirs(FOTO)
    manifesto = {}

    for slug, (arq, foco, uso) in sorted(BANCO_MAPA.items()):
        p = os.path.join(BANCO, arq)
        if os.path.exists(p):
            processa(p, slug, foco, uso, manifesto)

    for slug, (arq, foco, uso) in sorted(SPS_MAPA.items()):
        p = os.path.join(BANCO_SPS, arq)
        if os.path.exists(p):
            processa(p, slug, foco, uso, manifesto)
        else:
            print("  faltando: banco/sps/%s" % arq)

    # linha do tempo: só acrescenta WebP, mantém o enquadramento original
    linha = os.path.join(IMG, "linha")
    if os.path.isdir(linha):
        for f in sorted(os.listdir(linha)):
            if f.endswith(".jpg"):
                im = Image.open(os.path.join(linha, f)).convert("RGB")
                im.save(os.path.join(linha, f[:-4] + ".webp"), quality=80, method=6)

    # selo do rodapé aparece a 88px de altura e pesava 211 KB
    selo = os.path.join(IMG, "selo-13anos.png")
    if os.path.exists(selo):
        im = Image.open(selo).convert("RGBA")
        im.thumbnail((260, 260), Image.LANCZOS)
        im.save(os.path.join(IMG, "selo-13anos.webp"), quality=82, method=6)
        im.save(selo, optimize=True)

    # limpa sobras de execuções anteriores: só fica o que está no manifesto
    validos = set()
    for slug, d in manifesto.items():
        for i, lg in enumerate(d["larguras"]):
            sufixo = "" if i == 0 else "-%d" % lg
            validos.add("%s%s.webp" % (slug, sufixo))
            validos.add("%s%s.jpg" % (slug, sufixo))
    removidos = 0
    for f in os.listdir(FOTO):
        if f not in validos:
            os.remove(os.path.join(FOTO, f))
            removidos += 1
    if removidos:
        print("%d arquivo(s) obsoleto(s) removido(s)" % removidos)

    with open(os.path.join(IMG, "manifesto.json"), "w") as f:
        json.dump(manifesto, f, indent=1, sort_keys=True)

    print("%d fotos processadas" % len(manifesto))
    tot = sum(os.path.getsize(os.path.join(FOTO, f)) for f in os.listdir(FOTO))
    print("site/img/foto: %.1f MB em %d arquivos" % (tot / 1048576.0, len(os.listdir(FOTO))))


if __name__ == "__main__":
    main()
