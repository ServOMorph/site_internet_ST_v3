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

## Quiz
- Sur un téléphone et un navigateur de bureau : le conseil s'affiche au choix d'une réponse, la navigation au clavier fonctionne (focus visible).

## Transitions entre pages
- Sur un navigateur compatible, vérifier que le passage d'une page à l'autre est fluide (`@view-transition`).

## Arborescence
- Parcourir Accueil (dont les cartes En pratique, Actualités et Événements, sur téléphone réel), Comprendre, Fiches, Quiz et les liens du pied de page (Sources, Glossaire, À propos, Se former) ; vérifier que rien ne manque ou ne prête à confusion.
