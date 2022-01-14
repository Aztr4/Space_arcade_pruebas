#Importar el módulo pygame entero
import pygame, sys
from pygame.locals import *

#Lo siguiente para que funcione pygmae y lo ejecute
pygame.init()

#Constante pantalla que lleva la función para nuestra ventana de juego
PANTALLA = pygame.display.set_mode((500,400))
pygame.display.set_caption("Cygnus Arcade")

#PALETA DE COLORES
BLANCO=(255,255,255)
NEGRO=(0,0,0)
MORADO_CLARO= (122,0,255)
MORADO_OSCURO= (47,0,230)
AZUL_OSCURO= (8,25,250)
AZUL_2= (5,78,227)
CELESTE=(5,151,251)

PANTALLA.fill(AZUL_2)

#Dibujar un rectangulo, superficie, color, posición (mediante una tupla con posición ancho y alto, en ese orden)

rectangulo1= pygame.draw.rect(PANTALLA, MORADO_OSCURO, (100,50,100,50))
print(rectangulo1)

#Dibujar una línea
#Superficie, color, tula(coordenadas, donde empieza y donde acaba, INCLINACIÓN, GROSOR)

pygame.draw.line(PANTALLA, BLANCO, (100,184), (199,184),1)

#Posición x, y, radio del círculo , relleno, (si se pone 10, parecera un anillo)
pygame.draw.circle(PANTALLA,NEGRO, (122,250),20,0)

#ELIPSE
#X,Y, LARGO, ANCHO, fuera de la tupla hueco o no hueco
pygame.draw.ellipse(PANTALLA, AZUL_OSCURO, (275,200,40,88),14)

#POLIGONO (supeficie, color, puntos, grueso)
puntos= [(100,300),(100,100),(150,100)]
pygame.draw.polygon(PANTALLA, (0,150,255), puntos, 8)

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