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
