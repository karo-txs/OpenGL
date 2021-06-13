import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
import random

vertices = ((1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1), (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1))
edges = ((0, 1), (0, 3), (0, 4), (2, 1), (2, 3), (2, 7), (6, 3), (6, 4), (6, 7), (5, 1), (5, 4), (5, 7))
surfaces = ((0, 1, 2, 3), (3, 2, 7, 6), (6, 7, 5, 4), (4, 5, 1, 0), (1, 5, 7, 2), (4, 0, 3, 6))
blink = False


def cube():
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x += 1
            glColor3fv(blink_colors()[x])
            glVertex3fv(vertices[vertex])
    glEnd()
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glTranslatef(0, 0, -5)
    flag = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    flag = not flag
                elif event.key == pygame.K_b:
                    global blink
                    blink = not blink
        if flag:
            glRotatef(1, 0, 1, 1)
        else:
            glRotatef(0, 0, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        cube()
        pygame.display.flip()
        pygame.time.wait(10)


colors = [[1, 1, 0], [0, 0, 1], [1, 0, 0], [0, 0, 0], [1, 1, 1], [0, 1, 0],
          [0, 1, 1], [0, 1, 0], [1, 1, 0], [1, 0, 1], [1, 1, 0], [0, 1, 0]]


def blink_colors():
    global colors
    if blink:
        for i in range(len(colors)):
            for j in range(len(colors[i])):
                x = random.randint(0, 1)
                colors[i][j] = x
    return colors


if __name__ == "__main__":
    # type 'r' to rotate the cube and 'b' to change colors
    main()
