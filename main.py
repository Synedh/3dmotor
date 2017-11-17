import pygame
import pygame.locals as pl
import sys
from math import cos, sin
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

mouse_button_pressed = {}
keys_pressed = {}

# angle of rotation for the camera direction
angle = 0.0;
# actual vector representing the camera's direction
lx = 0.0
lz = -1.0
# XZ position of the camera
x = 0.0
z = 5.0
# the key states. These variables will be zero
# when no key is being presses
deltaAngle = 0.0
deltaMove = 0

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
    glColor3fv((1,1,1))
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

    # Points
    glPointSize(10)
    glColor3fv((1,1,1))
    glBegin(GL_POINTS)
    for verticie in verticies:
        glVertex3f(verticie[0], verticie[1], verticie[2])
    glEnd()


def computePos(deltaMove):
    global x, z, lx, lz
    x += deltaMove * lx * 0.1
    z += deltaMove * lz * 0.1


def computeDir(deltaAngle):
    global angle, lx, lz
    angle += deltaAngle
    lx = sin(angle)
    lz = -cos(angle)


def key_pressed(key, x, y):
    global keys_pressed, deltaAngle, deltaMove
    if key == b'\x1b':
        quit()
    print("Key pressed : {}, X : {}, Y: {}".format(key, x, y))
    keys_pressed[key] = True

    if key == 100:
        deltaAngle = -0.01
    if key == 101:
        deltaMove = 0.05
    if key == 102:
        deltaAngle = 0.01
    if key == 103:
        deltaMove = -0.05


def key_released(key, x, y):
    global keys_pressed, deltaAngle, deltaMove
    print("Key released : {}, X : {}, Y: {}".format(key, x, y))
    del keys_pressed[key]

    if key == 100 or key == 102:
        deltaAngle = 0.0
    if key == 101 or key == 103:
        deltaMove = 0.0


def mouse_pressed(key, state, x, y):
    global mouse_button_pressed, deltaAngle
    print("Key : {}, state : {}, X: {}, Y: {}".format(key, state, x, y))
    if state == GLUT_DOWN:
        mouse_button_pressed[key] = x, y
    else:
        if key == 2:
            deltaAngle = 0.0
        del mouse_button_pressed[key]


def mouse_move_while_pressed(x, y):
    global deltaAngle
    width, height = glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT)
    print('Key : {}, X : {}, Y : {}'.format(mouse_button_pressed, x, y))
    if 2 in mouse_button_pressed:
        print(x - mouse_button_pressed[2][0], y - mouse_button_pressed[2][1])
        if x - mouse_button_pressed[2][0] < 0:
            deltaAngle = 0.01
        else:
            deltaAngle = -0.01


def reshape (width, height):
    if height <= 1:
        height == 1
    glMatrixMode(GL_PROJECTION) # Switch to the projection matrix so that we can manipulate how our scene is viewed  
    glLoadIdentity() # Reset the projection matrix to the identity matrix so that we don't get any artifacts (cleaning up)  
    glViewport(0, 0, width, height) # Set our viewport to the size of our window  
    gluPerspective(45, width / height, 1.0, 100.0) # Set the Field of view angle (in degrees), the aspect ratio of our window, and the new and far planes  
    glMatrixMode(GL_MODELVIEW) # Switch back to the model view matrix, so that we can start drawing shapes correctly.


def display (): # Called on each iteration
    global deltaMove, deltaAngle, z, x, lx, lz
    if deltaMove:
        computePos(deltaMove)
        print(x, z, lx, lz)
    if deltaAngle:
        print(x, z, lx, lz)
        computeDir(deltaAngle)

    # Clear the color and depth buffers
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity();

    # print('ok')
    gluLookAt(x, 1.0, z,
              x + lx, 1.0, z + lz,
              0.0, 1.0, 0.0)

    # Loading objects
    cube()

    # Copy the off-screen buffer to the screen.
    glutSwapBuffers()
    glutPostRedisplay()


def main ():
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