import pygame

#Inicializar los módulos y tenerlos a disposición
pygame.init()

#Se crea una ventana 
#Dentro del modlo display se llama la función set_mode 
#a la que se le pasan las dimensiones dentro de una TUPLA
ventana= pygame.display.set_mode((800,600))

#Para poner un color a la ventana llamamos a la función FILL 
#se le pasa un argumento una tupla de 3 valores que represente el color
ventana.fill((51,92,255))
#Cuando llevamos a cabo alguna operacion sobre la ventana
#la información se guarda en memoria y no se muestra
#hasta que se llame la funcion UPDATE

pygame.display.update()

#Para mantener la ventana más tiempo abierta se llama el módulo time
#con la función time
pygame.time.delay(3000)

#Llamar a la función quit para cerrar los modulos 
#inicializados sin errores
pygame.quit()