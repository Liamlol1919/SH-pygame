#grundgerüst.py

#geiles tutorial: https://stackabuse.com/advanced-opengl-in-python-with-pygame-and-pyopengl/

#importieren der essenziellen bibliotheken  - jetzt auch opengl
import pygame

from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


#fenster und pygame initialisieren
pygame.init()
#grössen als tuple
höhe = 300
breite = 600
fgrösse = breite,höhe

# double buffer damit der frame erst im hintergrund gerendert wird
fenster = pygame.display.set_mode(fgrösse, DOUBLEBUF|OPENGL)

#titel
pygame.display.set_caption("test test fenster fenster")



cubeVertices = ((1,1,1),(1,1,-1),(1,-1,-1),(1,-1,1),(-1,1,1),(-1,-1,-1),(-1,-1,1),(-1, 1,-1))
cubeEdges = ((0,1),(0,3),(0,4),(1,2),(1,7),(2,5),(2,3),(3,6),(4,6),(4,7),(5,6),(5,7))
cubeQuads = ((0,3,6,4),(2,5,6,3),(1,2,5,7),(1,0,4,7),(7,4,6,5),(2,3,0,1))

def wireCube():
    glBegin(GL_LINES)
    for cubeEdge in cubeEdges:
        for cubeVertex in cubeEdge:
            glVertex3fv(cubeVertices[cubeVertex])
    glEnd()


#kamerapositionen/config
kamera_x = 0
kamera_z = -5
fov = 60


#hauptschleife:
läuft = True
while läuft == True:
    #schleife für alle ausgeführten events für die anzahl an events. dies passiert vor dem rendern des frames damit alles direkt mit opengl wird. pygame.event.get() entnimmt alle events aus der warteschlange (liste von objekten) wie zb ein tastendruck.
    for event in pygame.event.get():

        #exit event sollte die hauptschleife beenden
        if event.type == pygame.QUIT:
            läuft = False
        #tasten prüfen und bei escape schleife beenden
        if event.type == pygame.KEYDOWN:

            #
            if event.key == pygame.K_w:

                kamera_z += 1
            if event.key == pygame.K_s:

                kamera_z -= 1
            if event.key == pygame.K_d:

                kamera_x -= 1
            if event.key == pygame.K_a:

                kamera_x += 1
            if event.key == pygame.K_ESCAPE:
                läuft = False


    #dieser code löscht den 2. buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


    glLoadIdentity()


    #frustrum definieren (jeden frame)
    gluPerspective(fov, (breite / höhe), 0.1, 100.0)

    # jeden frame die kamera neu positionieren (nach matrix reset von 0,0,0 aus)
    glTranslatef(kamera_x, 0, kamera_z)

    wireCube()
    #frame updaten und cpu kurz pause geben
    pygame.display.flip()
    pygame.time.wait(10)
#wenn die schleife nicht mehr läuft: ende
pygame.quit()
