#Importar el módulo pygame entero
import pygame, sys
from pygame.locals import *

#Lo siguiente para que funcione pygmae y lo ejecute
pygame.init()

#Constante pantalla que lleva la función para nuestra ventana de juego
PANTALLA = pygame.display.set_mode((500,400))

#Fondo del Juego
fondo=pygame.image.load("assets/background.png")
#Para mostrarlo, llamamos a pantalla con el argumento fondo
#El 0,0 indicamos que no queremos margen
PANTALLA.blit(fondo,(0,0))

#Icono y título
pygame.display.set_caption("Cygnus Arcade")
#image.load para cargar una imagen, se pone como si fuese un string la extensión de la imagen
#especificando la imagen
icono= pygame.image.load("Nuevas Pruebas/pngicono.png")
#Display para que muestre el icono
pygame.display.set_icon(icono)

#Bucle para mantener la ventana abierta
#Explicación:
#Se mantiene siempre en True y solo tiene la posibilidad de salir con el quit

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit

#Primero inicia la ventana del juego, por defecto en negro
#Para aplicar el color de fondo necesita una actualización

    pygame.display.update()