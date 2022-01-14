import pygame
import random

#Tamaño de pantalla
ANCHO= 800
ALTO=600

#FPS
FPS=30

#PALETA DE COLORES
BLANCO=(255,255,255)
NEGRO=(0,0,0)
MORADO_CLARO= (122,0,255)
MORADO_OSCURO= (47,0,230)
AZUL_OSCURO= (8,25,250)
AZUL_2= (5,78,227)
CELESTE=(5,151,251)

class Jugador(pygame.sprite.Sprite):
    #Sprite del jugador
    def __init__(self):
        # Heredamos el init de la clase Sprite de pygame
        super().__init__()
        #Convert para optimizar el juego
        self.image = pygame.image.load("Nsprites/Principal.png").convert()
        #Para quitar el color
        self.image.set_colorkey(BLANCO)
        #cuando se llame a rect, se esta llamando al sprite
        self.rect = self.image.get_rect()
        self.rect.center = (200,200)
        #Velocidad del personaje inicial
        self.velocidad_x = 0
        self.velocidad_y = 0
    
    #ACTUALIZA CADA VUELTA DEL BUCLE
    def update(self):
        #Actualiza esto cada vuelta del bucle
        if self.rect.right <0:
            self.rect.left = ANCHO
        #Velocidad predeterminada cadavuelta del bucle msi no se pulsa nada
        self.velocidad_x=0
        self.velocidad_y=0
        
        # Mantiene las teclas pulsadas
        teclas = pygame.key.get_pressed()
        
        #Mover personaje a la izquierda
        if teclas[pygame.K_LEFT]:
            self.velocidad_x = -10
        
        #Mover personaje a la derecha
        if teclas[pygame.K_RIGHT]:
            self.velocidad_x = 10
        
        #Mover personaje arriba
        if teclas[pygame.K_UP]:
            self.velocidad_y = -10
        
        #Mover personaje abajo
        if teclas[pygame.K_DOWN]:
            self.velocidad_y = 10
        
        #Actualizar la velocidad o posición del personjae, referente a la variable velocidad
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y
        
        #Limitar el margen izquierdo
        if self.rect.left < 0:
            self.rect.left = 0
        
        #Limitar el margen derecho
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO
        
        #Limitar el margen inferior
        if self.rect.bottom > ALTO:
            self.rect.bottom = ALTO
        
        #Limitar el margen superior
        if self.rect.top <0:
            self.rect.top = 0

class Enemigos(pygame.sprite.Sprite):
    #Sprite del jugador
    def __init__(self):
        # Heredamos el init de la clase Sprite de pygame
        super().__init__()
        #Convert para optimizar el juego
        self.image = pygame.image.load("assets/meteorGrey_med2.png").convert()
        self.image.set_colorkey(NEGRO)
        #cuando se llame a rect, se esta llamando al sprite
        self.rect = self.image.get_rect()
        self.rect.x= random.randrange(ANCHO - self.rect.width)
        #lo mismo para que no se salga de los limites superior e inferioir
        self.rect.y= random.randrange(ALTO - self.rect.height)
        self.velocidad_x = random.randrange(1,10)
        self.velocidad_y = random.randrange(1,10)
    
    #crear un nuevo metodo para que el enmeigo haga esas vainas
    def update(self):
        #Actualizar la velocidad o posición del personjae, referente a la variable velocidad
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y
        
        #X e Y se estan incrementando, crea el efecto diagonal pero si toca un borde decrementa y crea el efecto de que se devuelve 
        
        #Limitar el margen izquierdo
        if self.rect.left < 0:
            self.velocidad_x += 1
        
        #Limitar el margen derecho
        if self.rect.right > ANCHO:
            self.velocidad_x -= 1
        
        #Limitar el margen inferior
        if self.rect.bottom > ALTO:
            self.velocidad_y -= 1
        
        #Limitar el margen superior
        if self.rect.top <0:
            self.velocidad_y += 1
        

#Inicialización de pygame, creación de la ventana, titulo y control del reloj

#Iniciar pygame debne estar en todo archivo 
pygame.init()
pantalla = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("Cygnus Arcade")
clock = pygame.time.Clock()

#Grupo de sprites, con esto podemos hacer agrupaciones apra que trabajen en conjunto
sprites = pygame.sprite.Group()
enemigos = pygame.sprite.Group()

#Instanciaciónd de enemigos
enemigo = Enemigos()
enemigos.add(enemigo)

#Aqui instanciamos al jugador
jugador = Jugador() 
sprites.add(jugador)

#Bucle del juego
ejecutando = True
#variable de ejecutar, que siempre que este en true, ejecutara el juego

while ejecutando:
    #Se especifica la velocidad del juego, este control de reloj, debe estar dentor del while para que se vaya actualizando
    clock.tick(FPS)
    #EVENTOS
    #Bucle for para salir de la ventana
    for event in pygame.event.get():
        #se cierra y termina el bucle
        if event.type == pygame.QUIT:
            ejecutando = False
    
    #Actualización de sprites Con solo llamar a update, se hace que todas las imagenes se vayan actualizando en la pantalla
    sprites.update()
    enemigos.update()
    
    #Spritecollide es un metodo de pygame que permite crear colisiones de manera facil y rapida
    #objeto que provoque la colisiones, luego grupo de sprites, los colisionados
    #false , siugnifica que no eliminará el sprite
    colision= pygame.sprite.spritecollide(jugador,enemigos, False)
    #¿Que pasa cuando pase dicha colision?
    if colision:
        enemigo.image = pygame.image.load("assets/regularExplosion01.png").convert()
        enemigo.velocidad_y += 20
    elif enemigo.rect.top > ALTO:
        enemigo.kill()
        
        
    
    #Fondo de pntalla, dibujo de sprites y formas
    pantalla.fill(NEGRO)
    sprites.draw(pantalla)
    enemigos.draw(pantalla)
    pygame.draw.line(pantalla, AZUL_2, (400,0),(400,800),1)
    pygame.draw.line(pantalla, MORADO_CLARO, (0,300),(800,300),1)
    
    #Actualiza el contenido de la pantalla
    pygame.display.flip()

pygame.quit()
    