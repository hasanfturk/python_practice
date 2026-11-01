#menülü hesap makinesi,dört işlem olacak,5 girince çıkış,bölmede bölenin 0 olmamasına dikkat edilecek

while True:
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("\nÇıkış yapmak için '5' giriniz.")

    islem = int(input("Hangi işlemi yapmak istersiniz? (Numarasını giriniz.)"))

    if islem == 1:
        sayi1 = int(input("Birinci sayi:"))
        sayi2 = int(input("Ikinci sayi:"))
        print("İşlem sonucu:",sayi1+sayi2,"\n")
    elif islem == 2:
        sayi3 = int(input("Birinci sayi:"))
        sayi4 = int(input("Ikinci sayi:"))
        print("İşlem sonucu:",sayi3-sayi4)
    elif islem == 3:
        sayi5 = int(input("Birinci sayi:"))
        sayi6 = int(input("Ikinci sayi:"))
        print("İşlem sonucu:",sayi6*sayi5)
    elif islem == 4:
        sayi7 = int(input("Birinci sayi:"))
        sayi8 = int(input("Ikinci sayi:"))
        if sayi8 == 0:
            print("Sıfır bölen sayı olarak girilemez.")
            continue
        print("İşlem sonucu:",sayi7/sayi8)
    elif islem == 5:
        print("Programdan çıkılıyor...")
        break
    else:
        print("Hatalı seçim,yeniden deneyiniz.")