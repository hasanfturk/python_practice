#kullanıcıdan başlangıç ve bitiş tam sayıları al.tek sayıları ve toplamını ekrana yazdır.

sayi1 = int(input("Ilk sayiyi giriniz: "))
sayi2 = int(input("Ikinci sayiyi giriniz: "))

toplam = 0

for sayi in range(sayi1,sayi2+1):
    if sayi%2 == 1:
        print(sayi)
        toplam += sayi

print("Sayıların toplamı:",toplam)