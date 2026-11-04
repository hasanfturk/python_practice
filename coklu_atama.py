#unpacking / destructuring

metin = "104, Ali, Çalışkan, 89"

numara, ad, soyad, ortalama = [parca.strip() for parca in metin.split(",")]

print("Numara:",numara,"\nAd:",ad,"\nSoyad:",soyad,"\nOrtalama:",ortalama)

list1 = [70,55,60]
not1,not2,not3 = list1
print(not1,not2,not3)