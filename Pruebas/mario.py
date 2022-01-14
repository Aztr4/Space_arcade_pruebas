from PIL.Image import Image
import arcade
from pyglet import window

#Constantes
ANCHO= 1000
ALTO=500
TITULO = "Mario Demo"

#Constantes para escalar los sprites
PERSONAJE_SCALING= 0.17
GROUND_SCALING= 0.20
CYLINDER_SCALING= 0.20

#Declarar una clase
#Me permite dicujar la pantalla
class MiProyecto(arcade.Window):
    
    def __init__(self):
        super().__init__(ANCHO,ALTO,TITULO)
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        #Listas que van a contener nuestros sprites 
        self.coin_list = None
        self.wall_list = None
        self.player_list = None
        
        #Definir una variable que va a contener el sprite del jugador
        self.player_sprite = None
             
    #Después se crean dos funciones
    
    #Esta setup, se utiliza para sprites o niveles si fuese el caso
    def setup(self):
        #Se inicializan las listas a objeto spritelist para controlar el movimiento
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        
        #Crear el jugador
        Image_source= "sprites/Principal.png"
        self.player_sprite = arcade.Sprite(Image_source, PERSONAJE_SCALING)
        self.player_sprite.center_x = 64  #Aqui se le da un eje x y y
        self.player_sprite.center_y = 93
        self.player_list.append(self.player_sprite) #Se agrega el sprite a la lista
        
        #Crear el piso
        for x in range(8,1250,64):
            wall = arcade.Sprite("sprites/ground.png", GROUND_SCALING)
            wall.center_x=x
            wall.center_y= 32
            self.wall_list.append(wall)
        
        #Crear los cilindros con una lista
        coordinate_list= [[215,110],[256,110],[768,110]]
        
        for coordinate in coordinate_list:
            wall = arcade.Sprite("sprites/crater.png", CYLINDER_SCALING)
            wall.position = coordinate
            self.wall_list.append(wall)
                        
    
    #Motor que empieza a dibujar y pintar lo definido en setup
    def on_draw(self):
        arcade.start_render()
        
        self.player_list.draw()
        self.wall_list.draw()

#Funcion principal donde se crea la ventana, se corre setup y el motor
def main():
    window = MiProyecto()
    window.setup()
    arcade.run()
    
#Correr la funcion principal, aqui se corre lo haya en main
if __name__=="__main__":
    main()