"""
kitaplar = [
    ("kitap1",100),
    ("kitap2",120),
    ("kitap3",290)]

for kitap_adi,sayfa_sayisi in kitaplar:
    print(kitap_adi,sayfa_sayisi)

"""

ogrenciler = {
    101:[70,80],
    102:[90,98],
    103:[67,78]
}

#print(ogrenciler)

for okul_no,sinav_notlari in ogrenciler.items():
    print(f"Okul no: {okul_no}")
    for notu in sinav_notlari:
        print(f" - Sınav Notu: {notu}")
    print()