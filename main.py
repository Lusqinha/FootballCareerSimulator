from logic.game import CareerSimulator

language:str = ""

try:
    ...
    lang_opt = int(input("Language:\n [ 1 ] EN-US [ 2 ] PT-BR \n >>> "))
    
    if lang_opt == 1:
        language = "ENUS"
    elif lang_opt == 2:
        language = "PTBR"
    else:
        raise ValueError("Invalid language option")

    
except ValueError as e:
    print(e)
    

simulator = CareerSimulator(language=language)

