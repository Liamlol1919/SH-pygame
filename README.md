## 🤖🤖CHANGELOG HIER:

- im unterricht erstmal bisschen ausprobiert mit version control und herunterladen der template von sh-pygame.

- setup der readme und erste überlegungen für ein spiel

- auf fehler in template gestoßen: pygame.error: File is not a Windows BMP file 
-- pillow paket installiert , damit png und jpg unterstützt werden von pygame https://pillow.readthedocs.io/en/latest/handbook/tutorial.html

- egal hab vergessen zu pushen alles hab am letzten monatag noch etwas weiter gemacht ab hier kommt alles was ich heute (8.6.) gemacht habe

- so als idee habe ich das erstellen einer simplen 3d engine in pygame, um das spiel etwas anspruchsvoller zu gestalten.

spielideen:
~~als ziel des spiels gilt es auf einer 2d quadrat map das ziel auf der map zu finden. die einzelnen quadrate sind levels, in denen man zwischen 2d und 3d ansicht wechseln kann, um sie einfacher zu schaffen.~~
okay bessere idee das spiel ist primär 3d, wobei man eine 2d x mal y karte besitzt, wo man mit der welt interargieren kann. beispielsweise könnte man in der 2d ansicht eine brücke bauen oder bomben von oben abfallen lassen. hier gefällt mir noch nicht, dass man die maus für 2 modi braucht also nicht gleichzeitig die 2d karte und 3d welt steuern kann. ich könnte die 2d und 3d interaktionen so gestalten, dass man nicht oft wechseln muss.

die 2d karte ist hier auch ähnlich wie die der template vom anfang.

3d modi:
man kann nur springen, gehen, rennen und in alle richtungen schauen.

ideen für 2d interaktionen:
bomben fallen lassen
brücke bauen
fahrstuhl bauen
gewicht platzieren


3d engine brainstorming:

...... steht an am 15.6. oder vorher ....



# 🤩🤩🤩🤩🤩🤩Liam's Spiel
Fork von der [SH-pygame Template](https://github.com/istichel/SH-pygame). Ein (noch vielleicht) Python Spiel für den Informatik Unterricht.



### Installation auf Linux

Schritt 1:
Terminal öffnen und Repo klonen
```bash
git clone https://github.com/Liamlol1919/SH-pygame/tree/main
```

Schritt 2:
Virtuelle Umgebung aktivieren
```bash
source venv/bin/activate
```

Schritt 3:
Spiel starten
```bash
python starten.py
```


