#!/usr/bin/env python3
"""Cherche les quasi-doublons de libellés dans tout l'arbre (niveaux 6 à 8), y compris entre branches éloignées.
Usage : python3 outils/doublons.py [seuil, défaut 0.6]  → verification/doublons.md"""
import json, os, re, sys, unicodedata, collections
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
seuil = float(sys.argv[1]) if len(sys.argv) > 1 else 0.6
VIDES = set("sans avec pour dans plus moins cher chez leur leurs quand faire rendre comme entre aussi tout tous cette celui deux sous vers etre avoir".split())


def mots(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return frozenset(m[:7] for m in re.sub(r"[^a-z0-9 ]+", " ", s).split() if len(m) > 3 and m not in VIDES)


t = json.load(open(os.path.join(R, "taxonomie.json"), encoding="utf8"))
B = [(b["id"], b["niveau"], b["libelle"], mots(b["libelle"])) for b in t if b["niveau"] >= 6]
index = collections.defaultdict(list)
for k, (_, _, _, m) in enumerate(B):
    for x in m:
        index[x].append(k)
paires = {}
for x, ks in index.items():
    if len(ks) > 400:
        continue
    for a in range(len(ks)):
        for b in range(a + 1, len(ks)):
            i, j = ks[a], ks[b]
            if (i, j) in paires:
                continue
            mi, mj = B[i][3], B[j][3]
            if abs(B[i][1] - B[j][1]) > 1 or min(len(mi), len(mj)) < 3:
                continue
            jac = len(mi & mj) / len(mi | mj)
            if jac >= seuil:
                paires[(i, j)] = jac
res = sorted(paires.items(), key=lambda kv: -kv[1])
L = [f"# Quasi-doublons de libellés (niveaux 6 à 8), similarité ≥ {seuil}", "", f"{len(res)} paires sur {len(B)} boîtes.", ""]
for (i, j), jac in res:
    meme = B[i][0].rsplit(".", 1)[0] == B[j][0].rsplit(".", 1)[0]
    L.append(f"- {jac:.2f} {'(sœurs)' if meme else ''}\n  - {B[i][0]} {B[i][2]}\n  - {B[j][0]} {B[j][2]}")
open(os.path.join(R, "verification/doublons.md"), "w", encoding="utf8").write("\n".join(L) + "\n")
print(len(res), "paires ≥", seuil, "sur", len(B), "boîtes ; exactes ou quasi (≥ 0.85) :", sum(1 for _, v in res if v >= 0.85))
