# Rapport — cartographie « Mieux se loger » et « Mieux consommer »

Version provisoire du 27 novembre 2026. Le travail a été arrêté avant la fin pour ne pas épuiser les crédits ; l'état exact et la marche à suivre pour finir sont dans `REPRISE.md`.

## 1. Ce qui est livré

| Niveau | Nombre | État |
|---|---|---|
| 1 Racine | 1 | Terminé |
| 2 Thématiques | 2 | Terminé |
| 3 Grands chantiers | 11 | Terminé, vérifié |
| 4 Leviers | 50 | Terminé, vérifié |
| 5 Chantiers | 207 | Terminé, vérifié |
| 6 Verrous | 934 | Terminé, relu |
| 7 Verrous précis | 2 038 | « Se loger » complet ; « Consommer » : 7 chantiers sur 90 |
| 8 Problèmes précis | 6 447 | idem ; non relu |

Total : 9 690 boîtes. « Mieux se loger » est complet du niveau 2 au niveau 8 (6 091 problèmes). « Mieux consommer » est complet jusqu'au niveau 6 ; ses niveaux 7 et 8 manquent pour 83 chantiers.

`index.html` contient les données et s'ouvre seul. Testée avec 16 700 boîtes factices, la page se charge en moins d'une seconde et répond en moins de 200 ms à la navigation et à la recherche.

## 2. Écarts avec le cadrage

- **11 grands chantiers, 50 leviers, 207 chantiers**, contre environ 8, 35 et 130 demandés. Au grain de l'étalon (« Chauffer les bâtiments sans énergie fossile » au niveau 3), huit grands chantiers ne couvraient pas les deux thématiques.
- **Niveau 8 : environ 46 problèmes par chantier.** À ce rythme, l'arbre complet en compterait autour de 9 500, au-dessus de la cible de 8 500.
- **Consommation : environ 30 millions de tokens**, contre 12 à 18 millions estimés au départ. Les 207 chantiers au lieu de 130 et un coût par agent sous-estimé expliquent l'écart.
- **Recherches** : trois des cinq listes de contrôle (économie circulaire, monde bâtiments, monde consommation) ont été écrites de mémoire par les agents, sans recherche web. Les listes SGPE et PNACC-3 viennent des documents officiels.
- **Niveaux 6 à 8** : rédigés à partir des connaissances des modèles, sans source. Aucun problème de niveau 8 n'est vérifié contre une référence.

## 3. Arbitrages de découpage

- **« Se loger » est découpé par fonction du bâtiment** : chauffer, garder la chaleur, rafraîchir, résister aux aléas, fonctionner, être construit.
- **Les verrous transverses n'ont qu'une place.** Décision, financement et filière de tous les travaux sur l'existant sont sous « Rénover » (1.1.2.2 à 1.1.2.4), y compris pour le chauffage, le confort d'été et la prévention des risques.
- **Technologie contre situation de départ.** Ce qui tient à la pompe à chaleur elle-même est sous « Électrifier la chaleur » (1.1.1.2.1), quel que soit le système remplacé ; le fioul et les convecteurs ne gardent que ce qui tient à leur situation.
- **Deux grands chantiers sont presque entièrement de l'adaptation** (rafraîchir, protéger des aléas). Ils sont formulés comme des fonctions du bâtiment, mais frôlent la règle « les défis ne sont jamais des branches ».
- **« Loger les villes en croissance rapide » (1.1.6.5) est une exception assumée** : un contexte géographique parmi des sœurs découpées par question.
- **« Consommer » suit la vie du produit** (choisir, concevoir, faire durer, valoriser), avec l'usage unique traité à part.
- **La réparation est découpée par famille de produits** (1.2.3.2), pour qu'un réparateur trouve son métier d'un seul tenant ; les règles communes ont leur chantier.
- **Le réemploi des emballages mêle deux axes** (1.2.4.2) : infrastructure commune et retour par le client, puis trois circuits.
- **La cuisson est dans « se loger »**, le numérique est réparti en trois (appareils, services, usages), l'électroménager en deux (électricité, durée de vie).
- **Exclusions écrites dans `frontieres.md`** : épargne des ménages, séismes, ouvrages collectifs de protection, réseaux publics d'eau, bruit et lumière, vélos et véhicules, conditions de travail.

## 4. Vérifications faites

### Niveaux 1 à 5

Quatre agents Opus indépendants, puis un cinquième en contre-vérification.

| Vérification | Résultat |
|---|---|
| Recouvrements et natures, boîte par boîte | 104 constats, dont 5 bloquants et 31 importants |
| Trous, à partir d'une liste indépendante de 136 sujets | 36 constats, dont 5 bloquants |
| Rangement de 225 éléments (SGPE, PNACC-3, monde bâtiments) | 134 rangés, 46 trop généraux, 18 hors périmètre, 19 sans place, 8 en double |
| Rangement de 280 éléments (SGPE, économie circulaire, monde consommation) | 173 rangés, 66 trop généraux, 20 hors périmètre, 10 sans place, 11 en double |
| Contre-vérification après correction | 87 constats graves : 81 résolus, 6 partiels, 0 non résolu |

Les 29 éléments sans place ont conduit à ajouter ou élargir des chantiers : bâtiments neufs à très basse consommation, chauffage électrique à résistance, eau saine au logement, toilettes, conserver plutôt que démolir, consigne pour recyclage, sacs de caisse, filières de responsabilité des producteurs, récupérateurs informels, contrôle des vendeurs en ligne. Les sept corrections demandées par la contre-vérification ont été appliquées, mais **pas revérifiées**.

### Niveau 6

Onze relecteurs Opus, un par grand chantier, ont relu les 934 verrous et corrigé directement doublons, recouvrements et défauts de forme (journaux `verification/n6-*.md`). Recherche automatique ensuite : 7 paires de libellés proches entre branches, dont une seule discutable (retour d'emballage pour réemploi et consigne pour recyclage).

### Niveaux 7 et 8

- **Forme** : chaque lot passe un contrôle automatique (nombre de filles, champs, longueur, doublons internes). Les 124 lots présents sont conformes.
- **Doublons sur tout l'arbre** : 18 paires de libellés proches sur 9 419 boîtes, aucune quasi identique (`verification/doublons.md`). Ce contrôle est lexical : il ne voit pas deux problèmes identiques formulés avec des mots différents.
- **Relecture par échantillonnage (10 %) : non faite.** Elle était prévue, a été coupée par la limite d'usage, puis abandonnée à votre demande.

## 5. Test final

60 situations tirées au hasard (type de bâtiment ou de produit, acteur, sujet, région), rédigées en problèmes concrets par un agent qui n'avait pas vu l'arbre, puis classées séparément par deux agents.

| Mesure | Résultat |
|---|---|
| Problèmes sans place ou hors périmètre | 0 sur 60 |
| Même chantier choisi par les deux classeurs | 51 sur 60 |
| Désaccord, le choix de l'un étant l'alternative de l'autre | 8 sur 60 |
| Désaccord franc | 1 sur 60 |
| Rangés sans hésitation par les deux | 15 sur 60 |

Le critère « un chantier unique » n'est donc tenu strictement que pour un quart des problèmes. Dans les autres cas, les classeurs citent un second chantier possible, presque toujours voisin : un problème de terrain a souvent deux facettes (la décision et la technique, le produit et son déchet). 99 renvois ont été ajoutés entre les 51 paires de chantiers concernées. Le test porte sur les niveaux 1 à 5 seulement.

## 6. Zones de doute

- **Niveaux 7 et 8 non relus** : attendez-vous à des problèmes hors périmètre de leur chantier, à des doublons de sens entre chantiers voisins et à quelques affirmations inexactes.
- **Frontière entre « Rénover » et les autres grands chantiers** : c'est la première source d'hésitation du test (décision ou financement d'un côté, technique de l'autre).
- **Usage unique contre déchets** : la conception des emballages (1.2.4.3) et leur recyclage (1.2.5.3) restent proches.
- **Chantiers étroits** : « Brasser l'air » (1.1.3.2.2), « Entraîner le marché par les achats des organisations » (deux chantiers seulement).
- **Habitat précaire** : réparti entre cinq chantiers reliés par des renvois.
- **Lacunes connues** : petits équipements thermiques de jardin et de terrasse ; chauffage des piscines.
- **Biais français** des listes de contrôle officielles, compensé par des listes mondiales écrites de mémoire.
