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
fgrösse = breite, höhe

# double buffer damit der frame erst im hintergrund gerendert wird
fenster = pygame.display.set_mode(fgrösse, DOUBLEBUF | OPENGL)

#titel
pygame.display.set_caption("2D-Karten-Grundgerüst (später mit 3D)")


karten_breite = 10
karten_höhe = 10
karten_daten = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 2, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]



#2d karte zeichnen funktion
def zeichne_2d_karte():
    # Orthografische Projektion (keine Perspektive)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, breite, höhe, 0, -1, 1)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Tiefentest ausschalten (Overlay ist alles)
    glDisable(GL_DEPTH_TEST)

    # Feldgröße berechnen
    feld_breite = breite / karten_breite
    feld_höhe = höhe / karten_höhe

    # Jedes Feld zeichnen
    for zeile in range(karten_höhe):
        for spalte in range(karten_breite):
            wert = karten_daten[zeile][spalte]








läuft = True
while läuft:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            läuft = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                läuft = False
            # Hier später die Bewegung/Interaktion einbauen
            # Im Moment noch keine Reaktion auf WASD etc.

    # Bildschirm löschen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # 2D-Karte zeichnen
    zeichne_2d_karte()

    # Frame anzeigen
    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
