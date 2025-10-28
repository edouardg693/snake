from pyray import *

SIDE = 40 #largeur d'un carreau
WIDTH = 20
HEIGHT = 20

snake = [   #on représente le serpent
    [1,1],
    [2,1],
    [3,1],
]



init_window(SIDE * WIDTH, SIDE * HEIGHT, "Mon jeu") #ouvre une fenêtre
set_target_fps(10) #Nombre d'images par secondes

while not window_should_close(): #tant qu'on ferme pas la fenêtre
    begin_drawing() #ça commence à dessiner
    clear_background(BLACK)    
    
    if is_key_pressed(KEY_UP) :
        vitesse = [0,-1]
    if is_key_pressed(KEY_DOWN) :
        vitesse = [0,1]
    if is_key_pressed(KEY_RIGHT) :
        vitesse = [1,0]
    if is_key_pressed(KEY_LEFT) :
        vitesse = [-1,0]

    #DESSIN    
    for i, (x,y) in enumerate(snake):
        color = GREEN if i==len(snake)-1 else DARKGREEN
        draw_rectangle(x*SIDE+1,y*SIDE+1,SIDE-2,SIDE-2,color)
    
    #ANIMATION 
    vx,vy = vitesse
    hx,hy = snake[-1]
    new_head = [hx+vx, hy+vy]
    snake = snake[1:] + [new_head]

    

    end_drawing() #ça arrête de dessiner
    close_window()



