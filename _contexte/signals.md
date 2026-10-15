# Signals — site_st   (MAJ 2026-10-15)

## Actions ouvertes
- [P1|ouvert] Intégrer les 8 visuels au site (WebP 640 et 1200 px, texte alternatif, fond intégré) et mesurer le poids de l'accueil
  - fait quand: les images s'affichent sur `/` (port 5000), `npm test` passe, poids gzip de l'accueil images comprises mesuré et noté.
  - réf: `scripts/prompts_b.json` (alt), `src/assets/brut/`, `scripts/test_phase1.js`, `roadmap_site_v3.md` Phase 1.
- [P2|ouvert] Trancher la ligne visuelle des images (mélange cartoon et photoréaliste) et décider si les anciennes versions `*_v1`/`*_v2` sont à supprimer
  - fait quand: choix noté dans `contexte.md`, images non retenues régénérées ou écartées.
  - réf: `src/assets/brut/`, artefact https://claude.ai/artifact/W9sDXecJ9yQUBMEW1PssWV
- [P2|ouvert] Décider d'ajouter les critères mobile-first et recherche IA aux tests des phases 1 et 2 de la roadmap
  - fait quand: réponse de l'utilisateur ; roadmap mise à jour si oui.
  - réf: `_contexte/contexte.md` (décisions du 2026-10-12), `roadmap_site_v3.md`.
- [P2|ouvert] Tests manuels : rendu sur smartphone réel (tunnel) et à 1920 px
  - fait quand: sections validées puis supprimées de `tests_manuels.md`.
  - réf: `tests_manuels.md`.

## Contexte chaud
- Serveur 11ty actif sur le port 5000 (a remplacé un Vite de Appli_TSA_SDI_TDAH arrêté sur demande). ComfyUI arrêté (port 8189 libre).
- Contact V2 : `server.js` Express (SendGrid) sur Render ; `.env` du V2 non lu.

## Dernière session (2026-10-15)
<!-- Écrasé intégralement par /close. Synthèse < 25 lignes. -->
# Session du 2026-10-15

## Décisions prises
- Direction artistique B « Nuit de laboratoire » retenue ; mobile-first puis PC/télé ; visibilité recherche IA.
- Qwen local pour les visuels ; PNG bruts non versionnés.

## Livrables produits ou modifiés
- Socle 11ty (config, gabarit, CSS, collections, sitemap, robots, JSON-LD) : fait.
- `scripts/test_phase1.js` : 97 contrôles OK. `scripts/gen_images.py` + `prompts_b.json` : 8 images générées.
- Artefact maquette (8 visuels) : publié, non vérifié sur téléphone.
- `roadmap_site_v3.md`, `tests_manuels.md`, `CHANGELOG.md`, `README.md` : mis à jour.

## Hypothèses validées / invalidées
- VALIDE : le script pilote ComfyUI ; images à fond sombre intégrables.
- INVALIDE : le prompt négatif exclut les croix (cfg 1) -> prompt positif reformulé.
- EN ATTENTE : rendu 1920 px, rendu sur smartphone réel, poids avec images.

## Prochaine étape exacte
Intégrer les visuels au site, mesurer le poids, relancer `npm test`.

## Question bloquante pour la session suivante
Aucune
