# jeu_de_la_vie_John_Conway
Programmation du jeu de la vie de John Conway utilisant la bibliothèque pygame - Exemples du clignotant, glisseur, floraison, grenouille et canon (automates cellulaires). 

![image](https://user-images.githubusercontent.com/46868436/188279772-69e1992f-16c6-463b-8715-98a40e818918.png)

Le jeu de la vie a été inventé par le mathématicien John Conway en 1970. C'est le plus connu des automates cellaires.

L'objet de ce dépôt est de spécifier et implémenter ce jeu avec la bibliothèque Pygame.

Le jeu de la vie n'est pas à proprement parler un jeu avec des joueurs, mais une simulation qui se déroule sur une grille de cellules. 

Chaque cellule peut être vivante ou morte. Chaque cellule a 8 voisines (sauf les cellules du bordqui en ont 5 sur les bords et 3 sur les coins). L'état des cellules à un instant donné s'appelle une génération. La simulation calcule une nouvelle génération à partir de la génération courante à l'aide de deux règles simples : 
- Si une cellule vivante possède deux ou trois voisines vivantes, elle reste vivante, sinon elle meurt ;
- Si une cellule morte a exactement trois voisines vivantes, elle devient vivante, sinon elle reste morte. 

Certaines configurations de cellules donnent lieu à des comportements intéressants.Le plus simple est le clignotant : trois cellules alignées vont alterner entre un alignement vertical et un alignement horizontal. La plus connue est le glisseur, qui se reporduit identique à lui-même mais décalé d'une cellule en diagonale en quatre générations. La grenouille et la floraison sont directement inspirées de wikipédia : https://fr.wikipedia.org/wiki/Jeu_de_la_vie
