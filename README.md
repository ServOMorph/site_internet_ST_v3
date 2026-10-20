# site_st — Portail IA éco-responsable (serenia-tech.fr)

## Objectif
Un site façon appli (cartes à toucher, animations, parcours guidé et exploration libre) pour découvrir l'IA éco-responsable. Intègre le contenu du site V2, réorganisé et réécrit avec l'auteur.

## Stack
11ty (site statique), HTML/CSS/JS minimal, Vercel (frontend), Express sur Render (contact). Une URL HTML par carte, JavaScript en amélioration seulement.

## Structure
- `_contexte/` : protocole vibecoding (contexte, signals)
- `src/` : site 11ty (gabarits, pages, CSS, JS, polices, illustrations) ; `_site/` : sortie du build
- `scripts/` : tests de phase 2, génération des illustrations (Qwen local), génération de l'artefact de revue
- `revue/` : artefact de revue du site (aperçu, commentaires, questions)
- `roadmap_portail_ia.md` : roadmap en 10 phases
- `cadrage_phase1.md` : arborescence, arbitrage immersion/SEO, budget de poids
- `inventaire_v2.md` : inventaire du site V2
- Ancien travail : branche `archive/v3-direction-b`

## État actuel
Phase 2 en cours (socle et maquette) : 10 pages buildées, direction visuelle expressive (illustrations Qwen, teinte par carte) en attente de validation. Textes non définitifs (phase 3).

## Commandes
- `npm run build` : construit le site dans `_site/` ; `npm start` : serveur local ; `npm test` : tests de phase 2 (après un build)
