import random
from pyray import *
from raylib import *
import time 

SIDE = 40  # largeur d'un carreau
WIDTH = 20
HEIGHT = 20

#PARAMETRES DE DEBUT DE PARTIE
snake = [   # on représente le serpent
    [1,1],
    [2,1],
    [3,1],
]
s = 0  # score
vitesse = [0,1]
fruit = [WIDTH//2, HEIGHT//2]
super_fruit = [random.randint(0, WIDTH-1),
                 random.randint(0, HEIGHT-1)]
compteur_super_fruit = 0
temps_super_fruit = 0
perdu = False
nb_fps = 60

init_window(SIDE * WIDTH, SIDE * HEIGHT, "Mon jeu")  # ouvre une fenêtre
set_target_fps(nb_fps)  # maintenant 60 images par seconde

# POUR FLUIDIFIER LE MOUVEMENT DU SERPENT
nbre_frame = 0        
pas_mouvement = 6  # fait que le serpent garde une vitesse assez lente malgré 60 FPS       

while not window_should_close():
    begin_drawing()
    clear_background(BLACK)
    
    # ECRAN DE FIN DE PARTIE, RELANCE DU JEU
    if perdu:
        draw_text("GAME OVER", (WIDTH * SIDE) // 8, (HEIGHT * SIDE) // 2 - 50, 100, RED)
        draw_text(f"Score : {s}", 5, 0, 50, WHITE)
        draw_text("Appuie sur une touche pour rejouer", 90, (HEIGHT * SIDE) // 2 + 50, 35, YELLOW)

        if get_key_pressed() != 0:
            snake = [[1,1], [2,1], [3,1]]
            s = 0
            vitesse = [0,1]
            fruit = [WIDTH//2, HEIGHT//2]
            super_fruit = [random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1)]
            compteur_super_fruit = 0
            temps_super_fruit = 0
            perdu = False
            nbre_frame = 0
            nb_fps = 60
        end_drawing()
        continue

    # DETECTION DES TOUCHES
    if is_key_pressed(KEY_UP) and vitesse != [0,1]:
        vitesse = [0,-1]
    if is_key_pressed(KEY_DOWN) and vitesse != [0,-1]:
        vitesse = [0,1]
    if is_key_pressed(KEY_RIGHT) and vitesse != [-1,0]:
        vitesse = [1,0]
    if is_key_pressed(KEY_LEFT) and vitesse != [1,0]:
        vitesse = [-1,0]

    # DESSIN
    for i, (x, y) in enumerate(snake):
        color = GREEN if i == len(snake) - 1 else DARKGREEN
        draw_rectangle(x * SIDE + 1, y * SIDE + 1, SIDE - 2, SIDE - 2, color)
    draw_rectangle(fruit[0] * SIDE, fruit[1] * SIDE, SIDE, SIDE, BLUE)
    draw_text(f"Score : {s}", 5, 0, 50, WHITE)
    if compteur_super_fruit >= 5 and temps_super_fruit < 5*nb_fps:
        draw_rectangle(super_fruit[0] * SIDE, super_fruit[1] * SIDE, SIDE, SIDE, YELLOW)
        temps_super_fruit += 1
    elif temps_super_fruit >= 5*nb_fps : #gestion du super fruit qui disparaît après 5 secondes
        compteur_super_fruit = 0
        temps_super_fruit = 0

    # REGLAGE DU MOUVEMENT DU SERPENT A 60 FPS
    nbre_frame += 1
    if nbre_frame < pas_mouvement:
        end_drawing()
        continue
    nbre_frame = 0  

    # ANIMATION ET COMPTAGE DU SCORE
    vx, vy = vitesse
    hx, hy = snake[-1]
    new_head = [hx + vx, hy + vy]

    if new_head == fruit:
        fruit = [random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)]
        snake = snake + [new_head]
        s += 10
        compteur_super_fruit += 1
    elif new_head == super_fruit:
        super_fruit = [random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)]
        snake = snake + [new_head]
        s += 100
        compteur_super_fruit = 0
        temps_super_fruit = 0
    else:
        snake = snake[1:] + [new_head]

    # JEU CIRCULAIRE ET CONDITION FIN DE PARTIE
    if new_head[0] < 0:
        new_head[0] = WIDTH
    elif new_head[0] >= WIDTH:
        new_head[0] = 0
    elif new_head[1] < 0:
        new_head[1] = HEIGHT
    elif new_head[1] >= HEIGHT:
        new_head[1] = 0
    elif new_head in snake[:-1]:
        perdu = True

    end_drawing()
