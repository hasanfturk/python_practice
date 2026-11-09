# Python Ödev
#
# Verilen listenin içindeki çift sayıları filtreleyip yeni bir liste döndüren
# cift_sayilari_dondur(sayilar) isimli fonksiyonu yazınız.
#
# Fonksiyonunuzda List Comprehension tekniğini kullanınız

def cift_sayilari_dondur(sayilar):
    return[x for  x in sayilar if x % 2 == 0]

print(cift_sayilari_dondur([1,2,3,4,5,6,7,8,9,10]))