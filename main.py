import pygame, sys
from juego import *

def main():
    pygame.init()

    pantalla = pygame.display.set_mode(tamaño)
    pygame.display.set_caption("Friends Fight Club")
    ico = pygame.image.load("assets/Sprites/ico/ico.png")
    pygame.display.set_icon(ico)
    
    done = False
    
    clock = pygame.time.Clock()

    game = Juego()

    while not done:
        done = game.proceso_eventos()
        game.correr_logica()
        game.frame_pantalla(pantalla)
        clock.tick(20)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
