class Tesla:
    #renk = "Beyaz"
    #batarya ="Uzun Menzil"
    #jant = 20
    #otopilot =  False

    GECERLI_RENKLER = ["Beyaz","Siyah","Kırmızı"]

    sis_fari = 2   #sınıf değişkeni

    def __init__(self,renk = "Beyaz",batarya = "Uzun Menzil",jant = 20,otopilot = False):
        # Eğer verilen renk geçerli değilse varsayılan olarak "Beyaz" ayarlanır
        if renk in Tesla.GECERLI_RENKLER:
            self.__renk = renk #nesne değişkeni
        else:
            self.__renk = "Beyaz"
        self.batarya = batarya #nesne değişkeni
        self.jant = jant #nesne değişkeni
        self.otopilot = otopilot #nesne değişkeni

    def goster_bilgi(self):
        print(f"Renk: {self.__renk},Batarya: {self.batarya},Jant: {self.jant},Otopilot: {self.otopilot}")

    def set_renk(self, yeni_renk):
        if yeni_renk in Tesla.GECERLI_RENKLER:
            self.__renk = yeni_renk
        else:
            print("Geçersiz Renk: ", yeni_renk)

    def get_renk(self):
        return self.__renk



benim_teslam = Tesla()
benim_teslam.set_renk("Kırmızı")

benim_teslam.goster_bilgi()

aysenin_teslası = Tesla()
aysenin_teslası.otopilot= True
aysenin_teslası.goster_bilgi()



print(benim_teslam.get_renk(),benim_teslam.batarya,benim_teslam.jant,benim_teslam.otopilot)

benim_teslam.jant = 21

print(benim_teslam.get_renk(),benim_teslam.batarya,benim_teslam.jant,benim_teslam.otopilot)

velinin_teslası = Tesla()
velinin_teslası.set_renk("Siyah")
velinin_teslası.otopilot = True

print(velinin_teslası.get_renk(),velinin_teslası.batarya,velinin_teslası.jant,velinin_teslası.otopilot)