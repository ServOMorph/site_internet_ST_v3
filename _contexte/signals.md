# Signals — site_st   (MAJ 2026-10-22)

## Actions ouvertes
- [P1|ouvert] Trancher la refonte « humanisme numérique » : formule officielle (« Une IA humaniste est une IA au service de l'autonomie humaine… »), bloc « Un principe » sur l'accueil, mot « humanisme » dans les titres ; puis construire page « Notre approche », étiquettes de thème des fiches (Planète, Maîtrise, Humain), quiz à deux axes, glossaire enrichi
  - fait quand: décisions actées par l'utilisateur et éléments en maquette dans l'artefact de revue.
  - réf: `humanisme_numerique_ia.md`, artefact de revue, `roadmap_portail_ia.md` Phase 2.
- [P1|ouvert] Faire les contrôles manuels de `tests_manuels.md` sur téléphone réel (hero, animations, quiz, « Reprendre », transitions, arborescence), puis clore la phase 2 (thème C et accueil déjà validés)
  - fait quand: `tests_manuels.md` vidé et Phase 2 marquée [FAIT] dans la roadmap.
  - réf: `tests_manuels.md`, `roadmap_portail_ia.md` Phase 2.
- [P2|ouvert] Trancher le nom de la section « Fiches » (l'utilisateur n'aime pas le mot ; proposition « Questions », « En pratique » écarté car déjà pris par la nouvelle section) et l'URL `/fiches/` ; le mot est dans la navigation, la page Sources et les gabarits (occurrences non recensées)
  - fait quand: nom et URL choisis, puis appliqués partout.
  - réf: `src/fiches/index.njk`, `src/_includes/base.njk`, `src/_data/fiches.json`.
- [P2|ouvert] Corriger `humanisme_numerique_ia.md` avant publication : source 6 = conférence 2025 (pas 2026), principe 6 non attribuable au Manifeste de Vienne (dépendance cognitive et « moments sans IA » absents), phrase « version grand public » présentée comme citation mais non vérifiée
  - fait quand: document corrigé, citations limitées à ce qui est vérifié, Springer vérifié ou retiré.
  - réf: `humanisme_numerique_ia.md`, Manifeste de Vienne (PDF TU Wien), page UNESCO.
- [P2|ouvert] Définir le gabarit d'entrée et l'alimentation des sections « En pratique » (pratiques de SérénIATech, à fournir par l'utilisateur), « Actualités » (veille à mettre en place, publication manuelle d'abord) et « Événements » ; pages actuellement « Contenu à venir » ; ne publier aucune entrée inventée
  - fait quand: gabarit d'entrée en maquette et premières entrées réelles fournies, ou décision de masquer les cartes tant qu'elles sont vides.
  - réf: `src/en-pratique/`, `src/actualites/`, `src/evenements/`, `roadmap_portail_ia.md` Phase 3.
- [P2|ouvert] Mettre à jour `cadrage_phase1.md` pour la nouvelle arborescence (Explorer supprimé, Comprendre 7 cartes, Fiches, Quiz, En pratique, Actualités, Événements, Sources, Glossaire, À propos) et trancher l'URL `/parcours/` ou `/comprendre/`
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
  - réf: `_contexte/contexte.md` (hébergement V2), V2 `render.yaml`, `server.js`.

## Contexte chaud
- Artefact de revue du site (URL stable) : https://claude.ai/artifact/J4AEiAdJgip9J1Y6WetTZg (version 20, publiée cette session). Republier : `npm run build`, `node scripts/build_revue.js`, republier `revue/revue_site.html`. Base lue en fin de session : 9 commentaires tous traités ; questions restantes : q1 (répondue), q3 (non répondue).
- Serveur local : `python run.py` (port fixe 8765, Eleventy en rechargement automatique).
- Génération d'images : ComfyUI-Qwen sur `http://127.0.0.1:8189` (`D:\ServOMorph\ComfyUI-Qwen`, `lancer.bat`), `scripts/gen_theme_c.py` (thème C, dont `en-pratique`, `actualites`, `evenements`) ; lancé pendant la session et non arrêté à la clôture (la question de l'arrêter est restée sans réponse) : à arrêter si la VRAM est nécessaire. Un blocage de 45 min a été observé une fois (VRAM saturée) : redémarrer ComfyUI. Demander avant de lancer.
- Branche `archive/v3-direction-b` sur `bc53de8`. PNG Qwen non versionnés dans `src/assets/brut/` (dont `c/` et `propositions/`). `explorer.webp` n'est plus utilisée.
- Logo SéréniaTech repris du V2 (`assets/logo_optimized`), en pied de page et en favicon.
- Humanisme numérique : sources vérifiées par lecture = Manifeste de Vienne (mai 2019, phrase « shape technologies… » exacte), UNESCO Recommandation (nov. 2021). Non vérifiées : phrase de la version grand public, chapitre Springer.
- V2 reste en ligne jusqu'à la bascule ; il affiche encore les badges « Flux.1 » / « Ollama local » (non modifié, à votre décision). `.env` V2 non lu.

## Dernière session (2026-10-22)
# Session du 2026-10-22

## Décisions prises
- Accueil : la carte « Dernière fiche » devient « En pratique » (pratiques de SérénIATech) ; deux cartes pleine largeur « Actualités » et « Événements » (hauteur 7 rem, image à gauche) sous la grille ; accueil validé par l'utilisateur.
- Fiches reste dans la navigation, sans carte d'accueil ; le mot « fiche » déplaît à l'utilisateur (renommage à trancher).
- Veille d'actualité à mettre en place plus tard ; hero : hauteur minimale supprimée (hauteur = texte).

## Livrables produits ou modifiés
- `src/index.njk`, `src/assets/css/app.css`, `scripts/gen_theme_c.py` : modifiés ; `src/en-pratique/`, `src/actualites/`, `src/evenements/` (pages « Contenu à venir ») et 3 images Qwen (`en-pratique`, `actualites`, `evenements`) : créés ; tests OK (20 pages)
- Artefact de revue republié (version 20) ; `roadmap_portail_ia.md`, `tests_manuels.md` : mis à jour

## Hypothèses validées / invalidées
- VALIDE : accueil et images validés à l'écran par l'utilisateur ; `scripts/test_phase2.js` OK.
- INVALIDE : « En pratique » comme nouveau nom de la section Fiches (contenu différent) -> section dédiée aux pratiques.
- EN ATTENTE : nom de la section « Fiches » ; formule officielle ; contenus des trois nouvelles sections ; contrôles sur téléphone réel.

## Prochaine étape exacte
Faire valider la formule officielle et corriger `humanisme_numerique_ia.md`, trancher le nom de « Fiches », puis construire « Notre approche », les thèmes de fiches et le quiz à deux axes.

## Question bloquante pour la session suivante
Votre formule (« Une IA humaniste est une IA au service de l'autonomie humaine… ») devient-elle la définition officielle du site ?
