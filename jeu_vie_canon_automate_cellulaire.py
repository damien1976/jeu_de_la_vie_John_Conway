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
colors=[WHITE, WHITE, BLACK, BLACK] # [WHITE, RED, BLUE, GREEN]

# Grille
taille_x=36
taille_y=15
blockSize = 20 #Set the size of the grid block
WINDOW_HEIGHT = blockSize*taille_y
WINDOW_WIDTH = blockSize*taille_x

# Etat initial + quelques figures
cellules = np.zeros((taille_x, taille_y), dtype=int) # Ce tableau contient l'état des cellules

# Canon (automate cellulaire)
cellules[0][4]=VIVANTE
cellules[1][4]=VIVANTE
cellules[0][5]=VIVANTE
cellules[1][5]=VIVANTE

cellules[10][4]=VIVANTE
cellules[10][5]=VIVANTE
cellules[10][6]=VIVANTE
cellules[11][7]=VIVANTE
cellules[12][8]=VIVANTE
cellules[13][8]=VIVANTE
cellules[15][7]=VIVANTE
cellules[16][6]=VIVANTE
cellules[16][5]=VIVANTE
cellules[16][4]=VIVANTE
cellules[17][5]=VIVANTE
cellules[14][5]=VIVANTE
cellules[15][3]=VIVANTE
cellules[13][2]=VIVANTE
cellules[12][2]=VIVANTE
cellules[11][3]=VIVANTE

cellules[20][2]=VIVANTE
cellules[20][3]=VIVANTE
cellules[20][4]=VIVANTE
cellules[21][2]=VIVANTE
cellules[21][3]=VIVANTE
cellules[21][4]=VIVANTE
cellules[22][1]=VIVANTE
cellules[22][5]=VIVANTE
cellules[24][0]=VIVANTE
cellules[24][1]=VIVANTE
cellules[24][5]=VIVANTE
cellules[24][6]=VIVANTE

cellules[34][2]=VIVANTE
cellules[34][3]=VIVANTE
cellules[35][2]=VIVANTE
cellules[35][3]=VIVANTE

# On introduit quelques fonctions utiles pour la suite

def est_dans_grille(i, j):
    """
    Vérifie si une cellule de coordonnées (i, j) est dans la grille
    """
    if i>=0 and j>=0 and i<taille_x and j<taille_y:
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
pygame.display.set_caption('Jeu de la vie -  Gosper Glider Gun')
SCREEN.fill(WHITE)

while True:
    drawGrid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    time.sleep(0.1)
    avance_generation()
