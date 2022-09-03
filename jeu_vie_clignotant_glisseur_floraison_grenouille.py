import numpy as np
import pygame
import sys
import time

# Liste des états
MORTE=0
VIENT_DE_MOURIR=1
VIVANTE=2
RESTE_VIVANTE=3

# Liste des couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 250)
GREEN = (0,127,0)
colors=[WHITE, RED, BLUE, GREEN]

# Grille
taille_x=20
taille_y=20
blockSize = 20 #Set the size of the grid block
WINDOW_HEIGHT = blockSize*taille_x
WINDOW_WIDTH = blockSize*taille_y

# Etat initial + quelques figures
cellules = np.zeros((taille_x, taille_y), dtype=int) # Ce tableau contient l'état des cellules

# On introduit quelques figures : clignotant, glisseur, floraison, grenouille
# Clignotant
cellules[1][1]=VIVANTE
cellules[1][2]=VIVANTE
cellules[1][0]=VIVANTE

# Glisseur
cellules[5][13]=VIVANTE
cellules[5][14]=VIVANTE
cellules[5][12]=VIVANTE
cellules[6][14]=VIVANTE
cellules[7][13]=VIVANTE

# Floraison
cellules[10][7]=VIVANTE
cellules[11][6]=VIVANTE
cellules[11][8]=VIVANTE
cellules[12][6]=VIVANTE
cellules[12][7]=VIVANTE
cellules[12][8]=VIVANTE
cellules[13][6]=VIVANTE
cellules[13][8]=VIVANTE
cellules[14][7]=VIVANTE

# Grenouille
cellules[16][16]=VIVANTE
cellules[16][17]=VIVANTE
cellules[17][16]=VIVANTE
cellules[17][17]=VIVANTE
cellules[15][17]=VIVANTE
cellules[18][16]=VIVANTE

# On introduit quelques fonctions utiles pour la suite

def est_dans_grille(i, j):
    """
    Vérifie si une cellule de coordonnées (i, j) est dans la grille
    """
    if i>=0 and j>=0 and i<taille_y and j<taille_y:
        return True
    else:
        return False


def nb_voisins_vivants(i, j):
    """
    Recherche le nombre de voisins vivants pour la cellule (i, j)
    """
    cpt=0
    if est_dans_grille(i-1, j-1):
        if cellules[i-1][j-1]>=VIVANTE:
            cpt+=1
    if est_dans_grille(i-1, j):
        if cellules[i-1][j]>=VIVANTE:
            cpt+=1
    if est_dans_grille(i-1, j+1):
        if cellules[i-1][j+1]>=VIVANTE:
            cpt+=1
    if est_dans_grille(i, j-1):
        if cellules[i][j-1]>=VIVANTE:
            cpt+=1
    if est_dans_grille(i, j+1):
        if cellules[i][j+1]>=VIVANTE:
            cpt+=1
    if est_dans_grille(i+1, j-1):
        if cellules[i+1][j-1]>=VIVANTE:
            cpt+=1
    if est_dans_grille(i+1, j):
        if cellules[i+1][j]>=VIVANTE:
            cpt+=1
    if est_dans_grille(i+1, j+1):
        if cellules[i+1][j+1]>=VIVANTE:
            cpt+=1
    return cpt  

def avance_generation():
    tab = np.zeros((taille_x, taille_y)) # Ce tableau contient le nombre de voisins vivants
    for i in range(taille_x):
        for j in range(taille_y):
            tab[i][j]=nb_voisins_vivants(i,j)

    for i in range(taille_x):
        for j in range(taille_y):
            anc_etat=cellules[i][j]
            if tab[i][j]==3 and cellules[i][j]<=VIENT_DE_MOURIR: # etat 0 ou 1 : mort ou vient de mourir
                cellules[i][j]=VIVANTE # etat 2 vivante
            elif (tab[i][j]==2 or tab[i][j]==3) and cellules[i][j]>=VIVANTE:
                cellules[i][j]=RESTE_VIVANTE
            else:
                cellules[i][j]=MORTE
            if anc_etat>=VIVANTE and cellules[i][j]==MORTE:
                    cellules[i][j]=VIENT_DE_MOURIR # recemment morte


def drawGrid():
    for i in range(taille_x):
        for j in range(taille_y):
            rect=pygame.Rect(i*blockSize, j*blockSize, blockSize, blockSize)
            pygame.display.get_surface().fill(colors[cellules[i][j]], rect)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)

  
pygame.init()
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Jeu de la vie')
SCREEN.fill(WHITE)

while True:
    drawGrid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    time.sleep(1)
    avance_generation()
