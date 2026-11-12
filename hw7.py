#içinde kar kelimesi geçen stringleri string listesinden bulan program

def kar_filtrele(kelimeler):
    return[kelime for kelime in kelimeler if "kar" in kelime]

kelimeler = ["karpuz","elma","kardan adam","kayak","kar yağışı","güneşli hava"]

print(kar_filtrele(kelimeler))