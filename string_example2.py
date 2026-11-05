#slicing ve for döngüsüyle alınan kelimeyi ters çevir

kelime = input("Bir kelime giriniz:")
ters_kelime = kelime[::-1]
print(ters_kelime)

tersi = ""
for harf in kelime:
    tersi = harf + tersi

print(tersi)