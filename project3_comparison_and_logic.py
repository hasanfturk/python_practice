sayi = int(input("Bir tam sayı giriniz: "))

if sayi > 20 and sayi % 2 == 1:
    print(sayi, "20den büyük bir tek sayıdır.")
else:
    print(f"{sayi} istenilen kriterleri karşılamıyor.")