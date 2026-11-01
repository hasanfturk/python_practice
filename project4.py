"""
isimler --> ali ece kaan mete batu veli ayşe
numaralar --> 145 178 164 175 185 180 134

öğrencilerle okul numaraları sıralı olarak eşleşmiştir

en yüksek ve düşük numaralı öğrenciyi ve numarasını yazdır
"""


isimler = ["Ali","Ece","Kaan","Mete","Batu","Veli","Ayşe"]
numaralar = [145,178,164,175,185,180,134]
"""
max_numara = 0
max_ogrenci = ""

for x in range(len(numaralar)):
    if numaralar[x] > max_numara:
        max_numara = numaralar[x]
        max_ogrenci = isimler[x]

print("\nEn yüksek okul numarası:",max_numara)
print("En yüksek okul numarasının sahibi:",max_ogrenci)

min_numara = 9**9
min_ogrenci = ""

for i in range(len(numaralar)):
    if numaralar[i] < min_numara:
        min_numara = numaralar[i]
        min_ogrenci = isimler[i]

print("\nEn düşük okul numarası:",min_numara)    
print("En düşük okul numarasının sahibi:",min_ogrenci,"\n")

"""


#2.yöntem
max_numara = max(numaralar)
max_index = numaralar.index(max_numara)
print(isimler[max_index])
print(max_numara)

min_numara = min(numaralar)
min_index = numaralar.index(min_numara)
print(isimler[min_index])
print(min_numara)