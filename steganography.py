from PIL import Image

def mesaj_ascuns(imagine, mesaj, iesire, key):
    img = Image.open(imagine)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    print("Imagine deschisa cu succes!")

    copie = img.copy()
    latime, inaltime = img.size

    i = 0

    mesaj += key
    mesaj_binar = ''.join([format(ord(char), '08b') for char in mesaj])

    for linie in range(inaltime):
        for coloana in range(latime):
            pixel = list(img.getpixel((coloana, linie)))
            for n in range(3):
                if i < len(mesaj_binar):
                    pixel[n] = pixel[n] & ~1 | int(mesaj_binar[i])
                    i += 1
            copie.putpixel((coloana, linie), tuple(pixel))
            if i >= len(mesaj_binar):
                break
        if i >= len(mesaj_binar):
            break
    copie.save(iesire, format='PNG')
    print(f"Mesaj ascuns in {iesire}!")

if __name__ == "__main__":
    imagine = input("Introdu numele fișierului de imagine : ")
    mesaj = input("Introdu mesajul pe care vrei să-l ascunzi: ")
    iesire = input("Introdu numele fișierului de ieșire : ")
    key = input("Introdu cheia secreta: ")

    mesaj_ascuns(imagine, mesaj, iesire, key)
    print("Mesajul a fost introdus cu succes!")
