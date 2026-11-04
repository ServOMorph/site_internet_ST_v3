# Signals — site_st   (MAJ 2026-11-04)

## Actions ouvertes
- [P1|ouvert] Ajouter l'événement « 1 jour moins numérique » (8 nov. 2026, dans quatre jours) dans `/evenements/` de la V3 ; date, lieu et titre uniquement, avec accord du client
  - fait quand: entrée créée dans `/evenements/` et accord du client obtenu, ou décision de ne pas l'ajouter.
  - réf: V2 `pages/1-jour-moins-numerique.html`, `pages/evenements.html`, `src/evenements/index.njk`, `roadmap_portail_ia.md` Phase 3.
- [P1|ouvert] Recueillir le retour de l'utilisateur sur les 8 cartes de Comprendre (texte en brouillon dans `src/_data/parcours.json` ; cartes 1, 4, 6, 7 et 8 retouchées le 2026-10-23, aucune validation formelle exprimée ; cartes 3 et 5 non relues) ; fournir une illustration dédiée à « L'IA locale » (réutilise `outils.webp`) ; sourcer la définition de l'IA locale et les descriptions des outils (carte 7, sans source) si l'utilisateur le veut
  - fait quand: textes des 8 cartes validés par l'utilisateur, image dédiée en place.
  - réf: `src/_data/parcours.json`, `src/parcours/`, `roadmap_portail_ia.md` Phase 3.
- [P1|ouvert] Vérifier le +17 % (2025) et le doublement d'ici 2030 sur le communiqué ou le rapport AIE d'avril 2026 sur iea.org (non lu en source primaire : recoupé par la presse, une source donne 15 % et 485 TWh) ; chiffre affiché sur l'accueil, la carte « Pourquoi » et la page Sources
  - fait quand: chiffre lu sur iea.org et confirmé, ou texte corrigé.
  - réf: `src/index.njk`, `src/_data/parcours.json`, `src/sources/index.njk`.
- [P1|ouvert] Trancher la refonte « humanisme numérique » : formule officielle (« Une IA humaniste est une IA au service de l'autonomie humaine… »), bloc « Un principe » sur l'accueil ; puis construire page « Notre approche », étiquettes de thème des fiches (Planète, Maîtrise, Humain), quiz à deux axes, glossaire enrichi
  - fait quand: décisions actées par l'utilisateur et éléments en maquette dans l'artefact de revue.
  - réf: `humanisme_numerique_ia.md`, artefact de revue, `roadmap_portail_ia.md` Phase 2.
- [P1|ouvert] Faire les contrôles manuels de `tests_manuels.md` sur téléphone réel (accueil, bandeau des témoignages, cartes uniformisées, Ressources, À propos, barre basse, Comprendre, quiz, transitions), puis clore la phase 2 (thème C et accueil déjà validés)
  - fait quand: `tests_manuels.md` vidé et Phase 2 marquée [FAIT] dans la roadmap.
  - réf: `tests_manuels.md`, `roadmap_portail_ia.md` Phase 2.
- [P2|ouvert] Déployer sur Netlify (préproduction) : choisir entre dépôt Git relié (build par `netlify.toml`) et glisser-déposer de `dist/` ; trancher Netlify vs Vercel (roadmap phase 5) ; contact absent du site ; textes de Comprendre en brouillon et +17 % non lu sur iea.org, donc URL non publique
  - fait quand: site en ligne sur une URL Netlify de préproduction, ou décision d'hébergeur actée dans la roadmap.
  - réf: `netlify.toml`, `.eleventy.js`, `roadmap_portail_ia.md` Phase 5.
- [P2|ouvert] Reprendre le reste du contenu V2 : catalogue des 9 formations (page Se former encore en maquette), services, portfolio, tarifs et mention OPCO (validés le 2026-10-17, à ne publier qu'avec accord) ; témoignages du V2 non relus
  - fait quand: pages Se former, services et portfolio rédigées au « je » avec accord de l'utilisateur sur les tarifs.
  - réf: V2 `pages/formations.html`, `pages/services.html`, `pages/portfolio.html`, `docs/guides/TARIFS.md`, `inventaire_v2.md`, `roadmap_portail_ia.md` Phase 3.
- [P2|ouvert] Définir le gabarit d'entrée et l'alimentation des sections « Actualités » (veille à mettre en place, publication manuelle d'abord) et « Événements » ; pages actuellement « Contenu à venir » ; ne publier aucune entrée inventée (« En pratique » est rédigée)
  - fait quand: gabarit d'entrée en maquette et premières entrées réelles fournies, ou décision de masquer les cartes tant qu'elles sont vides.
  - réf: `src/actualites/`, `src/evenements/`, `roadmap_portail_ia.md` Phase 3.
- [P2|ouvert] Trancher le nom de la section « Fiches » (l'utilisateur n'aime pas le mot ; proposition « Questions ») et l'URL `/fiches/` ; Fiches n'est plus dans l'en-tête ni sur l'accueil : la section n'est liée que depuis ses propres pages et la page Sources
  - fait quand: nom, URL et emplacement dans la navigation choisis, puis appliqués partout.
  - réf: `src/fiches/index.njk`, `src/_includes/base.njk`, `src/_data/fiches.json`.
- [P2|ouvert] Corriger `humanisme_numerique_ia.md` avant publication : source 6 = conférence 2025 (pas 2026), principe 6 non attribuable au Manifeste de Vienne, phrase « version grand public » présentée comme citation mais non vérifiée
  - fait quand: document corrigé, citations limitées à ce qui est vérifié, Springer vérifié ou retiré.
  - réf: `humanisme_numerique_ia.md`, Manifeste de Vienne (PDF TU Wien), page UNESCO.
- [P2|ouvert] Mettre à jour `cadrage_phase1.md` pour la nouvelle arborescence (Explorer supprimé, Comprendre 8 cartes, Fiches, Quiz, En pratique, Actualités, Événements, Ressources, Sources, Glossaire, À propos ; en-tête à 6 entrées ; public = associations) et trancher l'URL `/parcours/` ou `/comprendre/`
  - fait quand: cadrage à jour et URL choisie.
  - réf: `cadrage_phase1.md`, `src/`.
- [P2|ouvert] Confirmer avec l'utilisateur la section Ressources : article « IA locale open source » placé sous `/ressources/` faute de section Blog décidée ; mention de cadrage (texte validé, cite Claude Code) absente des blocs « IA locale » et « images » ; URL unique `/ressources/` (pages dédiées supprimées à la demande de l'utilisateur, ce qui annule « une URL par partie »)
  - fait quand: emplacement de l'article et mention des deux guides tranchés par l'utilisateur.
  - réf: `src/ressources/index.njk`, `src/_data/ressources.json`.
- [P2|ouvert] Compléter la lecture du guide SEO V2 (sections 2 à 5 et 7 non lues) avant de figer les gabarits SEO
  - fait quand: sections lues et points utiles reportés dans `cadrage_phase1.md`.
  - réf: V2 `docs/guides/GUIDE_SEO_IA_SEARCH.md`.
- [P3|ouvert] Décider du sort des phases 6 à 9 (mise à jour auto, veille IA locales, newsletter, extraits CreaZik) au regard du but « référence » : mon avis = garder la newsletter et la veille comme source de « Actualités », reconsidérer `site_com.md` et CreaZik
  - fait quand: décision actée dans la roadmap.
  - réf: `roadmap_portail_ia.md` phases 6 à 9.
- [P3|ouvert] Corriger l'hébergeur OVH dans les pages légales (V3) ; trancher Gmail vs SendGrid en lisant `server.js` V2 (phase 4) ; vérifier l'orthographe « SérénIA Tech » dans l'image du logo (non vérifiée)
  - fait quand: mentions légales V3 indiquent l'hébergeur réel ; messagerie du contact identifiée ; logo contrôlé.
  - réf: `_contexte/archive_decisions.md` (hébergement V2), V2 `render.yaml`, `server.js`, `src/assets/img/logo.webp`.

## Contexte chaud
- Artefact de revue du site (URL stable) : https://claude.ai/artifact/J4AEiAdJgip9J1Y6WetTZg (version 23, publiée le 2026-11-04 via `npm run build`, `node scripts/build_revue.js`, `publish_files` sur `revue/revue_site.html`). Base commentaires/questions non relue (dernier état connu : 9 commentaires traités, q1 répondue, q3 non répondue).
- Serveur local : `python run.py` (port fixe 8765, sortie dans `dist/`). ComfyUI-Qwen (`D:\ServOMorph\ComfyUI-Qwen`, `lancer.bat`, port 8189) a été lancé le 2026-11-04 et tourne encore : le fermer pour libérer la VRAM ; `scripts/gen_bandeau.py` a généré `src/assets/img/temoignages.webp` (PNG brut non versionné).
- Session « Business SerenIA Tech » (dossier `...\SérénIATech_dev\Business`) : l'utilisateur autorise d'avance ses demandes (`.claude/memory.md`) ; elle a fourni le positionnement (S-01, public = associations), le récit de marque (S-02), les témoignages et la ressource agents IA. La règle « un seul bouton par page » n'est pas validée (S-05 en attente côté Business). Contact : aucun affichage pour l'instant.
- Ressources du V2 : page Ressources, 3 articles de blog (seul « IA locale open source » repris, réécrit), guides Gumroad/SEO/tarifs non publiés. Google Fonts et Google Analytics présents sur le V2, absents du V3. Article V2 attribuait à tort à la CNIL « un projet local demande du temps et des compétences » ; sources commerciales de l'article non reprises. Futura Sciences écarté (chiffres sans source). Source de la ressource agents : page du dossier client Marion-Pargade, lue en entier, aucune donnée de client trouvée.
- Comparaisons de pays (carte 1) : Japon pour 945 TWh en 2030 (phrase AIE lue, résumé WebFetch) ; Allemagne pour 415 TWh en 2024 (environ 512 TWh bruts, estimation préliminaire BDEW lue dans un résumé de recherche, non lue sur bdew.de ; rapport 415/512 calculé par nous, pas par l'AIE). Liens carte 8 : Arcep, CNIL, UNESCO ouverts ; TU Wien et `chat.mistral.ai` non ouverts ; page ADEME en erreur 403.
- Humanisme numérique : sources vérifiées par lecture/recherche = Manifeste de Vienne (mai 2019), UNESCO Recommandation (nov. 2021, texte officiel non lu). Non vérifiées : phrase de la version grand public, chapitre Springer.
- Chiffres éco (sources secondaires) : AIE 415 TWh (2024), environ 945 TWh (2030), +17 % en 2025 ; Epoch AI 0,3 Wh ; Arcep (21 mai 2026) : peu de transparence sur l'inférence. Source brésilienne divergente (15 %, 485 TWh) non retenue.
- V2 reste en ligne jusqu'à la bascule ; il affiche encore les badges « Flux.1 » / « Ollama local » (non modifié). `.env` V2 non lu. Branche `archive/v3-direction-b` sur `bc53de8`.

## Dernière session (2026-11-04)
# Session du 2026-11-04

## Décisions prises
- Positionnement (S-01) et récit de marque (S-02) appliqués : marque « SérénIA Tech », public = associations, ton « je » et vouvoiement, À propos réécrit (indépendance validée).
- Ressources V2 : guide images repris, article IA locale réécrit, liens CNIL repris, Futura écarté, appel « Me contacter » non repris ; section `/ressources/` en URL unique avec accordéons (pages dédiées supprimées).
- Témoignages Réseau Toiles et Jean Luc en bandeau sur l'accueil ; image de fond générée avec Qwen ; autorisation permanente des demandes de la session Business notée en mémoire projet.

## Livrables produits ou modifiés
- `src/` : site.json, index.njk (accroche, bandeau, étiquettes), a-propos, en-pratique, sources, se-former, base.njk, fiche.njk, parcours.json, app.css, `ressources/index.njk`, `_data/ressources.json`, `_includes/arbre.njk`, `img/temoignages.webp` ; `scripts/gen_bandeau.py`
- `roadmap_portail_ia.md`, `README.md`, `CHANGELOG.md` (v0.9), `tests_manuels.md`, `revue/revue_site.html` (artefact version 23) : mis à jour

## Hypothèses validées / invalidées
- VALIDE : build (21 pages) et `npm test` passent ; rendu de l'accueil vu avec Playwright à 1300 px (cartes uniformes, bandeau lisible).
- EN ATTENTE : rendu mobile, page `/ressources/`, À propos et En pratique non vus à l'écran ; accord écrit des auteurs de témoignages déclaré, non vu.

## Prochaine étape exacte
Ajouter l'événement du 8 novembre dans `/evenements/` avec l'accord du client, puis contrôler le rendu sur téléphone réel (`tests_manuels.md`) et fermer ComfyUI.

## Question bloquante pour la session suivante
Votre formule (« Une IA humaniste est une IA au service de l'autonomie humaine… ») devient-elle la définition officielle du site ?
