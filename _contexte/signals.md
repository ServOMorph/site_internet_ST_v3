# Signals — site_st   (MAJ 2026-10-22)

## Actions ouvertes
- [P1|ouvert] Trancher la refonte « humanisme numérique » : formule officielle (« Une IA humaniste est une IA au service de l'autonomie humaine… »), bloc « Un principe » sur l'accueil, mot « humanisme » dans les titres ; puis construire page « Notre approche », étiquettes de thème des fiches (Planète, Maîtrise, Humain), quiz à deux axes, glossaire enrichi
  - fait quand: décisions actées par l'utilisateur et éléments en maquette dans l'artefact de revue.
  - réf: `humanisme_numerique_ia.md`, artefact de revue, `roadmap_portail_ia.md` Phase 2.
- [P1|ouvert] Faire les contrôles manuels de `tests_manuels.md` sur téléphone réel (hero, animations, quiz, « Reprendre », transitions), puis clore la phase 2 (direction visuelle thème C déjà validée)
  - fait quand: `tests_manuels.md` vidé et Phase 2 marquée [FAIT] dans la roadmap.
  - réf: `tests_manuels.md`, `roadmap_portail_ia.md` Phase 2.
- [P2|ouvert] Corriger `humanisme_numerique_ia.md` avant publication : source 6 = conférence 2025 (pas 2026), principe 6 non attribuable au Manifeste de Vienne (dépendance cognitive et « moments sans IA » absents), phrase « version grand public » présentée comme citation mais non vérifiée
  - fait quand: document corrigé, citations limitées à ce qui est vérifié, Springer vérifié ou retiré.
  - réf: `humanisme_numerique_ia.md`, Manifeste de Vienne (PDF TU Wien), page UNESCO.
- [P2|ouvert] Mettre à jour `cadrage_phase1.md` pour la nouvelle arborescence (Explorer supprimé, Comprendre 7 cartes, Fiches, Quiz, Sources, Glossaire, À propos) et trancher l'URL `/parcours/` ou `/comprendre/`
  - fait quand: cadrage à jour et URL choisie.
  - réf: `cadrage_phase1.md`, `src/`.
- [P2|ouvert] Compléter la lecture du guide SEO V2 (sections 2 à 5 et 7 non lues) avant de figer les gabarits SEO
  - fait quand: sections lues et points utiles reportés dans `cadrage_phase1.md`.
  - réf: V2 `docs/guides/GUIDE_SEO_IA_SEARCH.md`.
- [P2|ouvert] Ajouter l'événement « 1 jour moins numérique » (8 nov. 2026, seul événement concerné) à la V3 ; date, lieu et titre uniquement, avec accord du client
  - fait quand: fiche événement créée en phase 3.
  - réf: V2 `pages/1-jour-moins-numerique.html`, `pages/evenements.html`.
- [P3|ouvert] Décider du sort des phases 6 à 9 (mise à jour auto, veille IA locales, newsletter, extraits CreaZik) au regard du but « référence » : mon avis = garder la newsletter et la veille comme source de fiches, reconsidérer `site_com.md` et CreaZik
  - fait quand: décision actée dans la roadmap.
  - réf: `roadmap_portail_ia.md` phases 6 à 9.
- [P3|ouvert] Corriger l'hébergeur OVH dans les pages légales (V3) ; trancher Gmail vs SendGrid en lisant `server.js` V2 (phase 4)
  - fait quand: mentions légales V3 indiquent l'hébergeur réel ; messagerie du contact identifiée.
  - réf: `_contexte/contexte.md` (hébergement V2), V2 `render.yaml`, `server.js`.

## Contexte chaud
- Artefact de revue du site (URL stable) : https://claude.ai/artifact/J4AEiAdJgip9J1Y6WetTZg (version 19). Republier : `npm run build`, `node scripts/build_revue.js`, republier `revue/revue_site.html`. Commentaires tous traités ; questions restantes en base : q1 (répondue), q3 (non répondue).
- Serveur local : `python run.py` (port fixe 8765, Eleventy en rechargement automatique).
- Génération d'images : ComfyUI-Qwen sur `http://127.0.0.1:8189` (`D:\ServOMorph\ComfyUI-Qwen`, `lancer.bat`), `scripts/gen_theme_c.py` (thème C), `scripts/gen_propositions.py` ; arrêté en fin de session. Un blocage de 45 min a été observé (VRAM saturée) : redémarrer ComfyUI. L'utilisateur peut avoir besoin de la VRAM : demander avant de lancer.
- Branche `archive/v3-direction-b` sur `bc53de8`. PNG Qwen non versionnés dans `src/assets/brut/` (dont `c/` et `propositions/`). `explorer.webp` n'est plus utilisée.
- Logo SéréniaTech repris du V2 (`assets/logo_optimized`), en pied de page et en favicon.
- Humanisme numérique : sources vérifiées par lecture = Manifeste de Vienne (mai 2019, phrase « shape technologies… » exacte), UNESCO Recommandation (nov. 2021). Non vérifiées : phrase de la version grand public, chapitre Springer.
- V2 reste en ligne jusqu'à la bascule ; il affiche encore les badges « Flux.1 » / « Ollama local » (non modifié, à votre décision). `.env` V2 non lu.

## Dernière session (2026-10-22)
# Session du 2026-10-22

## Décisions prises
- Thème C validé (sombre, feuille-circuit, vert néon, particules) ; mode sombre uniquement.
- Titre du site : « IA éco-responsable et humaniste ».
- Arborescence : Comprendre (parcours en 7 cartes, ajout « Garder la main »), Fiches, Quiz ; Explorer supprimé ; Se former en carte d'accueil et pied de page ; Sources, Glossaire, À propos en pied.
- Peu de texte sur le site ; aucun rythme de fiches annoncé ; logo en pied de page.

## Livrables produits ou modifiés
- `src/`, CSS thème C, 16 pages (fiches, quiz, glossaire, sources, à propos), 10 illustrations, hero, logo : créés ou modifiés ; tests OK
- `run.py`, `scripts/gen_theme_c.py`, `scripts/gen_propositions.py`, `scripts/build_revue.js`, `humanisme_numerique_ia.md`, `tests_manuels.md` : créés ou modifiés
- Artefact de revue republié (v19) ; commentaires traités

## Hypothèses validées / invalidées
- VALIDE : budget de poids (4 à 5 Ko par page hors polices) ; rendu mobile et PC contrôlé à l'écran (accueil, fiche, parcours, carte 4).
- INVALIDE : titre du hero sur une ligne en mobile -> deux lignes ; document humanisme : source 6 datée 2026 (en fait 2025), principe 6 attribué au Manifeste.
- EN ATTENTE : quiz, glossaire, page Sources, animations sur téléphone réel ; formule officielle ; bloc « Un principe ».

## Prochaine étape exacte
Faire valider les décisions de la refonte humanisme et corriger le document, puis construire « Notre approche », les thèmes de fiches et le quiz à deux axes.

## Question bloquante pour la session suivante
Votre formule (« Une IA humaniste est une IA au service de l'autonomie humaine… ») devient-elle la définition officielle du site ?
