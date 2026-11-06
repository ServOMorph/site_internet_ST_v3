# Signals — site_st   (MAJ 2026-11-06)

## Actions ouvertes
- [P1|ouvert] Recueillir le retour de l'utilisateur sur les 8 cartes de Comprendre (texte en brouillon dans `src/_data/parcours.json` ; cartes 1, 4, 6, 7 et 8 retouchées le 2026-10-23, aucune validation formelle exprimée ; cartes 3 et 5 non relues) ; sourcer la définition de l'IA locale et les descriptions des outils (carte 7) si l'utilisateur le veut
  - fait quand: textes des 8 cartes validés par l'utilisateur.
  - réf: `src/_data/parcours.json`, `src/parcours/`, `roadmap_portail_ia.md` Phase 3.
- [P1|ouvert] Vérifier le +17 % (2025) et le doublement d'ici 2030 sur le communiqué ou le rapport AIE d'avril 2026 sur iea.org (non lu en source primaire : recoupé par la presse, une source donne 15 % et 485 TWh) ; chiffre affiché sur l'accueil, la carte « Pourquoi » et la page Sources
  - fait quand: chiffre lu sur iea.org et confirmé, ou texte corrigé.
  - réf: `src/index.njk`, `src/_data/parcours.json`, `src/sources/index.njk`.
- [P1|ouvert] Trancher la refonte « humanisme numérique » : formule officielle (« Une IA humaniste est une IA au service de l'autonomie humaine… »), bloc « Un principe » sur l'accueil ; puis construire page « Notre approche », étiquettes de thème des fiches (Planète, Maîtrise, Humain), quiz à deux axes, glossaire enrichi
  - fait quand: décisions actées par l'utilisateur et éléments en maquette dans l'artefact de revue.
  - réf: `humanisme_numerique_ia.md`, artefact de revue, `roadmap_portail_ia.md` Phase 2.
- [P1|ouvert] Faire les contrôles manuels de `tests_manuels.md` sur téléphone réel (accueil, nouvelles illustrations, bandeau des 3 témoignages, Formations, Ressources, contact, barre basse, Comprendre, quiz, transitions), puis clore la phase 2
  - fait quand: `tests_manuels.md` vidé et Phase 2 marquée [FAIT] dans la roadmap.
  - réf: `tests_manuels.md`, `roadmap_portail_ia.md` Phase 2.
- [P2|ouvert] Déployer le site complet sur Netlify (préproduction) : choisir entre dépôt Git relié (build par `netlify.toml`) et glisser-déposer de `dist/` ; trancher Netlify vs Vercel (roadmap phase 5) ; textes de Comprendre en brouillon et +17 % non lu sur iea.org, donc URL non publique. Le dossier autonome du guide agents (`dist_ressources_claudecode/`) est déjà déployé par l'utilisateur, avec l'ancien titre (non régénéré)
  - fait quand: site en ligne sur une URL Netlify de préproduction, ou décision d'hébergeur actée ; `npm run build:ressources-claudecode` relancé si le titre du guide doit être aligné.
  - réf: `netlify.toml`, `.eleventy.js`, `scripts/build_ressources_autonome.js`, `roadmap_portail_ia.md` Phase 5.
- [P2|ouvert] Compléter le reste du contenu V2 : services, portfolio ; page Formations rédigée (3 offres, tarifs S-07 fournis par la session Business) ; mention OPCO non reprise ; témoignage de Valérie ajouté
  - fait quand: pages services et portfolio rédigées au « je » avec accord de l'utilisateur.
  - réf: V2 `pages/services.html`, `pages/portfolio.html`, `docs/guides/TARIFS.md`, `inventaire_v2.md`, `roadmap_portail_ia.md` Phase 3.
- [P2|ouvert] Définir le gabarit d'entrée et l'alimentation des sections « Actualités » (veille, publication manuelle d'abord) et « Événements » ; pages « Contenu à venir » ; l'événement du 8 novembre est abandonné (rien à supprimer dans `src/`) ; aucune entrée inventée
  - fait quand: gabarit d'entrée en maquette et premières entrées réelles fournies, ou décision de masquer les cartes tant qu'elles sont vides.
  - réf: `src/actualites/`, `src/evenements/`, `roadmap_portail_ia.md` Phase 3.
- [P2|ouvert] Trancher le nom de la section « Fiches » (l'utilisateur n'aime pas le mot ; proposition « Questions ») et l'URL `/fiches/` ; section liée seulement depuis ses pages et la page Sources
  - fait quand: nom, URL et emplacement dans la navigation choisis, puis appliqués partout.
  - réf: `src/fiches/index.njk`, `src/_includes/base.njk`, `src/_data/fiches.json`.
- [P2|ouvert] Corriger `humanisme_numerique_ia.md` avant publication : source 6 = conférence 2025 (pas 2026), principe 6 non attribuable au Manifeste de Vienne, phrase « version grand public » présentée comme citation mais non vérifiée
  - fait quand: document corrigé, citations limitées à ce qui est vérifié, Springer vérifié ou retiré.
  - réf: `humanisme_numerique_ia.md`, Manifeste de Vienne (PDF TU Wien), page UNESCO.
- [P2|ouvert] Mettre à jour `cadrage_phase1.md` pour la nouvelle arborescence (Comprendre 8 cartes, Fiches, Quiz, En pratique, Actualités, Événements, Ressources, Sources, Glossaire, À propos, Formations ; en-tête à 6 entrées ; public = associations) et trancher l'URL `/parcours/` ou `/comprendre/`
  - fait quand: cadrage à jour et URL choisie.
  - réf: `cadrage_phase1.md`, `src/`.
- [P2|ouvert] Confirmer avec l'utilisateur la section Ressources : article « IA locale open source » sous `/ressources/` faute de section Blog décidée ; mention de cadrage absente des blocs « IA locale » et « images » ; URL unique `/ressources/`
  - fait quand: emplacement de l'article et mention des deux guides tranchés par l'utilisateur.
  - réf: `src/ressources/index.njk`, `src/_data/ressources.json`.
- [P2|ouvert] Compléter la lecture du guide SEO V2 (sections 2 à 5 et 7 non lues) avant de figer les gabarits SEO
  - fait quand: sections lues et points utiles reportés dans `cadrage_phase1.md`.
  - réf: V2 `docs/guides/GUIDE_SEO_IA_SEARCH.md`.
- [P3|ouvert] Décider du sort des phases 6 à 9 (mise à jour auto, veille IA locales, newsletter, extraits CreaZik) au regard du but « référence » : mon avis = garder la newsletter et la veille comme source de « Actualités », reconsidérer `site_com.md` et CreaZik
  - fait quand: décision actée dans la roadmap.
  - réf: `roadmap_portail_ia.md` phases 6 à 9.
- [P3|ouvert] Corriger l'hébergeur OVH dans les pages légales (V3) ; trancher Gmail vs SendGrid en lisant `server.js` V2 (phase 4) ; vérifier l'orthographe « SérénIA Tech » dans l'image du logo (non vérifiée) ; le contact actuel est un lien e-mail (À propos), pas un formulaire
  - fait quand: mentions légales V3 indiquent l'hébergeur réel ; messagerie du contact identifiée ; logo contrôlé.
  - réf: `_contexte/archive_decisions.md` (hébergement V2), V2 `render.yaml`, `server.js`, `src/assets/img/logo.webp`.
- [P3|ouvert] Backlog `/telephone` : aucune correction de format de l'utilisateur relevée dans cette session ; la commande a été copiée depuis VibeObs (`.claude/commands/telephone.md`)
  - fait quand: sans objet tant qu'aucune correction n'est exprimée.
  - réf: `.claude/commands/telephone.md`.

## Contexte chaud
- Artefact de revue du site (URL stable) : https://claude.ai/artifact/J4AEiAdJgip9J1Y6WetTZg (version 23, publiée le 2026-11-04, non régénéré depuis). Artefact de revue des illustrations : https://claude.ai/artifact/RaK8TrUF322Nw8F6LZoH8X (vidé, base `validations`), régénéré par `node scripts/build_revue_images.js` (listes TOUTES et ACTUELLES vides).
- Serveur local : `python run.py` (port 8765, sortie `dist/`). ComfyUI-Qwen (port 8189) arrêté ; `scripts/gen_theme_c.py <ids>` génère les illustrations (bruts non versionnés dans `src/assets/brut/c/`).
- Session « Business SerenIA Tech » : demandes autorisées d'avance (`.claude/memory.md`) ; a fourni positionnement, récit de marque, témoignages, offres de formations (S-07), titre du guide agents. Contact par e-mail `mailto:` ajouté dans À propos.
- Comparaisons de pays (carte 1) : Japon pour 945 TWh en 2030 (phrase AIE lue, résumé WebFetch) ; Allemagne pour 415 TWh en 2024 (environ 512 TWh bruts, estimation BDEW lue dans un résumé de recherche, non lue sur bdew.de ; rapport calculé par nous). Liens carte 8 : Arcep, CNIL, UNESCO ouverts ; TU Wien et `chat.mistral.ai` non ouverts ; page ADEME en erreur 403.
- Humanisme numérique : sources lues = Manifeste de Vienne (mai 2019), UNESCO Recommandation (nov. 2021, texte officiel non lu). Non vérifiées : phrase de la version grand public, chapitre Springer.
- Chiffres éco (sources secondaires) : AIE 415 TWh (2024), environ 945 TWh (2030), +17 % en 2025 ; Epoch AI 0,3 Wh ; Arcep (21 mai 2026). Source brésilienne divergente (15 %, 485 TWh) non retenue.
- V2 reste en ligne jusqu'à la bascule. Branche `archive/v3-direction-b` sur `bc53de8`.

## Dernière session (2026-11-06)
# Session du 2026-11-06

## Décisions prises
- Événement « 1 jour moins numérique » abandonné ; carte « Se former » renommée « Formations » (étiquette « Avec moi »), nom appliqué partout ; ressources reliées depuis la page Formations, chaque lien ouvrant seule la ressource ciblée avec liens vers les autres.
- Neuf illustrations Qwen validées par l'utilisateur via l'artefact et en place : atelier, conférence, formation de groupe, trois miniatures de ressources, cartes d'accueil Actualités, Événements, Formations, Quiz (l'image Quiz sert aussi la carte 6 de Comprendre).
- Guide agents : titre « économiser les tokens, donc l'énergie » ; dossier autonome `dist_ressources_claudecode/` généré ; offres de formations et tarifs (S-07), témoignage de Valérie, contact par e-mail repris de la session Business ; commande `/telephone` installée.

## Livrables produits ou modifiés
- `src/` (index, se-former, ressources, a-propos, en-pratique, base.njk, parcours.json, app.css, `assets/js/ouvrir-ancre.js`, 9 images) ; `scripts/` (gen_theme_c.py, build_ressources_autonome.js, build_revue_images.js) ; `package.json`, `.gitignore`, `tests_manuels.md`, `.claude/commands/telephone.md`, `revue/revue_images.html` : modifiés
- `npm test` : 21 pages, tous les contrôles passent.

## Hypothèses validées / invalidées
- VALIDE : build et `npm test` après remplacement des images.
- EN ATTENTE : rendu visuel des nouvelles images, page Formations, Ressources et contact sur téléphone réel (`tests_manuels.md`) ; dossier autonome déployé avec l'ancien titre.

## Prochaine étape exacte
Faire les contrôles manuels sur téléphone (accueil en premier), puis reprendre la relecture des cartes de Comprendre et trancher la formule humaniste.

## Question bloquante pour la session suivante
Votre formule (« Une IA humaniste est une IA au service de l'autonomie humaine… ») devient-elle la définition officielle du site ?
