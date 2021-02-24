# Versión 2
# Este es un juego basado en adivinar una password de una lista de potenciales paswords
# generados por la computadora.
# Se muestra la lista de passwords posibles
# El jugador tiene permitido 1 intento para adivinar la password.
# El juego indica que el jugador falla al adivinar la password correcta.
# Independientemente de lo que el usuario introduzca;
# Se borra la pantalla
# Con mensajes centrados se muestra; la password introducida y tres mensajes de error.
# Espera a que el usuario pulse enter
# La ventana se cierra

from uagame import Window
from time import sleep
import os

# Creamos una ventana

ventana = Window('Hacking', 600, 500)
ventana.set_font_name('couriernew')
ventana.set_font_size(18)
ventana.set_font_color('green')
ventana.set_bg_color('black')

# Se inicializan variables

tiempo_espera = 0.5
x_coord = 0
nlineafin = 7
y_coord = 0
altura_texto = ventana.get_font_height()


def linea_inicio(linea):
    primera = linea * altura_texto
    return primera


def centrar_texto(linea, texto):
    primera = linea_inicio(linea)
    c_x = (ventana.get_width() - ventana.get_string_width(texto)) // 2
    c_y = (ventana.get_height() - primera) // 2
    if texto == "": c_x = 0  # "" para que funcione la verificacion

    ventana.draw_string(texto, c_x, c_y)
    ventana.update()
    print(sleep(tiempo_espera))


    linea -= 2

    return linea


def vt(texto: str, ycoord):
    if texto != 'DEBUG MODE':
        ycoord = ycoord + ventana.get_font_height()

    ventana.draw_string(texto, x_coord, ycoord)

    ventana.update()
    sleep(tiempo_espera)
    return ycoord


# display header
y_coord = vt('DEBUG MODE', 0)

# display intentos
y_coord = vt('1 ATTEMPT(S) LEFT', y_coord)

# display password
y_coord = vt("", y_coord)  # "" para que funcione la verificacion
y_coord = vt('PROVIDE', y_coord); y_coord = vt('SETTING', y_coord); y_coord = vt('CANTINA', y_coord); y_coord = vt('CUTTING', y_coord);
y_coord = vt('HUNTERS', y_coord); y_coord = vt('SURVIVE', y_coord); y_coord = vt('HEARING', y_coord); y_coord = vt('HUNTING', y_coord);
y_coord = vt('REALIZE', y_coord); y_coord = vt('NOTHING', y_coord); y_coord = vt('OVERLAP', y_coord); y_coord = vt('FINDING', y_coord);
y_coord = vt('PUTTING', y_coord)

# pedir contraseña
y_coord = vt("", y_coord)  # "" para que funcione la verificacion
y_coord = y_coord + ventana.get_font_height()
contrasena = ventana.input_string("ENTER PASSWORD >", 0, y_coord)

# end game
ventana.clear()

nlineafin = centrar_texto(nlineafin, contrasena)
nlineafin = centrar_texto(nlineafin, "")  # "" para que funcione la verificacion
nlineafin = centrar_texto(nlineafin, 'LOGIN FAILURE - TERMINAL LOCKED')
nlineafin = centrar_texto(nlineafin, "")  # "" para que funcione la verificacion
nlineafin = centrar_texto(nlineafin, 'PLEASE CONTACT AN ADMINISTRATOR')
nlineafin = centrar_texto(nlineafin, "")  # "" para que funcione la verificacion

centrar_x = (ventana.get_width() - ventana.get_string_width("PRESS ENTER TO EXIT")) // 2
centrar_y = (ventana.get_height() - linea_inicio(nlineafin)) // 2
ventana.input_string("PRESS ENTER TO EXIT", centrar_x, centrar_y)
ventana.close()

#   prompt for end
