# Changelog

## v0.5 — 2026-10-22

### Ajouté
- Accueil : carte « En pratique » (remplace « Dernière fiche ») et cartes pleine largeur « Actualités » et « Événements » ; pages `/en-pratique/`, `/actualites/`, `/evenements/` (« Contenu à venir ») ; 3 illustrations Qwen du thème C (`scripts/gen_theme_c.py`).

### Modifié
- Hero de l'accueil : hauteur adaptée au texte (hauteur minimale supprimée).
- Artefact de revue republié (version 20) ; `roadmap_portail_ia.md` et `tests_manuels.md` mis à jour.

## v0.4 — 2026-10-22

### Ajouté
- Thème C (sombre, feuille-circuit, vert néon, particules et animations CSS), 10 illustrations Qwen sur fond sombre dont « Garder la main », logo SéréniaTech (repris du V2) en pied de page et favicon.
- Pages Fiches (gabarit, pagination par 6), Quiz, Glossaire, Sources et méthode, À propos ; bloc « chiffre clé » animé sur l'accueil.
- `run.py` (serveur local, port 8765, rechargement automatique), `scripts/gen_theme_c.py`, `scripts/gen_propositions.py`, `humanisme_numerique_ia.md`.

### Modifié
- Titre du site : « IA éco-responsable et humaniste » ; parcours à 7 cartes (ajout de « Garder la main »), page réduite au bouton Commencer ; Explorer supprimé ; textes allégés ; mode sombre uniquement.
- Artefact de revue republié (version 19) ; `tests_manuels.md` réécrit.

## v0.3 — 2026-10-20

### Ajouté
- Socle 11ty (10 pages : accueil, parcours en 6 cartes, explorer, se former), gabarit mobile-first avec barre d'onglets, polices Inter et Space Grotesk hébergées, JS de 0,4 Ko, tests de phase 2.
- Direction visuelle expressive : 9 illustrations Qwen locales (`scripts/gen_illustrations.py`) et teinte par carte ; « Se former » en premier sur l'accueil.
- Artefact de revue du site (aperçu, commentaires, questions, bouton « Envoyer à Claude ») : `revue/`, `scripts/build_revue.js`.
- `tests_manuels.md`, `_contexte/archive_decisions.md`, `_contexte/archive_sessions.md`.

## v0.2 — 2026-10-17

### Modifié
- Pivot vers un portail IA éco-responsable façon appli ; ancien travail archivé (branche `archive/v3-direction-b`), code retiré de `main`.
- Roadmap en 10 phases (`roadmap_portail_ia.md`) ; phase 1 terminée.

### Ajouté
- `cadrage_phase1.md` (arborescence, arbitrage immersion/SEO, budget de poids), `inventaire_v2.md`, `.claude/memory.md`.
- Décisions validées : tarifs, témoignage Réseau Toiles, mention OPCO, suppression des badges de galerie, sources chiffrées retenues.

## v0.1 — 2026-10-15

### Ajouté
- Socle 11ty (direction B), collections, sitemap, robots.txt, JSON-LD, tests de phase 1 (code archivé).
