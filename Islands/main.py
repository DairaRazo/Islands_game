#pgzero
import random

#Medidas de la pantalla y datos basicos
WIDTH = 1000
HEIGHT = 600
TITLE = "ISLANDS"
FPS = 30

#Objetos
background = Actor('mundo_principal',)
boat = Actor('boat',(850,280))
personaje_left = Actor('character1_left',(850,290))
personaje_normal = Actor('character1_standing',(650,200))
ganar = Actor('victory',)

#Isla de hielo
part1_winter = Actor('part1_winter',)
#Variables
estado_msg =  0 #Estado de las letras y numeros
obstacles_winter = 0
snowball_1_position_y = random.randint(5,550)
snowball_2_position_y = random.randint(5,550)
snowball_3_position_x = random.randint(10,900)
counter_obs_w = 0 #Contador de los obstaculos
counter_crystal = 0 #Contador de los cristales

snowball_1 = Actor('snowball',(10,snowball_1_position_y))
snowball_2 = Actor('snowball',(550,snowball_2_position_y))
snowball_3 = Actor('snowball',(snowball_3_position_x,0))

crystal = Actor('pink_crystal',(500,500))
game_over = Actor('game_over',)


#Dibujar los personajes
def draw():
    global estado_msg
    global counter_crystal
    
    if estado_msg == 0:
        background.draw()
        boat.draw()
        personaje_left.draw()
        
        #Numeros de las islas
        screen.draw.text("A", pos=(100,180), color="black", fontsize=70)
        screen.draw.text("B", pos=(330,500), color="black", fontsize=70)
        screen.draw.text("C", pos=(650,180), color="black", fontsize=70)
        screen.draw.text("D", pos=(750,450), color="black", fontsize=70)

    #Enumerar las islas
    elif estado_msg == 1:
        part1_winter.draw()
        personaje_normal.draw()
        snowball_1.draw()
        snowball_2.draw()
        snowball_3.draw()        
        crystal.draw()
        screen.draw.text(str(counter_crystal)+"/7", pos=(10, 10), color="black", fontsize = 30)
    elif estado_msg == 2:
        ganar.draw()
    
    elif estado_msg == 5:
        game_over.draw()


def update(dt):
    global estado_msg
    global personaje_normal
    global counter_obs_w
    global counter_crystal
    #Accion de acuerdo a la isla seleccionada
    if keyboard.A:
        estado_msg = 1
    
    #Movimiento de las bolas de nieve
    if snowball_1.x < 900:
        snowball_1.x += 7
        snowball_1.angle += 5
    else:
        snowball_1.y = random.randint(5,550)
        snowball_1.x = 10
        counter_obs_w += 1
    
    if snowball_2.x > 10:
        snowball_2.x -= 10
        snowball_2.angle += 8
    else:
        snowball_2.y = random.randint(5,550)
        snowball_2.x = 900
        counter_obs_w += 1
    
    if snowball_3.y < 600:
        snowball_3.y += 16
        snowball_3.angle += 14
    else:
        snowball_3.x = random.randint(10,900)
        snowball_3.y = 0
        counter_obs_w += 1
    
    #Movimiento del cristal
    if counter_obs_w == 7:
        crystal.x = random.randint(10,900)
        crystal.y = random.randint(10,550)
        counter_obs_w = 0
    
        
        
    #Movimiento del personaje
    if (keyboard.left or keyboard.A) and personaje_normal.x > 45:
        personaje_normal.image = 'character1_left'
        personaje_normal.x -= 12
    
    elif (keyboard.right or keyboard.D) and personaje_normal.x < 890:
        personaje_normal.image = 'character1_right'
        personaje_normal.x += 12
    
    elif (keyboard.down or keyboard.S) and personaje_normal.y < 550:
        personaje_normal.image = 'character1_standing'
        personaje_normal.y += 12
    
    elif (keyboard.up or keyboard.W) and personaje_normal.y > 45:
        personaje_normal.image = 'character1_turned'
        personaje_normal.y -= 12
    
    #Colisiones
    #Colisiones con los obstaculos
    if personaje_normal.colliderect(snowball_1) or personaje_normal.colliderect(snowball_2) or personaje_normal.colliderect(snowball_3):  
        estado_msg = 0
        counter_crystal = 0
    
    elif personaje_normal.colliderect(crystal):
        counter_crystal += 1
        crystal.x = random.randint(10,900)
        crystal.y = random.randint(10,550)
    
    if counter_crystal == 7:
        estado_msg = 2
        