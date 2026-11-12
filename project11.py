#sayı tahmin oyunu

import random

def oyun():

    hedef = random.randint(1,100)
    hak = 7

    print("1 ile 100 arasında  bir sayı tahmin edin.7 hakkınız var.")

    while hak > 0:
        giris = input(f"Kalan hakkınız: {hak} , Tahmininiz:")

        if not giris.isdigit():
            print("Lütfen bir sayı girin.")
            continue

        tahmin = int(giris)

        if tahmin < 1 or tahmin> 100:
            print("Lütfen 1 ile 100 arasında bir sayı girin.")
            continue

        if tahmin == hedef:
            print("Tebrikler,doğru tahmin ettiniz !")
            return

        elif tahmin<hedef:
            print("Daha büyük bir sayı girin.")

        else:
            print("Daha küçük bir sayı girin.")

        hak -=1

    print(f"Bilemediniz,Sayı '{hedef}' idi")


while True:
    oyun()

    while True:
        cevap = input("Tekrar oynamak ister misiniz? (E/H) : ").strip().upper()
        if cevap == "E" or cevap == "H":
            break
        print("Lütfen 'E' ya da 'H' yazınız.") #evet hayır


    if cevap == "H":
        print("Oyun sona erdi.")
        break