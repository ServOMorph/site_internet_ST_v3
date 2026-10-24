# Roadmap — Portail IA éco-responsable et humaniste (serenia-tech.fr)
Objectif : un site qui ressemble à une appli pour découvrir l'IA éco-responsable et humaniste, contenu V2 intégré et réécrit, puis anciennes fonctionnalités intégrées (phases 6 à 9 à reconsidérer, voir `signals.md`).
Créée le : 2026-10-17 (validée le même jour). Ancienne roadmap : branche `archive/v3-direction-b`.

---

## Phase 1 — Cadrage [FAIT]
- [x] Inventaire du contenu V2 à reprendre (`inventaire_v2.md`, titres seulement)
- [x] Lecture des sources éditoriales : document des Shorts (lu), articles et page Ressources du V2 (relus)
- [x] Lecture de `docs/CHARTE_GRAPHIQUE_SérénIATech.md` et `docs/guides/GUIDE_SEO_IA_SEARCH.md` du V2 (sections 1 et 6 lues ; reste en P2 dans signals)
- [x] Parcours : arborescence des écrans, parcours guidé et exploration libre, cartes
- [x] Arbitrage immersion / référencement : le contenu reste lisible en HTML sans JavaScript
- [x] Budget de poids et règles d'éco-conception à fixer avec l'utilisateur
- [x] Tests : aucun (livrable = documents de cadrage validés)

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

---

## Phase 2 — Socle et maquette appli [EN COURS]
- [x] Socle 11ty, gabarit mobile-first, navigation type appli (cartes, transitions CSS)
- [x] Direction visuelle : thème C (sombre, feuille-circuit, vert néon, illustrations Qwen, particules CSS) validé par l'utilisateur le 2026-10-22, mode sombre uniquement
- [x] Arborescence refondue : Comprendre (8 cartes dont « L'IA locale » et « Garder la main », sommaire = liste des cartes, textes éco-responsabilité et humanisme en brouillon), Fiches, Quiz, Sources, Glossaire, À propos ; Explorer supprimé ; titre « IA éco-responsable et humaniste »
- [x] Accueil : carte « En pratique », cartes pleine largeur « Actualités » et « Événements » (pages vides), validé par l'utilisateur le 2026-10-22
- [ ] Refonte humanisme numérique : page « Notre approche », étiquettes de thème des fiches, bloc « Un principe », quiz à deux axes, glossaire enrichi (décisions en attente, voir `signals.md`)
- [x] Tests : build, poids de page, HTML lisible sans JavaScript (`scripts/test_phase2.js`) ; rendu mobile / PC vu avec Playwright ; contrôles visuels restants dans `tests_manuels.md`

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

---

## Phase 3 — Contenus réécrits [TODO]
- [ ] Textes écrits avec l'utilisateur, faits validés un par un (Comprendre : brouillon des 8 cartes écrit, cartes 1, 4, 6, 7 et 8 retouchées le 2026-10-23, relecture de l'utilisateur en cours)
- [ ] Reprise du contenu V2 réorganisé (formations, services, ressources, portfolio, fiches, événement) ; peu de texte, textes courts
- [ ] Sections « En pratique » (pratiques de SérénIATech, fournies par l'utilisateur), « Actualités » (veille à mettre en place) et « Événements » : gabarit d'entrée, contenus réels uniquement
- [ ] Événement « 1 jour moins numérique » (8 nov. 2026) dans `/evenements/` : date, lieu, titre, avec accord du client
- [ ] Reprendre tarifs de formation, mention OPCO et témoignage Réseau Toiles (validés le 2026-10-17, voir `_contexte/archive_decisions.md`) ; autres prestations « sur devis »
- [ ] Chiffres sur l'impact énergétique : sources retenues dans `_contexte/archive_decisions.md` et page Sources du site (AIE, Arcep, Epoch AI), citées avec date et limites
- [ ] Tests : liens internes, SEO de base, JSON-LD, accessibilité

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

---

## Phase 4 — Contact et pages légales [TODO]
- [ ] Formulaire contact relié au backend Express existant (Render)
- [ ] Mentions légales, confidentialité, cookies, CGV mises à jour
- [ ] Tests : envoi réel du formulaire (ajouté à `tests_manuels.md`), liens légaux

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

---

## Phase 5 — Mise en ligne sur serenia-tech.fr [TODO]
- [ ] Hébergeur à trancher (Vercel prévu, Netlify demandé le 2026-10-24 : `netlify.toml` et `dist/` prêts) ; projet relié au dépôt (préproduction d'abord)
- [ ] Redirections 301/308 des URLs V2 vers les nouvelles (préserver le SEO)
- [ ] Bascule du domaine, V2 conservé en repli
- [ ] Tests manuels : formulaire en production, Search Console, redirections

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

---

## Phase 6 — Mise à jour automatique [TODO]
- [ ] Format `site_com.md` (fichier dédié par projet suivi, seule source lue)
- [ ] Commande `/maj_site` : détecte les `site_com.md` modifiés, produit un brouillon, publication après validation
- [ ] Garde-fou : aucun scan de dossier client, aucune donnée nominative publiée
- [ ] Tests : un avancement de projet et un événement passent de bout en bout

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

---

## Phase 7 — Veille IA locales [TODO]
- [ ] Détection des IA utilisées dans les projets récents
- [ ] Proposition de mise à jour de TableauDeBord, puis page « IA locales » générée depuis TableauDeBord
- [ ] Tests : une IA ajoutée dans un projet récent est détectée et proposée

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

---

## Phase 8 — Newsletter [TODO]
- [ ] Inscription avec double opt-in, lien de désinscription, adresses stockées hors git
- [ ] Envoi (canal selon délivrabilité), modèle d'édition, politique de confidentialité mise à jour
- [ ] Tests : inscription, confirmation, désinscription, envoi test

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

---

## Phase 9 — Extraits CreaZik [TODO]
- [ ] Vérification des droits de chaque morceau retenu
- [ ] Lecteur audio léger (pas de lecture automatique, fichiers compressés)
- [ ] Tests : lecture mobile/desktop, poids des fichiers

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

---

## Phase 10 — Capitalisation VibeObs [TODO]
- [ ] Remonter au kit les écarts constatés pendant le projet
- [ ] Rédiger `creation_superagent.md` à partir de ce qui a réellement fonctionné
