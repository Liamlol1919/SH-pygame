## 🤖🤖CHANGELOG HIER:

3d engine brainstorming:

opengl für das 3d rendering nutzen

technische zusammenfassung:

pygame nutzen für die spiel logik und opengl für das rendering der 3d szene.
beispielsweise nutze ich pygame um tastatur input zu nehmen und dann positionen, funktionen und alles andere zu berechnen. visualisiert wird das in opengl (der 3d part) und die karte wird entweder mit opengl orthografischer projektion oder pygame.

https://www.pygame.org/docs/tut/PygameIntro.html

### schritt 1 leeres fenster und grobe logik für das spiel definieren

okay ich habe schon genug kommentare in 
```bash
leeresfenstertest.py
```
hinterlassen. es enthält noch kein opengl, aber die grundlegende logik des spiel frames besteht aus input anschauen -> spiellogik bearbeiten -> opengl ackern lassen -> frame zeichnen.

mal schauen ob ich heute noch weiter mache...:

tatsächlich 23:45 okay ich habe mir ein tutorial https://stackabuse.com/advanced-opengl-in-python-with-pygame-and-pyopengl/ angeschaut und das hilft mir sehr weiter die opengl logik ins spiel zu implementieren.
ich habe double buffer und das [Frustrum](https://de.wikipedia.org/wiki/Frustum) hinzugefügt, neue konzepte für mich.

-zwischenstand: habe kurz weiter angeschaut wie man opengl in pygame nutzen kann und habe die ersten schritte in grundgerüst.py gemacht. gute nacht.



# 🤩🤩🤩🤩🤩🤩Liam's Spiel
Fork von der [SH-pygame Template](https://github.com/istichel/SH-pygame). Ein Python Spiel für den Informatik Unterricht.



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

Schritt 4:
Benötigte Pakete installieren
```bash
pip install -r requirements.txt
```

Schritt 4:
Spiel starten
```bash
python starten.py
```


