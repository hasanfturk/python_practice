#bir sayı gir, o sayıya kadar olan fibonacci serisini yazdır

def fibonacci_yazdir():
    sayi = int(input("Bir sayı girin:"))

    if sayi<= 2:
        print("Lütfen 2'den büyük bir sayı giriniz.")
        return

    seri =[0,1]

    while True:
        sonraki = seri[-1] + seri[-2]

        if sonraki > sayi:
            break

        seri.append(sonraki)
                
    print("Fibonacci Serisi:",seri)

fibonacci_yazdir()