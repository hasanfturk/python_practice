"""

#kullanıcıdan vücut sıcaklik degerini al(float),37ye (normal vucut sıcaklıgına) gore kıyasla

sicaklik = float(input("Vücut sıcaklıgınızı giriniz: "))

if sicaklik > 37:
    print("Dikkat, yüksek ateş!")
else:
    print("Normal vücut sıcaklığı.")

"""


#girilen tam sayiyi 0,pozitif ya da negatif olarak tanımla.

sayi = int(input("Bir tam sayı giriniz: "))

if sayi > 0:
    print("Sayı pozitiftir.")
elif sayi < 0:
    print("Sayı negatiftir.")
else:
    print("Sayı sıfırdır.")