import pygame
import sys

#inicializar pygame
pygame.init()

#configuración de la ventana
width, height= 640, 480
screen= pygame.display.set_mode((width, height))
pygame.display.set_caption("Cuadrado asesino")

#color de fondo
background_color=(0, 0, 0)

#tamaño y posición incial del cuadrado
square_size=50
x=width//2-square_size//2
y=height//2-square_size//2

#velocidad de movimiento del cuadrado
speed=5

#Bucle principal del juego
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    #detectar teclas presionadas
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y-=speed #mueve el cuadrado hacia arriba
    if keys[pygame.K_DOWN]:
        y+=speed
    if keys[pygame.K_RIGHT]:
        x+=speed
    if keys[pygame.K_LEFT]:
        x-=speed
    
    #mantener el cuadro dentro de los límetes superiores de la pantalla
    if y<0:
        y=0
    if x<0:
        x=0
    if y<0:
        y=-480
    if x<0:
        x=-640

    #rellenar el fondo y dibujar el cuadrado
    screen.fill(background_color)
    pygame.draw.rect(screen, (255, 0, 0), (x, y, square_size, square_size))

    #atualizar la pantalla
    pygame.display.flip()

    #controlar la velocidad del bucle
    pygame.time.Clock().tick(60)

#salir de pygame
pygame.quit()
sys.exit