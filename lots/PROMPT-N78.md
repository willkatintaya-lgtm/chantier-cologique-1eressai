Tu produis les NIVEAUX 7 et 8 (verrous précis et problèmes précis) d'un arbre de la transition écologique, pour UN chantier de niveau 5.

1. Lis en entier /home/user/chantier-cologique-1eressai/lots/CONSIGNES.md (règles, étalon, ce qu'est un bon niveau 8, format). Les fichiers de l'arbre qu'il cite sont déjà résumés pour toi à l'étape 2 : ne les lis pas.
2. Lis en entier le fichier de contexte de ton chantier : /home/user/chantier-cologique-1eressai/lots/contexte/<id du chantier>.md. Il donne sa lignée, sa définition, ses verrous de niveau 6 numérotés, les chantiers voisins (dont le contenu ne va pas chez toi) et les chantiers transverses.
3. Pour CHAQUE verrou de niveau 6 de ton chantier, dans l'ordre, écris :
   - son critère de partage (comment ses filles sont découpées) ;
   - 3 à 5 verrous précis de niveau 7 (le plus souvent 3 ou 4), chacun avec libellé, définition, critère de partage, défis, nature ;
   - sous chaque niveau 7, 3 à 5 problèmes précis de niveau 8 (le plus souvent 3 ou 4), chacun avec libellé, définition, défis, nature.
4. Exigences de fond :
   - Le niveau 8 suit strictement la forme « une fonction à remplir + la contrainte qui bloque ». Relis les exemples des consignes avant d'écrire. Chaque problème doit être un vrai point dur d'aujourd'hui, que tu saurais expliquer à un professionnel du secteur sans qu'il hausse les épaules.
   - La définition d'un niveau 8 dit en une phrase pourquoi c'est dur ou pour qui (un fait, une cause) ; elle ne répète pas le libellé.
   - Varie les natures au niveau 8 (technique, économique, réglementaire, organisationnelle, comportementale) à l'intérieur de chaque verrou quand le réel s'y prête.
   - Zéro doublon dans tout ton fichier : avant d'écrire un problème, vérifie qu'il n'existe pas déjà ailleurs sous une autre formulation. Deux problèmes qui ne diffèrent que par un adjectif, un type de bâtiment ou un produit, sans que la difficulté change, sont un doublon.
   - Zéro remplissage : si un verrou n'a que 3 sous-verrous réels, ou un sous-verrou que 3 problèmes réels, arrête-toi à 3. Ne descends jamais sous 3 ; si tu n'en trouves que 2, c'est que le niveau au-dessus est mal découpé : redécoupe-le.
   - Pas de chiffre inventé, pas de nom de marque, pas de solution imposée.
   - Reste dans le périmètre de ton chantier : rien de ce qui appartient aux chantiers frères, aux renvois ou aux chantiers transverses.
   - Pense au monde entier : quand le chantier se pose au Sud, des problèmes du Sud doivent apparaître.
5. Écris le résultat dans le fichier indiqué, au format « niveaux 7 et 8 » des consignes, sans rien d'autre (aucun titre, aucun commentaire).
6. Lance le contrôle de forme : `python3 /home/user/chantier-cologique-1eressai/outils/verifier_lot.py <ton fichier> <nombre de verrous de niveau 6>`. Corrige jusqu'à obtenir « FORME CORRECTE ». Examine aussi chaque ligne « à vérifier » : si deux libellés proches sont le même problème, supprimes-en un ou réécris-le.
7. Relis ton fichier en entier une dernière fois ; supprime ou réécris tout niveau 8 vague, sans contrainte, en doublon ou hors périmètre ; relance le contrôle si tu as modifié.
8. Réponse finale : 2 lignes maximum (nombre de niveaux 7 et de niveaux 8, doutes éventuels). Ne modifie aucun autre fichier, pas de commit git.
