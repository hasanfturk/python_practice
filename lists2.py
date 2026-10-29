"""
otel_zinciri1 = ["Antalya","İzmir"]
otel_zinciri2 = ["İstanbul","Ankara"]

abc_turizm = [otel_zinciri1,otel_zinciri2]
print(abc_turizm[0][1])
"""


"""
liste1 = ["Ali", 20,[50,70,90]]
liste1[2][0] = 100
print(liste1)

alt_liste1 = liste1[2]
print(alt_liste1)

#negatif index numarasıyla sondan sırasıyla -1,-2,-3 ... şeklinde düşünerek veriye ulaşabilirsin
print(alt_liste1[-1])

print(liste1[len(liste1)-1])
"""


#in operatörü ,bir elemanın bir veri yapısında olup olmadığını kontrol eder.
meyveler = ["elma","muz","erik","çilek"]

if "elma" in meyveler:
    print("elma listede var")
else:
    print("elma listede yok")