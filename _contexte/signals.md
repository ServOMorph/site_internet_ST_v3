# Signals — site_st   (MAJ 2026-10-24)

## Actions ouvertes
- [P1|ouvert] Recueillir le retour de l'utilisateur sur les 8 cartes de Comprendre (texte en brouillon dans `src/_data/parcours.json` ; cartes 1, 4, 6, 7 et 8 retouchées le 2026-10-23 à la demande de l'utilisateur, aucune validation formelle exprimée ; cartes 3 et 5 non relues cette session) ; fournir une illustration dédiée à « L'IA locale » (réutilise `outils.webp`) ; sourcer la définition de l'IA locale et les descriptions des outils (carte 7, sans source) si l'utilisateur le veut
  - fait quand: textes des 8 cartes validés par l'utilisateur, image dédiée en place.
  - réf: `src/_data/parcours.json`, `src/parcours/`, `roadmap_portail_ia.md` Phase 3.
- [P1|ouvert] Vérifier le +17 % (2025) et le doublement d'ici 2030 sur le communiqué ou le rapport AIE d'avril 2026 sur iea.org (non lu en source primaire : recoupé par la presse, une source donne 15 % et 485 TWh) ; chiffre affiché sur l'accueil, la carte « Pourquoi » et la page Sources
  - fait quand: chiffre lu sur iea.org et confirmé, ou texte corrigé.
  - réf: `src/index.njk`, `src/_data/parcours.json`, `src/sources/index.njk`.
- [P1|ouvert] Trancher la refonte « humanisme numérique » : formule officielle (« Une IA humaniste est une IA au service de l'autonomie humaine… »), bloc « Un principe » sur l'accueil ; les cartes Données, Garder la main et Essayer de Comprendre nomment déjà l'humanisme numérique (sans la formule) ; puis construire page « Notre approche », étiquettes de thème des fiches (Planète, Maîtrise, Humain), quiz à deux axes, glossaire enrichi
  - fait quand: décisions actées par l'utilisateur et éléments en maquette dans l'artefact de revue.
  - réf: `humanisme_numerique_ia.md`, artefact de revue, `roadmap_portail_ia.md` Phase 2.
- [P1|ouvert] Faire les contrôles manuels de `tests_manuels.md` sur téléphone réel (hero sans boutons, carte chiffre, barre basse à 6 entrées, Comprendre et ses 8 cartes, animations, quiz, transitions, arborescence), puis clore la phase 2 (thème C et accueil déjà validés)
  - fait quand: `tests_manuels.md` vidé et Phase 2 marquée [FAIT] dans la roadmap.
  - réf: `tests_manuels.md`, `roadmap_portail_ia.md` Phase 2.
- [P2|ouvert] Déployer sur Netlify (préproduction) : choisir entre dépôt Git relié (build par `netlify.toml`) et glisser-déposer de `dist/` ; trancher Netlify vs Vercel (roadmap phase 5) ; contact Render non relié ; textes de Comprendre en brouillon et +17 % non lu sur iea.org, donc URL non publique
  - fait quand : site en ligne sur une URL Netlify de préproduction, ou décision d'hébergeur actée dans la roadmap.
  - réf : `netlify.toml`, `.eleventy.js`, `roadmap_portail_ia.md` Phase 5.
- [P2|ouvert] Trancher le nom de la section « Fiches » (l'utilisateur n'aime pas le mot ; proposition « Questions ») et l'URL `/fiches/` ; Fiches n'est plus dans l'en-tête (ni sur l'accueil) : la section n'est plus liée que depuis ses propres pages et la page Sources, à décider (la remettre dans la navigation, ou la lier autrement)
  - fait quand: nom, URL et emplacement dans la navigation choisis, puis appliqués partout.
  - réf: `src/fiches/index.njk`, `src/_includes/base.njk`, `src/_data/fiches.json`.
- [P2|ouvert] Corriger `humanisme_numerique_ia.md` avant publication : source 6 = conférence 2025 (pas 2026), principe 6 non attribuable au Manifeste de Vienne (dépendance cognitive et « moments sans IA » absents ; l'idée « IA contradicteur » est reprise sans source dans la carte « Essayer »), phrase « version grand public » présentée comme citation mais non vérifiée
  - fait quand: document corrigé, citations limitées à ce qui est vérifié, Springer vérifié ou retiré.
  - réf: `humanisme_numerique_ia.md`, Manifeste de Vienne (PDF TU Wien), page UNESCO.
- [P2|ouvert] Définir le gabarit d'entrée et l'alimentation des sections « En pratique » (pratiques de SérénIATech, à fournir par l'utilisateur), « Actualités » (veille à mettre en place, publication manuelle d'abord) et « Événements » ; pages actuellement « Contenu à venir » ; ne publier aucune entrée inventée
  - fait quand: gabarit d'entrée en maquette et premières entrées réelles fournies, ou décision de masquer les cartes tant qu'elles sont vides.
  - réf: `src/en-pratique/`, `src/actualites/`, `src/evenements/`, `roadmap_portail_ia.md` Phase 3.
- [P2|ouvert] Mettre à jour `cadrage_phase1.md` pour la nouvelle arborescence (Explorer supprimé, Comprendre 8 cartes sans bouton Commencer ni suivi, Fiches, Quiz, En pratique, Actualités, Événements, Sources, Glossaire, À propos ; en-tête à 6 entrées) et trancher l'URL `/parcours/` ou `/comprendre/`
  - fait quand: cadrage à jour et URL choisie.
  - réf: `cadrage_phase1.md`, `src/`.
- [P2|ouvert] Compléter la lecture du guide SEO V2 (sections 2 à 5 et 7 non lues) avant de figer les gabarits SEO
  - fait quand: sections lues et points utiles reportés dans `cadrage_phase1.md`.
  - réf: V2 `docs/guides/GUIDE_SEO_IA_SEARCH.md`.
- [P2|ouvert] Ajouter l'événement « 1 jour moins numérique » (8 nov. 2026, seul événement concerné) dans la section `/evenements/` de la V3 ; date, lieu et titre uniquement, avec accord du client
  - fait quand: entrée créée dans `/evenements/` en phase 3.
  - réf: V2 `pages/1-jour-moins-numerique.html`, `pages/evenements.html`, `src/evenements/index.njk`.
- [P3|ouvert] Décider du sort des phases 6 à 9 (mise à jour auto, veille IA locales, newsletter, extraits CreaZik) au regard du but « référence » : mon avis = garder la newsletter et la veille comme source de « Actualités », reconsidérer `site_com.md` et CreaZik
  - fait quand: décision actée dans la roadmap.
  - réf: `roadmap_portail_ia.md` phases 6 à 9.
- [P3|ouvert] Corriger l'hébergeur OVH dans les pages légales (V3) ; trancher Gmail vs SendGrid en lisant `server.js` V2 (phase 4)
  - fait quand: mentions légales V3 indiquent l'hébergeur réel ; messagerie du contact identifiée.
  - réf: `_contexte/archive_decisions.md` (hébergement V2), V2 `render.yaml`, `server.js`.

## Contexte chaud
- Artefact de revue du site (URL stable) : https://claude.ai/artifact/J4AEiAdJgip9J1Y6WetTZg (version 22, publiée le 2026-10-23, après retouche des cartes 1, 4, 6, 7 et 8). Republier : `npm run build` (sortie `dist/`), `node scripts/build_revue.js` (lit `dist/`, non relancé depuis le changement), republier `revue/revue_site.html`. Base commentaires/questions non relue cette session (dernier état connu : 9 commentaires traités, q1 répondue, q3 non répondue).
- Serveur local : `python run.py` (port fixe 8765, Eleventy en rechargement automatique ; sortie dans `dist/`, ancien `_site/` supprimé).
- Génération d'images : ComfyUI-Qwen sur `http://127.0.0.1:8189` (`D:\ServOMorph\ComfyUI-Qwen`, `lancer.bat`), `scripts/gen_theme_c.py` ; non lancé cette session ; un blocage de 45 min a été observé une fois (VRAM saturée) : redémarrer ComfyUI. Demander avant de lancer.
- Branche `archive/v3-direction-b` sur `bc53de8`. PNG Qwen non versionnés dans `src/assets/brut/`. `explorer.webp` n'est plus utilisée.
- Comparaisons de pays (carte 1) : Japon pour 945 TWh en 2030 (phrase AIE lue, résumé WebFetch) ; Allemagne pour 415 TWh en 2024 (environ 512 TWh bruts, estimation préliminaire BDEW lue dans un résumé de recherche, non lue sur bdew.de ; rapport 415/512 calculé par nous, pas par l'AIE). Liens carte 8 : Arcep, CNIL, UNESCO ouverts ; TU Wien et `chat.mistral.ai` (Vibe = Le Chat renommé) non ouverts ; page ADEME en erreur 403, pas de guide grand public trouvé.
- Logo SéréniaTech repris du V2 (`assets/logo_optimized`), en pied de page et en favicon.
- Humanisme numérique : sources vérifiées par lecture/recherche = Manifeste de Vienne (mai 2019, phrase « shape technologies… » retrouvée dans la copie TU Wien), UNESCO Recommandation (nov. 2021, supervision humaine confirmée par résumés secondaires, texte officiel non lu cette session). Non vérifiées : phrase de la version grand public, chapitre Springer.
- Chiffres éco (recoupés par recherche web cette session, sources secondaires) : AIE 415 TWh (2024), environ 945 TWh (2030), +17 % en 2025 contre environ 3 % pour la demande mondiale ; Epoch AI 0,3 Wh ; OpenAI environ 0,34 Wh (juin 2025) ; Arcep (21 mai 2026) : peu de transparence sur l'inférence. Source brésilienne divergente (15 %, 485 TWh) non retenue.
- V2 reste en ligne jusqu'à la bascule ; il affiche encore les badges « Flux.1 » / « Ollama local » (non modifié, à votre décision). `.env` V2 non lu.

## Dernière session (2026-10-24)
# Session du 2026-10-24

## Décisions prises
- Sortie du build 11ty passée de `_site/` à `dist/` pour un déploiement Netlify ; `netlify.toml` créé (build `npm run build`, publication `dist`).

## Livrables produits ou modifiés
- `.eleventy.js`, `.gitignore`, `scripts/build_revue.js`, `scripts/test_phase2.js`, `README.md` : sortie `dist/` ; `netlify.toml` : créé
- Build (20 pages, 384 Ko) et `npm test` OK ; `CHANGELOG.md` (v0.8), `roadmap_portail_ia.md`, `contexte.md` : mis à jour

## Hypothèses validées / invalidées
- VALIDE : build et `npm test` passent avec `dist/`.
- EN ATTENTE : déploiement Netlify non effectué ni testé ; `build_revue.js` non relancé après le changement de dossier.

## Prochaine étape exacte
Choisir le mode de déploiement Netlify (dépôt relié ou glisser-déposer de `dist/`) et trancher Netlify vs Vercel ; sinon recueillir le retour sur les cartes de Comprendre, vérifier le +17 % sur iea.org, faire valider la formule humaniste.

## Question bloquante pour la session suivante
Votre formule (« Une IA humaniste est une IA au service de l'autonomie humaine… ») devient-elle la définition officielle du site ?
