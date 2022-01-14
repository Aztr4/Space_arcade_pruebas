import pygame
import sys

"""Iniciación de pygame"""
pygame.init()

"""Pantalla-Ventana"""
ANCHO=1000
ALTO=600

PANTALLA = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("Cygnus Arcade")
icono=pygame.image.load("Nuevas Pruebas/pngicono.png")
pygame.display.set_icon(icono)

"""Fondo del Juego"""
fondo= pygame.image.load("assets/background.png")

"""MUSICA DE FONDO"""
"""#Parca cargar la musica se debe de poner el modulo
pygame.mixer.music.load("sonidos/intergalactic_odyssey.ogg")
#Luego se pone -1 para reproducir la musica de manera infinita
pygame.mixer.music.play(-1)"""

pygame.mixer.music.load('sonidos/intergalactic_odyssey.ogg')
pygame.mixer.music.play(-1)



"""Personajes"""
#Las imagenes que van a ser las animaciones, los sprites que juntandolas
#Cuando el personaje vaya a algun lado se carguen las imagenes de ese lado
quieto= pygame.image.load("Nsprites/Principal.png")

Personaje_der =[pygame.image.load("Nsprites/der_1.png"), 
                pygame.image.load("Nsprites/der_2.png"),
                pygame.image.load("Nsprites/der_3.png"),
                pygame.image.load("Nsprites/der_4.png"),]

Personaje_izq =[pygame.image.load("Nsprites/izq_1.png"), 
                pygame.image.load("Nsprites/izq_2.png"),
                pygame.image.load("Nsprites/izq_3.png"),
                pygame.image.load("Nsprites/izq_4.png"),]

Personaje_arr =[pygame.image.load("Nsprites/arr_1.png"), 
                pygame.image.load("Nsprites/arr_2.png"),
                pygame.image.load("Nsprites/arr_3.png"),
                pygame.image.load("Nsprites/arr_4.png"),]

Personaje_baj =[pygame.image.load("Nsprites/Principal.png"),
                pygame.image.load("Nsprites/baj_2.png"),
                pygame.image.load("Nsprites/baj_3.png"),
                pygame.image.load("Nsprites/baj_4.png"),]

#sonido
#Imagenes para cuando se pulsan ciertas teclas
#Sonido
sonido_arriba = pygame.image.load('sonidos/mas_volumen.png')
sonido_abajo = pygame.image.load('sonidos/menos_volumen.png')
sonido_mute = pygame.image.load('sonidos/mute_volumen.png')
sonido_max = pygame.image.load('sonidos/max_volumen.png')

x=0
px= 50
py= 200
ancho_= 40
velocidad= 10

"""CONTROL DE FPS"""
reloj= pygame.time.Clock()

#Variables dirección
izquierda= False
derecha = False
arriba= False
abajo= False

#Pasos 
cuentaPasos = 0

"""Movimiento"""

#Función para incluir el movimiento

def recargaPantalla():
    
    #Variable globales para poderlas utilizar dentro de esta función
    global cuentaPasos
    global x
    
    #Fondo en Movimiento
    #Aqui se puede poner estatico o en movimiento
    #Se incluye aqui, porque luego la función se llama en el 
    #bucle del juego 
    x_relativa= x% fondo.get_rect().width
    PANTALLA.blit(fondo,(x_relativa-fondo.get_rect().width,0))
    if x_relativa < ANCHO:
        PANTALLA.blit(fondo, (x_relativa,0))
    x-=5
    
    #Contador de pasos 
    #Lo que hace es un calculo para mostrar cada imagen de la lista
    #creada para los movimientos
    # El 4 depende de la cantidad e imagenes
    # Estos condicionales, es que basicamente, cada vez que se vaya moviendo
    # vaya incrementando el valor de cuenta pasos, e incrementando el valor de cuenta pasos
    #cuando sea igual a 4, es decir la cantidad de pasos de la animación
    # que vuelva a ser igual a 0, y vuelva una y otra vez a mostrar en bucle la animación
    #Osea si son "ifs" pero se reporoducen en bucle porque están dentro del bucle de juego
    if cuentaPasos +1 >=4: 
        cuentaPasos = 0
    """Movimiento a la izquierda"""
    #Aqui convierto las posiciones obtenidas en integer para que no me den floats, lo smimo
    #Con la división entera
    if izquierda:
        PANTALLA.blit(Personaje_izq[cuentaPasos//1], (int(px), int(py)))
        cuentaPasos +=1
        
      #"""Movimiento a la Derecha"""
    elif derecha:
        PANTALLA.blit(Personaje_der[cuentaPasos//1], (int(px), int(py)))
        cuentaPasos +=1
    
    elif abajo:
        PANTALLA.blit(Personaje_baj[cuentaPasos//1], (int(px),int(py)))
        cuentaPasos +=1
    
    elif arriba:
        PANTALLA.blit(Personaje_arr[cuentaPasos//1], (int(px), int(py)))
        cuentaPasos +=1
    
    else:
        PANTALLA.blit(quieto, (int(px),int(py)))

ejecutar= True

"""Bucle de acciones y controles"""
while ejecutar:
    #FPS
    reloj.tick(18)
    
    #Bucle del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutar = False
    
    #Opción tecla pulsada
    #Aquí especificamos las teclas, con esta varibale keys y dandole ese valor, lo que hacemos es
    #que realice las acciones manteniendo la tecla pulsada
    #si no se pone tocaría mover el personaje apretando y soltando
    # y eso daría una mala experiencia de juego
    keys = pygame.key.get_pressed()
    
    #Tecla left- movimiento a la izquierda
    #Se especifica que la flecha izquierda será para el movmiento
    #a la izquierda 
    #Lo que hace es poner la variable izquierda en true, y la derecha para que no entre
    # en conflicto es false 
    if keys[pygame.K_LEFT] and px > velocidad:
        px -= velocidad
        izquierda = True
        derecha = False
        arriba= False
        abajo= False

    
    #Tecla right - mov a la derecha
    #Aqui en la derecha es lo mismo, pero con la flecha derecha
    #aquí especifico unos margenes de tope para que el personaje no se salga de la pantalla
    elif keys[pygame.K_RIGHT] and px <750 - velocidad - ancho_:
        px += velocidad
        izquierda = False
        derecha = True
        arriba= False
        abajo= False
        
    #Tecla up, para mover hacia arriba
    #Se especifican unos margenes de límite
    elif keys[pygame.K_UP] and py >10:
        py -= velocidad
        izquierda = False
        derecha = False
        arriba= True
        abajo= False
    
    #Tecla down para abajo
    elif keys[pygame.K_DOWN] and py<500:
        py += velocidad
        izquierda = False
        derecha = False
        arriba= False
        abajo= True
    
    else:
        izquierda = False
        derecha = False
        arriba= False
        abajo= False
        cuentaPasos=0
    
    #SET = ESTABLECE/ASIGNA VALORES
    #GET= OBTIENE VALORES
    
    """CONTROL DEL AUDIO

    #Baja volumen
    #cONFIGURAMOS LA TECLA para bajar el volumen que en este caso es el menos 
    #ese pygame.mixer.get_volume el set especifica el volumen, aqui estamos es
    #obteniendo el valor del volumen que hay en ese momento de la musica, puede estar en 0.10, etc
    #vamos a obtener ese volumen
    #cuando se presione la tecla, mientras no este en mute, se ejecuta el codigo de ahí
    #que cambie el valor
    #obten el sonido y me decrementas en 0.01, es decir tenemos 100 niveles de sonido
    #si se pone 0.1 serian 10 niveles de volumen
    if keys[pygame.K_9] and pygame.mixer.music.get_volume() > 0.0:
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.01)
        PANTALLA.blit(menos_sonido,(850,25))
    #aqui hay una condición que mientras sea igual a 0 le diga al usuario con la imagen que ya esta min
    elif keys[pygame.K_9] and pygame.mixer.music.get_volume() == 0.0:
        PANTALLA.blit(mute_sonido,(850,25))
    
    SUBE VOLUMEN
    #Aqui es a la inversa, con la tecla +, mientras el valor no este en el maximo
    #ve incrementado en 0.01 el sonido y muestra la imagen de subir
    if keys[pygame.K_PLUS] and pygame.mixer.music.get_volume() < 1.0:
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume()+0.01)
        PANTALLA.blit(mas_sonido,(650,25))
        #cuando el valor sea 1, muestra el volumen max, mientras se este oprimiendo
        #si no estuviera esto se quedaría ahi la imagem
    elif keys[pygame.K_PLUS] and pygame.mixer.music.get_volume() == 1.0:
        PANTALLA.blit(max_sonido,(650,25))
    
        DESACTIVAR SONIDO
        #Cuando se obtenga el sonido en el momento de 0.0 osea nada aparezca la img mute
    elif keys [pygame.K_ASTERISK]:
        pygame.mixer.music.set_volume(0.0)
        PANTALLA.blit(mute_sonido,(650,25))
        
        REACTIVAR SONIDO
        #Cuando se obtenga el volumen sonido 1.0 osea todo, aparezca max img
    elif keys[pygame.K_SLASH]:
        pygame.mixer.music.set_volume(1.0)
        PANTALLA.blit(max_sonido, (650,25))"""
    
    # Control del audio
    #Baja volumen
    if keys[pygame.K_9] and pygame.mixer.music.get_volume() > 0.0:
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.01)
        PANTALLA.blit(sonido_abajo, (850, 25))
    elif keys[pygame.K_9] and pygame.mixer.music.get_volume() == 0.0:
        PANTALLA.blit(sonido_mute, (850, 25))

    #Sube volumen
    if keys[pygame.K_0] and pygame.mixer.music.get_volume() < 1.0:
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)
        PANTALLA.blit(sonido_arriba, (850, 25))
    elif keys [pygame.K_0] and pygame.mixer.music.get_volume() == 1.0:
            PANTALLA.blit(sonido_max, (850, 25))

    #Desactivar sonido
    elif keys[pygame.K_m]:
        pygame.mixer.music.set_volume(0.0)
        PANTALLA.blit(sonido_mute, (850, 25))

    #Reactivar sonido
    elif keys[pygame.K_COMMA]:
        pygame.mixer.music.set_volume(1.0)
        PANTALLA.blit(sonido_max, (850, 25))
        
    #Actualización de la pantalla
    #Dentro de la función la actualización, muy importante
    #para que se vaya actualizando
    pygame.display.update()  
    #LLAMADO A LA FUNCIÓN DE ACTUALIZACIÓN DE VENTANA
    recargaPantalla()

#Salida del juego
pygame.quit()
    