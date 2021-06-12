import random

import sys
import pygame.draw
import time
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.mixer import *

from jupyter2D.Asteroid import Asteroid
from jupyter2D.Garbage import Garbage
from jupyter2D.Jupyter import Jupyter
from jupyter2D.Star import Star

if __name__ == '__main__':
    init(frequency=22050, size=-16, channels=2, buffer=4096)
    # music.load('../music/Billy\'s Sacrifice.mp3')  # https://dos88.itch.io/dos-88-music-library?download
    # music.play()

    # Configurações de tela
    size = (1366, 768)
    boxy = 0
    boxx = 0
    screen = pygame.display.set_mode(size, pygame.OPENGL | pygame.DOUBLEBUF)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(100, float(size[0]) / size[1], 10, 1000)
    glMatrixMode(GL_MODELVIEW)

    t = 0

    # Criação de objetos
    stars, asteroids, garbage = [], [], []
    for i in range(20):
        asteroids.append(Asteroid())
        garbage.append(Garbage())
    for i in range(100):
        stars.append(Star())
    jupyter = Jupyter()

    # Configurações (tamanho, posicoes, qtd)
    generate_obj = True
    max = 100
    tam_gar = [40, 50, 60]
    tam_ast = [20, 30]
    pos_stars_x, pos_stars_y = [], []
    pos_asteroids_x, pos_asteroids_y = [], []
    pos_garbage_x, pos_garbage_y = [], []

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
                    if boxx <= 0:
                        boxx = 0
                    else:
                        boxx -= 2
                elif ev.key == pygame.K_RIGHT:
                    if boxx >= 40:
                        boxx = 40
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

        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        jupyter.draw_jupyter_matrix(boxx, boxy)

        for s, x, y in zip(stars, pos_stars_x, pos_stars_y):
            s.draw_star_matrix(x, y, t)

        # Gerando posições com numeros aleatorios
        if generate_obj:
            for i in range(max):
                pos_garbage_x.append(random.randint(50, 100))
                pos_garbage_y.append(random.randint(-100, 50))

                pos_stars_x.append(random.randint(-100, 100))
                pos_stars_y.append(random.randint(-100, 100))

                pos_asteroids_x.append(random.randint(50, 100))
                pos_asteroids_y.append(random.randint(-100, 50))
            generate_obj = False

        i = 0
        for ast, gar in zip(asteroids, garbage):
            if ast.x < -50:
                ast.x = random.randint(50, 100)
            if gar.x < -50:
                gar.x = random.randint(50, 100)
            i += 1

        # 'Pintando' os objetos de acordo com as coordenadas geradas
        flag = True
        for a, x, y in zip(asteroids, pos_asteroids_x, pos_asteroids_y):
            if flag:
                a.draw_asteroid_matrix(x, y, tam_ast[0])
                flag = False
            else:
                a.draw_asteroid_matrix(x, y, tam_ast[1])
                flag = True

        for g, x, y in zip(garbage, pos_garbage_x, pos_garbage_y):
            for tam in tam_gar:
                g.draw_garbage_matrix(x, y, tam)

        pygame.display.flip()
        time.sleep(0.01)

