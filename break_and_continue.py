"""for sayi in range(1,11):
    if sayi == 5:
        print("Döngü 'break' ile sonlandırıldı.")
        break
    print(sayi)
"""



#3 sayısı yazdırılmayacak , döngü kaldığı yerden devam edecek
for x in range(1,11):
    if x == 3:
        continue
    print(x)