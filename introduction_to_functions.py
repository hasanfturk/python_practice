"""
def fonksiyon_adi():
    işlem bloğu
"""




"""
def ekrana_yazma_fonksiyonu():
    print("Merhaba")
    print("Hoşgeldiniz")

ekrana_yazma_fonksiyonu()
"""


"""
def selamla(isim):
    print(type(isim))
    print("Merhaba",isim)
    print("Hoşgeldiniz...")


selamla("Ali")
"""



"""
def topla(a,b):
    print("Toplam:",a+b)

topla(4,6)


def carp(x,y):
    return x *y 

print(carp(3,4))
"""



x = 10  # global

def f():
    global x
    x = 20          # global xi değiştirir
    y = 5           # local 
    print("f içinde x:", x)
    print("f içinde y:", y)

f()
print("dışarıda x:", x)
# print(y)  # HATA: y sadece f içinde var