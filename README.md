# site_st — Portail IA éco-responsable et humaniste (serenia-tech.fr)

## Objectif
Un site façon appli (cartes à toucher, animations, parcours guidé) pour découvrir l'IA éco-responsable et l'humanisme numérique. But : référence, public : les associations. Intègre le contenu du site V2, réorganisé et réécrit avec l'auteur.

## Stack
11ty (site statique), HTML/CSS/JS minimal, Vercel (frontend, `vercel.json` ; Netlify écarté), Express sur Render (contact). Une URL HTML par carte, JavaScript en amélioration seulement.

## Structure
- `_contexte/` : protocole vibecoding (contexte, signals, archives)
- `src/` : site 11ty (gabarits, pages, CSS, JS, polices, illustrations) ; `dist/` : sortie du build
- `scripts/` : tests de phase 2, génération des illustrations (Qwen local : `gen_illustrations.py`, `gen_theme_c.py`, `gen_propositions.py`, `gen_bandeau.py`), génération des artefacts de revue (`build_revue.js`, `build_revue_images.js`) et du dossier autonome du guide agents (`build_ressources_autonome.js`)
- `revue/` : artefact de revue du site (aperçu, commentaires, questions)
- `run.py` : serveur local avec rechargement automatique (port 8765)
- `roadmap_portail_ia.md` : roadmap en 10 phases ; `tests_manuels.md` : contrôles manuels en attente
- `cadrage_phase1.md` : arbitrage immersion/SEO, budget de poids (arborescence à mettre à jour)
- `inventaire_v2.md` : inventaire du site V2
- `humanisme_numerique_ia.md` : document source sur l'humanisme numérique appliqué à l'IA (à corriger avant publication)
- Ancien travail : branche `archive/v3-direction-b`

## État actuel
Périmètre V1 (S-08) en préproduction sur Vercel (`site-internet-st-v3.vercel.app`) : 22 pages dans `dist/` (Accueil, Comprendre en 8 cartes validées, Fiches, En pratique, Ressources, Glossaire, Sources, À propos, Formations réservées aux structures, Mentions légales, Confidentialité). Barre à 5 entrées ; Actualités et Événements retirés de la navigation. Reste la relecture juridique, puis les redirections V2 et la bascule de `serenia-tech.fr`.

## Commandes
- `python run.py` : serveur local avec rechargement automatique, ouvre le navigateur sur http://localhost:8765/
- `npm run build` : construit le site dans `dist/` ; `npm start` : serveur Eleventy sur le port 5000 ; `npm test` : tests de phase 2 (après un build)
