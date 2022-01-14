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

#PARA CREAR UN TEXTO

#Definir una fuente
fuente1 = pygame.font.SysFont("Small Fonts", 32)
fuente2= pygame.font.SysFont("consolas", 24)
#Crear un objeto de ti´po superficie donde poner el texto 
                     #Texto #Suavizar Bordes #Color,#FondoTexto
texto = fuente1.render("CUADRADOS", False, BLANCO)

#Datos_
puntos=0
vueltas=0

r_x =100
r_y =100

# Como la ventana va a desaparecer de inmmediato
#Se crea un bucle infinito, una vez ya está definida la ventana

#Bucle principal
jugando = True

while jugando:
    
    #Para todos los evento que esta función va a recoger en la ventana 
    for event in pygame.event.get() :
        if event.type == pygame.QUIT: #Se refiere a la cruz
            jugando= False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                puntos +=1
    
    #Lógica del programa
    
    #Por cada actualización aumenta en 1 pixel
    r_x +=1
    if r_x > ANCHO:
        r_x = 0
        vueltas +=1
        
    texto_puntos= fuente2.render("Puntos: " + str(puntos), True, BLANCO)
    texto_vueltas= fuente2.render("Vueltas: " + str(vueltas), True, BLANCO)
    
    #Dibujos
    ventana.fill((NEGRO))
    
    #Pegar la superficie en la ventana 
    ventana.blit(texto, (260,20))
    ventana.blit(texto_puntos, (30,20))
    ventana.blit(texto_vueltas, (640,20))
    
    pygame.draw.rect(ventana, VERDE, (r_x,r_y,50,50))
    #Actualizar
    pygame.display.update()
    #pygame se llama cada vez que se use un modulo o una función
    
    #Aqiu se retrasa 5milisegundos por cada iteración
    pygame.time.delay(5)

pygame.quit()