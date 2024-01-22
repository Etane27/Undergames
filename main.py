import pendu 
import juste_prix
import pygame
import sys 
import os
#configuration de la fenêtre principale 
pygame.init()
taille = width,height = 1920,1080
ecran = pygame.display.set_mode(taille)
background_path = os.path.join("Undergames", "sprites", "menu_background.gif")
background = pygame.image.load(background_path)
background = pygame.transform.scale(background,taille)

#chargement logo
logo_path = os.path.join("Undergames","sprites","logo_menu.png")
logo = pygame.image.load(logo_path)
logo_position = ((width - logo.get_width()) // 2,100)


# Boucle principale Pygame
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Logique du jeu ici

    # Dessiner l'arrière-plan
    ecran.blit(background, (0, 0))
    ecran.blit(logo,logo_position)

    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
sys.exit()