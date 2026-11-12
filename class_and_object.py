class Tesla:
    renk = "Beyaz"
    batarya ="Uzun Menzil"
    jant = 20
    otopilot =  False

benim_teslam = Tesla()

print(benim_teslam.renk,benim_teslam.batarya,benim_teslam.jant,benim_teslam.otopilot)

benim_teslam.jant = 21

print(benim_teslam.renk,benim_teslam.batarya,benim_teslam.jant,benim_teslam.otopilot)

velinin_teslası = Tesla()
velinin_teslası.renk = "siyah"
velinin_teslası.otopilot = True

print(velinin_teslası.renk,velinin_teslası.batarya,velinin_teslası.jant,velinin_teslası.otopilot)
