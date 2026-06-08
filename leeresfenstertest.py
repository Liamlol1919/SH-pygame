#importieren der essenziellen bibliotheken für eine leere pygame/opengl szene
import pygame

#fenster und pygame initialisieren
pygame.init()
#grössen als tuple
höhe = 300
breite = 600
fgrösse = breite,höhe

fenster =pygame.display.set_mode(fgrösse)

#titel
pygame.display.set_caption("test test fenster fenster")


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
