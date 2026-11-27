#!/usr/bin/env python3
"""Fabrique, pour chaque chantier de niveau 5, le contexte donné à l'agent qui écrit ses niveaux 7 et 8 : lots/contexte/<id>.md"""
import os, sys, json, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import assembler as A

R = A.RACINE
b = A.lire_haut()
A.lire_n6(b)
enf = {}
for x in b.values():
    if x["parent"]:
        enf.setdefault(x["parent"], []).append(x)
for v in enf.values():
    v.sort(key=lambda x: A.cle(x["id"]))
os.makedirs(os.path.join(R, "lots/contexte"), exist_ok=True)
TRANSVERSES = ["1.1.2.2", "1.1.2.3", "1.1.2.4", "1.2.1.1", "1.2.1.3", "1.2.1.4", "1.2.3.2.6", "1.2.5.1.3"]
liste = []
for c in sorted((x for x in b.values() if x["niveau"] == 5), key=lambda x: A.cle(x["id"])):
    i = c["id"]
    L = [f"# Contexte du chantier {i} « {c['libelle']} »", "", "## Sa lignée (du plus large au plus précis)"]
    anc, p = [], c
    while p:
        anc.insert(0, p)
        p = b.get(p["parent"]) if p["parent"] else None
    for a in anc:
        L.append(f"- Niveau {a['niveau']} — {a['id']} **{a['libelle']}** : {a['definition']}" + (f" _Découpage de ses filles : {a['critere']}_" if a["critere"] else ""))
    if c["renvois"]:
        L += ["", "## Ses renvois (sujets voisins traités ailleurs : ne les développe pas ici)"]
        L += [f"- {r} {b[r]['libelle']} : {b[r]['definition']}" for r in c["renvois"] if r in b]
    v6 = enf.get(i, [])
    L += ["", f"## Ses {len(v6)} verrous de niveau 6 (à développer, dans cet ordre, sous « @ 1 », « @ 2 »…)"]
    for k, v in enumerate(v6, 1):
        L.append(f"{k}. **{v['libelle']}** — {v['definition']} (nature dominante : {v.get('nature')}, défis : {', '.join(v['defis'])})")
    L += ["", "## Les chantiers frères (même levier) et leurs verrous : ce qu'ils couvrent ne va PAS chez toi"]
    for f in enf[c["parent"]]:
        if f["id"] == i:
            continue
        L.append(f"- {f['id']} **{f['libelle']}** : {f['definition']}")
        for v in enf.get(f["id"], []):
            L.append(f"    - {v['libelle']}")
    gc = b[b[c["parent"]]["parent"]]
    L += ["", f"## Les autres chantiers du même grand chantier ({gc['libelle']})"]
    for lev in enf[gc["id"]]:
        if lev["id"] == c["parent"]:
            continue
        L.append(f"- {lev['id']} {lev['libelle']} : " + " ; ".join(f"{f['libelle']}" for f in enf[lev["id"]]))
    L += ["", "## Les chantiers transverses de l'arbre (un verrou générique de ce type n'a sa place que là-bas)"]
    for t in TRANSVERSES:
        if t in b and not i.startswith(t):
            L.append(f"- {t} {b[t]['libelle']}" + (" : " + " ; ".join(f["libelle"] for f in enf.get(t, [])) if b[t]["niveau"] == 4 else ""))
    L += ["", "## Hors périmètre de tout l'arbre", "Se déplacer (véhicules, vélos, transport de colis), se nourrir (ce que l'on mange, gaspillage alimentaire), produire (énergie des usines, centrales, réseaux électriques, centres de données), préserver les écosystèmes (gestion des forêts, de l'eau, des milieux), séismes, ouvrages collectifs de protection, réseaux publics d'eau, conditions de travail.", ""]
    open(os.path.join(R, f"lots/contexte/{i}.md"), "w", encoding="utf8").write("\n".join(L))
    # dossier complet en un seul fichier : mission + consignes + contexte
    mission = open(os.path.join(R, "lots/PROMPT-N78-COURT.md"), encoding="utf8").read().replace("<ID>", i).replace("<N6>", str(len(v6)))
    consignes = open(os.path.join(R, "lots/CONSIGNES.md"), encoding="utf8").read()
    consignes = consignes.split("## Format de fichier, niveau 6")[0] + "## Format de fichier, niveaux 7 et 8" + consignes.split("## Format de fichier, niveaux 7 et 8")[1]
    os.makedirs(os.path.join(R, "lots/dossier"), exist_ok=True)
    open(os.path.join(R, f"lots/dossier/{i}.md"), "w", encoding="utf8").write(mission + "\n\n---\n\n" + consignes + "\n\n---\n\n" + "\n".join(L))
    liste.append({"id": i, "lib": c["libelle"], "n6": len(v6)})
json.dump(liste, open(os.path.join(R, "lots/contexte/_liste.json"), "w", encoding="utf8"), ensure_ascii=False)
print(len(liste), "contextes ;", sum(1 for x in liste if x["n6"] == 0), "chantiers sans niveau 6 ;", sum(x["n6"] for x in liste), "verrous de niveau 6")
