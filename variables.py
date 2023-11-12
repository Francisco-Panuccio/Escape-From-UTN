#Variables

""" General """
running = {"value": True} #Implica comenzar el programa
clock = {"value": 0} #Contador de Tiempo por segundo desde que el programa inicia
clock_two = {"value": 0} #Segundo Contador de Tiempo para Evitar Delay en Sonidos
rect_controller = {"value": True} #Desactiva la Colisión de Rectángulos
screamer_levels = {"value": False} #Screamer de Niveles Desactivado
data = {"Players": []} #Lista de Nombres y Puntajes de Jugadores para el Score Global

""" Main """
volume = True #Implica jugar con volumen
language = False #Implica jugar en Español
score = {"value": 666} #Puntaje Inicial
screamer = {"value": False} #Implica que no se activó el Screamer del Logo
play = {"value": "Main"} #Implica estar en la Pantalla Inicial
player = {"name": ""} #Nombre del Jugador

""" Nivel Uno """
ghostly_vision = {"value": False} #Visión Fantasmal Desactivada
crate_hit = {"value": 0} #Golpes dados a la Caja del Nivel 1
crate_states = [] #Lista que contendrá los distintos Sprites Crate
hammer_screw = {"value": False} #Implica que el Martillo/Destornillador del Nivel Uno está Desactivado
hammer_screw_used = {"value": False} #Implica que el Martillo/Destornillador del Nivel Uno no se utilizó
lock_states = [] #Lista que contendrá los distintos Sprites Lock
lock_condition = {"value": False} #Implica que el Candado se encuentra Cerrado

""" Nivel Dos """
level_two_check = {"value": "Board"} #Secuencia de objetos del Nivel Dos
level_two_image = {"value": ""} #Imagen a blitear de los anteriores objetos
code_door = {"value": ""} #Código de la Puerta
codelock_condition = {"value": False} #Implica que la Puerta con Contraseña se encuentra Cerrada

""" Nivel Tres """
final_timer = {"value": 60} #Temporizador para el Nivel Final
level_three_check = {"value": "Locker"} #Secuencia de objetos del Nivel Tres
timer_condition = {"value": False} #Temporizador Desactivado
good_ending = {"value": False} #Final Bueno Desactivado
return_main = {"value": False} #Volver al menú principal