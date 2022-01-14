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

#Bucle principal
jugando = True

while jugando:
    
    for event in pygame.event.get() :
        if event.type == pygame.QUIT: #Se refiere a la cruz
            jugando= False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                jugando = False
    
    #Dibujos
    ventana.fill((NEGRO))
    pygame.draw.rect(ventana, VERDE, (200,200,60,60))
    pygame.draw.rect(ventana, AZUL, (600,500,60,60))
    
    #Actualizar
    pygame.display.update()

pygame.quit()