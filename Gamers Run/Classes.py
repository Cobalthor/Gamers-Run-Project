from random import randint

from Constantes import *

#Classe gérant les curseurs de l'écran de sélection des personnages


class Curseur:

    """Classe permettant de créer un curseur"""
    def __init__(self):
        #Position du curseur en cases et en pixels
        self.perso_x = 0
        self.perso_y = 0
        self.x = 50
        self.y = 155
        self.perso = Donkey_Kong

    def ia(self):
        perso_alea = randint(1, 11)
        self.perso = personnages[perso_alea]

    def deplacer(self, direction):
        """Methode permettant de déplacer la cible"""
        #Déplacement vers la droite
        if direction == 'droite':
            if self.perso_y <= 1:
                if self.perso_x != 4:
                    self.perso_x += 1
                    self.x += 85
            elif self.perso_y == 2:
                if self.perso_x != 1:
                    self.perso_x += 1
                    self.x += 85

        #Déplacement vers la gauche
        if direction == 'gauche':
            if self.perso_y <= 1:
                if self.perso_x != 0:
                    self.perso_x -= 1
                    self.x -= 85
            elif self.perso_y == 2:
                if self.perso_x != 0:
                    self.perso_x -= 1
                    self.x -= 85

        #Déplacement vers le haut
        if direction == 'haut':
            if self.perso_y != 0:
                if self.perso_y != 2:
                    self.perso_y -= 1
                    self.y -= 68
                else:
                    if self.perso_x == 0:
                        self.perso_y = 1
                        self.perso_x = 1
                        self.y -= 68
                        self.x = 135
                    elif self.perso_x == 1:
                        self.perso_y = 1
                        self.perso_x = 3
                        self.y -= 68
                        self.x = 305
            elif self.perso_y == 0:
                self.perso_y -= 1
                self.y = 0
                self.x = 0

        #Déplacement vers le bas
        if direction == 'bas':
            if self.perso_y != 2:
                if self.perso_y == 0:
                    self.perso_y += 1
                    self.y += 68
                elif self.perso_y == 1:
                    if self.perso_x <= 2:
                        self.perso_y += 1
                        self.perso_x = 0
                        self.y += 68
                        self.x = 177
                    if self.perso_x >= 3:
                        self.perso_y += 1
                        self.perso_x = 1
                        self.y += 68
                        self.x = 262

    def placer(self):
        #Fonction déterminant le personnage sélectionné
        if self.perso_x == 0:
            if self.perso_y == 0:
                self.perso = Donkey_Kong
            if self.perso_y == 1:
                self.perso = Pacman
            if self.perso_y == 2:
                self.perso = Sonic
        if self.perso_x == 1:
            if self.perso_y == 0:
                self.perso = Kirby
            if self.perso_y == 1:
                self.perso = Pikachu
            if self.perso_y == 2:
                self.perso = Yoshi
        if self.perso_x == 2:
            if self.perso_y == 0:
                self.perso = Link
            if self.perso_y == 1:
                self.perso = Pit
        if self.perso_x == 3:
            if self.perso_y == 0:
                self.perso = Mario
            if self.perso_y == 1:
                self.perso = Samus
        if self.perso_x == 4:
            if self.perso_y == 0:
                self.perso = Mega_Man
            if self.perso_y == 1:
                self.perso = Shovel_Knight


"""""class Perso:
    #Classe définissant les personnages
    def __init__(self):
        if self == 'DONKEY_KONG'
            self.sprite_x =
            self.sprite_y =
        if self = 'KIRBY'
            self.sprite_x = 50
            self.sprite_y = 50
        if self = 'LINK'
            self.sprite_x =
            self.sprite_y =
        if self = 'MARIO'
            self.sprite_x =
            self.sprite_y =
        if self = 'MEGA_MAN'
            self.sprite_x =
            self.sprite_y =
        if self = 'PACMAN'
            self.sprite_x =
            self.sprite_y =
        if self = 'PIKACHU'
            self.sprite_x =
            self.sprite_y =
        if self = 'PIT'
            self.sprite_x =
            self.sprite_y =
        if self = 'SAMUS'
            self.sprite_x =
            self.sprite_y =
        if self = 'SHOVEL_KNIGHT'
            self.sprite_x =
            self.sprite_y =
        if self = 'SONIC'
            self.sprite_x =
            self.sprite_y =
        if self = 'YOSHI'
            self.sprite_x =
            self.sprite_y ="""""
