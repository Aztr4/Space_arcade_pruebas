import pygame

#Inicializar
pygame.init()

#Creación de constantes

#Medidas
ANCHO = 1280
ALTO = 720

#Colroes
BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)

#ventana
#Si se quiere la pantalla completa se agrega un argumento a set_mode
ventana=pygame.display.set_mode((ANCHO,ALTO), pygame.FULLSCREEN)

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
            if event.key == pygame.K_ESCAPE:
                jugando = False
    
    #Dibujos
    ventana.fill((255,0,0))
    
    #Actualización pantalla
    pygame.display.update()
    #pygame se llama cada vez que se use un modulo o una función

#Salir
pygame.quit()