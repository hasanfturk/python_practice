#girilen cümlede seçilen harf kaç defa geçiyor

cumle = input("Lütfen bir cümle giriniz:").lower()
harf = input("Istediginiz harfi giriniz:").lower()

sayac = 0

for h in cumle:
    if harf == h:
        sayac += 1

print(f"'{harf}' harfi cumlede {sayac} defa geçiyor.")