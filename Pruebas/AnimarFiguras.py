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

#Funciones

def nave_arriba(superficie, x,y):
    pygame.draw.rect(ventana, AZUL, (x,y,60,60))
    pygame.draw.rect(ventana, NEGRO, (x,y,15,30))
    pygame.draw.rect(ventana, NEGRO, (x + 45,y,15,30))

def nave_abajo(superficie, x,y):
    pygame.draw.rect(ventana, AZUL, (x,y,60,60))
    pygame.draw.rect(ventana, NEGRO, (x,y+30,15,30))
    pygame.draw.rect(ventana, NEGRO, (x+45,y+30,15,30))
    
def nave_derecha(superficie, x,y):
    pygame.draw.rect(ventana, AZUL, (x,y,60,60))
    pygame.draw.rect(ventana, NEGRO, (x+30,y,30,15))
    pygame.draw.rect(ventana, NEGRO, (x+30,y+45,30,15))

def nave_izquierda(superficie, x,y):
    pygame.draw.rect(ventana, AZUL, (x,y,60,60))
    pygame.draw.rect(ventana, NEGRO, (x,y,30,15))
    pygame.draw.rect(ventana, NEGRO, (x,y+45,30,15))

def asteroide_1(superficie,x,y):
    pygame.draw.rect(ventana, VERDE, (x,y,60,60))
    pygame.draw.rect(ventana, NEGRO, (x,y,20,20))

def asteroide_2(superficie,x,y):
    pygame.draw.rect(ventana, VERDE, (x,y,60,60))
    pygame.draw.rect(ventana, NEGRO, (x+40,y,20,20))

def asteroide_3(superficie,x,y):
    pygame.draw.rect(ventana, VERDE, (x,y,60,60))
    pygame.draw.rect(ventana, NEGRO, (x+40,y+40,20,20))
    
def asteroide_4(superficie,x,y):
    pygame.draw.rect(ventana, VERDE, (x,y,60,60))
    pygame.draw.rect(ventana, NEGRO, (x,y+40,20,20))

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

direccion= "arriba"

contador=0

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
    

    
    #Dibujos
    ventana.fill((NEGRO))
    
    contador+=1
    if contador >=41: #21
        contador=1
    
    
    if contador<11: #Para que rote mas rapido #6
        asteroide_1(ventana, aste_pos_x,aste_pos_y)
    elif contador<21: #11
        asteroide_2(ventana, aste_pos_x,aste_pos_y)
    elif contador<31: #16
        asteroide_3(ventana, aste_pos_x,aste_pos_y)
    elif contador<41: #21
        asteroide_4(ventana, aste_pos_x,aste_pos_y)
    
    if direccion == "arriba":
        nave_arriba(ventana, nave_pos_x, nave_pos_y)
    elif direccion == "abajo":
        nave_abajo(ventana, nave_pos_x, nave_pos_y)
    elif direccion == "izquierda":
        nave_izquierda(ventana, nave_pos_x, nave_pos_y)
    elif direccion == "derecha":
        nave_derecha(ventana, nave_pos_x, nave_pos_y)
        
        
        
    #Actualizar
    pygame.display.update() #pygame se llama cada vez que se use un modulo o una función

pygame.quit()