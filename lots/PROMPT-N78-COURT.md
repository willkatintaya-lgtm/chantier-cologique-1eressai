# Ta mission

Tu produis les NIVEAUX 7 et 8 (verrous précis et problèmes précis) d'un arbre de la transition écologique, pour le chantier <ID>. Tout ce qu'il te faut est dans ce seul fichier : la mission, les consignes, puis le contexte du chantier. Ne lis aucun autre fichier.

Pour CHACUN des <N6> verrous de niveau 6 du chantier (listés dans le contexte), dans l'ordre, écris :
- son critère de partage (comment ses filles sont découpées) ;
- 3 ou 4 verrous précis de niveau 7 (5 seulement si chacun est indispensable), chacun avec libellé, définition, critère de partage, défis, nature ;
- sous chaque niveau 7, 3 ou 4 problèmes précis de niveau 8 (5 seulement si chacun est indispensable), chacun avec libellé, définition, défis, nature.

Exigences de fond :
- Le niveau 8 suit strictement la forme « une fonction à remplir + la contrainte qui bloque ». Chaque problème est un vrai point dur d'aujourd'hui, que tu saurais expliquer à un professionnel du secteur sans qu'il hausse les épaules.
- La définition d'un niveau 8 dit en une phrase pourquoi c'est dur ou pour qui (un fait, une cause) ; elle ne répète pas le libellé.
- Varie les natures au niveau 8 (technique, économique, réglementaire, organisationnelle, comportementale) quand le réel s'y prête.
- Zéro doublon dans tout ton fichier : deux problèmes qui ne diffèrent que par un adjectif, un type de bâtiment ou un produit, sans que la difficulté change, sont un doublon.
- Zéro remplissage : si un verrou n'a que 3 sous-verrous réels, ou un sous-verrou que 3 problèmes réels, arrête-toi à 3. Jamais moins de 3.
- Pas de chiffre inventé, pas de nom de marque, pas de solution imposée.
- Reste dans le périmètre du chantier : rien de ce qui appartient aux chantiers frères, aux renvois ou aux chantiers transverses.
- Pense au monde entier : quand le chantier se pose au Sud, des problèmes du Sud doivent apparaître.

Déroulé, en peu d'étapes :
1. Réfléchis au plan complet (tous les niveaux 7 de tous les verrous), puis écris d'un seul coup le fichier /home/user/chantier-cologique-1eressai/lots/n78/<ID>.txt, au format « niveaux 7 et 8 » des consignes, sans rien d'autre (aucun titre, aucun commentaire).
2. Lance `python3 /home/user/chantier-cologique-1eressai/outils/verifier_lot.py /home/user/chantier-cologique-1eressai/lots/n78/<ID>.txt <N6>`. Corrige jusqu'à « FORME CORRECTE ». Pour chaque ligne « à vérifier » signalant deux libellés proches : si c'est le même problème, réécris-en un.
3. Réponse finale : une ligne (nombre de niveaux 7 et de niveaux 8). Ne modifie aucun autre fichier, pas de commit git.
