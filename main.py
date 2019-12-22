perg = {
    "oi": "1",
    "oie": "1",
    "olá": "1",
    "ola": "1",
    "bom dia": "2",
    "dia bom": "2",
    "boa tarde": "4",
    "tarde boa": "4",
    "boa noite": "8",
    "noite boa": "8"
}

resp = {
    "1": "Oie ^^",
    "2": "Bom Dia",
    "3": "Oi, Bom Dia",
    "4": "Boa Tarde",
    "5": "Oi, Boa Tarde",
    "8": "Boa Noite",
    "9": "Oi, Boa Noite",
}

while True:
    user = input('Você: ')
    num = 0
    for i in perg:
        if i in user:
            num += int(perg[i])
    try:
        print('Mei: ' + resp[str(num)])
    except:
        print('Mei: Eu não Entendi')
        continue