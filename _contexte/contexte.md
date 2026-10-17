# Contexte — site_st

## Objectif (immuable sauf décision explicite)
Portail vers l'IA éco-responsable pour serenia-tech.fr : un site qui ressemble à une appli (cartes à toucher, animations, parcours guidé et exploration libre) pour découvrir ce qu'est l'IA éco-responsable. Il intègre le contenu du site V2, réorganisé et réécrit avec l'utilisateur.

## Stack / contraintes techniques (stable, rarement modifié)
Stack de diffusion conservée : 11ty (site statique), HTML/CSS/JS, Express sur Render (contact), Vercel. Équilibre à trouver entre immersion (appli) et référencement classique + moteurs IA. Pas de PWA prévue. Mobile-first puis PC/télé.

## État actuel (réécrit intégralement à chaque /close)
Pivot du 2026-10-17 : portail IA éco-responsable façon appli. Ancien travail archivé (branche `archive/v3-direction-b`), code retiré de `main`.
Phase 1 (cadrage) terminée et validée : `cadrage_phase1.md`. Roadmap `roadmap_portail_ia.md` en 10 phases.
Phase suivante : 2 (socle et maquette). Aucun code V3 pour l'instant.
Les 8 PNG Qwen restent sur disque (`src/assets/brut/`, non versionnés), écartés.

## Décisions structurantes (append only — 10 entrées max, 5 lignes max/entrée, archiver au-delà)
- 2026-10-12 : Initialisation du protocole vibecoding.
- 2026-10-17 : Pivot vers un portail « IA éco-responsable » façon appli ; redémarrage à zéro, ancien travail archivé (branche `archive/v3-direction-b`). Visuels Qwen et direction B écartés.
- 2026-10-17 : Hypothèse de travail (validée) : public = curieux et professionnels découvrant l'IA locale ; objectif = comprendre l'IA éco-responsable puis découvrir les formations. Définition : IA locale, modèles modestes, sobriété d'usage (ex. écrire sa demande avant d'interroger l'IA), souveraineté des données.
- 2026-10-17 : Roadmap `roadmap_portail_ia.md` validée. Les anciennes fonctions (mise à jour automatique `site_com.md`, veille IA locales, newsletter, extraits CreaZik) sont intégrées au site, dans des phases ultérieures à ajouter. Source du contenu V2 : voir `.claude/memory.md`.
- 2026-10-17 : Sources retenues pour d'éventuels chiffres (lues via outil, à citer avec leur date et leurs limites) :
  - AIE, *Energy and AI* (2025) : centres de données ~415 TWh en 2024 (~1,5 % de l'électricité mondiale), ~945 TWh attendus en 2030 ; l'IA est le principal moteur de la hausse (pas de part chiffrée sur la page lue). https://www.iea.org/reports/energy-and-ai/executive-summary
  - Arcep, *IA générative : quels défis environnementaux ?* (21 mai 2026) : les plus grands modèles sont les plus gourmands, des modèles plus sobres peuvent répondre aussi bien ; manque de transparence des acteurs ; pas de valeur par requête sur la page lue. https://www.arcep.fr/la-regulation/grands-dossiers-thematiques-transverses/lempreinte-environnementale-du-numerique/le-rapport-intelligence-artificielle-generative-quels-defis-environnementaux.html
  - Epoch AI (7 fév. 2025) : ~0,3 Wh pour une requête texte GPT-4o typique, fourchette 0,1 à 4 Wh selon hypothèses ; estimation, pas une mesure, exclut images, voix, entraînement et fabrication. https://epoch.ai/gradient-updates/how-much-energy-does-chatgpt-use
  - Non lus en source primaire (à vérifier avant usage) : AI Energy Score (Hugging Face/Salesforce), étude Microsoft sur l'inférence (0,31 Wh médian), ADEME (aucune étude IA générative trouvée).
- 2026-10-17 : Chiffres et sources ci-dessus à publier (avec date et limites). Anciennes fonctionnalités intégrées en phases 6 à 10 de la roadmap.
- 2026-10-17 : Hébergement V2 constaté dans le dossier : frontend Vercel (`vercel.json`), backend Render (`sereniatech-backend`, région Frankfurt, offre gratuite), OVH = registrar du domaine uniquement (`CHANGELOG.md` V2). Le `README.md` V2 et les mentions légales citent encore OVH comme hébergeur : à corriger dans la V3. Événement « 1 jour moins numérique » (8 nov. 2026) à ajouter à la V3.
- 2026-10-17 : Validations utilisateur : tarifs de formation V2 repris tels quels (590 € HT découverte 3 h ; 1 190 € HT Claude/ChatGPT/NotebookLM/prompt/Perplexity ; 1 500 € HT IA locale ; 1 700 € HT pédagogie ; 2 400 € HT pilotage) ; autres prestations « sur devis », rien repris de `TARIFS.md` ; témoignage Réseau Toiles validé ; mention OPCO « sous conditions d'éligibilité » conservée (« ok sur tout »). Aucun témoignage fictif.
- 2026-10-17 : Galerie V2 (`data/galerie.json`, 4 images) : Ollama n'a pas été utilisé pour Flux.1 ; tous les badges (« Flux.1 », « Ollama local ») sont supprimés à la reprise dans la V3. V2 non modifié (le site V2 publié affiche encore ces badges).
- 2026-10-17 : Contenu réécrit à deux ; source éditoriale : `C:\Users\raph6\Documents\SerenIATech\SérénIATech_dev\Communication\SHORTS\prompts\TSERENIATECH_Prompt_Maitre_Production.docx` (série de 10 Shorts, règles de rigueur : pas d'affirmation absolue, pas de résultat inventé).
- 2026-10-17 : Cadrage phase 1 validé (`cadrage_phase1.md`) : parcours guidé 6 cartes + Explorer + Se former ; une URL HTML par carte, JS en amélioration ; budget page ≤ 100 Ko hors images, JS ≤ 20 Ko, images ≤ 100 Ko ; polices Inter/Space Grotesk hébergées (repli système si budget dépassé) ; blog à part, formations en entrée directe.
