from clases import *
import pygame
from pygame.locals import *

############################################################################################################

#---    VARIABLES     ---

AZUL = (52, 110, 158)
DORADO = (230, 170, 0)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
BLANCO = (255,255,255)
GRISOSC = (20, 20, 20)

ancho = 860
alto = 480
tamaño = (ancho, alto)

############################################################################################################

class Juego(object):
    """
    CLASE 'JUEGO', ESTA CLASE ES EL JUEGO EN SI, SUS INSTRUCCIONES,
    COMO FUNCIONA EL JUEGO Y LAS COSAS EN ESTE
    """
    def __init__(self):
        """
        FUNCION CONSTRUCTORA DEL JUEGO, CREA LOS OBJETOS
        Y ESTADOS NECESARIOS PARA QUE EL JUEGO FUNCIONE
        """
        
        #---    ESTADOS DEL JUEGO   ---#
        self.menuInicio = False
        self.seleccion = False
        self.pelea = True
        self.pausa = False
        self.finPelea = False
        #------------------------------#

        self.fuente = pygame.font.Font(None, 24)
        self.fuenteGrande = pygame.font.Font(None, 40)

        self.ground = pygame.image.load('assets/Sprites/Terreno/Ground.png').convert_alpha()

        self.lista_sprites = pygame.sprite.Group()

        #---    INICIO DE PERSONAJES    ---#
        self.jugador1 = Jugador1("hombre")
        self.jugador2 = Jugador2("hombre2")
        self.lista_sprites.add(self.jugador1)
        self.lista_sprites.add(self.jugador2)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    def proceso_eventos(self):
        for event in pygame.event.get():

            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
            #  PASE DE LAS TECLAS A LA FUNCION MOV   #
            #            DE LOS JUGADORES            #
            if event.type == KEYDOWN:
                tecla = pygame.key.name(event.key)
                self.jugador1.movimiento(tecla)
                self.jugador2.movimiento(tecla)
            #                                        #
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

            if event.type == QUIT:
                    return True
            if self.menuInicio:
                if event.type == KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return True
                    if event.key == pygame.K_SPACE:
                        self.menuInicio = False
                        self.pelea = True
            if self.pelea:
                if event.type == KEYUP:
                    if event.key == pygame.K_d and self.jugador1.estado == "caminaD":
                        self.jugador1.estado = "quietoD"
                    if event.key == pygame.K_a and self.jugador1.estado == "caminaI":
                        self.jugador1.estado = "quietoI"
                    if event.key == pygame.K_s and self.jugador1.estado == "cargando":
                        self.jugador1.estado = "frente"
                    if event.key == pygame.K_RIGHT and self.jugador2.estado == "caminaD":
                        self.jugador2.estado = "quietoD"
                    if event.key == pygame.K_LEFT and self.jugador2.estado == "caminaI":
                        self.jugador2.estado = "quietoI"
                    if event.key == pygame.K_DOWN and self.jugador2.estado == "cargando":
                        self.jugador2.estado = "frente"
                if event.type == KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.pelea = False
                        self.menuInicio = True
        return False

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    def correr_logica(self):
        if self.pelea:
            self.jugador1.actualizar()
            self.jugador2.actualizar()

            if self.jugador1.estado == ("patadaI" or "patadaD") and pygame.sprite.spritecollide(self.jugador1, self.lista_sprites, False):
                self.jugador2.vida -= 1
            if self.jugador2.estado == ("patadaI" or "patadaD") and pygame.sprite.spritecollide(self.jugador2, self.lista_sprites, False):
                self.jugador1.vida -= 1

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    def frame_pantalla(self, pantalla):
        pantalla.fill(NEGRO)
        if self.menuInicio:

            tituloJ = self.fuenteGrande.render("Ultra-Fight", True, BLANCO)
            tituloJ_rect = tituloJ.get_rect(center = (ancho//2,alto//3))
            pantalla.blit(tituloJ, tituloJ_rect)

            espInicio = self.fuente.render("Preciona espacio para entrar al juego..", True, BLANCO)
            espInicio_rect = espInicio.get_rect(center = (ancho//2, alto//1.2))
            pantalla.blit(espInicio, espInicio_rect)

        if self.pelea:
            pantalla.blit(self.ground, (0, 280))

            contenedorVida = pygame.draw.rect(pantalla, GRISOSC, (13, 13, 206, 15))
            barraVida = pygame.draw.rect(pantalla, ROJO, (16, 16, self.jugador1.vida*2, 10))

            contenedorEnergia = pygame.draw.rect(pantalla, GRISOSC, (13, 30, 156, 10))
            barraEnergia = pygame.draw.rect(pantalla, AZUL, (16, 33, self.jugador1.energia*1.5, 5))

            self.lista_sprites.draw(pantalla)
        pygame.display.flip()