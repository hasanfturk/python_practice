#bölme ve çıkarma işlemi yapan iki fonksiyon,bölen 0sa uyarı

def bol(a,b):
    if b == 0:
        print("Bölen '0' olamaz")
        return "Hatalı işlem"
    else:
        c = a / b
    print(c)

def cikarma(x,y):
    z = x - y
    print(z)

bol(2,1)
cikarma(9,2)
print(bol(2,0))