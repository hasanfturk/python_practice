
import random
"""#randint()
print(random.randint(0,100))
"""
#shuffle(list)

isimler = ["Ahmet","Ayşe","Mehmet","Can","Elif"]
print("Karıştırmadan önce:",isimler)
print("İsimler karıştırılıyor...")
random.shuffle(isimler)
print("Yeni sıralama:",isimler)