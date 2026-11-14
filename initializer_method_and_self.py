class Tesla:
    #renk = "Beyaz"
    #batarya ="Uzun Menzil"
    #jant = 20
    #otopilot =  False

    sis_fari = 2   #sınıf değişkeni

    def __init__(self,renk = "Beyaz",batarya = "Uzun Menzil",jant = 20,otopilot = False):
        self.renk = renk #nesne değişkeni
        self.batarya = batarya #nesne değişkeni
        self.jant = jant #nesne değişkeni
        self.otopilot = otopilot #nesne değişkeni

    def goster_bilgi(self):
        print(f"Renk: {self.renk},Batarya: {self.batarya},Jant: {self.jant},Otopilot: {self.otopilot}")



benim_teslam = Tesla()

benim_teslam.goster_bilgi()

aysenin_teslası = Tesla()
aysenin_teslası.otopilot= True
aysenin_teslası.goster_bilgi()



print(benim_teslam.renk,benim_teslam.batarya,benim_teslam.jant,benim_teslam.otopilot)

benim_teslam.jant = 21

print(benim_teslam.renk,benim_teslam.batarya,benim_teslam.jant,benim_teslam.otopilot)

velinin_teslası = Tesla()
velinin_teslası.renk = "siyah"
velinin_teslası.otopilot = True

print(velinin_teslası.renk,velinin_teslası.batarya,velinin_teslası.jant,velinin_teslası.otopilot)
