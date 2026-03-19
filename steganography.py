from PIL import Image


def mesaj_ascuns(imagine, mesaj, iesire):
    img = Image.open(imagine)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    print("Imagine deschisa cu succes!")

    copie = img.copy()
    latime, inaltime = img.size

    i = 0

    mesaj += '###'
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


def reveal_mesaj(imagine):
    img = Image.open(imagine)
    mesaj_binar = ""
    for linie in range(img.height):
        for coloana in range(img.width):
            pixel = img.getpixel((coloana, linie))
            for n in range(3):
                mesaj_binar += str(pixel[n] & 1)

    bits = [mesaj_binar[i:i + 8] for i in range(0, len(mesaj_binar), 8)]
    decodat = ''.join([chr(int(b, 2)) for b in bits])
    return decodat.split('###')[0]

mesaj_ascuns("imagine.png", "Mesaj secret!", "imagine_codificata.png")
print("Mesaj extras:", reveal_mesaj("imagine_codificata.png"))

def vizualizeaza_diferente(original, codificata, iesire):
    img_orig = Image.open(original)
    img_codif = Image.open(codificata)

    if img_orig.size != img_codif.size:
        print("Imaginile au dimensiuni diferite!")
        return

    latime, inaltime = img_orig.size
    viz = Image.new("RGB", (latime, inaltime), "black")

    for linie in range(inaltime):
        for coloana in range(latime):
            pixel_orig = img_orig.getpixel((coloana, linie))
            pixel_codif = img_codif.getpixel((coloana, linie))

            # Dacă există diferență în LSB, pixelul devine alb
            if any((pixel_orig[i] & 1) != (pixel_codif[i] & 1) for i in range(3)):
                viz.putpixel((coloana, linie), (255, 255, 255))

    viz.save(iesire)
    print(f"Imaginea cu diferențe a fost salvată în {iesire}!")

mesaj_ascuns("imagine.png", "Mesaj secret!", "imagine_codificata.png")
print("Mesaj extras:", reveal_mesaj("imagine_codificata.png"))
vizualizeaza_diferente("imagine.png", "imagine_codificata.png", "diferente.png")


