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

#Fuentes

consolas = pygame.font.match_font('consolas')
times = pygame.font.match_font('times')
arial = pygame.font.match_font('arial')
courier = pygame.font.match_font('courier')

#Sonidos
pygame.mixer.init()
pygame.mixer.Sound("assets/laser5.ogg")
laser = pygame.mixer.Sound("assets/laser5.ogg")
ambiente = pygame.mixer.Sound("sonidos/intergalactic_odyssey.ogg")

ambiente.play()

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
        self.rect.center = (400,600)
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
        
        laser.play()

#CLASE 1#######################################
class Enemigos1(pygame.sprite.Sprite):
    #Sprite del jugador
    def __init__(self):
        # Heredamos el init de la clase Sprite de pygame
        super().__init__()
        #Convert para optimizar el juego
        self.image = pygame.image.load("assets/meteorGrey_tiny1.png").convert()
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

#CLASE 2##################################
class Enemigos2(pygame.sprite.Sprite):
    #Sprite del jugador
    def __init__(self):
        # Heredamos el init de la clase Sprite de pygame
        super().__init__()
        #Convert para optimizar el juego
        self.image = pygame.image.load("assets/meteorGrey_tiny2.png").convert()
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

#CLASE 3#####################################
class Enemigos3(pygame.sprite.Sprite):
    #Sprite del jugador
    def __init__(self):
        # Heredamos el init de la clase Sprite de pygame
        super().__init__()
        #Convert para optimizar el juego
        self.image = pygame.image.load("assets/meteorGrey_small1.png").convert()
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

#CLASE 4########################
class Enemigos4(pygame.sprite.Sprite):
    #Sprite del jugador
    def __init__(self):
        # Heredamos el init de la clase Sprite de pygame
        super().__init__()
        #Convert para optimizar el juego
        self.image = pygame.image.load("assets/meteorGrey_small2.png").convert()
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

class Meteoritos(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #Primero una variable que genere numeros aleatorios
        self.img_aleatoria = random.randrange(3)
        if self.img_aleatoria ==0:
            self.image = pygame.transform.scale(pygame.image.load("assets/meteorGrey_med1.png").convert(),(100,100))
            #para colisiones
            self.radius = 50
        if self.img_aleatoria ==1:
            self.image = pygame.transform.scale(pygame.image.load("assets/meteorGrey_med1.png").convert(),(100,100))
            self.radius = 25
        if self.img_aleatoria ==2:
            self.image = pygame.transform.scale(pygame.image.load("assets/meteorGrey_med1.png").convert(),(100,100))
            self.radius = 12
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(ANCHO-self.rect.width)
        #en Y, evitamos que se genere por dentro de la pantalla, se resta el alto para evitar qeu se teletransporte
        self.rect.y = -self.rect.width
        #La velocidad sera aleatoria enter 1 y 10
        self.velocidad_y = random.randrange(1,10)
    
    #Actualizacion
    def update(self):
        #en el movimiento de y, se incremente segun la velocidad que lleve
        self.rect.y += self.velocidad_y
        # si la parte superior es mayor que alto, si ha desaparecido de la pantalla
        #que vuelva a tomar los valores inicales
        if self.rect.top > ALTO:
            self.rect.x = random.randrange (ANCHO - self.rect.width)
            self.rect.y = -self.rect.width
            #Ancho
            self.velocidad_y = random.randrange(1,10)
               
#Inicialización de pygame, creación de la ventana, titulo y control del reloj

#Iniciar pygame debne estar en todo archivo 
pygame.init()
pantalla = pygame.display.set_mode((ANCHO,ALTO))

#Sistemas de Puntuacion
puntuacion = 0

def muestra_texto(pantalla,fuente,texto,color, dimensiones, x, y):
	tipo_letra = pygame.font.Font(fuente,dimensiones)
	superficie = tipo_letra.render(texto,True, color)
	rectangulo = superficie.get_rect()
	rectangulo.center = (x, y)
	pantalla.blit(superficie,rectangulo)

#Fondo de Pantalla
fondo = pygame.transform.scale(pygame.image.load("assets/background.png").convert(),(1000,600))
pygame.display.set_caption("Cygnus Arcade")
clock = pygame.time.Clock()

#Grupo de sprites, con esto podemos hacer agrupaciones apra que trabajen en conjunto
sprites = pygame.sprite.Group()
enemigos_1 = pygame.sprite.Group()
enemigos_2 = pygame.sprite.Group()
enemigos_3 = pygame.sprite.Group()
enemigos_4 = pygame.sprite.Group()
balas = pygame.sprite.Group()
meteoritos = pygame.sprite.Group()

#Aqui instanciamos al jugador
jugador = Jugador() 
sprites.add(jugador)

#Bucle del juego
ejecutando = True
#variable de ejecutar, que siempre que este en true, ejecutara el juego

while ejecutando:
    #Se especifica la velocidad del juego, este control de reloj, debe estar dentor del while para que se vaya actualizando
    clock.tick(FPS)
    pantalla.blit(fondo, (0,0))
    #EVENTOS
    #Bucle for para salir de la ventana
    for event in pygame.event.get():
        #se cierra y termina el bucle
        if event.type == pygame.QUIT:
            ejecutando = False
    
    #Actualización de sprites Con solo llamar a update, se hace que todas las imagenes se vayan actualizando en la pantalla
    sprites.update()
    enemigos_1.update()
    enemigos_2.update()
    enemigos_3.update()
    enemigos_4.update()
    balas.update()
    meteoritos.update()
    
    colision_disparos_1= pygame.sprite.groupcollide(enemigos_1, balas, True, True, pygame.sprite.collide_circle)
    
    colision_disparos_2= pygame.sprite.groupcollide(enemigos_2, balas, True, True, pygame.sprite.collide_circle)
    
    colision_disparos_3= pygame.sprite.groupcollide(enemigos_3, balas, True, True, pygame.sprite.collide_circle)
    
    colision_disparos_4= pygame.sprite.groupcollide(enemigos_4, balas, True, True, pygame.sprite.collide_circle)
    
    if colision_disparos_1:
        puntuacion +=10
    
    if colision_disparos_2:
        puntuacion +=25
        
    if colision_disparos_3:
        puntuacion +=50
        
    if colision_disparos_4:
        puntuacion +=100
    
    if not enemigos_1 and not enemigos_2 and not enemigos_3 and not enemigos_4:
        enemigo__1 = Enemigos1()
        enemigos_1.add(enemigo__1)
        
        enemigo__2 = Enemigos2()
        enemigos_2.add(enemigo__2)

        enemigo__3 = Enemigos3()
        enemigos_3.add(enemigo__3)

        enemigo__4 = Enemigos4()
        enemigos_4.add(enemigo__4)
    
    #Fondo de pntalla, dibujo de sprites y formas
    sprites.draw(pantalla)
    enemigos_1.draw(pantalla)
    enemigos_2.draw(pantalla)
    enemigos_3.draw(pantalla)
    enemigos_4.draw(pantalla)
    balas.draw(pantalla)
    #meteoritos.draw(pantalla)   
    #Dbujo de textos en pantalla
    muestra_texto(pantalla,arial,str(puntuacion).zfill(7), MORADO_CLARO, 40, 700, 50)

#Actualiza el contenido de la pantalla
    pygame.display.flip()

pygame.quit()