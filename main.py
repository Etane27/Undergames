import pygame
import sys 
import os

# Configuration de la fenêtre Pygame
pygame.init()
taille = width, height = 1920, 1080
ecran = pygame.display.set_mode(taille)
pygame.display.set_caption("Menu Principal")

# Chargement de l'image de fond
background_path = os.path.join("Undergames", "sprites", "menu_background.gif")
background = pygame.image.load(background_path)
background = pygame.transform.scale(background, taille)

# Chargement du logo
logo_path = os.path.join("Undergames", "sprites", "logo_menu.png")
logo = pygame.image.load(logo_path)
logo_position = ((width - logo.get_width()) // 2, 100)

# Chargement de la musique
musiques_path = "C:\\Users\\etane\\OneDrive\\Documents\\PROGRAMES\\UNDERGAMES\\Undergames\\sounds\\menu_theme.mp3"
pygame.mixer.music.load(musiques_path)

# Boucle principale Pygame
pygame.mixer.music.play(loops=-1)
running = True
while running:
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load('C:\\Users\\etane\\OneDrive\\Documents\\PROGRAMES\\UNDERGAMES\\Undergames\\sounds\\menu_theme.mp3')
        pygame.mixer.music.play()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Logique du jeu ici

    # Dessiner l'arrière-plan
    ecran.blit(background, (0, 0))
    ecran.blit(logo, logo_position)

    # Mettre à jour l'affichage
    pygame.display.flip()

# Arrêter la musique avant de quitter
pygame.mixer.music.stop()

# Quitter Pygame
pygame.quit()
sys.exit()
