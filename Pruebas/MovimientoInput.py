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
reloj = pygame.time.Clock()

#Datos
aste_pos_x=100
aste_pos_y=100
aste_vel_x =5

nave_pos_x = 600
nave_pos_y = 500
nave_vel_x= 0
nave_vel_y=0


# Como la ventana va a desaparecer de inmmediato
#Se crea un bucle infinito, una vez ya está definida la ventana

#Bucle principal
jugando = True

while jugando:
    
    reloj.tick(60)
    
    #Para todos los evento que esta función va a recoger en la 
    #ventana 
    for event in pygame.event.get() :
        if event.type == pygame.QUIT: #Se refiere a la cruz
            jugando= False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                jugando = False
            if event.key == pygame.K_RIGHT:
                nave_vel_x = 10
            if event.key == pygame.K_LEFT:
                nave_vel_x = -10
            if event.key == pygame.K_DOWN:
                nave_vel_y = 10
            if event.key == pygame.K_UP:
                nave_vel_y = -10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                nave_vel_x = 0
            if event.key == pygame.K_LEFT:
                nave_vel_x = 0
            if event.key == pygame.K_DOWN:
                nave_vel_y = 0
            if event.key == pygame.K_UP:
                nave_vel_y = 0
        
        
    
    #Lógica del programa
    aste_pos_x += aste_vel_x
    if aste_pos_x >ANCHO:
        aste_pos_x = -60
        
    nave_pos_x += nave_vel_x
    nave_pos_y += nave_vel_y
    

    
    #Dibujos
    ventana.fill((NEGRO))
    
    pygame.draw.rect(ventana, VERDE, (aste_pos_x,aste_pos_y,60,60))
    pygame.draw.rect(ventana, AZUL, (nave_pos_x,nave_pos_y,60,60))
    #Actualizar
    pygame.display.update() #pygame se llama cada vez que se use un modulo o una función

pygame.quit()