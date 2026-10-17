# Inventaire du site V2
Source : `C:\Users\raph6\Documents\ServOMorph\site_internet_Sereniatech_V2` (lecture seule, `.env` non lu).
Méthode : extraction automatique des titres, balises title et meta description de chaque page. Le corps des textes n'a pas été relu : toute reprise de contenu exige une relecture page par page.

## Pages
| Page V2 | Contenu (titres) | Devenir proposé dans le portail |
|---|---|---|
| `index.html` | 3 domaines d'expertise (accompagnement informatique, IA éthique, automatisation), zone d'intervention, FAQ | Écran d'accueil du parcours ; services repris en cartes |
| `pages/about.html` | Philosophie, mission, valeurs, différenciation, histoire | Carte « Qui est derrière » (texte à réécrire à deux) |
| `pages/services.html` | 3 services détaillés (ce qu'on couvre, bénéfices) | Cartes services |
| `pages/formations.html` | 9 formations (Découvrir l'IA en 3 h, Claude, ChatGPT, NotebookLM, prompt, Perplexity, IA locale souveraine RGPD/AI Act, IA en pédagogie, piloter son entreprise avec l'IA), prise en charge possible | Parcours « Se former » ; reprise du catalogue |
| `pages/ressources.html` | Créer des images avec l'IA (méthode éco-responsable en 3 étapes, recette du prompt), outils (Vibe-Mistral, Ollama, Qwen-Image 2.1), comprendre l'IA (IA générative, empreinte écologique de l'IA, données), faire tourner une IA chez soi | Coeur du portail : parcours « Comprendre l'IA éco-responsable » |
| `pages/portfolio.html` | AutoClaude, « Quand l'IA explique l'IA aux Ados », créations IA locales (galerie) | Cartes réalisations |
| `pages/blog.html` + 3 articles | IA locale open source acte militant ; IA sur WhatsApp ; Wi-Fi satellite sans abonnement. Chaque article a une section « Sources factuelles » | Articles à garder en pages indexables ; l'article IA locale alimente le parcours éco-responsable |
| `pages/evenements.html`, `pages/1-jour-moins-numerique.html` | Événement « 1 jour moins numérique » le 8 novembre 2026 | Carte événement (date, lieu, titre seulement, accord du client) |
| `pages/contact.html` | Formulaire, prise de rendez-vous en ligne, coordonnées, FAQ | Écran contact ; backend `server.js` Express (SendGrid) sur Render |
| `pages/legal/` | Mentions légales, confidentialité RGPD, cookies, CGV (vente d'un guide) | À reprendre et mettre à jour (hébergement, outils, périmètre) |
| `403.html`, `404.html`, `500.html` | Pages d'erreur | À refaire dans le style appli |

## Autres éléments
- `data/galerie.json` : 4 images (Flux.1) avec titre, alt, prompt. Le badge « Ollama local » est associé à Flux.1 : à vérifier avant reprise, je n'ai pas contrôlé que c'est exact.
- `server.js`, `render.yaml`, `vercel.json`, `.htaccess`, `sitemap.xml`, `robots.txt` : base technique et SEO à reprendre. Le `.htaccess` suggère un ancien hébergement Apache (OVH, cf. `docs/deployment/GUIDE_DEPLOIEMENT_OVH.md`) : hébergement actuel à confirmer.
- `docs/guides/GUIDE_SEO_IA_SEARCH.md` et `docs/development/AUDIT_WEB_IA_2025.md` : travail existant sur la visibilité dans les recherches IA, à lire en phase 2.
- `docs/CHARTE_GRAPHIQUE_SérénIATech.md` : charte graphique V2, à lire avant de proposer une direction visuelle.
- `docs/guides/TARIFS.md`, `TEMOIGNAGES.md`, `GUMROAD_DESCRIPTION*` : contenus commerciaux ; les témoignages sont des données à contrôler avant toute publication.
- `Blog/*.md` : sources Markdown des articles ; `1_JOUR_MOINS_NUMERIQUE/` : zone-projet de l'événement du 8 novembre 2026.
- 91 fichiers image/vidéo non inventoriés un par un.

## Points d'attention
- Données personnelles : mentions légales et confidentialité contiennent des informations sur l'éditeur ; à reprendre après relecture, sans copier de secret.
- Témoignages et tarifs : ne rien publier sans accord explicite.
- L'événement du 8 novembre 2026 est proche (22 jours après la date du jour) : la V2 reste en ligne tant que le portail n'est pas prêt.
- URLs V2 à rediriger (301) pour préserver le référencement : `/pages/*.html` et `/pages/blog/*.html`.
