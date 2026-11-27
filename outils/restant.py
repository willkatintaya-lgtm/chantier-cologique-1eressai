#!/usr/bin/env python3
"""Dit où en est la production des niveaux 7 et 8 : lots corrects, lots en erreur, chantiers restant à écrire.
Usage : python3 outils/restant.py [--json]"""
import json, os, sys, subprocess
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
l = json.load(open(os.path.join(R, "lots/contexte/_liste.json"), encoding="utf8"))
ok, ko, ab = [], [], []
for x in l:
    f = os.path.join(R, "lots/n78", x["id"] + ".txt")
    if not os.path.exists(f):
        ab.append(x)
        continue
    r = subprocess.run([sys.executable, os.path.join(R, "outils/verifier_lot.py"), f, str(x["n6"])], capture_output=True, text=True)
    (ok if r.returncode == 0 else ko).append(x)
if "--json" in sys.argv:
    print(json.dumps([[x["id"], x["n6"]] for x in ab + ko], separators=(",", ":")))
else:
    print(f"{len(ok)} chantiers complets, {len(ko)} en erreur, {len(ab)} à écrire, sur {len(l)}")
    for x in ko:
        print("  en erreur :", x["id"], x["lib"])
    for x in ab:
        print("  à écrire  :", x["id"], x["lib"])
