

import pygame

pygame.init()

#Creación de constantes
ANCHO = 800
ALTO = 600

BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
VERDE=(0,255,0)
AZUL=(0,0,255)

ventana=pygame.display.set_mode((ANCHO,ALTO))

# Como la ventana va a desaparecer de inmmediato
#Se crea un bucle infinito, una vez ya está definida la ventana

#Bucle principal
jugando = True

while jugando:
    
    #Para todos los evento que esta función va a recoger en la 
    #ventana 
    for event in pygame.event.get() :
        if event.type == pygame.QUIT: #Se refiere a la cruz
            jugando= False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                jugando = False
    
    #Dibujos
    ventana.fill((NEGRO))
    pygame.draw.circle(ventana, VERDE, (60,60),50)
    pygame.draw.line(ventana, BLANCO, (200,300), (300,500))
    pygame.draw.polygon(ventana, AZUL, ((300,300), (350,300), (350,250), (400,250), (400,300), (450,300), (450,350), (300,350)))
    #Actualizar
    pygame.display.update()
    #pygame se llama cada vez que se use un modulo o una función

pygame.quit()