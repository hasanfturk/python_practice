def selamla(isim = "Misafir"):
    print("Merhaba:",isim)

selamla("Ahmet")
selamla()

#belirsiz sayıda parametre    *args
def toplama(*args):
    print(type(args))
    return sum(args)

print(toplama(1,2,3))