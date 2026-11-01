"""
sayi = 0
toplam = 0

while sayi < 10:  #1den 9a kadar sayıların toplamı
    toplam+= sayi
    sayi+=1
    

print(toplam)
"""

"""
while True:
    sayi = int(input("Lütfen bir tam sayı giriniz (çıkmak için -1 giriniz)"))

    if sayi == -1:
        print("Programdan çıkılıyor")
        break

    sayinin_karesi = sayi*sayi
    print(f"{sayi} sayısının karesi :",sayinin_karesi)
"""


while True:
    sayi = int(input("Lütfen bir tam sayı giriniz (çıkmak için -1 giriniz)"))

    if sayi == -1:
        print("Programdan çıkılıyor")
        break

    #sayinin_karesi = sayi*sayi
    print(f"{sayi} sayısının karesi : {sayi*sayi}")