def agirlikli_ortalama_hesapla(mt1,mt2,f):
    ortalama = (mt1 * 2/10 + mt2 * 35/100 + f*45/100)
    print(f"Ağırlıklı ortalama: {ortalama:.2f}")

    if ortalama < 50 or f < 20:
        print("Bütünlemeye kaldınız")
    else:
        print("geçtiniz")

agirlikli_ortalama_hesapla(30,30,30)
agirlikli_ortalama_hesapla(70,80,90)