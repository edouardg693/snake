import random
from pyray import *
from raylib import *
SIDE = 40 #largeur d'un carreau
WIDTH = 20
HEIGHT = 20

snake = [   #on représente le serpent
    [1,1],
    [2,1],
    [3,1],
]

s=0 #score


vitesse = [0,1]
fruit = [WIDTH//2,HEIGHT//2]
super_fruit = [random.randint(0,WIDTH-1),
                 random.randint(0,HEIGHT-1)]
compteur_super_fruit = 0
perdu = False

init_window(SIDE * WIDTH, SIDE * HEIGHT, "Mon jeu") #ouvre une fenêtre
set_target_fps(10) #Nombre d'images par secondes

while not window_should_close(): #tant qu'on ferme pas la fenêtre
    begin_drawing() #ça commence à dessiner
    clear_background(BLACK)    
    
    #DETECTION DES TOUCHES
    if is_key_pressed(KEY_UP) and vitesse != [0,1] :
        vitesse = [0,-1]
    if is_key_pressed(KEY_DOWN) and vitesse != [0,-1]:
        vitesse = [0,1]
    if is_key_pressed(KEY_RIGHT) and vitesse != [-1,0]:
        vitesse = [1,0]
    if is_key_pressed(KEY_LEFT) and vitesse != [1,0]:
        vitesse = [-1,0]

    #DESSIN    
    for i, (x,y) in enumerate(snake):
        color = GREEN if i==len(snake)-1 else DARKGREEN
        draw_rectangle(x*SIDE+1,y*SIDE+1,SIDE-2,SIDE-2,color)
    draw_rectangle(fruit[0]*SIDE,fruit[1]*SIDE,SIDE,SIDE,BLUE)
    draw_text(f"Score : {s}",5,0,50,WHITE) 
    if compteur_super_fruit == 3 :
        draw_rectangle(super_fruit[0]*SIDE,super_fruit[1]*SIDE,SIDE,SIDE,YELLOW)
        compteur_super_fruit = 0
    #ANIMATION 
    vx,vy = vitesse
    hx,hy = snake[-1]
    new_head = [hx+vx, hy+vy]
    if new_head == fruit :
        fruit = [random.randint(0,WIDTH-1),
                 random.randint(0,HEIGHT-1)]
        snake = snake + [new_head]
        s=s+10
        compteur_super_fruit +=1
       
    elif new_head == super_fruit :
        super_fruit = [random.randint(0,WIDTH-1),
                 random.randint(0,HEIGHT-1)]
        snake = snake + [new_head]
        s=s+100

        
    else : 
        snake = snake[1:] + [new_head]

    #FIN DE PARTIE

    if new_head[0]<0 :
        new_head[0]=WIDTH
    elif new_head[0]>=WIDTH :
        new_head[0]=0
    elif new_head[1]<0 :
        new_head[1]= HEIGHT
    elif new_head[1]>=HEIGHT :
        new_head[1]=0
    elif new_head in snake[:-1] :
        draw_text("GAME OVER",(WIDTH*SIDE)//8,(HEIGHT*SIDE)//2,100,RED)


    end_drawing() #ça arrête de dessiner




"""score
game over
fruit circulaire
super fruit
jeu circulaire"""