# Cadrage phase 1 — Portail IA éco-responsable
Date : 2026-10-17. Statut : VALIDÉ par l'utilisateur le 2026-10-17 (arborescence, une URL par carte, budget de poids, blog, formations, polices).
Sources relues (V2, lecture seule) : `pages/ressources.html`, `pages/blog/ia-locale-open-source.html`, `docs/CHARTE_GRAPHIQUE_SérénIATech.md`, `docs/guides/GUIDE_SEO_IA_SEARCH.md` (sections 1 et 6 seulement).

## 1. Constats de la relecture
- Ressources : trois blocs (créer des images avec méthode en 3 étapes + recette de prompt ; outils Vibe-Mistral, Ollama, Qwen-Image 2.1 ; comprendre l'IA via CNIL et Futura Sciences) puis « faire tourner une IA chez soi ». La méthode « écrire dans le Bloc-notes, reformuler avec Le Chat, puis générer » est le geste de sobriété concret du site : bon pivot du parcours.
- Article IA locale : structure en 6 questions, ton nuancé (« local ne veut pas dire magiquement conforme »). Point faible : les affirmations s'appuient surtout sur des blogs de prestataires (étiquettes airagent, quelllm, flowt, jamespot, twintransformation, delos) ; la liste « Sources factuelles » ne cite que CNIL et Ollama. À réécrire avec les sources primaires déjà retenues (AIE, Arcep, Epoch AI, CNIL).
- Aucun chiffre énergétique dans ces textes : les chiffres sourcés de `_contexte/contexte.md` sont nouveaux.
- Charte V2 : fond clair, vert d'eau `#A5C9CA`, texte `#1A1A1A`, Inter + Space Grotesk chargées depuis Google Fonts, mode sombre automatique, WCAG AA, `prefers-reduced-motion` respecté. Contrainte : le blanc sur `#A5C9CA` (bouton primaire de la charte) a un contraste faible, à vérifier avant reprise (non calculé ici).
- Guide SEO V2 : recommande intro factuelle, FAQ, Schema.org, cohérence schéma/contenu visible, cibles LCP < 2,5 s, INP < 200 ms, CLS < 0,1, images < 100 Ko, CSS critique inline, JS en `defer`. Les affirmations du type « sans E-E-A-T votre contenu sera ignoré » sont des opinions, pas des faits établis.

## 2. Arborescence proposée
Principe : chaque carte est une vraie page HTML avec son URL et son texte complet. Le JavaScript ne fait qu'ajouter les transitions et le parcours (amélioration progressive).

- Accueil : choix de trois entrées (Parcours guidé, Explorer, Se former)
- Parcours guidé « Comprendre l'IA éco-responsable » (6 cartes, suite linéaire, retour libre)
  1. Pourquoi : l'impact de l'IA, chiffres sourcés (AIE, Arcep, Epoch AI) avec limites
  2. Les leviers : modèles modestes, IA locale, sobriété d'usage
  3. Essayer : méthode éco-responsable en 3 étapes, recette du prompt
  4. Les outils : Vibe-Mistral, Ollama, Qwen-Image
  5. Données et souveraineté : RGPD, IA locale open source (reprise de l'article)
  6. Aller plus loin : formations et contact
- Explorer (cartes libres) : Comprendre, Essayer, Outils, Réalisations (AutoClaude, IA explique l'IA aux ados, galerie sans badge), Blog (3 articles), Événement « 1 jour moins numérique »
- Se former : catalogue des 9 formations, tarifs validés, mention OPCO
- Qui je suis ; Contact ; Mentions légales, confidentialité, cookies, CGV
- Fonctions des phases 6 à 10 : sections « IA locales », « Newsletter », « Extraits CreaZik » à placer dans Explorer plus tard

Questions ouvertes : le blog (articles datés, indexés) reste-t-il une section à part ? Les formations viennent-elles à la fin du parcours seulement ou aussi en entrée directe ? (je recommande les deux).

## 3. Arbitrage immersion / référencement (recommandation)
- Chaque carte = une URL, un `<h1>`, du texte dans le HTML servi, des liens `<a>` classiques. Le parcours guidé est un enchaînement de liens « suivant / précédent ».
- JS limité aux transitions entre cartes (View Transitions API si le navigateur la gère, sinon navigation normale) et à la mémorisation de la progression. Sans JS, tout reste lisible et navigable.
- Pas d'application monopage qui charge le contenu par JS : c'est le risque principal pour le référencement classique et pour les robots d'IA (l'affirmation que certains robots n'exécutent pas le JS est à vérifier avant de la publier).
- Conserver du V2 : intro factuelle par page, FAQ visible, Schema.org cohérent avec le texte, sitemap, robots, redirections 301 des anciennes URLs.

## 4. Budget de poids et éco-conception (proposition à valider)
Les valeurs ci-dessous sont des propositions, pas des mesures.
- Page de contenu : HTML + CSS + JS ≤ 100 Ko transférés (hors images) ; JS ≤ 20 Ko.
- Images : WebP ou AVIF, ≤ 100 Ko chacune (seuil du guide V2), `width`/`height` et `loading="lazy"`.
- Polices : hébergées sur le site (pas de Google Fonts), 1 famille variable ou polices système. Évite une requête tierce et un sujet RGPD.
- Pas de vidéo en lecture automatique, pas de bibliothèque d'animation : animations en CSS, désactivées avec `prefers-reduced-motion`.
- Mesures à l'étape 2 : poids réel par page et Core Web Vitals (LCP < 2,5 s, INP < 200 ms, CLS < 0,1).

## 5. Décisions validées (2026-10-17)
1. Arborescence du §2 retenue. Blog : section à part dans Explorer ; l'article IA locale garde sa propre URL et alimente la carte 5 ; les deux autres articles sous « Autres sujets ». Formations : entrée directe « Se former » et renvoi depuis la carte 6 ; un seul appel à l'action dans le parcours (dernière carte).
2. Une URL par carte, JavaScript en amélioration seulement.
3. Budget de poids du §4 retenu (à mesurer en phase 2).
4. Polices : Inter et Space Grotesk hébergées sur le site, une police variable chacune ; repli sur polices système pour le texte courant si le budget de 100 Ko ne tient pas (à mesurer en phase 2).
