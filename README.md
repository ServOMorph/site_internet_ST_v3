# site_internet_ST_v3

## Objectif
Refonte de serenia-tech.fr : vitrine d'art IA locale et éco-responsable, formations, portfolio et newsletter.

## Stack
11ty (site statique), HTML/CSS sans JavaScript, Express sur Render (contact, newsletter), Vercel, Qwen local (images).

## Structure
- `src/` : gabarits, CSS, contenus Markdown (`src/content/`).
- `scripts/` : tests (`test_phase1.js`) et génération d'images (`gen_images.py`).
- `roadmap_site_v3.md`, `_contexte/` : suivi du projet.

## Commandes
- `npm run build` : génère `_site/`.
- `npm start` : serveur de test sur le port 5000.
- `npm test` : contrôles de la phase 1.

## État actuel
Phase 1 en cours : socle 11ty en place, 8 visuels générés, intégration des images et mesures de poids restantes.
