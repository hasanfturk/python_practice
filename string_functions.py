metin = "Merhaba Python"

"""
print(metin.upper())

print(metin.lower())

print(len(metin))
"""

#capitalize() and title()
#print(metin.capitalize())
#print(metin.title())

#strip lstrip rstrip

metin = "    Merhaba Python    "
"""
print(metin.strip()+".")
print(metin.lstrip())
print(metin.rstrip()+".")"""

"""
metin = "Python güzeldir,Python öğren"
print(metin.replace("Python","Java"))

metin = "Python güzeldir,Python öğren,Python"
print(metin.replace("Python","Java",2))
"""

#split()
#metin = "Bir iki, üç dört"
#print(metin.split())
#print(metin.split(","))

#join
#liste = ["Bir","İki","üç","dört"]
#birlesik =" , ".join(liste)
#print(birlesik)

#find()
metin = "Hello Python, hello again"
print(metin.find("Python"))