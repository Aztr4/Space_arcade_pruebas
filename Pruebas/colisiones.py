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
NARANJA= (225,128,0)

#Funciones

def nave(superficie, x,y, ancho, alto):
    pygame.draw.rect(superficie, AZUL, (x,y,ancho,alto))

def asteroide(superficie, x,y, ancho, alto):
    pygame.draw.rect(superficie, NARANJA, (x,y,ancho,alto))

#ventana
ventana=pygame.display.set_mode((ANCHO,ALTO))
reloj = pygame.time.Clock()

#Datos
aste_ancho = 60
aste_alto = 60
aste_pos_x=100
aste_pos_y=100
aste_vel_x =5

nave_ancho=60
nave_alto=60
nave_pos_x = 600
nave_pos_y = 500
nave_vel_x= 0
nave_vel_y=0

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
                direccion="derecha"
                nave_vel_x = 10
            if event.key == pygame.K_LEFT:
                direccion="izquierda"
                nave_vel_x = -10
            if event.key == pygame.K_DOWN:
                direccion="abajo"
                nave_vel_y = 10
            if event.key == pygame.K_UP:
                direccion="arriba"
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
    
    if aste_pos_x+aste_ancho > nave_pos_x and \
       aste_pos_x < nave_pos_x+nave_ancho and \
       aste_pos_y+aste_alto>nave_pos_y and\
       aste_pos_y < nave_pos_y + nave_alto:
           pygame.time.delay(1000)
           aste_pos_x=100
           aste_pos_y=100 
    
    #Dibujos
    ventana.fill((NEGRO))
    
    asteroide(ventana, aste_pos_x,aste_pos_y, aste_ancho, aste_alto)
    
    nave(ventana, nave_pos_x, nave_pos_y, nave_ancho, nave_alto)
        
        
    #Actualizar
    pygame.display.update() #pygame se llama cada vez que se use un modulo o una función

pygame.quit()