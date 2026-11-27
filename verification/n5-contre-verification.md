# Contre-vérification de l'arbre corrigé (niveaux 1 à 5 : 50 leviers, 207 chantiers)

Base : arbre/niveaux-1-4.txt, arbre/niveau-5.txt et frontieres.md tels qu'ils sont au commit 9dfd39b. Les id cités sont ceux de la version corrigée. Quand un rapport citait un ancien id, on indique le nouvel id. Tous les renvois pointent vers un id qui existe (contrôle fait par script). Toutes les boîtes ont entre 3 et 6 filles, sauf 1.2.1.4, qui en a 2. Tous les libellés sont des actions.

## 1. Suivi des constats BLOQUANT et IMPORTANT

Décompte : **87 constats suivis. 81 sont RÉSOLUS, 6 PARTIELLEMENT RÉSOLUS, 0 NON RÉSOLU.**

### n5-recouvrements.md (5 BLOQUANT, 31 IMPORTANT)

| Constat | Verdict | Commentaire |
|---|---|---|
| B · isolation été / hiver | RÉSOLU | 1.1.3.1.2 exclut l'isolation et renvoie à 1.1.2.1.2 ; 1.1.2.1.2 vaut « contre le froid comme contre la chaleur ». |
| B · précarité énergétique | RÉSOLU | 1.1.5.3.5 est limité aux aides au paiement, sans les travaux ; il renvoie à 1.1.2.3.1 et 1.1.3.4.1. Le renvoi en sens inverse manque (mineur). |
| B · vrac, recharge, concentrés | RÉSOLU | L'ancien 1.2.4.2.5 est supprimé ; 1.2.4.1.1 devient « Vendre en vrac et en recharge » ; 1.2.4.1.2 prend les concentrés. Il manque le renvoi de 1.2.4.1.4 vers 1.2.4.1.1 (mineur). |
| B · traçabilité quadruplée | RÉSOLU | 1.2.1.1.1 est le parent principal ; les anciens 1.2.2.3.4 et 1.2.2.2.5 sont supprimés. |
| B · végétalisation triplée | RÉSOLU | 1.1.3.1.3 est principal pour le bâti végétalisé et 1.1.6.2.2 pour la pluie ; 1.1.6.2.3 renvoie à 1.1.3.1.3. |
| I · deux axes dans le critère de 1.1 | RÉSOLU | Les critères de 1.1 et de 1.1.2 rangent une seule fois, sous « Rénover », les conditions communes à tous les travaux. |
| I · 1.1.2.2 à 1.1.2.4 limités à l'énergie | RÉSOLU | Leurs définitions sont élargies : 1.1.2.2.2, 1.1.2.2.5, 1.1.2.3.1, 1.1.2.4.1 (installateurs de chaud et de froid), 1.1.2.4.4. |
| I · financement des travaux hors isolation | PARTIEL | Le critère de 1.1.4 envoie ce financement vers 1.1.2.3, mais le libellé de 1.1.4.5.2 dit encore « financer leur prévention » (voir N3). |
| I · critère de 1.1.1 | RÉSOLU | Nouveau critère « par système en place » ; renvois de 1.1.1.1.1 vers 1.1.1.4.1 et de 1.1.1.1.2 vers 1.1.1.3.3. |
| I · contradiction de 1.1.5 sur le chauffage | RÉSOLU | La définition de 1.1.5 inclut le pilotage de l'ensemble ; 1.1.5.3 précise « chauffage et froid compris ». |
| I · nature de 1.1.6.5 | RÉSOLU | Exception assumée dans le critère, découpage par mode de production ; les solutions techniques restent dans leurs leviers. |
| I · 1.2.4 casse le critère de 1.2 | RÉSOLU | Le critère de 1.2 répartit l'usage unique entre 1.2.4 et 1.2.5. |
| I · numérique placé sous « concevoir » | RÉSOLU | Déplacé en 1.2.1.2.4 ; 1.2.2.4 est redécoupé par type de service. |
| I · rénovation globale en triple | RÉSOLU | 1.1.2.1.4 devient « Rénover par éléments préfabriqués » ; 1.1.2.4.3 contrôle et mesure. |
| I · contrat de performance énergétique en triple | RÉSOLU | Renvoi de 1.1.2.3.3 vers 1.1.5.3.4 ; 1.1.2.4.3 se limite au contrôle. |
| I · tertiaire : décider ou exploiter | RÉSOLU | 1.1.2.2.5 porte sur les travaux (enveloppe et systèmes) et renvoie à 1.1.5.3.4. |
| I · accompagnement en double | RÉSOLU | Retiré de 1.1.2.2 ; « conseil » ajouté au critère de 1.1.2.4. |
| I · bâti ancien (1.1.2.1.5) | RÉSOLU | Critère réécrit, 1.1.2.1.5 parent principal, renvoi depuis 1.1.2.1.1. |
| I · ventilation promise par 1.1.2.1 | RÉSOLU | Retirée de 1.1.2.1 ; 1.1.5.6.1 est principal ; renvois depuis 1.1.2.1.3 et 1.1.3.2.1. |
| I · conception bioclimatique en triple | RÉSOLU | 1.1.3.1.4 est principal ; renvoi depuis 1.1.6.5.4. Une nouvelle frontière apparaît avec 1.1.6.3.6 (voir N6). |
| I · habitat précaire découpé en quatre | PARTIEL | Plus de « toits de tôle » dans 1.1.3.4.1, mais 1.1.6.5.2 recouvre désormais 1.1.5.4.4 et 1.1.5.5.x (voir N1). |
| I · fluides frigorigènes limités à la clim | RÉSOLU | 1.1.3.3.2 couvre tous les équipements ; renvois depuis 1.1.1.2.1 et 1.1.5.1.3. |
| I · eaux pluviales en triple | RÉSOLU | 1.1.6.2.2 est principal ; 1.1.4.1.1 et 1.1.5.5.3 y renvoient. |
| I · reconstruction en double | RÉSOLU | 1.1.4.5.3 se limite aux catastrophes de grande ampleur ; renvois depuis 1.1.4.1.3 et 1.1.4.2.4. |
| I · surélévation en double | RÉSOLU | Placée en 1.1.6.2.1 seulement. |
| I · surproduction de la mode | RÉSOLU | 1.2.1.2.2 ne cite plus les collections : il garde promotions, prix cassés et crédit, et renvoie à 1.2.2.3.2. |
| I · demande de matière recyclée en quintuple | RÉSOLU | 1.2.5.3.6 est principal (taux, prix, normes) ; 1.2.4.3.2 et 1.2.2.1.5 y renvoient. |
| I · responsabilité élargie du producteur éclatée | RÉSOLU | Nouveau 1.2.5.1.3, en renvoi réciproque avec 1.2.1.3.1 ; renvoi depuis 1.2.3.2.6. |
| I · critère double de 1.2.2.2 | RÉSOLU | Un seul axe : le type de danger. |
| I · pièces et documentation en double | RÉSOLU | 1.2.3.1.2 garde la conception ; l'accès aux pièces passe en 1.2.3.2.6. |
| I · « confiance » dans le critère de 1.2.3.2 | RÉSOLU | Levier redécoupé par famille ; la garantie après réparation est en 1.2.3.2.6. |
| I · retour et logistique des emballages confondus | RÉSOLU | 1.2.4.2.1 (infrastructure) et 1.2.4.2.2 (retour par les clients) sont nettement distincts. |
| I · piles en quadruple | RÉSOLU | La collecte est en 1.2.5.2.4 ; 1.2.5.5.4 traite ce qui est déjà collecté et y renvoie. |
| I · décharges contre dépôts sauvages | PARTIEL | 1.2.5.5.1 est renommé. Mais un dépotoir qui brûle peut encore aller en 1.2.5.5.1 ou en 1.2.5.1.5, et le brûlage dans un village sans service en 1.2.5.1.1 ou en 1.2.5.1.5. |
| I · fuites vers la mer, dépollution | RÉSOLU | 1.2.5.1.6 intercepte en ville ; la dépollution est exclue dans frontieres.md. |
| I · tri des biodéchets en double | RÉSOLU | 1.2.5.2 précise « hors biodéchets » et renvoie à 1.2.5.4. |

### n5-trous.md (5 BLOQUANT, 16 IMPORTANT)

| Constat | Verdict | Commentaire |
|---|---|---|
| 1 B · performance énergétique du neuf | RÉSOLU | Ajout de 1.1.6.3.6. |
| 2 B · ne pas démolir | RÉSOLU | 1.1.6.1.3 devient « Transformer… plutôt que les démolir ». |
| 3 B · faire respecter les règles produits | RÉSOLU | Ajout de 1.2.1.3.4. |
| 4 B · qualité de l'eau dans le bâtiment | RÉSOLU | Ajout de 1.1.5.5.1. |
| 5 B · conditions des travaux réservées à l'enveloppe | RÉSOLU | Voir les critères de 1.1 et 1.1.2. |
| 6 · chauffage électrique direct | RÉSOLU | Nouveau levier 1.1.1.5. Il crée une frontière avec 1.1.1.2.1 (voir N2). |
| 7 · 1.1.6.5.1 trop large | RÉSOLU | Scindé en 1.1.6.5.1 (foncier) et 1.1.6.5.2 (équiper). |
| 8 · 1.1.3.2 trop étroit | PARTIEL | Passé de 4 à 3 chantiers, mais 1.1.3.2.2 « Brasser l'air » reste mince. |
| 9 · argiles en triple | RÉSOLU | 1.1.4.2 est rééquilibré (1.1.4.2.1 à 1.1.4.2.4). |
| 10 · réemploi découpé en verrous | RÉSOLU | Les maillons sont fusionnés en 1.2.4.2.1, et des circuits sont ajoutés. |
| 11 · réparation sans familles de produits | RÉSOLU | 1.2.3.2 est découpé par famille ; une liste fermée de familles est ajoutée aux consignes des niveaux 6 à 8. |
| 12 · précarité énergétique | RÉSOLU | Voir plus haut. |
| 13 · neuf en climat chaud | RÉSOLU | 1.1.6.5.4 renvoie à 1.1.3.1.4. |
| 14 · groupes électrogènes, outils thermiques | RÉSOLU | 1.1.5.4.4 inclut les groupes ; les outils thermiques sont exclus dans frontieres.md. Le chauffage des piscines reste sans place (mineur). |
| 15 · fluides frigorigènes | RÉSOLU | 1.1.3.3.2. |
| 16 · assainissement | RÉSOLU | 1.1.5.5 est renommé ; 1.1.5.5.5 et 1.1.5.5.6 sont créés. |
| 17 · séismes | RÉSOLU | Exclusion écrite dans frontieres.md. |
| 18 · responsabilité élargie du producteur | RÉSOLU | 1.2.5.1.3. |
| 19 · adaptation dans la consommation | RÉSOLU | Étiquette D sur 1.2, 1.2.5.1.1, 1.2.4.1.4, 1.2.2.3.1 et 1.2.5.1.6. |
| 20 · étiquettes de la rénovation | RÉSOLU | B, R, P et D ajoutés ; la faune du bâti est citée dans 1.1.2.1.1. |
| 21 · sable | RÉSOLU | 1.1.6.3.4 inclut l'extraction, le sable et les granulats tracés. |

### n5-rangement-batiments.md (3 BLOQUANT, 14 IMPORTANT)

| Constat | Verdict | Commentaire |
|---|---|---|
| T1 B · neuf | RÉSOLU | 1.1.6.3.6. |
| T7 B · financer et déclencher l'adaptation | RÉSOLU | Le critère de 1.1.4 renvoie à 1.1.2.3 ; 1.1.2.3.1 couvre « l'adaptation ». Le recouvrement qui reste est traité en N3. |
| R1 B · enveloppe été / hiver | RÉSOLU | 1.1.3.1.1 et 1.1.3.1.2 ne citent plus ni vitrages ni isolation, et renvoient à 1.1.2.1.x. |
| T2 · effet Joule | RÉSOLU | 1.1.1.5. |
| T3 · carbone des matériaux de rénovation | RÉSOLU | 1.1.6.3 couvre « construction et rénovation ». Il manque le renvoi de 1.1.2.1.1 vers 1.1.6.3.2 (mineur). |
| T4 · logement sain au-delà de l'air | RÉSOLU | Exclu dans frontieres.md. |
| T5 · sismique | RÉSOLU | Exclu dans frontieres.md. |
| T8 · protection collective | RÉSOLU | Exclue dans frontieres.md ; l'échelle du lotissement est gardée en 1.1.4.3.3. |
| T9 · décision sur le confort d'été | RÉSOLU | Couverte par 1.1.2 et 1.1.2.4.4. |
| T11 · conserver plutôt que démolir | RÉSOLU | 1.1.6.1.3. |
| T13 · accès à l'eau potable du logement | PARTIEL | Les réseaux publics sont exclus, et frontieres.md inclut les solutions à l'échelle du bâtiment. Mais hors quartiers informels (1.1.6.5.2), aucun chantier ne porte l'accès à l'eau d'un logement non desservi : 1.1.5.5.1 ne traite que la qualité de l'eau (voir N5). |
| T15 · hors réseau non résidentiel | RÉSOLU | 1.1.5.4.4. |
| R2 · végétalisation | RÉSOLU | Voir plus haut. |
| R3 · risques dans l'informel | RÉSOLU | Retirés de 1.1.6.5.x ; l'habitat précaire est nommé en 1.1.4.1.2 et 1.1.4.2.2. |
| R5 · réparer et reconstruire | RÉSOLU | Voir plus haut. |
| R6 · eaux pluviales | RÉSOLU | Voir plus haut. |
| R7 · cuisine professionnelle | RÉSOLU | Passée de 1.1.5.1.4 à 1.1.5.2.3. |

### n5-rangement-consommation.md (3 BLOQUANT, 10 IMPORTANT)

| Constat | Verdict | Commentaire |
|---|---|---|
| B · consigne pour recyclage | RÉSOLU | 1.2.5.2.3, avec renvoi depuis 1.2.4.2.2. |
| B · sacs et emballages remis en caisse | RÉSOLU | 1.2.4.1.5. |
| B · pilotage des filières REP | RÉSOLU | 1.2.5.1.3. |
| I · récupérateurs informels | RÉSOLU | 1.2.5.1.2. |
| I · contrôle des produits importés | RÉSOLU | 1.2.1.3.4, mais il recouvre 1.2.5.1.3 (voir N4). |
| I · déchets en temps de crise | RÉSOLU | Couverts par 1.2.5.1.1. |
| I · conception pour le recyclage des biens durables | RÉSOLU | 1.2.2.1.6. |
| I · indices de réparabilité et de durabilité | PARTIEL | 1.2.3.1.4 cite encore « les indices », alors que 1.2.1.1.2 affiche ; renvoi seulement. |
| I · bonus réparation | RÉSOLU | 1.2.3.2.6 « aides à la réparation », avec renvoi vers 1.2.1.3.1. |
| I · traçabilité | RÉSOLU | Voir plus haut. |
| I · substances | RÉSOLU | Voir plus haut. |
| I · numérique | RÉSOLU | Voir plus haut. |
| I · déchets des ménages ou des activités | RÉSOLU | 1.2.5 couvre ménages, commerces et bureaux. frontieres.md dit encore « déchets des ménages » (mineur). |

## 2. Nouveaux problèmes introduits par les corrections

| # | Gravité | Id | Problème | Correction |
|---|---|---|---|---|
| N1 | IMPORTANT | 1.1.6.5.2 / 1.1.5.4.4 / 1.1.5.5.1 / 1.1.5.5.5 / 1.1.5.5.6 | La définition « Apporter eau, assainissement, électricité » contredit le critère de 1.1.6.5 (« les solutions techniques restent dans leurs leviers »). Exemple : « électrifier un quartier informel de Nairobi » se range en 1.1.6.5.2 et en 1.1.5.4.4 ; « toilettes dans un bidonville » en 1.1.6.5.2 et en 1.1.5.5.5. | Redéfinir 1.1.6.5.2 « Conduire la réhabilitation sur place des quartiers informels » : programme, phasage, maîtrise d'ouvrage avec les habitants, coût par ménage. Les équipements restent en renvoi. Ajouter les renvois réciproques depuis 1.1.5.4.4 et 1.1.5.5.5. |
| N2 | IMPORTANT | 1.1.1.2.1 / 1.1.1.5.1 / 1.1.1.1.1 / 1.1.1.1.2 (et 1.1.1.4.1 ; 1.1.1.2.3 / 1.1.1.5.2) | 1.1.1.2.1, rangé sous « Sortir du gaz », se dit « chantier de référence pour la PAC quel que soit le système remplacé ». Or 1.1.1.5.1 s'intitule « Remplacer les convecteurs… par des pompes à chaleur ». Aucune règle ne dit quels verrous vont où, d'où un risque de verrous PAC en triple. Même chose pour le bois, et pour le chauffe-eau thermodynamique, présent en 1.1.1.2.3 et en 1.1.1.5.2. | Écrire dans le critère de 1.1.1 que 1.1.1.2.1 et 1.1.1.4.1 portent les verrous de la technologie elle-même (coût, bruit, installateurs, appareil). Les chantiers « par situation de départ » (1.1.1.1.x, 1.1.1.5.x, 1.1.1.2.3) ne portent que ce qui est propre à cette situation. Renommer 1.1.1.5.1 « Sortir les logements du chauffage par convecteurs ». |
| N3 | IMPORTANT | 1.1.4.5.2 / 1.1.2.3.1 / critère de 1.1.4 | Le libellé « Assurer les bâtiments exposés et financer leur prévention » contredit le critère de 1.1.4, qui range le financement de la prévention en 1.1.2.3. Exemple : « subvention pour poser des batardeaux » se range sous les deux. | Renommer 1.1.4.5.2 « Garder les bâtiments exposés assurables ». N'y laisser que la prévention imposée ou financée par l'assureur ; les aides publiques vont en 1.1.2.3.1. |
| N4 | IMPORTANT | 1.2.1.3.4 / 1.2.5.1.3 | « Faire payer leur contribution REP aux places de marché étrangères » se range sous les deux (« contributions dues » et « contrôler les filières »). Aucun renvoi entre eux. | 1.2.1.3.4 prend le contrôle des vendeurs étrangers et en ligne, y compris le paiement des contributions REP ; 1.2.5.1.3 garde la conception et la gouvernance des filières. Ajouter le renvoi réciproque. |
| N5 | IMPORTANT (trou résiduel) | 1.1.5.5.1 / 1.1.5.5.3 / 1.1.6.5.2 | L'accès à l'eau des logements non desservis hors quartiers informels (rural du Sud : puits, stockage, filtres) n'a pas de chantier, alors que frontieres.md l'inclut. | Élargir 1.1.5.5.1 en « Garantir l'accès à une eau saine au logement » : plomb, légionelle, stockage, puits et traitement domestique là où il n'y a pas de réseau. |
| N6 | MINEUR | 1.1.6.3.6 / 1.1.3.1.4 | Pour le neuf en climat chaud, la frontière n'est pas écrite : 1.1.6.3.6 vaut « sous tous les climats ». | Préciser que 1.1.6.3.6 porte les exigences, les codes et le contrôle de la performance, et 1.1.3.1.4 la conception passive contre la chaleur. Ajouter le renvoi de 1.1.3.1.4 vers 1.1.6.3.6. |
| N7 | MINEUR | 1.1.6.5.5 / 1.1.4.5.3 | Le relogement des sinistrés et l'abri des déplacés climatiques se recouvrent. | 1.1.4.5.3 garde le relogement temporaire après sinistre ; 1.1.6.5.5 garde les abris durables. Ajouter le renvoi. |
| N8 | MINEUR | 1.2.2.1.6 / 1.2.3.1.2 | La démontabilité sert à la fois le recyclage et la réparation. Aucun renvoi. | Ajouter le renvoi ; 1.2.2.1.6 se limite au choix et à la séparabilité des matières. |
| N9 | MINEUR | 1.2.4.2.1 / 1.2.4.2.3 / 1.2.4.2.4 (et 1.2.3.2.6 face aux familles) | Double axe fonction commune / circuit. Exemple : « laver des bocaux consignés » se range en 1.2.4.2.1 et en 1.2.4.2.3. | Écrire dans le critère que les chantiers par circuit ne portent que l'adoption propre à ce circuit. |
| N10 | MINEUR | 1.2.1.4 | Après la fusion, il reste 2 filles (limite de tolérance). | Acceptable. |
| N11 | MINEUR | 1.2.1.2.4 / 1.2.2.4.2 / 1.2.2.4.3 | L'usage est cité dans les deux branches (« par le choix de leurs usages », trafic vidéo). | Limiter 1.2.2.4.x à la conception. |
| N12 | MINEUR | 1.1.5.5.1 / 1.1.5.6.2 | « Plomb du bâti » contre plomb des canalisations. | Écrire « peintures au plomb » en 1.1.5.6.2. |
| N13 | MINEUR | 1.1.1.5.2 / 1.1.5.4.3 | Piloter les ballons d'eau chaude figure dans les deux. | Ajouter le renvoi. |
| N14 | MINEUR | 1.1.3.3.2 / 1.2.5.3.3 | La récupération des fluides en fin de vie (dégazage des réfrigérateurs) figure dans les deux. | Ajouter le renvoi. |
| N15 | MINEUR | 1.2.4.1.5 / 1.2.4.2.4 / 1.2.4.4.2 ; 1.2.4.1.4 / 1.2.4.1.1 | Le gobelet de comptoir et la vente fractionnée n'ont pas de renvoi. | Ajouter les renvois. |

## 3. Verdict

**Oui, l'arbre des niveaux 1 à 5 est assez solide pour descendre**, à condition de faire d'abord les corrections ci-dessous. Elles se font toutes en quelques phrases (définitions ou critères), sans restructuration. Tous les BLOQUANT des quatre rapports sont résolus. Les recouvrements qui restent sont localisés. Les exclusions sont écrites. La règle « un verrou transverse n'a qu'une place » est écrite dans les consignes des niveaux 6 à 8, avec deux listes fermées : familles de produits et types de bâtiments.

Corrections qui changent le périmètre d'un chantier, à faire avant de descendre (par ordre de gravité) :

1. **N1** : redéfinir 1.1.6.5.2 comme programme de réhabilitation sur place, les équipements restant en renvoi (sinon, verrous d'électrification et d'assainissement en double).
2. **N2** : écrire la règle « technologie contre situation de départ » pour les PAC et le bois (1.1.1.2.1, 1.1.1.4.1 face à 1.1.1.1.x et 1.1.1.5.x), et pour le chauffe-eau thermodynamique (1.1.1.2.3 face à 1.1.1.5.2).
3. **N3** : renommer 1.1.4.5.2 et en retirer le financement public de la prévention.
4. **N4** : tracer la frontière et le renvoi entre 1.2.1.3.4 et 1.2.5.1.3.
5. **N5** : élargir 1.1.5.5.1 à l'accès à l'eau des logements non desservis.
6. Indices de réparabilité : les retirer de 1.2.3.1.4 (ils sont affichés en 1.2.1.1.2).
7. Brûlage : écrire que celui des dépotoirs relève de 1.2.5.5.1, celui des zones sans service de 1.2.5.1.1, et que 1.2.5.1.5 ne garde que l'abandon diffus.

Peuvent attendre : N6 à N15, la minceur de 1.1.3.2.2, et les critères de 1.1.2.3, 1.1.5.6, 1.1.6.2 et 1.2.4.4, qui décrivent encore imparfaitement leurs filles.
