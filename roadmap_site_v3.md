# Roadmap — Refonte serenia-tech.fr (V3)
Objectif : mettre en ligne une vitrine d'art IA locale et éco-responsable (formations, portfolio, événements), puis automatiser sa mise à jour depuis les projets du PC ; tester VibeObs en parallèle.
Créée le : 2026-10-12

---

## Phase 1 — Socle 11ty et direction artistique [EN COURS]
- [x] Inventaire du V2 réutilisable (textes formations, mentions légales, assets, galerie IA, formulaire contact Express) — lecture seule, aucune copie de `.env`
- [x] Initialiser 11ty (zéro JS par défaut), structure contenus en Markdown (`content/projets/`, `content/formations/`, `content/evenements/`)
- [x] Proposer 3 directions artistiques (palette, typographie, principe visuel) ; choix utilisateur (B « Nuit de laboratoire »)
- [x] Générer un premier lot de visuels avec Qwen local selon la direction retenue (8 images dans `src/assets/brut/`, non intégrées au site)
- [ ] Maquette de l'accueil (faite sans images dans le site, avec images dans l'artefact claude.ai ; intégration WebP 640/1200 au site restante)
- [ ] Tests : build sans erreur, poids de page accueil mesuré, rendu mobile/desktop (Playwright) — fait : `npm test` (97 contrôles OK), mobile 390 et PC 1280 ; reste : poids avec images, rendu 1920 (voir `tests_manuels.md`)

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer. Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

---

## Phase 2 — Contenus MVP [TODO]
- [ ] Portfolio : TableauDeBord, JeGeekUtile, Appli_TSA_SDI_TDAH, AutoClaude, CreaZik_V3 (une fiche Markdown chacun, faits validés par l'utilisateur)
- [ ] Formations : présentation simple, reprise du catalogue V2
- [ ] Événements : atelier Espace L'Invariable du 17 octobre 2026 (date, lieu, titre uniquement)
- [ ] Contact (backend Express Render existant), mentions légales, confidentialité, cookies
- [ ] Tests : liens internes, SEO de base (title, meta, sitemap), accessibilité contraste/clavier

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer. Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

---

## Phase 3 — Mise en ligne sur serenia-tech.fr [TODO]
- [ ] Projet Vercel relié au dépôt V3 (préproduction d'abord)
- [ ] Redirections 301/308 des anciennes URLs V2 vers les nouvelles (préserver le SEO)
- [ ] Bascule du domaine serenia-tech.fr, V2 conservé en repli
- [ ] Tests manuels : formulaire contact en production, Search Console, redirections (ajoutés à `tests_manuels.md`)

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer. Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

---

## Phase 4 — Commande de mise à jour automatique [TODO]
- [ ] Format `site_com.md` (fichier dédié par projet suivi, seule source lue)
- [ ] Commande `/maj_site` : détecte les `site_com.md` modifiés, produit un brouillon de contenu, publication seulement après validation
- [ ] Garde-fou : aucun scan de dossier client, aucune donnée nominative publiée
- [ ] Tests : JeGeekUtile (avancement projet) et un événement (atelier) passent de bout en bout

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer. Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

---

## Phase 5 — Veille IA locales [TODO]
- [ ] Process de détection des IA utilisées dans les projets récents
- [ ] Proposition de mise à jour de TableauDeBord, puis page « IA locales » du site générée depuis TableauDeBord
- [ ] Tests : une IA ajoutée dans un projet récent est détectée et proposée

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer. Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

---

## Phase 6 — Newsletter maison [TODO]
- [ ] Inscription avec double opt-in, lien de désinscription, stockage des adresses hors git
- [ ] Envoi (choix du canal selon délivrabilité), modèle d'édition
- [ ] Mise à jour de la politique de confidentialité
- [ ] Tests : inscription, confirmation, désinscription, envoi test

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer. Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

---

## Phase 7 — Extraits CreaZik [TODO]
- [ ] Vérification des droits de chaque morceau retenu
- [ ] Lecteur audio léger (pas de lecture automatique, fichiers compressés)
- [ ] Tests : lecture mobile/desktop, poids des fichiers

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer. Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

---

## Phase 8 — Capitalisation VibeObs [TODO]
- [ ] Remonter au kit les écarts constatés pendant le projet
- [ ] Rédiger `creation_superagent.md` à partir de ce qui a réellement fonctionné
