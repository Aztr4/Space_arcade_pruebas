import pygame
import random

from pygame import image

#Tamaño de pantalla
ANCHO= 1000
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
        self.radius = 27
        #pygame.draw.circule(self.image,MORADO_CLARO, self.rect.center, self.radius)
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
        
        #Mover personaje abajo
        if teclas[pygame.K_SPACE]:
            #Con esto instanciamos cada vez que se oprime espacio
            jugador.disparo()
            jugador.disparo2()
            jugador.disparo3()
        
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
    
    #Poner un metodo
    #Estamos instanciando objetois con un metodo de una clase, denntro de otra clase, estos es POO
    def disparo(self):
        #Nos referimos, que la bala se instancia e el centro del jugador y en posicion y arriba
        #asignamos así dinamicamente la bala
        bala = Disparos(self.rect.centerx,self.rect.top)
        balas.add(bala)
    
    def disparo2(self):
        bala = Disparos(self.rect.centerx+23,self.rect.top+30)
        balas.add(bala)
    
    def disparo3(self):
        bala = Disparos(self.rect.centerx-23,self.rect.top+30)
        balas.add(bala)

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

class Disparos(pygame.sprite.Sprite):
    #debemos poner x.y como argumentos para pasarle como parametro la zona donde se van a poner los disparos
    #como el personaje se mueve, debemos obtner la posicion exacta
    def __init__(self,x,y):
        super().__init__()
        #redimensionar una imagen
        self.image = pygame.transform.scale(pygame.image.load("assets/laser1.png").convert(),(10,20))
        self.image.set_colorkey(NEGRO)
        #obtenemos el rectangulo de la imagen
        self.rect = self.image.get_rect()
        #En la imagen de la nave, va a centrar justo en medio del rectangulo 
        self.rect.bottom = y
        self.rect.centerx = x
    
    def update(self):
        self.rect.y -= 25
        #Cuando la bala sea inferior a la parte 0 de la pantalla se elimine
        if self.rect.bottom <0:
            self.kill()
        
        

#Inicialización de pygame, creación de la ventana, titulo y control del reloj

#Iniciar pygame debne estar en todo archivo 
pygame.init()
pantalla = pygame.display.set_mode((ANCHO,ALTO))
fondo = pygame.transform.scale(pygame.image.load("assets/background.png").convert(),(1000,600))
pygame.display.set_caption("Cygnus Arcade")
clock = pygame.time.Clock()

#Grupo de sprites, con esto podemos hacer agrupaciones apra que trabajen en conjunto
sprites = pygame.sprite.Group()
enemigos = pygame.sprite.Group()
balas = pygame.sprite.Group()

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
    balas.update()
    
    colision_nave= pygame.sprite.spritecollide(jugador,enemigos, False)
    
    colision= pygame.sprite.groupcollide(enemigos,balas, False, True)
    
    
    
    #¿Que pasa cuando pase dicha colision?
    if colision:
        enemigo.image = pygame.image.load("assets/regularExplosion01.png").convert()
        enemigo.velocidad_y += 20
    elif enemigo.rect.top > ALTO:
        enemigo.kill()
        
        
    
    #Fondo de pntalla, dibujo de sprites y formas
    #pantalla.fill(fondo)
    pantalla.blit(fondo,[0,0])
    sprites.draw(pantalla)
    enemigos.draw(pantalla)
    balas.draw(pantalla)
    
    #Actualiza el contenido de la pantalla
    pygame.display.flip()

pygame.quit()
    