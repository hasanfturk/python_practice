sinav_notlari = [70,80,90]
print(sinav_notlari)
print(type(sinav_notlari))

"""
sinav_notlari[0] = 95
print(sinav_notlari)
"""

print(len(sinav_notlari))

sinav_notlari.append(100)
print(sinav_notlari)

sinav_notlari.insert(1,98)
print(sinav_notlari)

notlar = [50,60]
sinav_notlari.extend(notlar)
sinav_notlari.extend([78])
print(sinav_notlari)

sinav_notlari.remove(50)
print(sinav_notlari)

kaldirilan_not = sinav_notlari.pop(0)
print("Kaldırılan not: ",kaldirilan_not)
print(sinav_notlari)

indeks = sinav_notlari.index(80)
print(indeks)

if 20 in sinav_notlari:
    print(sinav_notlari.index(20))
else:
    print("Bu not listede yok!")

print(sinav_notlari)

adet = sinav_notlari.count(100)
print(adet)

sinav_notlari.sort()
print(sinav_notlari)

sinav_notlari.reverse()
print(sinav_notlari)

sinav_notlari.clear()
print(sinav_notlari)