import pygame

pygame.init()

#Creación de constantes
ANCHO = 800
ALTO = 600

BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)

ventana=pygame.display.set_mode((ANCHO,ALTO))

# Como la ventana va a desaparecer de inmmediato
#Se crea un bucle infinito, una vez ya está definida la ventana

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
    
    ventana.fill((255,0,0))
    #Actualizar
    pygame.display.update()
    #pygame se llama cada vez que se use un modulo o una función

pygame.quit()