# Session du 2026-10-17

## Décisions prises
- Phase 1 validée : arborescence (parcours guidé 6 cartes, Explorer, Se former), une URL HTML par carte avec JS en amélioration, budget de poids (page <= 100 Ko hors images, JS <= 20 Ko, images <= 100 Ko).
- Blog à part dans Explorer ; formations en entrée directe et renvoi depuis la carte 6 ; polices Inter/Space Grotesk hébergées.
- Tarifs, témoignage Réseau Toiles, mention OPCO validés ; badges de galerie supprimés à la reprise.

## Livrables produits ou modifiés
- `cadrage_phase1.md`, `roadmap_portail_ia.md`, `inventaire_v2.md`, `.claude/memory.md` : créés
- `_contexte/contexte.md`, `_contexte/signals.md` : réécrits ; ancien code V3 retiré de main (archive en branche)

## Hypothèses validées / invalidées
- VALIDE : hébergement V2 = Vercel + Render, OVH registrar seulement.
- INVALIDE : badge « Ollama local » sur Flux.1 -> supprimé.
- EN ATTENTE : guide SEO V2 lu en partie (sections 1 et 6).

## Prochaine étape exacte
Phase 2 (socle et maquette appli), après `/compact`.

## Question bloquante pour la session suivante
Aucune

---

# Session du 2026-10-20

## Décisions prises
- Direction visuelle « plus expressive » choisie par l'utilisateur : illustrations Qwen locales et teinte par carte ; accueil avec « Se former » en premier.
- Revue du site par artefact avec bouton « Envoyer à Claude » (règle enregistrée dans `.claude/memory.md`).

## Livrables produits ou modifiés
- `package.json`, `.eleventy.js`, `src/` (10 pages, gabarit, CSS, JS 0,4 Ko, polices hébergées, 9 illustrations WebP) : créés
- `scripts/test_phase2.js`, `scripts/gen_illustrations.py`, `scripts/build_revue.js`, `revue/` : créés ; tests OK
- `.claude/memory.md` : 2 entrées (artefact de revue, publication automatique)
- `tests_manuels.md` : contrôles visuels en attente

## Hypothèses validées / invalidées
- VALIDE : budget de poids tenu sur la maquette (HTML+CSS+JS ~3 Ko, polices 69 Ko), HTML lisible sans JS.
- INVALIDE : cases à cocher natives pour les questions (bug d'identifiant) -> boutons de choix, identifiants lus sur une copie des données.
- EN ATTENTE : rendu écran des cartes illustrées, mode sombre, transitions de pages, niveau d'expressivité (question 4).

## Prochaine étape exacte
Lire la réponse à la question 4 de l'artefact, ajuster si besoin, valider la direction visuelle, puis passer au checkpoint de fin de phase 2 (`/compact`).

## Question bloquante pour la session suivante
Aucune

---
# Session du 2026-10-22

## Décisions prises
- Thème C validé (sombre, feuille-circuit, vert néon, particules) ; mode sombre uniquement.
- Titre du site : « IA éco-responsable et humaniste ».
- Arborescence : Comprendre (parcours en 7 cartes, ajout « Garder la main »), Fiches, Quiz ; Explorer supprimé ; Se former en carte d'accueil et pied de page ; Sources, Glossaire, À propos en pied.
- Peu de texte sur le site ; aucun rythme de fiches annoncé ; logo en pied de page.

## Livrables produits ou modifiés
- `src/`, CSS thème C, 16 pages (fiches, quiz, glossaire, sources, à propos), 10 illustrations, hero, logo : créés ou modifiés ; tests OK
- `run.py`, `scripts/gen_theme_c.py`, `scripts/gen_propositions.py`, `scripts/build_revue.js`, `humanisme_numerique_ia.md`, `tests_manuels.md` : créés ou modifiés
- Artefact de revue republié (v19) ; commentaires traités

## Hypothèses validées / invalidées
- VALIDE : budget de poids (4 à 5 Ko par page hors polices) ; rendu mobile et PC contrôlé à l'écran (accueil, fiche, parcours, carte 4).
- INVALIDE : titre du hero sur une ligne en mobile -> deux lignes ; document humanisme : source 6 datée 2026 (en fait 2025), principe 6 attribué au Manifeste.
- EN ATTENTE : quiz, glossaire, page Sources, animations sur téléphone réel ; formule officielle ; bloc « Un principe ».

## Prochaine étape exacte
Faire valider les décisions de la refonte humanisme et corriger le document, puis construire « Notre approche », les thèmes de fiches et le quiz à deux axes.

## Question bloquante pour la session suivante
Votre formule (« Une IA humaniste est une IA au service de l'autonomie humaine… ») devient-elle la définition officielle du site ?

---

# Session du 2026-10-22

## Décisions prises
- Accueil : la carte « Dernière fiche » devient « En pratique » (pratiques de SérénIATech) ; deux cartes pleine largeur « Actualités » et « Événements » (hauteur 7 rem, image à gauche) sous la grille ; accueil validé par l'utilisateur.
- Fiches reste dans la navigation, sans carte d'accueil ; le mot « fiche » déplaît à l'utilisateur (renommage à trancher).
- Veille d'actualité à mettre en place plus tard ; hero : hauteur minimale supprimée (hauteur = texte).

## Livrables produits ou modifiés
- `src/index.njk`, `src/assets/css/app.css`, `scripts/gen_theme_c.py` : modifiés ; `src/en-pratique/`, `src/actualites/`, `src/evenements/` (pages « Contenu à venir ») et 3 images Qwen (`en-pratique`, `actualites`, `evenements`) : créés ; tests OK (20 pages)
- Artefact de revue republié (version 20) ; `roadmap_portail_ia.md`, `tests_manuels.md` : mis à jour

## Hypothèses validées / invalidées
- VALIDE : accueil et images validés à l'écran par l'utilisateur ; `scripts/test_phase2.js` OK.
- INVALIDE : « En pratique » comme nouveau nom de la section Fiches (contenu différent) -> section dédiée aux pratiques.
- EN ATTENTE : nom de la section « Fiches » ; formule officielle ; contenus des trois nouvelles sections ; contrôles sur téléphone réel.

## Prochaine étape exacte
Faire valider la formule officielle et corriger `humanisme_numerique_ia.md`, trancher le nom de « Fiches », puis construire « Notre approche », les thèmes de fiches et le quiz à deux axes.

## Question bloquante pour la session suivante
Votre formule (« Une IA humaniste est une IA au service de l'autonomie humaine… ») devient-elle la définition officielle du site ?

---
# Session du 2026-10-22

## Décisions prises
- En-tête aligné sur l'accueil : Accueil, Comprendre, En pratique, Quiz, Actualités, Événements ; Fiches retirée de la navigation, Se former reste en pied de page.
- Comprendre passe à 8 cartes (ajout « L'IA locale » en 2e position, avant la première mention) ; textes éco-responsabilité et humanisme numérique en brouillon dans `src/_data/parcours.json` ; sources en petit, une par ligne, sous un filet.
- Suivi du parcours en local (« Reprendre », « vu ») et bouton « Commencer » supprimés ; page sommaire = liste des cartes ; titre « … éco-responsable et humaniste ».
- Accueil : hero sans boutons et moins haut ; chiffre d'accueil = AIE 415 TWh (2024), +17 % (2025), doublement d'ici 2030 ; 485 TWh non repris.

## Livrables produits ou modifiés
- `src/_includes/base.njk`, `src/index.njk`, `src/assets/css/app.css`, `src/sources/index.njk`, `src/parcours/index.njk`, `src/parcours/carte.njk`, `src/_data/parcours.json`, `scripts/build_revue.js` : modifiés ; `src/assets/js/app.js` : supprimé ; tests OK (21 pages)
- Artefact de revue republié (version 21) ; `roadmap_portail_ia.md`, `tests_manuels.md`, `README.md`, `CHANGELOG.md` (v0.6) : mis à jour

## Hypothèses validées / invalidées
- VALIDE : Manifeste de Vienne (phrase exacte), 415 TWh et 945 TWh (AIE 2025), 0,3 Wh (Epoch AI) recoupés par recherche web ; `scripts/test_phase2.js` OK.
- EN ATTENTE : +17 % (2025) non lu sur iea.org ; textes des cartes 3 à 8 à valider par l'utilisateur ; rendu navigateur non vérifié (barre à 6 entrées, sources, titre).

## Prochaine étape exacte
Recueillir le retour de l'utilisateur sur les cartes 3 à 8 de Comprendre, puis vérifier le +17 % sur iea.org et faire valider la formule officielle humaniste (corriger `humanisme_numerique_ia.md`).

## Question bloquante pour la session suivante
Votre formule (« Une IA humaniste est une IA au service de l'autonomie humaine… ») devient-elle la définition officielle du site ?

---
# Session du 2026-10-23

## Décisions prises
- Carte 1 « Pourquoi » : comparaisons de pays ajoutées (415 TWh en 2024 = environ les quatre cinquièmes de la consommation brute de l'Allemagne, environ 512 TWh, BDEW ; 945 TWh en 2030 = un peu plus que le Japon, phrase AIE).
- Carte 4 : définition du RGPD ajoutée. Carte 6 : étapes de la méthode sur des lignes séparées, paragraphe « bloc-notes avant le prompt ».
- Carte 7 « Les outils » réécrite : Ollama (chat), ComfyUI (images et musique), Vibe-Mistral (chat français) ; Qwen-Image retiré ; liens ajoutés.
- Carte 8 : liens vers Se former et À propos ; paragraphe de sites de référence (Arcep, CNIL, UNESCO, TU Wien).

## Livrables produits ou modifiés
- `src/_data/parcours.json` : modifié (cartes 1, 4, 6, 7, 8) ; build et `scripts/test_phase2.js` OK (21 pages)
- `README.md`, `CHANGELOG.md` (v0.7), `roadmap_portail_ia.md`, `tests_manuels.md` : mis à jour

## Hypothèses validées / invalidées
- VALIDE : phrase AIE « slightly more than Japan's total electricity consumption today » (résumé WebFetch de la page AIE).
- EN ATTENTE : 512 TWh BDEW lu dans un résumé de recherche, non sur bdew.de ; +17 % non lu sur iea.org ; liens TU Wien et chat.mistral.ai non ouverts ; rendu navigateur non contrôlé.

## Prochaine étape exacte
Recueillir le retour de l'utilisateur sur les cartes de Comprendre, vérifier le +17 % sur iea.org, puis faire valider la formule officielle humaniste.

## Question bloquante pour la session suivante
Votre formule (« Une IA humaniste est une IA au service de l'autonomie humaine… ») devient-elle la définition officielle du site ?
