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

#ventana
ventana=pygame.display.set_mode((ANCHO,ALTO))

#Datos_

r1_x =100
r1_y =100

r2_x =200
r2_y =200

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
    
    #Lógica del programa
    
    #Por cada actualización aumenta en 1 pixel
    
    #Movimiento de izquierda a derecha
    #pos_x +=1
    #if pos_x > ANCHO:
    #    pos_x = -50
        
    #Movimiento de derecha a izquierda
    r1_x -=1
    if r1_x < -50:
        r1_x = ANCHO
    
   #Movimiento Diagonal
    r2_x +=1
    r2_y +=1
    if r2_x > ANCHO:
        r2_x = -50
    if r2_y >ALTO:
        r2_y = -50
    
    #Dibujos
    ventana.fill((NEGRO))
    pygame.draw.rect(ventana, VERDE, (r1_x,r1_y,50,50))
    pygame.draw.rect(ventana, AZUL, (r2_x,r2_y,50,50))
    #Actualizar
    pygame.display.update()
    #pygame se llama cada vez que se use un modulo o una función
    
    #Aqiu se retrasa 5milisegundos por cada iteración
    pygame.time.delay(5)

pygame.quit()