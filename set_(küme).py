"""
dersler_set = {"tarih","matematik","fizik"}
print(dersler_set) #unordered(sırasız) tutulur

dersler_set = {"tarih","tarih","matematik","fizik"}
print(dersler_set) #unordered(sırasız) tutulur

#set veri yapısı mutabledır
dersler_set.add("kimya")
print(dersler_set)

dersler_set.remove("tarih")
print(dersler_set)
"""

muhendislik_dersleri = {"tarih","fizik","kimya"}
sanat_dersleri = {"tarih","resim","müzik"}

ortak_dersler = muhendislik_dersleri.intersection(sanat_dersleri)
print(ortak_dersler)

muh_fark = muhendislik_dersleri.difference(sanat_dersleri)
print(muh_fark)

birlesim = muhendislik_dersleri.union(sanat_dersleri)
print(birlesim)