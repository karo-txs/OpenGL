import pygame

from OpenGL.GL import *
import random


vertices = ((1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1), (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1))
edges = ((0, 1), (0, 3), (0, 4), (2, 1), (2, 3), (2, 7), (6, 3), (6, 4), (6, 7), (5, 1), (5, 4), (5, 7))
surfaces = ((0, 1, 2, 3), (3, 2, 7, 6), (6, 7, 5, 4), (4, 5, 1, 0), (1, 5, 7, 2), (4, 0, 3, 6))

blink = False
flag = False
a = 1
x = 0
y = 1
z = 1


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


def start(window):
    glPushMatrix()
    glTranslatef(0, 0, -5)
    global a
    global x
    global y
    global z
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                global flag
                flag = not flag
            elif event.key == pygame.K_b:
                global blink
                blink = not blink
    if flag:
        a += 1
        x += 0
        y += 1
        z += 1
        glRotatef(a, x, y, z)
    else:
        glRotatef(a, x, y, z)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    cube()
    window.flip()
    pygame.time.wait(10)
    glPopMatrix()


# colors = [[1, 1, 0], [0, 0, 1], [1, 0, 0], [0, 0, 0], [1, 1, 1], [0, 1, 0], [0, 1, 1], [0, 1, 0], [1, 1, 0], [1, 0, 1],
#            [1, 1, 0], [0, 1, 0]]
# colors = [[1, 1, 1], [0, 0, 0], [1, 0, 0], [0, 1, 0], [1, 0, 0], [1, 0, 0], [0, 1, 1], [0, 0, 0], [0, 0, 1], [1, 0, 1],
#           [0, 0, 1], [0, 1, 0]]
colors = [[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 0, 0], [1, 1, 0], [1, 1, 1], [1, 1, 1], [0, 1, 1],
          [0, 0, 0], [1, 0, 0]]


def blink_colors():
    if blink:
        for i in range(len(colors)):
            for j in range(len(colors[i])):
                x = random.randint(0, 1)
                colors[i][j] = x
    print(colors)
    return colors
