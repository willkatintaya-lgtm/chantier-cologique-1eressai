# Contexte commun aux vérificateurs

On construit un arbre (taxonomie) de la transition écologique pour un entrepreneur qui doit y voir TOUS les chantiers de deux thématiques, « Mieux se loger » et « Mieux consommer », sans trou, puis descendre jusqu'aux problèmes précis à résoudre. Périmètre mondial (pays riches ET pays du Sud), libellés en français, formulés comme des actions.

Fichiers à lire (chemins absolus) :
- /home/user/chantier-cologique-1eressai/arbre/niveaux-1-4.txt : niveaux 1 à 4 (racine, 2 thématiques, 11 grands chantiers, 49 leviers)
- /home/user/chantier-cologique-1eressai/arbre/niveau-5.txt : niveau 5 (197 chantiers)
- /home/user/chantier-cologique-1eressai/frontieres.md : ce qui est dans et hors périmètre
Format des lignes : id | libellé | définition | critère de partage des filles | défis | renvois. L'id donne le parent (1.1.2.3 est fille de 1.1.2).

Règles que l'arbre doit respecter :
1. Chaque boîte a 3 à 6 filles (tolérance 2 à 7).
2. Les sœurs sont de même nature et de même échelle.
3. Les périmètres des sœurs ne se recouvrent pas ; un critère de partage est écrit dans la boîte parente.
4. Une boîte qui relève de deux parents a un parent principal et un renvoi (dernière colonne).
5. Pas de granularité régulière rompue ; aucune boîte de remplissage.
6. Les 5 défis (atténuation, adaptation, biodiversité, ressources, pollutions et santé) sont des étiquettes, jamais des branches.
7. Hors périmètre : se déplacer, se nourrir, produire (industrie, énergie centralisée), préserver les écosystèmes. Voir frontieres.md.
Étalon de granularité : niveau 3 « Chauffer les bâtiments sans énergie fossile » > niveau 4 « Sortir du gaz » > niveau 5 « Électrifier la chaleur ». Sous chaque chantier de niveau 5 viendront ensuite 3 niveaux de verrous (≈ 40 à 60 problèmes précis par chantier) : un chantier de niveau 5 doit donc être assez large pour en contenir autant, et assez étroit pour rester un chantier identifiable.

Tu n'as pas produit cet arbre. Ton rôle est de le critiquer sévèrement et concrètement. Ne modifie AUCUN fichier de l'arbre ; écris seulement ton rapport dans le fichier indiqué. Pas de commit git. Chaque constat doit citer les id concernés et proposer une correction précise (nouveau libellé, déplacement, fusion, scission, ajout). Classe chaque constat : BLOQUANT (trou ou recouvrement réel), IMPORTANT, MINEUR. Ne signale pas ce qui va bien. Ta réponse finale : 6 lignes maximum (nombre de constats par gravité, les 3 plus graves).
