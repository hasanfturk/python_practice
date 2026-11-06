# key - value (anahtar - değer) ilişkisi tutar

ogrenciler_dict = {100:"Ali Kaya",101:"Zeynep Dağ"}

"""
print(ogrenciler_dict[101])

print(ogrenciler_dict.get(101))
deger = print(ogrenciler_dict.get(102)) #hata vermez,none değeri döner

if deger is None:
    print("Yeniden deneyiniz.")

liste = list(ogrenciler_dict.keys())
print(liste)
"""

ogrenciler_dict[105] = "Kaan Ak"
print(ogrenciler_dict)

ogrenciler_dict.pop(105) #del ogrenciler_dict[105]
print(ogrenciler_dict)

ogrenciler_dict = {100:"Ali Kaya",101:"Zeynep Dağ",103:[90,78,89]}
print(ogrenciler_dict)