#!/usr/bin/env python3
"""Vérifie la forme d'un lot de niveaux 7 et 8. Usage : python3 outils/verifier_lot.py <fichier> [nombre de verrous de niveau 6 attendus]"""
import sys, re, unicodedata, collections

DEFIS, NATURES = set("ADBRP"), set("TEROC")


def mots(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return [m for m in re.sub(r"[^a-z0-9 ]+", " ", s).split() if len(m) > 3]


def verifier(chemin, attendus=None):
    err, avert = [], []
    blocs, b7, lib = [], None, []
    for no, l in enumerate(open(chemin, encoding="utf8"), 1):
        l = l.strip()
        if not l:
            continue
        c = [x.strip() for x in l.split("|")]
        if c[0].startswith("@"):
            num = c[0][1:].strip()
            if not num.isdigit():
                err.append(f"ligne {no} : « @ » doit être suivi du numéro du verrou (1, 2, 3…)")
            if len(c) != 2 or not c[1]:
                err.append(f"ligne {no} : la ligne « @ » doit avoir 2 champs : numéro | critère de partage")
            blocs.append({"no": no, "num": num, "n7": []})
            b7 = None
        elif c[0] == "7":
            if not blocs:
                err.append(f"ligne {no} : ligne « 7 » avant toute ligne « @ »")
                continue
            if len(c) != 6:
                err.append(f"ligne {no} : une ligne « 7 » doit avoir 6 champs (7 | libellé | définition | critère | défis | nature), elle en a {len(c)}")
                continue
            b7 = {"no": no, "n8": 0}
            blocs[-1]["n7"].append(b7)
            controle(c[1], c[2], c[4], c[5], no, err, avert)
            if not c[3]:
                err.append(f"ligne {no} : critère de partage vide")
            lib.append((no, c[1]))
        elif c[0] == "8":
            if b7 is None:
                err.append(f"ligne {no} : ligne « 8 » sans ligne « 7 » au-dessus")
                continue
            if len(c) != 5:
                err.append(f"ligne {no} : une ligne « 8 » doit avoir 5 champs (8 | libellé | définition | défis | nature), elle en a {len(c)}")
                continue
            b7["n8"] += 1
            controle(c[1], c[2], c[3], c[4], no, err, avert)
            n = len(c[1].split())
            if n < 6:
                err.append(f"ligne {no} : niveau 8 trop court ({n} mots) : il manque sans doute la contrainte")
            if n > 24:
                err.append(f"ligne {no} : niveau 8 trop long ({n} mots)")
            lib.append((no, c[1]))
        else:
            err.append(f"ligne {no} : ligne non reconnue (doit commencer par @, 7 ou 8)")
    if attendus and len(blocs) != attendus:
        err.append(f"{len(blocs)} blocs « @ » au lieu de {attendus} (un par verrou de niveau 6 du chantier)")
    nums = [b["num"] for b in blocs]
    if nums != [str(i + 1) for i in range(len(blocs))]:
        err.append(f"les blocs « @ » doivent être numérotés 1, 2, 3… dans l'ordre ; trouvé : {', '.join(nums)}")
    for b in blocs:
        if not 3 <= len(b["n7"]) <= 6:
            err.append(f"verrou {b['num']} : {len(b['n7'])} niveaux 7 (il en faut 3 à 5)")
        for s in b["n7"]:
            if not 3 <= s["n8"] <= 6:
                err.append(f"ligne {s['no']} : ce niveau 7 a {s['n8']} niveaux 8 (il en faut 3 à 5)")
    # doublons et quasi-doublons
    ens = [(no, l, set(mots(l))) for no, l in lib]
    for i in range(len(ens)):
        for j in range(i + 1, len(ens)):
            a, b = ens[i][2], ens[j][2]
            if not a or not b:
                continue
            jac = len(a & b) / len(a | b)
            if jac >= 0.75:
                err.append(f"lignes {ens[i][0]} et {ens[j][0]} : libellés presque identiques (doublon)")
            elif jac >= 0.55:
                avert.append(f"lignes {ens[i][0]} et {ens[j][0]} : libellés proches, vérifier que ce ne sont pas deux fois le même problème")
    n7 = sum(len(b["n7"]) for b in blocs)
    n8 = sum(s["n8"] for b in blocs for s in b["n7"])
    return err, avert, len(blocs), n7, n8


def controle(lib, defi, d, nat, no, err, avert):
    if not lib or not defi:
        err.append(f"ligne {no} : libellé ou définition vide")
        return
    if lib.endswith("."):
        err.append(f"ligne {no} : le libellé ne doit pas finir par un point")
    if not defi.endswith("."):
        err.append(f"ligne {no} : la définition doit finir par un point")
    codes = d.split()
    if not codes or any(x not in DEFIS for x in codes) or len(codes) > 3:
        err.append(f"ligne {no} : défis invalides « {d} » (1 à 3 lettres parmi A D B R P, séparées par des espaces)")
    if nat not in NATURES:
        err.append(f"ligne {no} : nature invalide « {nat} » (une lettre parmi T E R O C)")
    premier = lib.split()[0].lower() if lib.split() else ""
    if not re.search(r"(er|ir|re|oir)$", premier.strip("'’")) and not premier.startswith(("s'", "s’", "se")):
        avert.append(f"ligne {no} : le libellé ne semble pas commencer par un verbe à l'infinitif (« {premier} »)")


if __name__ == "__main__":
    e, a, n6, n7, n8 = verifier(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else None)
    print(f"{n6} verrous, {n7} niveaux 7, {n8} niveaux 8")
    for x in e:
        print("ERREUR  ", x)
    for x in a:
        print("à vérifier", x)
    print("FORME CORRECTE" if not e else f"{len(e)} ERREUR(S) À CORRIGER")
    sys.exit(1 if e else 0)
