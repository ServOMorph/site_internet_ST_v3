# Contexte — site_st

## Objectif (immuable sauf décision explicite)
Refonte de serenia-tech.fr : vitrine d'art IA locale et éco-responsable, formations, portfolio et newsletter.

## Stack / contraintes techniques (stable, rarement modifié)
11ty (site statique), HTML/CSS/JS, Express sur Render (contact, newsletter), Vercel, Qwen local (images)

## État actuel (réécrit intégralement à chaque /close)
Phase 1 en cours. 11ty initialisé (direction B, collections projets/formations/événements, sitemap, robots, JSON-LD), `npm test` : 97 contrôles OK.
Serveur de test : `npm start` (port 5000). 8 visuels Qwen générés dans `src/assets/brut/` (non versionnés, non intégrés au site).
Fiches projets et formations : texte provisoire « Fiche à rédiger » (aucun fait validé).
Restant phase 1 : intégration des images (WebP 640/1200, alt), poids de page avec images, rendu 1920 px.

## Décisions structurantes (append only — 10 entrées max, 5 lignes max/entrée, archiver au-delà)
- 2026-10-12 : Initialisation du protocole vibecoding.
- 2026-10-12 : Contraintes de conception : (1) mobile-first, optimisé d'abord pour lecture sur smartphone, puis écran PC et télé ; (2) conçu pour la visibilité dans les recherches IA (moteurs génératifs) en plus du SEO classique.
- 2026-10-12 : Direction artistique retenue : B « Nuit de laboratoire » (fond #0E1517, texte #E8EEEE, accents #7FD1C7 et #E6B450 ; base du site : src/css/site.css et src/_includes/base.njk). Les images doivent s'harmoniser avec le fond sombre et apporter couleur, joie et sérénité.
- 2026-10-15 : Visuels générés par `scripts/gen_images.py` (ComfyUI-Qwen, port 8189, Q4_K_M, 1,5 à 5 min/image) à partir de `scripts/prompts_b.json`. PNG bruts non versionnés (`src/assets/brut/`).
- 2026-10-15 : Tests de phase 1 = `npm test` (`scripts/test_phase1.js`) + Playwright mobile 390 / PC 1280 ; budget accueil 50 Ko gzip hors images (fixé arbitrairement).
