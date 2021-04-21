import pygame
import os

pygame.font.init()
pygame.mixer.init()

#Dimensiones de la ventana
WIDTH, HEIGHT = 1024, 720

#Setear el size de la pantalla
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Juego Prueba")

#COLORES
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255 ,255)

#Background
SPACE_BACKGROUND = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))


#Variables del Juego
FPS = 60
PLAYER_VELOCITY = 4
BULLET_VEL = 7
MAX_BULLETS = 3
HEALTH_FONT = pygame.font.Font('monoweb.ttf', 30)
WINNER_FONT = pygame.font.Font('monoweb.ttf', 140)


SPACESHIP_WITHD, SPACESHIP_HEIGHT = 60, 50


#Size de la muralla en mitad del juego.
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)


#Sonidos
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'hitsound.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'firesound.mp3'))


#Nave AMARILLA
#Carga la Nave Amarilla al programa
YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))

#Rota y reescala la imaguen de la Nave roja en 90 grados
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WITHD, SPACESHIP_HEIGHT)), 90)

YELLOW_HIT = pygame.USEREVENT + 1


#Nave ROJA:
#Carga la Nave Roja al programa
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))

#Rota y reescala la imaguen de la Nave roja en 270 grados
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WITHD, SPACESHIP_HEIGHT)), 270)

RED_HIT = pygame.USEREVENT + 2

def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(SPACE_BACKGROUND, (0, 0))

    #Dibujar el texto que contiene la VIDA de las NAVES
    red_health_text = HEALTH_FONT.render("VIDA: " +str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render("VIDA: " +str(yellow_health), 1, WHITE)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))

    #Usar blit cuando se quiera usar dibujar una superficie
    #Dibujar a las naves
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))


    #Dibujar las balas de la NAVE ROJA
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    
    #Dibujar las balas de la NAVE AMARILLA
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    #Dibujar el borde
    pygame.draw.rect(WIN, BLACK, BORDER)





    pygame.display.update()


def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - PLAYER_VELOCITY > 0: #LEFT
        yellow.x -= PLAYER_VELOCITY
    if keys_pressed[pygame.K_d] and yellow.x + PLAYER_VELOCITY + yellow.width < BORDER.x: #RIGHT
        yellow.x += PLAYER_VELOCITY
    if keys_pressed[pygame.K_w] and yellow.y - PLAYER_VELOCITY > 0: #UP
        yellow.y -= PLAYER_VELOCITY
    if keys_pressed[pygame.K_s] and yellow.y + PLAYER_VELOCITY + yellow.height < HEIGHT - 12: #DOWN
        yellow.y += PLAYER_VELOCITY

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - PLAYER_VELOCITY > BORDER.x + BORDER.width: #LEFT
        red.x -= PLAYER_VELOCITY
    if keys_pressed[pygame.K_RIGHT]and red.x + PLAYER_VELOCITY + red.width < WIDTH: #RIGHT
        red.x += PLAYER_VELOCITY
    if keys_pressed[pygame.K_UP] and red.y - PLAYER_VELOCITY > 0: #UP
        red.y -= PLAYER_VELOCITY
    if keys_pressed[pygame.K_DOWN] and red.y + PLAYER_VELOCITY + red.height < HEIGHT - 12: #DOWN
        red.y += PLAYER_VELOCITY
    

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    
    #Checkear si la BALA AMARILLA dio a la NAVE ROJA
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT)) 
            yellow_bullets.remove(bullet)

        #Si la bala sale de la pantalla: Eliminala
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
    
    #Checkear si la BALA ROJA le dio a la NAVE AMARILLA
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        #Si la bala sale de la pantalla: Eliminala
        elif bullet.x < 0:
            red_bullets.remove(bullet)


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (
        WIDTH//2 - draw_text.get_width()//2, HEIGHT//2 - draw_text.get_height()//2
        ))
    pygame.display.update()
    pygame.time.delay(5000)



def main():

    red = pygame.Rect(700, 300, SPACESHIP_WITHD, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WITHD, SPACESHIP_HEIGHT)

    red_health = 10
    yellow_health = 10

    red_bullets = []
    yellow_bullets = []

    clock = pygame.time.Clock()

    playing = True
    while playing:
        
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()


                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
        

            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()

            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()

        #Definir la condicion de victoria de cada jugador.
        winner_text = ""

        if red_health <= 0:
            winner_text = "Amarillo gana!"

        if yellow_health <= 0:
            winner_text = "Rojo gana!"

        if winner_text != "":
            draw_winner(winner_text)
            break


        #Mover a la NAVE AMARILLA
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)

        #Ejecutar el script que controla las balas
        handle_bullets(yellow_bullets, red_bullets, yellow, red)


        #Setear el background del programa
        draw_window(
            red, yellow, 
            red_bullets, yellow_bullets, 
            red_health, yellow_health
            )

    main()


if __name__ == "__main__":
    main()