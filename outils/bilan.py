#!/usr/bin/env python3
"""Chiffres pour le rapport : tailles par niveau, filles par boîte, natures, défis, bilan des relectures."""
import json, os, re, glob, collections, statistics
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
t = json.load(open(os.path.join(R, "taxonomie.json"), encoding="utf8"))
niv = collections.Counter(b["niveau"] for b in t)
print("Boîtes par niveau :", dict(sorted(niv.items())), "total", len(t))
enf = collections.Counter(b["parent"] for b in t if b["parent"])
par = {b["id"]: b for b in t}
for n in range(1, 8):
    v = [enf[b["id"]] for b in t if b["niveau"] == n]
    print(f"  filles par boîte de niveau {n} : moyenne {statistics.mean(v):.2f}, min {min(v)}, max {max(v)}, répartition {dict(sorted(collections.Counter(v).items()))}")
for th in ("1.1", "1.2"):
    print(th, par[th]["libelle"], {n: sum(1 for b in t if b["niveau"] == n and b["id"].startswith(th)) for n in range(3, 9)})
for n in (6, 7, 8):
    c = collections.Counter(b.get("nature") for b in t if b["niveau"] == n)
    tot = sum(c.values())
    print(f"Natures niveau {n} :", {k: f"{100*v/tot:.0f} %" for k, v in c.most_common()})
c = collections.Counter(d for b in t if b["niveau"] == 8 for d in b["defis"])
n8 = niv[8]
print("Défis au niveau 8 :", {k: f"{100*v/n8:.0f} %" for k, v in c.most_common()})
print("Longueur des libellés de niveau 8 (mots) : médiane", statistics.median(len(b["libelle"].split()) for b in t if b["niveau"] == 8))
# relectures
tot = collections.Counter()
refaire = []
fichiers = sorted(glob.glob(os.path.join(R, "verification/n78-*.md")))
for f in fichiers:
    s = open(f, encoding="utf8").read()
    for cle, motif in [("n8", r"niveaux 8 du levier\s*:\s*(\d+)"), ("ech", r"chantillon relu au fond\s*:\s*(\d+)"), ("def", r"fectueux dans l.échantillon\s*:\s*(\d+)"),
                       ("dbl", r"doublons trouvés en passe 1\s*:\s*(\d+)"), ("hors", r"hors périmètre trouvés en passe 1\s*:\s*(\d+)"), ("cor", r"corrections faites\s*:\s*(\d+)")]:
        m = re.search(motif, s)
        if m:
            tot[cle] += int(m.group(1))
        else:
            tot["manque_" + cle] += 1
    m = re.search(r"lots à refaire\s*:\s*(.+)", s)
    if m and "aucun" not in m.group(1).lower():
        refaire.append((os.path.basename(f), m.group(1).strip()))
    for k, motif in [("forme", r"forme (\d+)"), ("réalité", r"réalité (\d+)"), ("précision", r"précision (\d+)"), ("place", r"place (\d+)"), ("définition", r"définition (\d+)")]:
        m = re.search(motif, s)
        if m:
            tot["t_" + k] += int(m.group(1))
print(f"Relectures des niveaux 7 et 8 : {len(fichiers)} journaux")
print(dict(tot))
if tot["ech"]:
    print(f"  échantillon : {tot['ech']} niveaux 8 relus au fond ({100*tot['ech']/max(1,n8):.1f} % du niveau 8) ; défectueux : {tot['def']} ({100*tot['def']/tot['ech']:.1f} %)")
print("  lots à refaire :", refaire or "aucun")
