# site_st — Portail IA éco-responsable et humaniste (serenia-tech.fr)

## Objectif
Un site façon appli (cartes à toucher, animations, parcours guidé) pour découvrir l'IA éco-responsable et l'humanisme numérique. But : référence, public grand public. Intègre le contenu du site V2, réorganisé et réécrit avec l'auteur.

## Stack
11ty (site statique), HTML/CSS/JS minimal, Vercel (frontend), Express sur Render (contact). Une URL HTML par carte, JavaScript en amélioration seulement.

## Structure
- `_contexte/` : protocole vibecoding (contexte, signals, archives)
- `src/` : site 11ty (gabarits, pages, CSS, JS, polices, illustrations) ; `_site/` : sortie du build
- `scripts/` : tests de phase 2, génération des illustrations (Qwen local : `gen_illustrations.py`, `gen_theme_c.py`, `gen_propositions.py`), génération de l'artefact de revue
- `revue/` : artefact de revue du site (aperçu, commentaires, questions)
- `run.py` : serveur local avec rechargement automatique (port 8765)
- `roadmap_portail_ia.md` : roadmap en 10 phases
- `cadrage_phase1.md` : arbitrage immersion/SEO, budget de poids (arborescence à mettre à jour)
- `inventaire_v2.md` : inventaire du site V2
- `humanisme_numerique_ia.md` : document source sur l'humanisme numérique appliqué à l'IA (à corriger avant publication)
- Ancien travail : branche `archive/v3-direction-b`

## État actuel
Phase 2 en cours (socle et maquette) : thème C et accueil validés, en-tête aligné sur l'accueil (Accueil, Comprendre, En pratique, Quiz, Actualités, Événements), 21 pages buildées (Accueil, Comprendre en 8 cartes dont « L'IA locale », Fiches, Quiz, En pratique, Actualités, Événements, Glossaire, Sources, À propos, Se former ; les trois nouvelles sections sont vides). Textes de Comprendre en brouillon, en relecture ; refonte humanisme numérique en attente de décisions. Textes non définitifs (phase 3).

## Commandes
- `python run.py` : serveur local avec rechargement automatique, ouvre le navigateur sur http://localhost:8765/
- `npm run build` : construit le site dans `_site/` ; `npm start` : serveur Eleventy sur le port 5000 ; `npm test` : tests de phase 2 (après un build)
