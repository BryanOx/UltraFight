import pygame
from pygame import *

#~~~~~~~~   Categorias de ataques ~~~~~~~~#
FISICO = "fisico"
ESPECIAL = "especial"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

class Personaje(pygame.sprite.Sprite):
    """
    Clase base para los personajes jugables dentro del juego.
    """
    def __init__(self, nombre):
        super().__init__()
        self.sheet = pygame.image.load("assets/Sprites/Personajes/"+nombre+".png").convert_alpha()
        self.sprites = {
            "frente":[
                self.sheet.subsurface(0,0,96,128),
                self.sheet.subsurface(0,0,96,128)
            ],
            "caminaD":[
                self.sheet.subsurface(0,128,96,128),
                self.sheet.subsurface(96,128,96,128),
                self.sheet.subsurface(192,128,96,128),
                self.sheet.subsurface(288,128,96,128),
                self.sheet.subsurface(384,128,96,128),
                self.sheet.subsurface(480,128,96,128),
                self.sheet.subsurface(576,128,96,128),
                self.sheet.subsurface(672,128,96,128)
                ],
            "caminaI":[
                self.sheet.subsurface(0,256,96,128),
                self.sheet.subsurface(96,256,96,128),
                self.sheet.subsurface(192,256,96,128),
                self.sheet.subsurface(288,256,96,128),
                self.sheet.subsurface(384,256,96,128),
                self.sheet.subsurface(480,256,96,128),
                self.sheet.subsurface(576,256,96,128),
                self.sheet.subsurface(672,256,96,128)
            ],
            "quietoD":[
                self.sheet.subsurface(384,0,96,128),
                self.sheet.subsurface(384,0,96,128),
                self.sheet.subsurface(384,0,96,128),
                self.sheet.subsurface(384,0,96,128),
                self.sheet.subsurface(480,0,96,128),
                self.sheet.subsurface(480,0,96,128),
                self.sheet.subsurface(480,0,96,128),
                self.sheet.subsurface(480,0,96,128),
            ],
            "quietoI":[
                self.sheet.subsurface(576,0,96,128),
                self.sheet.subsurface(576,0,96,128),
                self.sheet.subsurface(576,0,96,128),
                self.sheet.subsurface(576,0,96,128),
                self.sheet.subsurface(672,0,96,128),
                self.sheet.subsurface(672,0,96,128),
                self.sheet.subsurface(672,0,96,128),
                self.sheet.subsurface(672,0,96,128),
            ],
            "puñetazoD":[
                (),
                (),
                (),
                ()
            ],
            "puñetazoI":[
                (),
                (),
                (),
                ()
            ],
            "patadaD":[
                self.sheet.subsurface(0,384,96,128),
                self.sheet.subsurface(0,384,96,128),
                self.sheet.subsurface(96,384,96,128),
                self.sheet.subsurface(96,384,96,128),
                self.sheet.subsurface(192,384,96,128),
                self.sheet.subsurface(192,384,96,128),
                self.sheet.subsurface(288,384,96,128),
                self.sheet.subsurface(288,384,96,128)
            ],
            "patadaI":[
                self.sheet.subsurface(0,512,96,128),
                self.sheet.subsurface(0,512,96,128),
                self.sheet.subsurface(96,512,96,128),
                self.sheet.subsurface(96,512,96,128),
                self.sheet.subsurface(192,512,96,128),
                self.sheet.subsurface(192,512,96,128),
                self.sheet.subsurface(288,512,96,128),
                self.sheet.subsurface(288,512,96,128)
            ],
            "cargando":[
                self.sheet.subsurface(0,768,96,128),
                self.sheet.subsurface(0,768,96,128),
                self.sheet.subsurface(96,768,96,128),
                self.sheet.subsurface(96,768,96,128),
                self.sheet.subsurface(192,768,96,128),
                self.sheet.subsurface(192,768,96,128)
            ],
            "muerte":[
                self.sheet.subsurface(0,640,96,128),
                self.sheet.subsurface(0,640,96,128),
                self.sheet.subsurface(96,640,96,128),
                self.sheet.subsurface(96,640,96,128),
                self.sheet.subsurface(192,640,96,128),
                self.sheet.subsurface(192,640,96,128),
                self.sheet.subsurface(96,640,96,128),
                self.sheet.subsurface(96,640,96,128),
            ]
        }
        
        self.nombre = nombre
        self.ataques = []
        self.vida = 100
        self.energia = 100

        self.saltando = False
        self.saltoC = 0
        self.vel = 6
        self.estado = "frente"
        self.index = 0
        self.rect = pygame.Rect(0,0,96,128)
        self.rect.x = 430
        self.rect.y = 176

    def actualizar(self):
        if self.index >= len(self.sprites.get(self.estado)):
            self.index = 0
            if self.estado == "patadaD":
                self.estado = "quietoD"
            if self.estado == "patadaI":
                self.estado = "quietoI"
        self.image = self.sprites.get(self.estado)[self.index]
        self.index += 1
        
        #-----  LOGICA DE MOVIMIENTOS PARA LAS FUNCIONES    -----#
        #   SALTAR
        if self.saltando:
            self.saltoC += 2
            self.rect.y -= 20
            if self.saltoC == 10:
                self.saltando = False
        if not self.saltando and self.saltoC > 0:
            self.saltoC -= 2
            self.rect.y += 20
        #   CAMINAR DERECHA
        if self.estado == "caminaD":
            if self.rect.x + 96 <= 860:
                self.rect.x += self.vel
        #   CAMINA IZQUIERDA
        if self.estado == "caminaI" and self.rect.x > 0:
            self.rect.x -= self.vel
        #   RECARGA DE ENERGIA
        if self.estado == "cargando":
            self.energia += 1
            if self.energia > 100:
                self.energia = 100
            if self.energia < 100:
                self.energia = 0
        #   MUERTE DEL PERSONAJE
        if self.vida <= 0:
            self.vida = 0
            self.estado = "muerte"

    def movD(self):
        self.estado = "caminaD"

    def movI(self):
        self.estado = "caminaI"            
    
    def salto(self):
        if not self.saltando:
            self.saltando = True

    def carga(self):
        self.estado = "cargando"

    def patada(self):
        if self.estado == "quietoD":
            self.index = 0
            self.estado = "patadaD"
            self.energia -= 5
        elif self.estado == "quietoI":
            self.index = 0
            self.estado = "patadaI"
            self.energia -= 5

class Jugador1(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.movs = {
            "w": self.salto,
            "s": self.carga,
            "d": self.movD,
            "a": self.movI,
            "v": self.patada
        }

    def movimiento(self, tecla):        
        func = self.movs.get(tecla)
        if func:
            func()

class Jugador2(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.movs = {
            "up": self.salto,
            "down": self.carga,
            "right": self.movD,
            "left": self.movI,
            "k": self.patada
        }

    def movimiento(self, tecla):
        func = self.movs.get(tecla)
        if func:
            func()