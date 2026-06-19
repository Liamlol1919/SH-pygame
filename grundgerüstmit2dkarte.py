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
    # erst mal die projektion auf 2d umstellen ohne 3d raum
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # links 0, rechts breite, oben 0, unten höhe -> weil y gegenteilig ist
    glOrtho(0, breite, höhe, 0, -1, 1)

    # modell matrix zurücksetzen
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # tiefentest aus, weil die karte immer im vordergrund sein soll sonst würde opengl vielleicht sachen verdecken die vorne sind
    glDisable(GL_DEPTH_TEST)

    # grösse von jedem kästchen ausrechnen
    # wenn das fenster grösser wird werden die kasten auch grösser
    feld_breite = breite / karten_höhe
    feld_höhe = höhe / karten_höhe

    # farben für die verschiedenen zahlen in der karte 0 = boden (hellgrau), 1 = wand (dunkelgrau), 2 grün = später als rgb
    farben = {
        0: (0.8, 0.8, 0.8),
        1: (0.3, 0.3, 0.3),
        2: (0.0, 0.8, 0.0),
    }
    # default ist rot falls andere zahlen dort sind
    default_farbe = (1.0, 0.0, 1.0)

    # schleifen durch alle zeilen und spalten erst zeilen und dann zeilen
    for zeile in range(karten_höhe):
        for spalte in range(karten_breite):
            # der wert ist der jeweilige farbenwert ua der matrix
            wert = karten_daten[zeile][spalte]

            # die obere linke ecke des kästchens in pixel koordinaten im fenster
            # spalte * feldbreite = x, zeile * feldhöhe = y
            x = spalte * feld_breite
            y = zeile * feld_höhe

            # farbe ausm dictionary holen oder default falls andere zahl
            farbe = farben.get(wert, default_farbe)

            #  gefülltes rechteck malen (aus 2 dreiecken)
            glColor3f(*farbe)  # stern operator entpackt das tuple in 3 args

            glBegin(GL_QUADS)
            # die vier ecken im uhrzeigersinn oder dagegen
            glVertex2f(x, y)                         # oben links
            glVertex2f(x + feld_breite, y)           # oben rechts
            glVertex2f(x + feld_breite, y + feld_höhe) # unten rechts
            glVertex2f(x, y + feld_höhe)             # unten links
            glEnd()

            # gitterlinie drumrum malen, damit man jedes feld sieht
            glColor3f(0.0, 0.0, 0.0)  # schwarz für die linien
            glLineWidth(1)            # dünne linie 1 pixel

            glBegin(GL_LINE_LOOP)     # linie die am ende wieder zum anfang geht
            glVertex2f(x, y)
            glVertex2f(x + feld_breite, y)
            glVertex2f(x + feld_breite, y + feld_höhe)
            glVertex2f(x, y + feld_höhe)
            glEnd()





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
