import pygame
import pygame.locals as pl
import sys
from math import cos, sin
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from camera import Camera

mouse_button_pressed = []
keys_pressed = {}
camera = Camera()

colors = [
    (0,1,0),
    (1,0.5,0),
    (1,0,0),
    (1,1,0),
    (0,0,1),
    (1,0,1)
]

verticies = [
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
]

edges = [
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
]

surfaces = [
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
]

def text_ui(text, x, y):
    glColor3f(1,1,1)
    glWindowPos2s(x,y);
    for i in text:
        glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord(i))

def cube ():
    # Surfaces
    glBegin(GL_QUADS)
    for i, surface in enumerate(surfaces):
        for vertex in surface:
            glColor3fv(colors[i])
            glVertex3fv(verticies[vertex])
    glEnd()

    # Line
    glLineWidth(2)
    glColor3f(1,1,1)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

    # Points
    glPointSize(10)
    glColor3f(1,1,1)
    glBegin(GL_POINTS)
    for verticie in verticies:
        glVertex3f(verticie[0], verticie[1], verticie[2])
    glEnd()


def axis():
    glLineWidth(2)
    glBegin(GL_LINES)
    glColor3f(1,0,0)
    glVertex3f(-1000,0,0)
    glVertex3f(1000,0,0)
    glColor3f(0,1,0)
    glVertex3f(0,-1000,0)
    glVertex3f(0,1000,0)
    glColor3f(0,0,1)
    glVertex3f(0,0,-1000)
    glVertex3f(0,0,1000)
    glEnd()

    glColor3f(1,1,1)
    glPointSize(10)
    glBegin(GL_POINTS)
    glVertex3f(0, 0, 0)
    glEnd()


def key_pressed(key, x, y):
    if key == b'\x1b':
        quit()
    print("Key pressed : {}, X : {}, Y: {}".format(key, x, y))
    keys_pressed[key] = True


def key_released(key, x, y):
    print("Key released : {}, X : {}, Y: {}".format(key, x, y))
    del keys_pressed[key]


def mouse_pressed(key, state, x, y):
    global mouse_button_pressed
    print("Key : {}, state : {}, X: {}, Y: {}".format(key, state, x, y))
    if state == GLUT_DOWN:
        mouse_button_pressed.append([key, x, y, x, y])
    else:
        mouse_button_pressed.pop(-1)


def mouse_move_while_pressed(x, y):
    width, height = glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT)
    key = [mouse_button_pressed[-1][0], mouse_button_pressed[-1][3], mouse_button_pressed[-1][4], x, y]
    mouse_button_pressed[-1] = key
    if key[0] == 2:
        if key[1] < key[3]:
            camera.lookAt(1, 0)
        if key[1] > key[3]:
            camera.lookAt(-1, 0)
    print('Key : {}'.format(mouse_button_pressed[-1]))


def reshape(width, height): # Called when window is reshaped
    if height <= 1:
        height == 1
    glMatrixMode(GL_PROJECTION) # Switch to the projection matrix so that we can manipulate how our scene is viewed  
    glLoadIdentity() # Reset the projection matrix to the identity matrix so that we don't get any artifacts (cleaning up)  
    glViewport(0, 0, width, height) # Set our viewport to the size of our window  
    gluPerspective(45, width / height, 1.0, 100.0) # Set the Field of view angle (in degrees), the aspect ratio of our window, and the new and far planes  
    glMatrixMode(GL_MODELVIEW) # Switch back to the model view matrix, so that we can start drawing shapes correctly.


def display(): # Called on each iteration
    # Clear the color and depth buffers
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Load camera
    camera.update(keys_pressed)
    camera.draw()

    # Load objects
    cube()
    axis()
    glPointSize(10)
    glColor3f(1,1,1)
    glBegin(GL_POINTS)
    glVertex3f(camera.lx, camera.ly, camera.lz)
    glEnd()
    text_ui("Camera: {}, {}, {}".format(round(camera.x, 2), round(camera.y, 2), round(camera.z, 2)), 10, glutGet(GLUT_WINDOW_HEIGHT) - 20)
    text_ui("View: {}, {}, {}".format(round(camera.lx, 2), round(camera.ly, 2), round(camera.lz, 2)), 10, glutGet(GLUT_WINDOW_HEIGHT) - 35)

    # Copy the off-screen buffer to the screen.
    glutSwapBuffers()
    glutPostRedisplay()


def main():
    glutInit(sys.argv)

    # Create a double-buffer RGBA window.   (Single-buffering is possible. So is creating an index-mode window.)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

    # Create a window
    glutInitWindowPosition(100,100)
    glutInitWindowSize(800, 800)
    glutCreateWindow('3D Motor')

    # Set display, reshape, keyboard and mouse callbacks
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(key_pressed)
    glutSpecialFunc(key_pressed)
    glutKeyboardUpFunc(key_released)
    glutSpecialUpFunc(key_released)
    glutMouseFunc(mouse_pressed)
    glutMotionFunc(mouse_move_while_pressed)

    glutIgnoreKeyRepeat(1)

    # Enable depth test
    glEnable(GL_DEPTH_TEST)

    # Run the GLUT main loop until the user closes the window.
    glutMainLoop()

main()