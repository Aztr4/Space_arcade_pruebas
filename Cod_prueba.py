#En primera instancia se importa la libreria pygame entera, 
# también se importa random para algunas caracerísticas que
# se verán después en el juego
import pygame, random

#Se declaran las variables para las DIMENSIONES de la pantalla
ANCHO= 800
ALTO=600

#Se declaran las constantes para la PALETA DE COLORES
MORADO= (46,60,148)
ROJO= (125,33,0)
LILA= (92,110,224)
VERDE_1 = (134,224,70)
VERDE2 = (95,148,58)
BLANCO =(255,255,255)
NEGRO =(0,0,0)

#Pygame.init se utiliza para inicializar Pygame y ejecutarlo 
pygame.init()
#Lo mismo con esta, que se usa para Inicializar el sonido
pygame.mixer.init()
#Aquí se crea la constante pantalla que lleva la función para nuestra ventana de juego
pantalla= pygame.display.set_mode((ANCHO,ALTO))
#Función para el titulo de la ventana 
pygame.display.set_caption("Vostok Game")
#Reloj para fps
reloj = pygame.time.Clock()

#Para que aparezca texto en la ventana se crea una funcion que permita ello
def dibujar_texto(superficie, texto, dimensiones,x, y):
    fuente = pygame.font.SysFont("serif", dimensiones)
    #El rue depende de si sle o no bien definido
    superficie_txt= fuente.render(texto, True, BLANCO)
    txt_rect= superficie_txt.get_rect()
    txt_rect.midtop = (x,y)
    superficie.blit (superficie_txt, txt_rect)

def barra_vida(superficie_bar,x,y, porcentaje):
    LARGO_bar= 100
    ALTO_bar = 10
    calculo_barra= (porcentaje/100)* LARGO_bar
    borde = pygame.Rect(x,y, LARGO_bar, ALTO_bar)
    calculo_barra= pygame.Rect(x,y, calculo_barra, ALTO_bar)
    pygame.draw.rect(superficie_bar, ROJO, calculo_barra)
    pygame.draw.rect(superficie_bar, BLANCO, borde, 2)

#Aquí se define la clase del jugador, se especifica esta clase, lo que hace el jugador, si muere al hacer algo, las vidas 
#Dicha clase de jugador debe tener herencia del modulo Sprite para tener todas las funcionalidades
#esta nos facilita la vida porque se usa para todo lo que tiene que ver con sprotes y eso
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #Cargar la imagen
        #Las imagenes que se usen se pueden optimizar usando .convert para consumir menos recursos
        self.image = pygame.image.load("img_proyecto/PERSONAJE ESCALADO.png"). convert()
        self.image.set_colorkey(BLANCO)
        #Obteneer el cuadro del sprite
        self.rect = self.image.get_rect()
        #Ponerlo en pantalla
        self.rect.centerx = ANCHO //2
        self.rect.bottom = ALTO - 10
        self.vel_x = 0
        self.vel_y =0
        self.barra = 100
    
    #Este Metodo es perteneciente a la clase sprite y aCTUALIZA CADA VUELTA DEL BUCLE
    def update(self):
        self.vel_x = 0
        self.vel_y = 0
        #Variable de si alguna tecla ha sido presionada
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.vel_x = -5
        if keystate[pygame.K_RIGHT]:
            self.vel_x = 5
        if keystate[pygame.K_UP]:
            self.vel_y = -5
        if keystate[pygame.K_DOWN]:
            self.vel_y = 5
        
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        
        #Limite borde derecho
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO
        #Limite borde izquierdo
        #Si el borde de la nave es igual a 0 no puede seguir mas
        if self.rect.left < 0:
            self.rect.left = 0
        #Limite borde inferior
        if self.rect.bottom > ALTO:
            self.rect.bottom = ALTO
        #Limite borde superior
        if self.rect.top < 0:
            self.rect.top = 0
            
    #Crear un nuevo metodo para los disparos 
    def disparo(self):
        #Aqui la bala se instancia en el centro del jugador y en posicion Y arriba
        #asignando así dinamicamente la bala
        
        bullet= Bullet(self.rect.centerx, self.rect.top)
        sprites.add(bullet)
        bullets.add(bullet)
        sonido_laser.play()
        
        
class Meteoros(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = random.choice(meteor_images)
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        #Valor de inicio
        #Random para que aparezca en cualquier lugar
        self.rect.x = random.randrange(ANCHO -  self.rect.width)
        #Para que de el efecto de que esta bajando
        self.rect.y = random.randrange (-100,-40)
        #self.rect.y= random.randrange(ALTO - self.rect.height)
        #Definimos la velocidad, velocidad alteatoria
        self.vel_y = random.randrange (1,10)
        self.vel_x = random.randrange (-5,5)
    
    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        if self.rect.top > ALTO +10 or self.rect.left < -25 or self.rect.right > ANCHO +22:
            self.rect.x = random.randrange(ANCHO -  self.rect.width)
        #Para que de el efecto de que esta bajando
            self.rect.y = random.randrange (-150,-100)
        #Definimos la velocidad, velocidad alteatoria
            self.vel_y = random.randrange (1,8)

class Estrellas(pygame.sprite.Sprite):
    #Sprite del jugador
    def __init__(self):
        # Heredamos el init de la clase Sprite de pygame
        super().__init__()
        #Convert para optimizar el juego
        self.image = pygame.image.load("img_proyecto/estrella.png").convert()
        self.image.set_colorkey(NEGRO)
        #cuando se llame a rect, se esta llamando al sprite
        self.rect = self.image.get_rect()
        self.rect.x= random.randrange(ANCHO - self.rect.width)
        #lo mismo para que no se salga de los limites superior e inferioir
        self.rect.y= random.randrange(ALTO - self.rect.height)
        #self.velocidad_x = random.randrange(1,10)
        #self.velocidad_y = random.randrange(1,10)
    
    #crear un nuevo metodo para que el enmeigo haga esas vainas
    def update(self):
        pass



class Bullet(pygame.sprite.Sprite):
    #debemos poner x.y como argumentos para pasarle como parametro la zona donde se van a poner los disparos
    #como el personaje se mueve, debemos obtner la posicion exacta
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("assets/laser1.png")
        self.image.set_colorkey(NEGRO)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.centerx = x
        self.speedy= -10
    
    def update(self):
        self.rect.y += self.speedy
        #Parte de abajo del sprite
        #Con este metodo eliminamos las instancias de este objeto de cualquier lista y no toca hacerlo manual
        if self.rect.bottom < 0:
            self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        #Se comienza con la imagen 0, es decir con la primera que se carag para luego ir iterando
        self.image = explosion_anim[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        #Frame es el valor que va auymentando para ir cambiando la imagen y dar la ilusion de la animacion
        self.frame = 0
        #Se tien un reloj.tick que corre a 60frames por segundo
        #de alguna manera se pausa el juego por 60frames
        #entonces yo tengo que saber exactamente en que punto me encuentro para saber en ese momento hacer la animacion
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50 #Velocidad de la explosion
    
    def update(self):
        #Esta variable permite saber cuanto tiempos a transcurrido cuando se crea la eplosion, la perimera es cuando inicia, por eso se ocmpara enter las dos
        now = pygame.time.get_ticks()
        #Si lo que ha transcurrido ahora, menos lo que ya transcurrio es mayor que 50 se va a inicalizar la explosion
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            #luego se incrementa la variable para poder pasar por todos los elementos de la lista
            self.frame +=1
            #Aqui, se esta averiguando si ya se llego al final de la lista entonces elimina todos los sprites 
            if self.frame == len(explosion_anim):
                self.kill()
                #Por ultimo se crea la explosion con un else
            else:
                center = self.rect.center
                #se utiliza la variable frame para iterar
                self.image = explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
                #Con esto ya se cargo la explosion
        
def pantalla_game_over():
    pantalla.blit(fondo, [0,0])
    dibujar_texto(pantalla, "SPACE ARCADE", 65, ANCHO//2, ALTO//4)
    dibujar_texto(pantalla, "Tras nueve meses de una misión en la que fue abandonado el astronauta Ki", 27, ANCHO //2, ALTO//2)
    dibujar_texto(pantalla, "Presiona aquí", 20, ANCHO//2, ALTO * 3/4)
    pygame.display.flip()
    wait = True
    while wait:
        reloj.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                wait= False
         


meteor_images = []
meteor_list = ["assets/meteorGrey_big1.png", "assets/meteorGrey_big2.png", "assets/meteorGrey_big3.png", "assets/meteorGrey_big4.png",
				"assets/meteorGrey_med1.png", "assets/meteorGrey_med2.png", "assets/meteorGrey_small1.png", "assets/meteorGrey_small2.png",
				"assets/meteorGrey_tiny1.png", "assets/meteorGrey_tiny2.png"]
for img in meteor_list:
	meteor_images.append(pygame.image.load(img).convert())
    
    
##-------------EXPLOSION IMG-----------
explosion_anim= []
for a in range(9):
    file = "assets/regularExplosion0{}.png".format(a)
    img = pygame.image.load(file).convert()
    img.set_colorkey(NEGRO)
    img_scale = pygame.transform.scale(img, (70,70))
    explosion_anim.append(img_scale)

#Cargar fondo
fondo = pygame.image.load ("img_proyecto/fondo.png").convert()

#Cargar musica
sonido_laser= pygame.mixer.Sound("assets/laser5.ogg")
explosion_sound= pygame.mixer.Sound("assets/explosion.wav")
pygame.mixer.music.load("sonidos/intergalactic_odyssey.ogg")
pygame.mixer.music.set_volume(0.1)

#musica
pygame.mixer.music.play(loops=-1)

#Bucle
game_over = True

#variable de ejecutar, que siempre que este en true, ejecutara el juego
ejecutar = True
# Aqui inicia el Bucle princiapl del codigo pues es para mantener 
# la ventana abierta, entonces Se mantiene siempre en True y solo 
# tiene la posibilidad de salir con el quit
while ejecutar:
    
    if game_over:
        
        pantalla_game_over()
        
        game_over = False
        #Crear grupo
        #Grupo de sprites, con esto podemos hacer agrupaciones apra que trabajen en conjunto
        sprites = pygame.sprite.Group()
        meteor_list = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        estrella = pygame.sprite.Group()

        #Instanciar jugador
        jugador = Jugador()
        #Aqui al grupo se le agrego jugador para que tenga la img del jugador
        #y como son varias imagenes tambien las obtendrá 
        sprites.add(jugador)

        for i in range (10):
            meteor= Meteoros()
            sprites.add(meteor)
            meteor_list.add(meteor)
        
        for i in range(3):
            stars = Estrellas()
            sprites.add(stars)
            estrella.add(stars)
            
        #Para implementar un marcador definimos una varibale que es lo que va a llevar la cuenta
        score = 0
    #El reloj.tick especifica la velocidad del juego, este control de reloj debe estar dentor del while
    #para que se vaya actualizando    
    reloj.tick(60)
    #EVENTOS
    #Bucle for para salir de la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutar = False
    
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jugador.disparo()
    
    #Actualización de sprites, Con solo llamar a update, se hace que todas 
    # las imagenes se vayan actualizando en la pantalla
    sprites.update()
    
    
    #objeto que provoque las colisiones, luego grupo de sprites, los colisionados
    #false , significa que no eliminará el sprite
    
    #Colision meteoro-laser
    #Los dos true, significa que las dos desaparezcan
    colision = pygame.sprite.groupcollide(meteor_list, bullets, True, True)
    for i in colision:
        score += 10
        explosion_sound.play()
        #Agregar la explosion cada vex que meteoroo colsiione con laser
        #Tiene que ser en el mismo punto done esta elmeteoropor eso la i
        explosion = Explosion(i.rect.center)
        #Agregamos eso a trodos los sprotes
        sprites.add(explosion)
        meteor= Meteoros()
        sprites.add(meteor)
        meteor_list.add(meteor)
        
    #Spritecollide es un metodo de pygame que permite crear colisiones de manera facil y rapida
    #Colisiones meteoro-jugador
    colision = pygame.sprite.spritecollide(jugador, meteor_list, True)
    for n in colision:
        jugador.barra -=25
        meteor= Meteoros()
        sprites.add(meteor)
        meteor_list.add(meteor)
        if jugador.barra <=0:
            game_over = True
    
    
    ###############################IMPRIMIR
    
    #PANTALLA
    pantalla.blit(fondo, (0,0))
    
    #SPRITES
    sprites.draw(pantalla)
    
    #Marcador
    dibujar_texto(pantalla, str(score), 25, ANCHO//2, 10)
    
    #BARRA DE VIDA
    #En el argumento se especifica el jugador.barra para que haga el calculo 
    #de procentaje en torno a la vida del jugador la barra seria un 100*100, 
    #donde si se impacta un enemigo que quita 15,quitaria el 15% y 
    #ese es el porcen taje de barra que va a ir retirando
    barra_vida(pantalla, 5, 5, jugador.barra)  
    
    #Actualiza el contenido de la pantalla
    pygame.display.flip()
    
pygame.quit()
    
    
        
        
        



