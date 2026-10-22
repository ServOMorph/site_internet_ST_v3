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
