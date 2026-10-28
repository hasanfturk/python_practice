sicaklik = float(input("Vücut sıcaklığını giriniz: "))

if sicaklik > 40:
    print("Çok yüksek ateş,acil müdahale gerekli!")
elif sicaklik > 39:
    print("Yüksek ateş!")
elif sicaklik > 38:
    print("Ateşi var.")
elif sicaklik > 37.2:
    print("Düşük ateş")
else:
    print("Normal vücut sıcaklığı.")