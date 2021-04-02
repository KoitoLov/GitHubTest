import pygame
import os
import math

#Dimensiones de la ventana y display
ANCHO, LARGO = 800, 600
#Centro de la pantalla
CENTROX = ANCHO//2
CENTROY = LARGO//2

PANTALLA = pygame.display.set_mode((ANCHO, LARGO))


#Importar imagenes.

#Fondo.
BACKGROUND_IMAGE = pygame.image.load(
    os.path.join('battle_background.png'))

#Jugador / Alma
JUGADOR_SPRITE = pygame.image.load(
    os.path.join('soul_battle.png'))

ALMA_ANCHO, ALMA_LARGO =  20, 20



#Reescalar imagenes.
BACKGROUND = pygame.transform.rotate(pygame.transform.scale(
    BACKGROUND_IMAGE, (ANCHO, LARGO)), 0)


#Otras variables del juego
FPS = 60
VELOCIDAD = 3

normalizar_vector = pygame.math.Vector2.normalize

#Titulo del programa.
pygame.display.set_caption("Battle Engine: Test")



#Funcion que dibuja la pantalla
def draw_window(soul_hitbox):
    PANTALLA.blit(BACKGROUND, (0, 0))


    #Mostrar en pantalla al jugador
    PANTALLA.blit(JUGADOR_SPRITE, (soul_hitbox.x, soul_hitbox.y))

    #Updatear la pantalla
    pygame.display.update()



#Manejar el movimiento del jugador
def move_player(keys_pressed, soul_hitbox):

    if keys_pressed[pygame.K_LEFT] and soul_hitbox.x - VELOCIDAD > 0:
        soul_hitbox.x -= VELOCIDAD

    if keys_pressed[pygame.K_RIGHT] and soul_hitbox.x + VELOCIDAD + 13 < ANCHO:
        soul_hitbox.x += VELOCIDAD

    if keys_pressed[pygame.K_UP] and soul_hitbox.y - VELOCIDAD > 0:
        soul_hitbox.y -= VELOCIDAD

    if keys_pressed[pygame.K_DOWN] and soul_hitbox.y + VELOCIDAD + 156 < LARGO:
        soul_hitbox.y += VELOCIDAD
        

def normalize_vector(soul_hitbox):
    modulo = math.sqrt((soul_hitbox.x**2) + (soul_hitbox.y**2))
    unit_vector = (soul_hitbox.x/modulo, soul_hitbox.y/modulo)
    




# Funcion principal
def main():

    clock = pygame.time.Clock()

    soul_hitbox = pygame.Rect(CENTROX, CENTROY, ALMA_ANCHO, ALMA_LARGO)


    jugando = True
    while jugando:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jugando = False
                pygame.quit()
            

        
        #Mover al jugador
        keys_pressed = pygame.key.get_pressed()
        move_player(keys_pressed, soul_hitbox)


        draw_window(soul_hitbox)

    main()




#Llamar a la funcion principal
if __name__ == "__main__":
    main()