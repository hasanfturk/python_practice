#listede 170in üstünde sayfa sayısı olanları yazdır sayfa sayılarını topla

kitaplar = [
    ("Şeker Portakalı",180),
    ("Simyacı",184),
    ("1984",352),
    ("Hayvan Çiftliği",152)
]

toplam = 0

print("Sayfa sayısı 170ten fazla olan kitaplar:")
for kitap_adi,sayfa_sayisi in kitaplar:
    if sayfa_sayisi > 170:
        print(kitap_adi)
        toplam+=sayfa_sayisi

print()
print("Toplam sayfa sayısı:",toplam)