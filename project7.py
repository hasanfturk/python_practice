#1 ile 35 arasında sıcaklık değerlerinden 7 tane seç.listeyi ekrana yazdır.haftanın ortalama sıcaklığını hesapla

import random

sıcaklıklar = []

for i in range(7):
    sıcaklıklar.append(random.randint(1,35))

print("Haftalık sıcaklıklar:",sıcaklıklar)

ortalama = sum(sıcaklıklar) / len(sıcaklıklar)
print("Haftalık ortalama sıcaklık:",round(ortalama,2))