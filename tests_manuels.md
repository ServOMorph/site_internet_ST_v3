# Tests manuels en attente

## Accueil et thème sombre (téléphone réel)
- Hero : le recadrage mobile de la feuille, la lisibilité du titre sur l'image et la hauteur réduite du hero (sans boutons).
- Carte chiffre : « 17 % » reste sur une seule ligne, texte et source (AIE, avril 2026) lisibles.
- Animations : particules de fond, zoom lent du hero, compteur « 415 TWh », apparition des cartes au défilement, fluidité sur un vrai téléphone.
- Avec « réduire les animations » activé dans le système : aucune animation ne se joue et le chiffre affiche 415.

## En-tête et Comprendre (téléphone réel et PC)
- Barre basse à 6 entrées (Accueil, Comprendre, En pratique, Quiz, Actualités, Événements) : libellés lisibles, rien de coupé ; sur PC, en-tête sans retour à la ligne.
- Page Comprendre : titre « Comprendre l'IA éco-responsable et humaniste » avec « éco-responsable » sur une seule ligne ; liste des 8 cartes.
- Cartes du parcours : bloc « Sources » en petit sous un filet, une source par ligne ; Précédent / Suivant / Sommaire ; lecture des textes en brouillon (retour de l'utilisateur en cours).

## Liens et mise en forme des cartes (téléphone réel)
- Carte 7 : ouvrir les liens Ollama, ComfyUI et Vibe-Mistral (`chat.mistral.ai`) et vérifier qu'ils mènent aux bons sites.
- Carte 8 : ouvrir les liens Formations, À propos (ancre `#contact`), Arcep, CNIL, UNESCO et TU Wien ; lisibilité de la liste de sites séparés par des retours à la ligne.
- Carte 6 : les trois étapes de la méthode s'affichent chacune sur leur ligne.

## Quiz
- Sur un téléphone et un navigateur de bureau : le conseil s'affiche au choix d'une réponse, la navigation au clavier fonctionne (focus visible).

## Transitions entre pages
- Sur un navigateur compatible, vérifier que le passage d'une page à l'autre est fluide (`@view-transition`).

## Arborescence
- Parcourir Accueil (dont les cartes En pratique, Actualités et Événements, sur téléphone réel), Comprendre, Fiches, Quiz et les liens du pied de page (Sources, Glossaire, À propos, Formations) ; vérifier que rien ne manque ou ne prête à confusion.

## Accueil : bandeau et cartes (téléphone réel)
- Bandeau « Ils en parlent » : lisibilité des trois témoignages sur l'image de fond (bulles derrière le texte), une colonne sur téléphone, deux colonnes sur PC avec le dernier (Réseau Toiles) en pleine largeur.
- Page Formations : bloc « Pour aller plus loin » lisible ; chaque lien ouvre `/ressources/` avec seule la ressource choisie dépliée et, en bas, « Les autres ressources » (sans la ressource courante) ; `/ressources/` sans ancre affiche les trois blocs.
- Quatre cartes (Comprendre, En pratique, Quiz, Formations) : même hauteur, étiquette et titre alignés ; accroche sous le titre lisible.

## Nouvelles illustrations (téléphone réel et PC)
- Accueil : cartes Actualités, Événements, Quiz et Formations avec leurs nouvelles images ; Comprendre, carte 6 : image Quiz mise à jour.
- Page Formations : images atelier, conférence et formation (flottantes à droite, sans déborder) ; Ressources : miniatures des trois titres lisibles.

## Ressources, À propos, En pratique (téléphone réel et PC)
- `/ressources/` : les trois blocs se déplient sans second clic, sous-blocs imbriqués lisibles, blocs de code et liens sans débordement horizontal.
- À propos : texte long (parcours, anecdote, indépendance) lisible ; En pratique : listes lisibles.
- Page Formations : les trois offres (atelier, conférence, formation) et leurs prix sont lisibles sur téléphone, sans débordement.
- À propos, section Contact : le lien e-mail ouvre la messagerie du téléphone avec la bonne adresse ; depuis Formations, « écrivez-moi » mène à cette section.
