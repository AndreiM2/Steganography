from PIL import Image

def reveal_mesaj(imagine, key):
    try:
        img = Image.open(imagine)
    except FileNotFoundError:
        print(f"Eroare: Fișierul {imagine} nu a fost găsit.")
        return

    mesaj_binar = ""
    mesaj_final = ""
    terminat = False

    for linie in range(img.height):
        for coloana in range(img.width):
            pixel = img.getpixel((coloana, linie))
            for n in range(3):
                mesaj_binar += str(pixel[n] & 1)
                if len(mesaj_binar) % 8 == 0:  # S-a completat un caracter
                    caracter = chr(int(mesaj_binar[-8:], 2))
                    mesaj_final += caracter
                    if mesaj_final.endswith(key):
                        terminat = True
                        break
            if terminat:
                break
        if terminat:
            break

    if not terminat:
        print("Eroare: Cheia nu a fost găsită în imagine.")
        return

    return mesaj_final.split(key)[0]

if __name__ == "__main__":
    imagine = input("Introdu numele fișierului de imagine codificată: ")
    key = input("Introdu cuvântul cheie pentru delimitare: ")

    extras = reveal_mesaj(imagine, key)
    if extras is not None:
        print("Mesaj extras:", extras)
