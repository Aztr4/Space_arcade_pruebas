#Importar el módulo pygame entero
from os import altsep
import pygame, sys
from pygame.locals import *

#Lo siguiente para que funcione pygmae y lo ejecute
pygame.init()

"""PANTALLA-VENTANA"""
ANCHO= 800
ALTO= 600
#Constante pantalla que lleva la función para nuestra ventana de juego
PANTALLA = pygame.display.set_mode((ANCHO,ALTO))
#El numero de FPS es un pooc relativo porque cada vez que yo
#modifique el bucle del edcremeento, cada segundo movera un total de 120 segundos
#por segundo 
#Si aumento el decremento se mvera más rapido
FPS=120
RELOJ = pygame.time.Clock()


"""Fondo del Juego"""
#Las imagenes que se usen se pueden optimizar usando .convert para consumir menos recursos
fondo=pygame.image.load("assets/background.png").convert()
#Para mostrarlo, llamamos a pantalla con el argumento fondo
#El 0,0 indicamos que no queremos margen
#x para manipular mas facil la pantalla, que se pondrá en el bucle
x=0




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
#Para hacer que se mueva debe incrementarse o 
#decrementarse en 1 pixel los pixeles cada vez que se ejecute
#Conseguimos el ancho del fondo con el .width
#Se divide el valor de x, por el ancho del fondo y devuelva el resto, así se irá moviendo
    x_relativa= x% fondo.get_rect().width
    PANTALLA.blit(fondo,(x_relativa-fondo.get_rect().width,0))
    if x_relativa < ANCHO:
        PANTALLA.blit(fondo, (x_relativa,0))
    x -=1
#Valor de x relativa menos el ancho del fondo

#Primero inicia la ventana del juego, por defecto en negro
#Para aplicar el color de fondo necesita una actualización

    pygame.display.update()
    RELOJ.tick(FPS)