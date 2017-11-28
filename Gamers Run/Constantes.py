import pygame

pygame.init()

continuer_selec = 1
continuer = 1
principal = 1

titre_fenetre = 'Gamers Run'

#IMPORTATION DES SONS

menu_principal = pygame.mixer.Sound('menu.wav')
selection_musique = pygame.mixer.Sound('selection.wav')

#IMPORTATION DES IMAGES

#Écran de démarrage

fond_1 = 'Écran_titre.jpg'
button_1 = 'Press_Start_Button.png'

#Écran de sélection des personnages

#Fond
fond_selec = 'Fond 3.jpg'
toads = 'Toads.png'
retour = 'Retour.png'
#Personnages
donkey_kong = 'donkey kong.png'
kirby = 'kirby.png'
link = 'link.png'
mario = 'mario.png'
mega_man = 'Mega_Man.png'
pacman = 'Pacman.png'
pikachu = 'pikachu.png'
pit = 'Pit.png'
samus = 'samus.png'
shovel_knight = 'Shovel_Knight.png'
sonic = 'Sonic.png'
yoshi = 'yoshi.png'
#Curseurs
curseur_1 = 'curseur_J1.png'
curseur_2 = 'curseur_J2.png'
curseur_3 = 'curseur_J3.png'
#Joueurs
j1 = 'J1.png'
j2 = 'J2.png'
j3 = 'J3.png'


#CONVERSION DES IMAGES

#Images de l'écran de démarrage

Fond_1 = pygame.image.load(fond_1).convert_alpha()
Button_1 = pygame.image.load(button_1).convert_alpha()

#Images de l'écran de sélections des personnages

Fond_2 = pygame.image.load(fond_selec).convert_alpha()
Toads = pygame.image.load(toads).convert_alpha()
Retour = pygame.image.load(retour).convert_alpha()
Donkey_Kong = pygame.image.load(donkey_kong).convert_alpha()
Kirby = pygame.image.load(kirby).convert_alpha()
Link = pygame.image.load(link).convert_alpha()
Mario = pygame.image.load(mario).convert_alpha()
Mega_Man = pygame.image.load(mega_man).convert_alpha()
Pacman = pygame.image.load(pacman).convert_alpha()
Pikachu = pygame.image.load(pikachu).convert_alpha()
Pit = pygame.image.load(pit).convert_alpha()
Samus = pygame.image.load(samus).convert_alpha()
Shovel_Knight = pygame.image.load(shovel_knight).convert_alpha()
Sonic = pygame.image.load(sonic).convert_alpha()
Yoshi = pygame.image.load(yoshi).convert_alpha()
Curseur_1 = pygame.image.load(curseur_1).convert_alpha()
Curseur_2 = pygame.image.load(curseur_2).convert_alpha()
Curseur_3 = pygame.image.load(curseur_3).convert_alpha()
J1 = pygame.image.load(j1).convert_alpha()
J2 = pygame.image.load(j2).convert_alpha()
J3 = pygame.image.load(j3).convert_alpha()

personnages = [Donkey_Kong, Kirby, Link, Mario, Mega_Man, Pacman, Pikachu, Pit, Samus, Shovel_Knight, Sonic, Yoshi]