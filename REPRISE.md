# Où le travail s'est arrêté, et comment le reprendre

Arrêt volontaire le 27 novembre 2026, pour ne pas épuiser les crédits. Tout est commité et poussé sur la branche `claude/vigilant-mayer-pdb21a`.

## État exact

| Niveau | État | Nombre |
|---|---|---|
| 1 à 5 | Terminés, vérifiés par 5 agents indépendants, corrigés deux fois | 1 + 2 + 11 + 50 + 207 |
| 6 | Terminé sur les 207 chantiers, relu et corrigé par grand chantier | 934 verrous |
| 7 et 8, « Mieux se loger » | Terminés sur les 117 chantiers ; **non relus** | 1 931 et 6 091 |
| 7 et 8, « Mieux consommer » | Faits pour 7 chantiers sur 90 ; **83 restent à écrire** | 107 et 356 |

- `taxonomie.json` et `index.html` sont assemblés dans cet état : la page fonctionne, et les 83 chantiers manquants affichent « Cette boîte n'est pas encore détaillée » sous leur niveau 6.
- Aucune relecture des niveaux 7 et 8 par un agent n'a été faite. Seuls contrôles passés : la forme de chaque lot (`outils/verifier_lot.py`) et la recherche automatique de doublons sur tout l'arbre (`verification/doublons.md` : 18 paires proches, aucune quasi identique).
- Test final (60 problèmes) : fait, voir `rapport.md`.

## Ce qu'il reste à faire

1. Écrire les niveaux 7 et 8 des 83 chantiers restants (tous sous 1.2).
2. Réassembler et régénérer le rapport.
3. Facultatif : relire un échantillon des niveaux 7 et 8.

## Reprendre sans relire tout l'historique

Dire à Claude : « Lis REPRISE.md et reprends. » Tout ce qu'il faut est dans le dépôt :

```bash
python3 outils/restant.py          # liste les chantiers restant à écrire
python3 outils/restant.py --json   # la même liste, prête à passer aux agents
```

Pour chaque chantier restant, lancer un agent Sonnet avec cette seule consigne (le dossier contient la mission, les règles et le contexte) :

> Lis en entier `lots/dossier/<id>.md` et exécute la mission qu'il décrit pour le chantier `<id>`.

L'agent écrit `lots/n78/<id>.txt` et le contrôle lui-même. Puis :

```bash
python3 outils/assembler.py        # réécrit taxonomie.json et index.html, signale les anomalies
python3 outils/doublons.py         # doublons sur tout l'arbre → verification/doublons.md
python3 outils/bilan.py            # chiffres pour le rapport
```

## Coût à prévoir pour finir

- Un chantier coûte environ 100 000 tokens à un agent Sonnet (mesuré sur les 124 déjà faits), soit **environ 8 millions de tokens pour les 83 restants**.
- Pour dépenser moins : traiter une partie seulement (par exemple un grand chantier à la fois : 1.2.1 a 13 chantiers, 1.2.2 16, 1.2.3 19, 1.2.4 18, 1.2.5 24, moins les 7 déjà faits), ou demander 3 filles par boîte au lieu de 3 à 4.
- Lancer les agents par vagues de 10 au plus ; l'environnement n'a que 4 processeurs.

## Où trouver quoi

| Fichier ou dossier | Contenu |
|---|---|
| `arbre/niveaux-1-4.txt`, `arbre/niveau-5.txt` | Source des niveaux 1 à 5 (une ligne par boîte) |
| `lots/n6/<levier>.txt` | Source du niveau 6 |
| `lots/n78/<chantier>.txt` | Source des niveaux 7 et 8 (un fichier par chantier fait) |
| `lots/dossier/<chantier>.md` | Dossier complet pour l'agent qui écrit un chantier |
| `lots/CONSIGNES.md` | Règles de découpage et formats |
| `frontieres.md` | Ce qui est dans et hors périmètre |
| `listes-controle/` | SGPE, PNACC-3, économie circulaire, références mondiales |
| `verification/` | Rapports des vérificateurs, test final, doublons |
| `outils/` | Assemblage, contrôles, gabarit de la page |
| `rapport.md` | Arbitrages, doutes, résultats des vérifications |
