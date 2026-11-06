# site_st — Portail IA éco-responsable et humaniste (serenia-tech.fr)

## Objectif
Un site façon appli (cartes à toucher, animations, parcours guidé) pour découvrir l'IA éco-responsable et l'humanisme numérique. But : référence, public : les associations. Intègre le contenu du site V2, réorganisé et réécrit avec l'auteur.

## Stack
11ty (site statique), HTML/CSS/JS minimal, Vercel ou Netlify (frontend, à trancher ; `netlify.toml` prêt), Express sur Render (contact). Une URL HTML par carte, JavaScript en amélioration seulement.

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
Phase 2 en cours (socle et maquette), phase 3 (contenus) entamée : 21 pages buildées dans `dist/` (Accueil, Comprendre en 8 cartes, Fiches, Quiz, En pratique, Actualités, Événements, Ressources, Glossaire, Sources, À propos, Formations). Accueil avec bandeau de 3 témoignages ; Formations, À propos, En pratique et Ressources rédigés au « je » (marque « SérénIA Tech », public = associations) ; contact par e-mail. Actualités et Événements restent vides ; textes de Comprendre en brouillon ; refonte humanisme numérique en attente de décisions. Déploiement Netlify du site complet non fait (le guide agents est déployé à part).

## Commandes
- `python run.py` : serveur local avec rechargement automatique, ouvre le navigateur sur http://localhost:8765/
- `npm run build` : construit le site dans `dist/` ; `npm start` : serveur Eleventy sur le port 5000 ; `npm test` : tests de phase 2 (après un build)
