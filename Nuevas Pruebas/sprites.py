import pygame

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

#Las clases son algo que se toca más en POO pero es necesario
#para una mejor optimización y organización del juego
#se especifica en esta clase, lo que hace el jugador, si muere al hacer algo, las vidas 
#Dicha clase de jugador debe tener herencia del modulo Sprite para tener todas las funcionalidades
#esta nos facilita la vida porque se usa para todo lo que tiene que ver con sprotes y eso
class Jugador(pygame.sprite.Sprite):
    #Sprite del jugador
    def __init__(self):
        # Heredamos el init de la clase Sprite de pygame
        super().__init__()
        #Convert para optimizar el juego
        self.image = pygame.image.load("Nsprites/Principal.png").convert()
        #Para quitar el color
        self.image.set_colorkey(BLANCO)
        #obtiene el rectagulo o sprite
        #cuando se llame a rect, se esta llamando al sprite
        self.rect = self.image.get_rect()
        #Centrar el rectangulo o sprite
        #divide entre 2, de manera entera y así saca el centro
        self.rect.center = (ANCHO//2, ALTO//2)
    
    #Metodo perteneciente a la clase sprite
    #ACTUALIZA CADA VUELTA DEL BUCLE
    def update(self):
        #Actualiza esto cada vuelta del bucle
        #Hace que se mueva
        self.rect.y += 10
        #Para que vuelva a aparecer
        #Cuando el punto max de y sea mayor que alto
        #que ponga el punto min a 0 para que vuela a aparecer
        if self.rect.top > ALTO:
            self.rect.bottom = 0

#Inicialización de pygame, creación de la ventana, titulo y control del reloj

#Iniciar pygame debne estar en todo archivo 
pygame.init()
#Especificación de la pantalla con el ancho y alto en variables
pantalla = pygame.display.set_mode((ANCHO,ALTO))
#Titulo en la ventana
pygame.display.set_caption("Cygnus Arcade")
#Reloj, para Control de FPS
clock = pygame.time.Clock()

#Grupo de sprites, instanciación del objeto jugador

#Grupo de sprotes, con esto podemos hacer agrupaciones apra que trabajen en conjunto
sprites = pygame.sprite.Group()
#Aqui instanciamos al jugador
juador = Jugador()
#Aqui al grupo se le agrego jugador para que tenga la img del jugador
# si son varias imagenes tambien las obtendrá 
sprites.add(juador)

#Bucle del juego 

ejecutando = True
#variable de ejecutar, que siempre que este en true, ejecutara el juego

while ejecutando:
    #Se especifica la velocidad del juego, este control de reloj, debe estar dentor del while
    #para que se vaya actualizando
    clock.tick(FPS)
    #EVENTOS
    #Bucle for para salir de la ventana
    for event in pygame.event.get():
        #se cierra y termina el bucle
        if event.type == pygame.QUIT:
            ejecutando = False
    
    #Actualización de sprites
    #Con solo llamar a update, se hace que todas las imagenes se vayan actualizando en la pantalla
    sprites.update()
    
    #Fondo de pntalla, dibujo de sprites y formas
    pantalla.fill(NEGRO)
    sprites.draw(pantalla)
    pygame.draw.line(pantalla, AZUL_2, (400,0),(400,800),1)
    pygame.draw.line(pantalla, MORADO_CLARO, (0,300),(800,300),1)
    
    #Actualiza el contenido de la pantalla
    pygame.display.flip()

pygame.quit()
    