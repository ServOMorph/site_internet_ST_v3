# Signals — site_st   (MAJ 2026-11-14)

## Actions ouvertes
- [P1|ouvert] Relecture juridique de `/mentions-legales/` et `/confidentialite/` par l'utilisateur en préproduction (base « intérêt légitime », Google et Vercel nommés comme prestataires, transferts hors UE, téléphone de l'hébergeur = ligne de l'agent DMCA de Vercel, validée par lui) ; facultatif : déclarer l'exemption d'accessibilité sur demarche.numerique.gouv.fr
  - fait quand: relecture faite par l'utilisateur et corrections éventuelles appliquées.
  - réf: `src/mentions-legales/index.njk`, `src/confidentialite/index.njk`, `tests_manuels.md`.
- [P1|ouvert] Mise en ligne de la V1 sur serenia-tech.fr, sur instruction explicite de l'utilisateur : redirections V2 vers V3 (liste des anciennes URL à établir), bascule du domaine (remplace la V2 en ligne), puis signaler la mise en ligne à la session Business pour qu'elle passe S-08 à FAIT (la session Business s'est close : message à envoyer à sa réouverture ou via l'utilisateur)
  - fait quand: site V3 servi sur serenia-tech.fr, redirections testées, Business informée.
  - réf: `vercel.json`, `roadmap_portail_ia.md` Phase 5, Business `site_maj_a_transmettre.md` (S-08).
- [P2|ouvert] Préparer les CGV avant la première vente (offres réservées aux structures, aucune vente en ligne sur le site) avec le référentiel tarifaire ; confirmer par un juriste ou la DGCCRF qu'aucun médiateur de la consommation n'est requis pour une clientèle de structures (textes complets non lus : `economie.gouv.fr` en 403)
  - fait quand: CGV rédigées et validées par l'utilisateur, ou décision actée de s'en passer.
  - réf: `src/se-former/index.njk`, `_contexte/contexte.md` (décision du 2026-11-14).
- [P2|ouvert] Confirmer le lien du Manifeste de Vienne (`https://caiml.org/dighum/dighum-manifesto/`, carte 8, répond 200, contenu non lu) sur téléphone ; l'ancien domaine `dighum.ec.tuwien.ac.at` ne répond plus
  - fait quand: lien ouvert par l'utilisateur et conforme, ou retiré de `src/_data/parcours.json`.
  - réf: `src/_data/parcours.json`, `tests_manuels.md`.
- [P3|ouvert] Après la mise en ligne : contrôles restants de `tests_manuels.md` (Comprendre, quiz, transitions, Ressources, À propos, arborescence, illustrations), puis clore la phase 2
  - fait quand: `tests_manuels.md` vidé et Phase 2 marquée [FAIT] dans la roadmap.
  - réf: `tests_manuels.md`, `roadmap_portail_ia.md` Phase 2.
- [P3|ouvert] Améliorer les images en fond des offres de la page Formations : elles doivent occuper tout le cadre de chaque offre (demande de l'utilisateur, 2026-11-13) ; voile et `object-fit` à revoir
  - fait quand: images en plein cadre validées sur téléphone.
  - réf: `src/assets/css/app.css` (`.offre`, `.offre__img`), `src/se-former/index.njk`.
- [P3|ouvert] Refonte « humanisme numérique » reportée hors V1 : page « Notre approche », étiquettes de thème des fiches, quiz à deux axes, glossaire enrichi ; la formule officielle est appliquée (bloc « Un principe » de l'accueil, S-08)
  - fait quand: décision de reprendre la refonte actée et éléments en maquette dans l'artefact de revue.
  - réf: `humanisme_numerique_ia.md`, artefact de revue, `roadmap_portail_ia.md` Phase 2.
- [P3|ouvert] Compléter le reste du contenu V2 (services, portfolio) et définir le gabarit des sections « Actualités » et « Événements » (retirées de la barre et de l'accueil, pages encore présentes mais non liées) ; aucune entrée inventée
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
- [P3|ouvert] Règle de journal de session demandée par le kit VibeObs (message du 2026-11-14) et appliquée avec l'accord de l'utilisateur : suivre sa première utilisation au prochain `/start` et `/close`, signaler à VibeObs les écarts
  - fait quand: un cycle `/start` puis `/close` complet a utilisé le journal sans écart.
  - réf: `.claude/CLAUDE.md` (Spécificités projet), `.claude/commands/close.md`, `.claude/commands/start.md`, `_contexte/journal_session.md`.

## Contexte chaud
- Préproduction : projet Vercel `site-internet-st-v3`, URL https://site-internet-st-v3.vercel.app/, relié au dépôt GitHub `ServOMorph/site_internet_ST_v3` (branche `main`, redéploiement à chaque push), réglages dans `vercel.json` (build `npm run build`, sortie `dist/`). Un autre projet Vercel, `sereniatech`, sert `serenia-tech.fr`, `www.serenia-tech.fr` et `sereniatech.vercel.app` en Production (capture de l'utilisateur ; probablement la V2, non confirmé) : ne jamais le relier au dépôt V3 avant la bascule voulue. Netlify écarté (`netlify.toml` conservé).
- Session « Business SerenIA Tech » close le 2026-11-13 : S-08 (périmètre V1) lui a été rendu compte ; l'utilisateur poursuit la mise en ligne directement avec cette session. Demandes de Business autorisées d'avance (`.claude/memory.md`).
- Contrôle visuel sans extension navigateur : Chrome headless depuis `C:\Program Files\Google\Chrome\Application\chrome.exe`, avec une page enveloppe contenant une iframe de 375 px (la fenêtre minimale de Chrome rogne sinon la mise en page) ; l'animation du compteur est figée dans ces captures.
- Artefact de revue du site (URL stable) : https://claude.ai/artifact/J4AEiAdJgip9J1Y6WetTZg (version 23, non régénéré depuis le 2026-11-04). Artefact de revue des illustrations : https://claude.ai/artifact/RaK8TrUF322Nw8F6LZoH8X (vidé).
- Serveur local : `python run.py` (port 8765, sortie `dist/`). ComfyUI-Qwen (port 8189) arrêté ; `scripts/gen_theme_c.py <ids>` génère les illustrations.
- Chiffres éco : AIE 415 TWh (2024), environ 945 TWh (2030) ; +17 % en 2025 et doublement d'ici 2030 lus sur le communiqué AIE du 16 avril 2026 (iea.org), qui ne donne pas le niveau de 2025 ; Epoch AI 0,3 Wh ; Arcep (21 mai 2026). Comparaison avec l'Allemagne et source BDEW retirées de la carte 1 ; phrase OpenAI (0,34 Wh) retirée de la carte 3.
- Humanisme numérique : source lue = Manifeste de Vienne (mai 2019). UNESCO Recommandation 2021 : texte officiel non lu. Non vérifiées : phrase de la version grand public, chapitre Springer.
- V2 reste en ligne jusqu'à la bascule. Branche `archive/v3-direction-b` sur `bc53de8`.

## Dernière session (2026-11-14)
# Session du 2026-11-14

## Décisions prises
- Périmètre V1 (S-08, ordre de l'utilisateur relayé par Business) appliqué : formule humaniste en bloc « Un principe », barre à 5 entrées (Formations ajoutée, Actualités et Événements retirées), mention « Maquette » retirée, pages Mentions légales et Confidentialité créées.
- Hébergeur retenu : Vercel (nouveau projet de préproduction) ; téléphone de Vercel Inc. = ligne de l'agent DMCA, gardé par l'utilisateur.
- Offres vendues uniquement à des structures : pas de médiateur de la consommation ; ligne « Formation individuelle : sur demande » retirée. Cartes de Comprendre relues et validées (cartes 1 et 3 corrigées).
- Règle de journal de session (demande VibeObs) appliquée avec l'accord de l'utilisateur.

## Livrables produits ou modifiés
- `src/` (accueil, `_includes/base.njk`, `mentions-legales/`, `confidentialite/`, `se-former/`, `assets/css/app.css`, `assets/js/compteur.js`, `_data/parcours.json`), `vercel.json`, `tests_manuels.md` : commités et poussés (dernier avant clôture : `c51d525`).
- `.claude/CLAUDE.md`, `.claude/commands/close.md` et `start.md`, `.gitignore`, `_contexte/journal_session.md` (gitignoré) : commités au /close.
- Build 23 pages et `npm test` : tous les contrôles passent.

## Hypothèses validées / invalidées
- VALIDE : +17 % et doublement d'ici 2030 lus sur iea.org ; contrôles sur iPhone réel de l'accueil, de la barre, de Formations, du contact et des pages légales ; compteur de l'accueil (réécrit en JS).
- INVALIDE : lien `dighum.ec.tuwien.ac.at` (domaine mort) -> remplacé par `caiml.org/dighum/dighum-manifesto/`, à confirmer.
- EN ATTENTE : relecture juridique par l'utilisateur ; bascule du domaine ; CGV ; avis d'un juriste sur le médiateur.

## Prochaine étape exacte
Attendre la relecture juridique de l'utilisateur, puis, sur son instruction, dresser la liste des redirections V2 vers V3 et basculer le domaine `serenia-tech.fr` du projet `sereniatech` vers `site-internet-st-v3`.

## Question bloquante pour la session suivante
Aucune
