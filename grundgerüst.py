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

#frustrum definieren
gluPerspective(60, (breite / höhe), 0.1, 100.0)


#farbenliste mit zyklus
grau = (100,100,100)
farbenindex = 0
ListeVonFarben = [grau,"deeppink","blue","#ffffff"]

def farbenLoop():
    global farbenindex
    ausgabe = ListeVonFarben[farbenindex]
    farbenindex += 1

    if farbenindex == len(ListeVonFarben):
        farbenindex = 0

    return ausgabe

#hauptschleife:
läuft = True
while läuft == True:
    #schleife für alle ausgeführten events für die anzahl an events. dies passiert vor dem rendern des frames damit alles direkt mit opengl wird. pygame.event.get() entnimmt alle events aus der warteschlange (liste von objekten) wie zb ein tastendruck.
    for event in pygame.event.get():
        print(event)
        #exit event sollte die hauptschleife beenden
        if event.type == pygame.QUIT:
            läuft = False
        #tasten prüfen und bei escape schleife beenden
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print(f"{event.key} gedrückt") # zeigt auch alle maus bewegungen


                #neues bild anzeigen
                fenster.fill(farbenLoop())
                #um das neue bild zu sehen das bild updaten
                # pygame.display.flip() okay sollte eigentlich jeden frame passieren
            if event.key == pygame.K_ESCAPE:
                läuft = False


    #HIER sollte der opengl teil sein.

    #frame updaten und cpu kurz pause geben
    pygame.display.flip()
    pygame.time.wait(10)
#wenn die schleife nicht mehr läuft: ende
pygame.quit()
