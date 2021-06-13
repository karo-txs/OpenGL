import random

import sys
import pygame.draw
import time
from OpenGL.GL import *
from OpenGL.GLU import *

from pygame.mixer import *

from jupyter3D.Asteroid import Asteroid
from jupyter3D.Garbage import Garbage
from jupyter3D.Jupyter import Jupyter
from jupyter3D.Star import Star
from jupyter3D.scalable_cone import Cone

if __name__ == '__main__':
    init(frequency=22050, size=-16, channels=2, buffer=4096)
    # music.load('../music/Billy\'s Sacrifice.mp3')  # https://dos88.itch.io/dos-88-music-library?download
    # music.play()

    # Configurações de tela
    size = (1366, 768)
    boxy = 0
    boxx = 0
    screen = pygame.display.set_mode(size, pygame.OPENGL | pygame.DOUBLEBUF | GL_DEPTH)

    # Iluminação dos objetos
    especular = [1.0, 1.0, 1.0, 1.0]
    position = [0.0, 3.0, 1.0, 0.0]
    glShadeModel(GL_FLAT)
    glEnable(GL_COLOR_MATERIAL)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, especular)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 20.0)
    glLightfv(GL_LIGHT0, GL_SPECULAR, especular)
    glLightfv(GL_LIGHT0, GL_POSITION, position)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(50, size[0] / size[1], 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

    t = 0

    # Criação de objetos
    asteroids, garbage, cone = [], [], []
    for i in range(20):
        asteroids.append(Asteroid())
        garbage.append(Garbage())
        cone.append(Cone())
    jupyter = Jupyter()
    stars = Star()

    # Configurações (tamanho, posicoes, qtd)
    generate_obj = True
    max = 100
    tam_gar = [10, 20]
    tam_con = [2, 3]
    tam_ast = [8, 20]
    tam_ast2 = [30, 50]
    pos_stars_x, pos_stars_y = [], []
    pos_asteroids_x, pos_asteroids_y = [], []
    pos_garbage_x, pos_garbage_y, pos_garbage_z = [], [], []

    while True:
        t += 1
        # Controle de eventos do teclado
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                sys.exit()
            elif ev.type == pygame.KEYDOWN:
                if (ev.key == pygame.K_ESCAPE or
                        ev.key == pygame.K_q):
                    jupyter.draw_jupyter_matrix(boxx, boxy)
                elif ev.key == pygame.K_LEFT:
                    if boxx <= -40:
                        boxx = -40
                    else:
                        boxx -= 2
                elif ev.key == pygame.K_RIGHT:
                    if boxx >= 80:
                        boxx = 80
                    else:
                        boxx += 2
                elif ev.key == pygame.K_UP:
                    if boxy >= 10:
                        boxy = 10
                    else:
                        boxy += 2
                    jupyter.draw_jupyter_matrix(boxx, boxy)

                elif ev.key == pygame.K_DOWN:
                    if boxy <= -10:
                        boxy = -10
                    else:
                        boxy -= 2
                    jupyter.draw_jupyter_matrix(boxx, boxy)

                elif ev.key == pygame.K_a:
                    jupyter.draw_jupyter_matrix(50, 50)

        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        jupyter.draw_jupyter_matrix(boxx, boxy)

        # Gerando posições com numeros aleatorios
        if generate_obj:
            for i in range(max):
                pos_garbage_x.append(random.randint(50, 100))
                pos_garbage_y.append(random.randint(-100, 50))
                pos_garbage_z.append(random.randint(50, 100))

                pos_stars_x.append(random.randint(-100, 100))
                pos_stars_y.append(random.randint(-100, 100))

                pos_asteroids_x.append(random.randint(50, 100))
                pos_asteroids_y.append(random.randint(-100, 50))
            generate_obj = False

        stars.draw_star_matrix(pos_stars_x, pos_stars_y, t)

        i = 0
        for ast, gar, con in zip(asteroids, garbage, cone):
            if ast.x < -50:
                ast.x = random.randint(50, 100)
            if gar.x < -90:
                gar.x = random.randint(100, 200)
            i += 1

        # 'Pintando' os objetos de acordo com as coordenadas geradas
        flag = True
        for a, c, x, y in zip(asteroids, cone, pos_asteroids_x, pos_asteroids_y):
            if flag:
                a.draw_asteroid_matrix(x, y, tam_ast[0])
                a.draw_asteroid_matrix(x, y, tam_ast2[0])
                flag = False
            else:
                a.draw_asteroid_matrix(x, y, tam_ast[1])
                a.draw_asteroid_matrix(x, y, tam_ast2[1])
                flag = True

        flag = True
        for g, x, y, z in zip(garbage, pos_garbage_x, pos_garbage_y, pos_garbage_z):
            if flag:
                g.draw_garbage_matrix(x, y, z, tam_gar[0])
                flag = False
            else:
                g.draw_garbage_matrix(x, y, z, tam_gar[1])
                flag = True

        pygame.display.flip()
        time.sleep(0.001)
