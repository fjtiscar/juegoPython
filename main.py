import pyglet
from Juego import Juego
from pyglet.window import key

#Creamos la clase ventana para mostrar nuestro juego, le pasamos 2 objetos
class Ventana(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_location(400,100)
        self.frame_rate = 1/60.0
        #Llamamos a nuestra imagen de la nave y se la pasamos al jugador
        self.jugador = Juego(500,100, 'nave.png')
        self.fondo = Juego(0,0, 'espacio.jpg')


        #img = pyglet.image.load('nave.png')
        #self.jugador = pyglet.sprite.Sprite(img, x=500, y=200)

    #Cuando presione una tecla de movimiento, nos mueva nuestra nave a la pocisión de la tecla que hemos pulsado
    def on_key_press(self, tecla1, tecla2):
        if tecla1 == key.RIGHT:
            self.jugador.velx = 300
        if tecla1 == key.LEFT:
            self.jugador.velx = -300

    #Nos mueve nuestra nave 1 posición, sin este método la nave seguiria recorriendo el mapa de izquierda a derecha
    def on_key_release(self, tecla1, tecla2):
        if tecla1 in (key.RIGHT, key.LEFT):
            self.jugador.velx = 0


    def on_draw(self):
        self.clear()
        self.fondo.draw()
        self.jugador.draw()

    def update(self, dt):
        self.jugador.update(dt)

#Condición para que compruebe en que tipo de ventana estamos y que nos pinte una interfaz de 1200x900
if __name__ =="__main__":
    window = Ventana(1200, 600, "Space Invaders", resizable=False)
    pyglet.clock.schedule_interval(window.update, window.frame_rate)
    pyglet.app.run()