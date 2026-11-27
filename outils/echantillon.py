#!/usr/bin/env python3
"""Tire l'échantillon à relire au fond pour un levier : 12 % des niveaux 8 (au moins 5 par chantier), tirage reproductible.
Usage : python3 outils/echantillon.py <id du levier>"""
import sys, glob, os, random, hashlib
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
lev = sys.argv[1]
tot = 0
for f in sorted(glob.glob(os.path.join(R, f"lots/n78/{lev}.*.txt"))):
    lignes = [(no, l.strip()) for no, l in enumerate(open(f, encoding="utf8"), 1) if l.startswith("8")]
    rnd = random.Random(int(hashlib.md5(os.path.basename(f).encode()).hexdigest(), 16))
    k = max(5, round(0.12 * len(lignes)))
    tirage = sorted(rnd.sample(lignes, min(k, len(lignes))))
    tot += len(tirage)
    print(f"\n== {os.path.basename(f)} : {len(lignes)} niveaux 8, {len(tirage)} à relire au fond ==")
    for no, l in tirage:
        print(f"ligne {no} : {l.split('|')[1].strip()}")
print(f"\nTotal de l'échantillon : {tot} niveaux 8")
