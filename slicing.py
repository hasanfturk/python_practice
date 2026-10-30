"""
meyveler = ["elma","armut","muz","çilek","kiraz","şeftali"]

#orta_meyveler = meyveler[2:5] #2. indexten 5. indexe kadar elemanları al (5. dahil değil)
#print(orta_meyveler)

ilk_uc = meyveler[:3] #meyveler[0:3]
son_uc = meyveler[-3:] #sondan üç elemanı al
print(ilk_uc)
print(son_uc)

cift_indeksli = meyveler[::2] #baştan sona çift katlı indeksliler
print(cift_indeksli)

ters_meyveler = meyveler[::-1]
print(ters_meyveler)

meyveler_kopya = meyveler[::] #meyveler.copy()
"""


#SLICING STRINGS
kelime = "Merhaba"
ilk_uc_harf = kelime[:3]
print(ilk_uc_harf)

ters_kelime = kelime[::-1]
print(ters_kelime)

kelime_2 = kelime[::2]
print(kelime_2)

kelime_3 = kelime[2:4]
print(kelime_3)