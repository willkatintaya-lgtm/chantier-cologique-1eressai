Tu es RELECTEUR des niveaux 7 et 8 (verrous précis et problèmes précis) d'un arbre de la transition écologique, pour UN levier. Tu n'as pas produit ces niveaux.

1. Lis en entier /home/user/chantier-cologique-1eressai/lots/CONSIGNES.md (les règles données aux producteurs : 3 ou 4 filles par boîte, 5 si indispensable ; niveau 8 = une fonction + la contrainte qui bloque ; zéro doublon, zéro remplissage, périmètre du chantier). Ne lis pas les fichiers de l'arbre qu'il cite : les contextes de l'étape 2 les résument.
2. Pour chaque chantier de ton levier, lis son contexte /home/user/chantier-cologique-1eressai/lots/contexte/<id du chantier>.md puis son lot /home/user/chantier-cologique-1eressai/lots/n78/<id du chantier>.txt, en entier.
3. PASSE 1, sur TOUS les libellés du levier — doublons et périmètre :
   - deux niveaux 8 (ou deux niveaux 7) qui posent le même problème, dans un même chantier ou entre chantiers du levier ;
   - problèmes hors du périmètre du chantier (appartiennent à un chantier frère, à un renvoi, à un chantier transverse, ou à une thématique exclue) ;
   - verrous transverses génériques recopiés (« financer », « former », « informer ») sans rien de propre au chantier.
4. PASSE 2, au fond, sur un ÉCHANTILLON tiré au hasard : lance `python3 /home/user/chantier-cologique-1eressai/outils/echantillon.py <id du levier>`. Pour chaque niveau 8 tiré, juge-le sur ces critères et note le résultat (BON ou le défaut) :
   a. FORME : une fonction à remplir + la contrainte qui bloque ; verbe à l'infinitif ; compréhensible seul.
   b. RÉALITÉ : c'est un vrai point dur d'aujourd'hui, exact sur le fond (pas d'erreur technique, juridique ou économique, pas de chiffre inventé).
   c. PRÉCISION : assez précis pour qu'on imagine un produit, un service ou une règle ; pas une généralité ; pas une solution imposée.
   d. PLACE : il est bien sous le bon niveau 7 et le bon niveau 6 ; ses sœurs sont de même nature et ne le recouvrent pas.
   e. DÉFINITION : elle ajoute une information (cause, acteur) et ne paraphrase pas le libellé ; défis et nature plausibles.
5. CORRIGE directement les fichiers lots/n78/*.txt de ton levier : réécris les niveaux 8 défectueux, supprime ou remplace les doublons, déplace ce qui est mal placé, en gardant le format et au moins 3 filles par boîte. Ne te limite pas à l'échantillon : corrige tout défaut que tu as vu. Ne réécris pas ce qui est bon. Après chaque fichier modifié, relance `python3 /home/user/chantier-cologique-1eressai/outils/verifier_lot.py <fichier>` jusqu'à « FORME CORRECTE ».
6. Si, pour un chantier, plus d'un quart de l'échantillon est défectueux, ne tente pas de tout réparer : écris « LOT À REFAIRE : <id du chantier> — raison » dans ton journal et dans ta réponse finale.
7. Écris ton journal dans /home/user/chantier-cologique-1eressai/verification/n78-<id du levier>.md, avec exactement ces lignes en tête, puis le détail :
   ```
   niveaux 8 du levier : <nombre>
   échantillon relu au fond : <nombre>
   défectueux dans l'échantillon : <nombre> (forme <n>, réalité <n>, précision <n>, place <n>, définition <n>)
   doublons trouvés en passe 1 : <nombre>
   hors périmètre trouvés en passe 1 : <nombre>
   corrections faites : <nombre>
   lots à refaire : <ids ou « aucun »>
   ```
   Détail : une ligne par correction (« fichier, ligne — défaut — ce que tu as fait »), puis tes doutes non tranchés.
8. Réponse finale : les 7 lignes d'en-tête du journal, rien d'autre. Ne modifie aucun autre fichier, pas de commit git.
