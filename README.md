# Instrument de Steganografie în Imagini (Python)

O aplicație Python care permite ascunderea și extragerea de mesaje text în/din imagini folosind tehnica LSB (Least Significant Bit). Proiectul demonstrează manipularea pixelilor la nivel de bit pentru a stoca informații fără a altera vizibil calitatea imaginii.

## Caracteristici Principale
* **Codificare LSB:** Modifică cel mai puțin semnificativ bit al componentelor RGB pentru a insera date binare.
* **Procesare Pixel-level:** Utilizează biblioteca Pillow (PIL) pentru accesul direct și modificarea valorilor pixelilor.
* **Managementul Integrității:** Salvează imaginile rezultate în format PNG (lossless) pentru a preveni pierderea datelor cauzată de compresie.
* **Sistem de Delimitare:** Folosește un cheie de tip delimitator ("###") pentru a identifica sfârșitul mesajului în timpul decodificării.
* **Modul de Vizualizare:** Include o funcție specială pentru a genera o hartă a diferențelor între imaginea originală și cea codificată, evidențiind pixelii modificați.

## Detalii Tehnice
* **Limbaj:** Python.
* **Biblioteci:** PIL (Pillow).
* **Concepte utilizate:**
    * **Bit Manipulation:** Operatori bitwise (&, |, ~) pentru inserarea datelor fără a afecta culorile perceptibile.
    * **Binary Conversion:** Transformarea caracterelor ASCII în șiruri de 8 biți.
    * **Image Conversion:** Asigurarea modului de culoare `RGB` pentru compatibilitatea algoritmului.

## Cum Funcționează
1. **Ascunderea:** Mesajul este convertit în binar. Fiecare bit este scris în locul ultimului bit al fiecărui canal de culoare (R, G, B) al pixelilor imaginii.
2. **Extragerea:** Programul citește ultimul bit al fiecărui canal și reconstruiește caracterele din grupuri de câte 8 biți până când întâlnește delimitatorul.
3. **Vizualizarea:** O a treia imagine este creată, unde pixelii modificați devin albi pe un fundal negru pentru a evidenția localizarea datelor ascunse.

## Configurare și Utilizare
1. Instalați biblioteca Pillow: "pip install Pillow".
2. Asigurați-vă că aveți o imagine de sursă numită "imagine.png".
3. Rulați scriptul: "python steganography.py".
4. Verificați mesajul extras în consolă și imaginile generate: "imagine_codificata.png" și "diferente.png".
