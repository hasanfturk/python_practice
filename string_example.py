#cümleyi full büyük harf yap,kelimeleri ters sırala

cumle = input("Lütfen bir cümle giriniz:")

cumle = cumle.upper()
print(cumle)

kelimeler = cumle.split()
kelimeler.reverse() 

bosluk = " "
yeni_cumle = bosluk.join(kelimeler)

print(yeni_cumle)