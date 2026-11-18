# Signals — site_st   (MAJ 2026-11-18)

## Actions ouvertes
- [P1|ouvert] Mise en ligne de la V1 sur serenia-tech.fr, sur instruction explicite de l'utilisateur : bascule du domaine (remplace la V2 en ligne) du projet Vercel `sereniatech` vers `site-internet-st-v3` (Settings > Domains, dans le tableau de bord Vercel : à guider clic par clic), puis tester la règle `www` vers apex et les redirections sur le domaine réel, puis signaler la mise en ligne à la session Business pour qu'elle passe S-08 à FAIT (la session Business s'est close : message à envoyer à sa réouverture ou via l'utilisateur ou la session `sereniatech_dev`)
  - fait quand: site V3 servi sur serenia-tech.fr, redirections testées sur le domaine, Business informée.
  - réf: `vercel.json`, `roadmap_portail_ia.md` Phase 5, Business `site_maj_a_transmettre.md` (S-08, dépôt `SérénIATech_dev` accessible uniquement via la session `sereniatech_dev`).
- [P2|ouvert] Contrôles manuels restants de `tests_manuels.md`, à reprendre à la prochaine session : « Accueil : bandeau et cartes », « Nouvelles illustrations », « Ressources, À propos, En pratique » ; vérifier aussi sur téléphone les derniers correctifs poussés et non validés (bandeau de témoignages : texte 15 px et signature 12 px ; ordre de « Pour aller plus loin » avec agents IA en dernier ; carte et page « Mon approche »), puis clore la phase 2
  - fait quand: `tests_manuels.md` vidé et Phase 2 marquée [FAIT] dans la roadmap.
  - réf: `tests_manuels.md`, `roadmap_portail_ia.md` Phase 2.
- [P2|ouvert] Préparer les CGV avant la première vente (offres réservées aux structures, aucune vente en ligne sur le site) avec le référentiel tarifaire ; confirmer par un juriste ou la DGCCRF qu'aucun médiateur de la consommation n'est requis pour une clientèle de structures (textes complets non lus : `economie.gouv.fr` en 403) ; la page V2 `/pages/legal/cgv.html` renvoie 404 en V3 : vérifier qu'aucun devis ou e-mail existant n'y renvoie
  - fait quand: CGV rédigées et validées par l'utilisateur, ou décision actée de s'en passer ; absence de lien vers l'ancienne page CGV confirmée par l'utilisateur.
  - réf: `src/se-former/index.njk`, `_contexte/contexte.md` (décisions du 2026-11-14).
- [P2|ouvert] Décider de la visibilité du dépôt GitHub `ServOMorph/site_internet_ST_v3`, public depuis l'origine (0 fork, 0 étoile) : le laisser public ou le passer en privé (à vérifier d'abord : le plan gratuit de Vercel déploie-t-il un dépôt privé ?) ; demander au support GitHub la purge de l'ancien commit `49ba297`, encore lisible par son identifiant malgré la réécriture d'historique du 2026-11-18
  - fait quand: visibilité décidée et appliquée, déploiement Vercel vérifié si privé, purge demandée ou écartée.
  - réf: `_contexte/contexte.md` (décision du 2026-11-18), Contexte chaud ci-dessous.
- [P3|ouvert] Mail Vercel du 2026-11-18 (« SerenIA-Tech » pas membre de l'équipe, déploiement bloqué) : repérer dans Vercel (Deployments) le projet et le commit refusés ; le compte GitHub SerenIA-Tech n'a aucun commit dans le dépôt V3, donc origine probable = autre projet de l'équipe (non confirmé)
  - fait quand: origine identifiée, et compte rattaché à Vercel (Account Settings > Authentication) ou pushs refaits depuis ServOMorph.
  - réf: Contexte chaud ci-dessous, tableau de bord Vercel.
- [P3|ouvert] Trancher le libellé « En pratique » : la carte d'accueil et la page disent « Mon approche » (option 1 retenue le 2026-11-14) mais la barre de navigation (`src/_includes/base.njk`) et le titre d'onglet de la page (`titre: "En pratique"`) disent encore « En pratique » ; l'URL `/en-pratique/` est inchangée
  - fait quand: libellé de la barre et du titre d'onglet décidé et appliqué, ou conservé volontairement.
  - réf: `src/_includes/base.njk`, `src/en-pratique/index.njk`, `src/index.njk`.
- [P3|ouvert] Facultatif : déclarer l'exemption d'accessibilité sur demarche.numerique.gouv.fr (mentionné dans la relecture juridique, non fait)
  - fait quand: déclaration faite par l'utilisateur ou décision de ne pas la faire.
  - réf: `src/mentions-legales/index.njk`.
- [P3|ouvert] Améliorer les images en fond des offres de la page Formations : elles doivent occuper tout le cadre de chaque offre (demande de l'utilisateur, 2026-11-13) ; voile et `object-fit` à revoir
  - fait quand: images en plein cadre validées sur téléphone.
  - réf: `src/assets/css/app.css` (`.offre`, `.offre__img`), `src/se-former/index.njk`.
- [P3|ouvert] Refonte « humanisme numérique » reportée hors V1 : page « Notre approche », étiquettes de thème des fiches, quiz à deux axes (le quiz actuel a été retiré le 2026-11-14 ; la question 3 « images ou vidéos » avait un conseil sans consigne pour « Souvent » ; sa page est récupérable dans git au commit `53990e1^`), glossaire enrichi ; la formule officielle est appliquée (bloc « Un principe » de l'accueil, S-08)
  - fait quand: décision de reprendre la refonte actée et éléments en maquette dans l'artefact de revue.
  - réf: `humanisme_numerique_ia.md`, artefact de revue, `roadmap_portail_ia.md` Phase 2.
- [P3|ouvert] Compléter le reste du contenu V2 (services, portfolio) et définir le gabarit des sections « Actualités » et « Événements » (retirées de la barre et de l'accueil, pages encore présentes mais non liées) ; aucune entrée inventée ; redirections en place : services V2 vers `/se-former/`, portfolio V2 en 404
  - fait quand: pages services et portfolio rédigées au « je » avec accord de l'utilisateur ; gabarit d'entrée en maquette et premières entrées réelles, ou décision de masquer les pages.
  - réf: V2 `pages/services.html`, `pages/portfolio.html`, `inventaire_v2.md`, `src/actualites/`, `src/evenements/`.
- [P3|ouvert] Trancher le nom de la section « Fiches » (proposition « Questions ») et l'URL `/fiches/` ; trancher l'URL `/parcours/` ou `/comprendre/` ; mettre à jour `cadrage_phase1.md` pour la nouvelle arborescence
  - fait quand: noms et URL choisis et appliqués partout ; cadrage à jour.
  - réf: `src/fiches/index.njk`, `src/_includes/base.njk`, `src/_data/fiches.json`, `cadrage_phase1.md`.
- [P3|ouvert] Corriger `humanisme_numerique_ia.md` avant publication : source 6 = conférence 2025 (pas 2026), principe 6 non attribuable au Manifeste de Vienne, phrase « version grand public » présentée comme citation mais non vérifiée ; sourcer la définition de l'IA locale et les descriptions des outils (carte 7) si l'utilisateur le veut
  - fait quand: document corrigé, citations limitées à ce qui est vérifié, Springer vérifié ou retiré.
  - réf: `humanisme_numerique_ia.md`, Manifeste de Vienne, page UNESCO.
- [P3|ouvert] Confirmer avec l'utilisateur la section Ressources : article « IA locale open source » sous `/ressources/` faute de section Blog décidée ; mention de cadrage absente des blocs « IA locale » et « images »
  - fait quand: emplacement de l'article et mention des deux guides tranchés par l'utilisateur.
  - réf: `src/ressources/index.njk`, `src/_data/ressources.json`.
- [P3|ouvert] Compléter la lecture du guide SEO V2 (sections 2 à 5 et 7 non lues) avant de figer les gabarits SEO
  - fait quand: sections lues et points utiles reportés dans `cadrage_phase1.md`.
  - réf: V2 `docs/guides/GUIDE_SEO_IA_SEARCH.md`.
- [P3|ouvert] Décider du sort des phases 6 à 9 (mise à jour auto, veille IA locales, newsletter, extraits CreaZik) : mon avis = garder la newsletter et la veille comme source de « Actualités », reconsidérer `site_com.md` et CreaZik
  - fait quand: décision actée dans la roadmap.
  - réf: `roadmap_portail_ia.md` phases 6 à 9.
- [P3|ouvert] Contact : le contact actuel est un lien e-mail (À propos), pas un formulaire (phase 4 : trancher Gmail vs SendGrid en lisant `server.js` V2 si un formulaire est repris) ; vérifier l'orthographe « SérénIA Tech » dans l'image du logo (non vérifiée)
  - fait quand: décision formulaire ou lien e-mail définitif actée ; logo contrôlé.
  - réf: V2 `render.yaml`, `server.js`, `src/assets/img/logo.webp`.
- [P3|ouvert] Prix de la page Formations : retirés en attendant le réalignement de la grille avec le référentiel tarifaire ; les rétablir seulement sur demande de Business ; classe CSS `.offre__prix` inutilisée
  - fait quand: grille alignée transmise par Business (prix rétablis) ou « Tarif sur devis » confirmé comme définitif (classe CSS supprimée).
  - réf: `src/se-former/index.njk`, `src/assets/css/app.css`, `.claude/memory.md` (autorisation Business).
- [P3|ouvert] Backlog `/telephone` : aucune correction de format relevée dans cette session ; la commande a été copiée depuis VibeObs (`.claude/commands/telephone.md`)
  - fait quand: sans objet tant qu'aucune correction n'est exprimée.
  - réf: `.claude/commands/telephone.md`.
- [P3|ouvert] Règle de journal de session (demande VibeObs) : premier cycle `/start` puis `/close` mené le 2026-11-14 avec un écart à signaler à VibeObs : le journal n'a reçu que 10 lignes, et de nombreuses modifications de contenu (page En pratique, « Mon approche », témoignages, sources, titres de Formations, ordre des liens) n'y ont pas été écrites au moment de l'événement ; la synthèse a été reconstituée depuis la conversation ; même constat le 2026-11-18 (une seule ligne au journal)
  - fait quand: écart signalé à VibeObs et un cycle complet réalisé sans écart.
  - réf: `.claude/CLAUDE.md` (Spécificités projet), `.claude/commands/close.md`, `.claude/commands/start.md`, `_contexte/journal_session.md`.

## Contexte chaud
- Préproduction : projet Vercel `site-internet-st-v3`, URL https://site-internet-st-v3.vercel.app/, relié au dépôt GitHub `ServOMorph/site_internet_ST_v3` (branche `main`, redéploiement à chaque push), réglages et redirections 308 V2 vers V3 dans `vercel.json` (testées sur la préproduction ; la règle `www` vers apex ne joue qu'après la bascule). Un autre projet Vercel, `sereniatech`, sert `serenia-tech.fr`, `www.serenia-tech.fr` et `sereniatech.vercel.app` en Production (capture de l'utilisateur ; probablement la V2, non confirmé) : ne jamais le relier au dépôt V3 avant la bascule voulue. Netlify écarté (`netlify.toml` conservé).
- Session « Business SerenIA Tech » close le 2026-11-13 : S-08 (périmètre V1) lui a été rendu compte ; l'utilisateur poursuit la mise en ligne directement avec cette session. Demandes de Business autorisées d'avance (`.claude/memory.md`).
- Contrôle visuel sans extension navigateur : Chrome headless depuis `C:\Program Files\Google\Chrome\Application\chrome.exe`, avec une page enveloppe contenant une iframe de 375 px (la fenêtre minimale de Chrome rogne sinon la mise en page) ; l'animation du compteur est figée dans ces captures.
- Artefact de revue du site (URL stable) : https://claude.ai/artifact/J4AEiAdJgip9J1Y6WetTZg (version 23, non régénéré depuis le 2026-11-04 : ne reflète plus le site ; la règle de publication de `.claude/memory.md` n'a pas été appliquée pendant la session du 2026-11-14). Artefact de revue des illustrations : https://claude.ai/artifact/RaK8TrUF322Nw8F6LZoH8X (vidé).
- Serveur local : `python run.py` (port 8765, sortie `dist/`). Le build 11ty ne vide pas `dist/` : supprimer à la main un dossier retiré (ex. `dist/quiz/`) avant `npm test`. ComfyUI-Qwen (port 8189) arrêté ; `scripts/gen_theme_c.py <ids>` génère les illustrations.
- Chiffres éco : AIE 415 TWh (2024), environ 945 TWh (2030) ; +17 % en 2025 et doublement d'ici 2030 lus sur le communiqué AIE du 16 avril 2026 (iea.org), qui ne donne pas le niveau de 2025 ; Epoch AI 0,3 Wh ; Arcep (21 mai 2026). Comparaison avec l'Allemagne et source BDEW retirées de la carte 1 ; phrase OpenAI (0,34 Wh) retirée de la carte 3.
- Humanisme numérique : source lue = Manifeste de Vienne (mai 2019 ; lien `caiml.org` confirmé par l'utilisateur le 2026-11-14). UNESCO Recommandation 2021 : texte officiel non lu. Non vérifiées : phrase de la version grand public, chapitre Springer. Non vérifié dans les sources : l'exclusion des images des estimations citées (texte du conseil du quiz retiré).
- V2 reste en ligne jusqu'à la bascule. Branche locale `archive/v3-direction-b` sur `6391718` (réécrite, absente de GitHub).
- Dépôt GitHub public. Historique réécrit le 2026-11-18 (tarifs, chemin local et nom d'un lieu masqués) : les identifiants de commits cités avant cette date ne valent plus (quiz retiré au commit `53990e1`, dernier correctif de site `32c227f`). Sauvegarde de l'ancien dépôt : bundle dans le dossier temporaire de la session de 2026-11-18 (`...\scratchpad\site_st_avant_reecriture.bundle`), à copier si on veut la garder. `.claude/memory.md` n'est plus suivi par git (gitignore) mais garde ses vrais chemins sur le disque.
- Règles reçues de VibeObs : trois validations successives de l'utilisateur avant toute écriture dans un `CLAUDE.md`, `AGENTS.md` ou `GEMINI.md` ; aucun usage du GPU (Ollama, ComfyUI, torch CUDA, modèle local) sans jeton VRAM : `D:\ServOMorph\VertIA_v3\.venv\Scripts\python.exe D:\ServOMorph\VertIA_v3\_orchestrationram_lock.py acquire site_internet_v3 --wait` puis `ollama stop <modèle>` et `release site_internet_v3` (GPU mis en pause par l'utilisateur : code 7) ; aucune lecture ni écriture directe dans `SérénIATech_dev` (passer par la session `sereniatech_dev`).
- Mail Vercel du 2026-11-18 : compte GitHub SerenIA-Tech (créé le 2025-06-18, un seul dépôt public `blt`), sans commit dans le dépôt V3 ; déploiement V3 non concerné (dernier déploiement en succès, version en ligne comparée à un build local : identique).

## Dernière session (2026-11-18)
# Session du 2026-11-18

## Décisions prises
- Dossier `dist/` supprimé à la demande de l'utilisateur (demande Netlify faite par erreur : l'hébergeur est Vercel).
- Dépôt public examiné : aucune clé ni mot de passe ; à masquer = anciens tarifs, nom d'un lieu client, chemin local.
- Méthode « masquer les textes » retenue : historique réécrit (36 commits), force-push de `main` autorisé après sauvegarde ; `.claude/memory.md` retiré du suivi (restauré en local).
- Règles de VibeObs appliquées : trois validations avant d'écrire dans un `CLAUDE.md`, jeton VRAM avant tout GPU, pas d'accès direct à `SérénIATech_dev`.

## Livrables produits ou modifiés
- Historique git réécrit et poussé (`main` = `a2e3006` avant clôture) ; `.gitignore` (+ `.claude/memory.md`) ; bundle de sauvegarde dans le dossier temporaire de la session.
- `_contexte/`, `CHANGELOG.md` (v2.2) : commités au /close. Site inchangé : dernier déploiement Vercel en succès, `npm test` OK avant la réécriture.

## Hypothèses validées / invalidées
- VALIDE : version Vercel à jour (21 pages et CSS comparés au build local) ; 0 reste dans l'historique ; arbre identique hors 5 fichiers masqués.
- INVALIDE : le dépôt serait privé (public depuis l'origine).
- EN ATTENTE : origine du mail Vercel ; visibilité du dépôt ; purge GitHub de `49ba297` ; contrôles manuels restants ; bascule du domaine ; libellé de la barre.

## Prochaine étape exacte
Reprendre les contrôles manuels restants (bandeau, illustrations, Ressources, À propos, En pratique), puis, sur instruction explicite, guider la bascule de `serenia-tech.fr`.

## Question bloquante pour la session suivante
Le dépôt GitHub reste-t-il public ou passe-t-il en privé (après vérification du plan Vercel) ?
