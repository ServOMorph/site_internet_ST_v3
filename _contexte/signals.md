# Signals — site_st   (MAJ 2026-10-17)

## Actions ouvertes
- [P1|ouvert] Phase 2 : socle 11ty, gabarit mobile-first, navigation type appli, direction visuelle à proposer, mesure du poids réel (polices Inter/Space Grotesk hébergées, repli système si budget dépassé)
  - fait quand: socle buildé, rendu mobile/PC testé, poids par page mesuré et conforme au budget de `cadrage_phase1.md`, HTML lisible sans JS.
  - réf: `cadrage_phase1.md`, `roadmap_portail_ia.md` Phase 2.
- [P2|ouvert] Compléter la lecture du guide SEO V2 (sections 2 à 5 et 7 non lues) avant de figer les gabarits SEO
  - fait quand: sections lues et points utiles reportés dans `cadrage_phase1.md`.
  - réf: V2 `docs/guides/GUIDE_SEO_IA_SEARCH.md`.
- [P2|ouvert] Ajouter l'événement « 1 jour moins numérique » (8 nov. 2026, seul événement concerné) à la V3 ; date, lieu et titre uniquement, avec accord du client
  - fait quand: fiche événement créée en phase 3.
  - réf: V2 `pages/1-jour-moins-numerique.html`, `pages/evenements.html`.
- [P3|ouvert] Corriger l'hébergeur OVH dans les pages légales (V3) ; trancher Gmail vs SendGrid en lisant `server.js` V2 (phase 4)
  - fait quand: mentions légales V3 indiquent l'hébergeur réel ; messagerie du contact identifiée.
  - réf: `_contexte/contexte.md` (hébergement V2), V2 `render.yaml`, `server.js`.

## Contexte chaud
- Branche `archive/v3-direction-b` sur `bc53de8`. Ancien code retiré de `main`.
- PNG Qwen non versionnés dans `src/assets/brut/` : à supprimer ou garder à votre convenance.
- V2 reste en ligne jusqu'à la bascule ; il affiche encore les badges « Flux.1 » / « Ollama local » (non modifié, à votre décision).
- `.env` V2 non lu.

## Dernière session (2026-10-17)
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
