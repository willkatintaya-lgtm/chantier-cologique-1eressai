#!/usr/bin/env python3
"""Assemble l'arbre : lit arbre/*.txt (niveaux 1 à 5) et lots/ (niveaux 6 à 8),
contrôle la structure, écrit taxonomie.json et index.html.

Usage : python3 outils/assembler.py [--factice] [--sortie DOSSIER]
  --factice : complète les niveaux 6 à 8 manquants par des boîtes factices (test de fluidité).
"""
import json, os, re, sys, glob, collections, unicodedata, random

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFIS = {"A": "atténuation", "D": "adaptation", "B": "biodiversité", "R": "ressources", "P": "pollutions et santé"}
NATURES = {"T": "technique", "E": "économique", "R": "réglementaire", "O": "organisationnelle", "C": "comportementale"}
alertes = []


def alerte(msg):
    alertes.append(msg)


def champs(ligne):
    return [c.strip() for c in ligne.split("|")]


def defis(code, ou):
    out = []
    for c in code.split():
        if c not in DEFIS:
            alerte(f"défi inconnu « {c} » : {ou}")
            continue
        if DEFIS[c] not in out:
            out.append(DEFIS[c])
    if not out:
        alerte(f"aucun défi : {ou}")
    return out


def nature(code, ou):
    code = code.strip().upper()[:1]
    if code not in NATURES:
        alerte(f"nature inconnue « {code} » : {ou}")
        return None
    return NATURES[code]


def lire_haut():
    boites = {}
    for f in ["arbre/niveaux-1-4.txt", "arbre/niveau-5.txt"]:
        for l in open(os.path.join(RACINE, f), encoding="utf8"):
            l = l.strip()
            if not l or l.startswith("#"):
                continue
            c = champs(l)
            if len(c) != 6:
                alerte(f"{f} : {len(c)} champs : {l[:60]}")
                continue
            i = c[0]
            boites[i] = dict(id=i, parent=i.rsplit(".", 1)[0] if "." in i else None, niveau=i.count(".") + 1,
                             libelle=c[1], definition=c[2], critere=c[3], defis=defis(c[4], i), renvois=c[5].split())
    return boites


def lire_n6(boites):
    """lots/n6/<levier>.txt : « @ id-chantier | critère » puis « 6 | libellé | définition | défis | nature »."""
    for f in sorted(glob.glob(os.path.join(RACINE, "lots/n6/*.txt"))):
        courant, k = None, 0
        for no, l in enumerate(open(f, encoding="utf8"), 1):
            l = l.strip()
            if not l or l.startswith("#"):
                continue
            c = champs(l)
            ou = f"{os.path.basename(f)}:{no}"
            if c[0] == "@":
                courant, k = c[1], 0
                if courant not in boites or boites[courant]["niveau"] != 5:
                    alerte(f"chantier inconnu {courant} : {ou}")
                    courant = None
                    continue
                boites[courant]["critere"] = c[2] if len(c) > 2 else ""
            elif c[0] == "6" and courant:
                if len(c) != 5:
                    alerte(f"{len(c)} champs au lieu de 5 : {ou}")
                    continue
                k += 1
                i = f"{courant}.{k}"
                boites[i] = dict(id=i, parent=courant, niveau=6, libelle=c[1], definition=c[2], critere="",
                                 defis=defis(c[3], ou), renvois=[], nature=nature(c[4], ou))
            else:
                alerte(f"ligne non comprise : {ou}")


def lire_n78(boites):
    """lots/n78/<chantier>.txt : « @ n | critère du verrou n », « 7 | lib | déf | critère | défis | nature », « 8 | lib | déf | défis | nature »."""
    for f in sorted(glob.glob(os.path.join(RACINE, "lots/n78/*.txt"))):
        chantier = os.path.basename(f)[:-4]
        p6 = p7 = None
        k7 = k8 = 0
        for no, l in enumerate(open(f, encoding="utf8"), 1):
            l = l.strip()
            if not l or l.startswith("#"):
                continue
            c = champs(l)
            ou = f"{os.path.basename(f)}:{no}"
            if c[0] == "@":
                p6 = f"{chantier}.{c[1]}"
                p7, k7 = None, 0
                if p6 not in boites:
                    alerte(f"verrou inconnu {p6} : {ou}")
                    p6 = None
                    continue
                boites[p6]["critere"] = c[2] if len(c) > 2 else ""
            elif c[0] == "7" and p6:
                if len(c) != 6:
                    alerte(f"{len(c)} champs au lieu de 6 : {ou}")
                    continue
                k7 += 1
                k8 = 0
                p7 = f"{p6}.{k7}"
                boites[p7] = dict(id=p7, parent=p6, niveau=7, libelle=c[1], definition=c[2], critere=c[3],
                                  defis=defis(c[4], ou), renvois=[], nature=nature(c[5], ou))
            elif c[0] == "8" and p7:
                if len(c) != 5:
                    alerte(f"{len(c)} champs au lieu de 5 : {ou}")
                    continue
                k8 += 1
                i = f"{p7}.{k8}"
                boites[i] = dict(id=i, parent=p7, niveau=8, libelle=c[1], definition=c[2], critere="",
                                 defis=defis(c[3], ou), renvois=[], nature=nature(c[4], ou))
            else:
                alerte(f"ligne non comprise : {ou}")


def factice(boites):
    rnd = random.Random(1)
    mots = "rendre installer financer réparer faire revenir isoler remplacer collecter trier sans surcoût en logement occupé pour un artisan seul dans une copropriété ancienne avec un reste à charge nul".split()

    def phrase(n):
        return " ".join(rnd.choice(mots) for _ in range(n)).capitalize()

    for b in list(boites.values()):
        if b["niveau"] >= 5 and b["niveau"] < 8 and not any(x["parent"] == b["id"] for x in boites.values() if x["niveau"] == b["niveau"] + 1):
            pass
    enf = collections.Counter(b["parent"] for b in boites.values())
    file = [b for b in boites.values() if 5 <= b["niveau"] < 8 and not enf[b["id"]]]
    while file:
        b = file.pop()
        for k in range(1, rnd.choice([3, 4, 4, 5]) + 1):
            i = f"{b['id']}.{k}"
            boites[i] = dict(id=i, parent=b["id"], niveau=b["niveau"] + 1, libelle="[factice] " + phrase(9), definition=phrase(16) + ".",
                             critere="", defis=rnd.sample(list(DEFIS.values()), rnd.choice([1, 2])), renvois=[], nature=rnd.choice(list(NATURES.values())))
            if boites[i]["niveau"] < 8:
                file.append(boites[i])


def cle(i):
    return [int(x) for x in i.split(".")]


def norm(s):
    s = unicodedata.normalize("NFD", s.lower())
    return re.sub(r"[^a-z0-9 ]+", " ", "".join(c for c in s if unicodedata.category(c) != "Mn")).split()


def controler(boites, complet):
    enf = collections.defaultdict(list)
    for b in boites.values():
        if b["parent"]:
            if b["parent"] not in boites:
                alerte(f"orphelin {b['id']}")
            enf[b["parent"]].append(b["id"])
    for b in boites.values():
        n = len(enf[b["id"]])
        if b["niveau"] < 8 and n:
            if not 2 <= n <= 7:
                alerte(f"{n} filles (hors tolérance 2 à 7) : {b['id']} {b['libelle']}")
            if b["niveau"] > 1 and not b["critere"]:
                alerte(f"critère de partage manquant : {b['id']} {b['libelle']}")
        if complet and b["niveau"] < 8 and not n:
            alerte(f"boîte sans fille : {b['id']} {b['libelle']}")
        if not b["libelle"] or not b["definition"]:
            alerte(f"libellé ou définition vide : {b['id']}")
        if b["definition"] and not b["definition"].rstrip().endswith("."):
            alerte(f"définition sans point final : {b['id']}")
        for r in b["renvois"]:
            if r not in boites:
                alerte(f"renvoi inconnu {r} dans {b['id']}")
    # doublons exacts de libellé
    vus = collections.defaultdict(list)
    for b in boites.values():
        vus[" ".join(norm(b["libelle"]))].append(b["id"])
    for k, v in vus.items():
        if len(v) > 1:
            alerte(f"libellé en double : {', '.join(v)} « {k[:70]} »")
    return enf


def main():
    args = sys.argv[1:]
    sortie = RACINE
    if "--sortie" in args:
        sortie = args[args.index("--sortie") + 1]
        os.makedirs(sortie, exist_ok=True)
    boites = lire_haut()
    lire_n6(boites)
    lire_n78(boites)
    if "--factice" in args:
        factice(boites)
    complet = any(b["niveau"] == 8 for b in boites.values()) and "--partiel" not in args
    controler(boites, complet)
    liste = sorted(boites.values(), key=lambda b: cle(b["id"]))
    champs_ordre = ["id", "parent", "niveau", "libelle", "definition", "critere", "defis", "renvois", "nature"]
    liste = [{k: b[k] for k in champs_ordre if k in b and not (k == "nature" and b[k] is None)} for b in liste]
    lignes = ",\n".join(json.dumps(b, ensure_ascii=False, separators=(",", ":")) for b in liste)
    donnees = "[\n" + lignes + "\n]\n"
    open(os.path.join(sortie, "taxonomie.json"), "w", encoding="utf8").write(donnees)
    gabarit = open(os.path.join(RACINE, "outils/gabarit.html"), encoding="utf8").read()
    page = gabarit.replace("/*__DONNEES__*/", donnees.replace("</", "<\\/"))
    entete = '<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    tete, corps = page.split("</style>", 1)
    open(os.path.join(sortie, "index.html"), "w", encoding="utf8").write(
        entete + tete + "</style>\n</head>\n<body>" + corps + "</body>\n</html>\n")
    # variante sans données en ligne (lit taxonomie.json à côté), pour publication
    open(os.path.join(sortie, "page-publiee.html"), "w", encoding="utf8").write(gabarit.replace("/*__DONNEES__*/", ""))
    niv = collections.Counter(b["niveau"] for b in liste)
    print("Boîtes par niveau :", dict(sorted(niv.items())), "total", len(liste))
    print(f"{len(alertes)} alerte(s)")
    for a in alertes[:int(os.environ.get('MAX_ALERTES', '60'))]:
        print(" -", a)
    json.dump(alertes, open(os.path.join(sortie, "alertes.json"), "w", encoding="utf8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
