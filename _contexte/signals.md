# Signals — site_st   (MAJ 2026-10-20)

## Actions ouvertes
- [P1|ouvert] Terminer la phase 2 : obtenir la réponse à la question 4 de l'artefact (niveau d'expressivité), faire les contrôles visuels de `tests_manuels.md`, puis cocher la direction visuelle dans la roadmap
  - fait quand: direction visuelle validée par l'utilisateur et `tests_manuels.md` vidé.
  - réf: `tests_manuels.md`, `roadmap_portail_ia.md` Phase 2, artefact de revue.
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
- Artefact de revue du site (URL stable) : https://claude.ai/artifact/J4AEiAdJgip9J1Y6WetTZg ; collections db `commentaires`, `questions`, `reponses`. Republier : `npm run build`, `node scripts/build_revue.js`, republier `revue/revue_site.html`. Question 4 en attente de réponse ; la réponse à la question 1 (« plus expressive ») est enregistrée.
- Génération d'images : ComfyUI-Qwen sur `http://127.0.0.1:8189` (`D:\ServOMorph\ComfyUI-Qwen`, `lancer.bat`), `scripts/gen_illustrations.py` ; lent (jusqu'à plusieurs minutes par image sur la RTX 4060, mémoire déjà bien occupée).
- Branche `archive/v3-direction-b` sur `bc53de8`. PNG Qwen non versionnés dans `src/assets/brut/` (anciens visuels et nouvelles sources `ill_*.png`).
- V2 reste en ligne jusqu'à la bascule ; il affiche encore les badges « Flux.1 » / « Ollama local » (non modifié, à votre décision).
- `.env` V2 non lu. Le favicon n'existe pas encore (404 en local).

## Dernière session (2026-10-20)
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
