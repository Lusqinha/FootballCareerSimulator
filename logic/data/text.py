# Exception in case of wrong choice in texts
class OptException(Exception):
    def __init__(self):
        super().__init__("[ERROR] The argument that you provided don't match with the options.")


class LangENUS:
    def __init__(self):
        self.COLORS:dict = {
            'clear': '\033[0m',
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
            }
        # Player starter info
        self.input_name:str = "Please, insert the name of your player: \n>>> "
        self.number:str = "Please, insert the number of your player: \n>>> "
        self.position:str = "Now, choose between the following positions: \n"
        self.nationality:str = "Wow! Nice choice, only two more steps. Choose between the following nationalities:\n"
        self.transfer_step:str = "Finally! The last question. Choose between the following transfer steps: \n"

        # System
        self.value_error:str = "[ERROR] Please, insert a valid number, if you inserted a letter, symbol or decimal number, please, try again."        
        self.successful:str = f"{self.COLORS['yellow']}[INFO]{self.COLORS['clear']} Your player has been successfully created! Now, we will proceed with the simulation.\n"
        

    # system
    def selectionInfo(self, selection:str):
         return f'{self.COLORS["yellow"]}[INFO]{self.COLORS["clear"]} {self.COLORS["green"]}{selection}{self.COLORS["clear"]} has been successfully selected.'
    
    def balanceInfo(self, total_salary:int):
        return f'{self.COLORS["yellow"]}[INFO]{self.COLORS["clear"]} The current balance is {self.COLORS["red"]}${total_salary} M{self.COLORS["clear"]}.'
    
    # system - transfers
    def firstTransfer(self, player_name:str, team:str):
        return f"{self.COLORS['blue']}[REVEAL]{self.COLORS['clear']} {self.COLORS['green']}{player_name}{self.COLORS['clear']} has been seen by a scout of {self.COLORS['red']}{team}{self.COLORS['clear']}, and now he is part of the team with a shining future ahead."
        
    def registerTransfer(self, player_name:str, team:str, year:int, salary:int):
        return f'{self.COLORS["blue"]}[TRANSFER]{self.COLORS["clear"]} {self.COLORS["green"]}{player_name}{self.COLORS["clear"]} has been transferred to {self.COLORS["red"]}{team}{self.COLORS["clear"]} in {self.COLORS["red"]}{year}{self.COLORS["clear"]} for {self.COLORS["red"]}{salary}M{self.COLORS["clear"]} per year. Good luck!'

    def registerRenewal(self, player_name, previous_team, year, salary):
        return f'{self.COLORS["blue"]}[RENEW]{self.COLORS["clear"]} {self.COLORS["green"]}{player_name}{self.COLORS["clear"]} has renewed his contract with {self.COLORS["red"]}{previous_team}{self.COLORS["clear"]} at {self.COLORS["red"]}{year}{self.COLORS["clear"]} for {self.COLORS["red"]}{salary} M{self.COLORS["clear"]} per year. You are a loyal player!'
        
    # Simulate transfers text's
    def renewOffer(self, player_name:str, team:str, year:int, offer_salary:int, previous_team:str, renewal_salary:int):
        
        text_offer = f'{self.COLORS["red"]}[OFFER]{self.COLORS["clear"]} {self.COLORS["green"]}{player_name}{self.COLORS["clear"]} has been offered a contract by {self.COLORS["red"]}{team}{self.COLORS["clear"]} for the year {self.COLORS["red"]}{year}{self.COLORS["clear"]} at an annual salary of {self.COLORS["red"]}${offer_salary}M{self.COLORS["clear"]}. However, the manager of {self.COLORS["red"]}{previous_team}{self.COLORS["clear"]} has extended a renewal offer of {self.COLORS["red"]}${renewal_salary}M{self.COLORS["clear"]} per year. To renew the contract, type {self.COLORS["red"]}n{self.COLORS["clear"]}. To accept the offer, type {self.COLORS["red"]}y{self.COLORS["clear"]}.'
            
        return text_offer

    def renewOfferOpt(self, player_name:str, opt:str):
        text_n:str = f"{self.COLORS['yellow']}[INFO]{self.COLORS['clear']} {self.COLORS['green']}{player_name}{self.COLORS['clear']} has declined the offer. The contract has been renewed."

        text_y:str = f"{self.COLORS['yellow']}[INFO]{self.COLORS['clear']} {self.COLORS['green']}{player_name}{self.COLORS['clear']} has accepted the offer, thus the previous contract has been terminated."
        
        output:str
        
        match opt:
            case "n":
                output = text_n
            case "y":
                output = text_y
            case _:
                output = f"{self.COLORS['yellow']}[INFO]{self.COLORS['clear']} {self.COLORS['green']}{player_name}{self.COLORS['clear']} didn't answer the offer, so the offer has been rejected. The contract has been renewed."
        
        return output

    def simpleOffer(self, player_name:str, team:str, offer_salary:int):
        text_offer = f'{self.COLORS["red"]}[OFFER]{self.COLORS["clear"]} {self.COLORS["green"]}{player_name}{self.COLORS["clear"]} has been offered a contract by {self.COLORS["red"]}{team}{self.COLORS["clear"]} for {self.COLORS["red"]}${offer_salary}M{self.COLORS["clear"]} per year. To accept the offer, type {self.COLORS["red"]}y{self.COLORS["clear"]}; to reject the offer, type {self.COLORS["red"]}n{self.COLORS["clear"]}.'

        return text_offer
        
    def simpleOfferOpt(self, player_name:str, opt:str):
        text_y:str = f"{self.COLORS['yellow']}[INFO]{self.COLORS['clear']} {self.COLORS['green']}{player_name}{self.COLORS['clear']} has accepted the offer, and the previous contract has been terminated."

        text_n:str = f"{self.COLORS['yellow']}[INFO]{self.COLORS['clear']} {self.COLORS['green']}{player_name}{self.COLORS['clear']} has rejected the offer. The contract has been renewed."
        
        output:str
        
        match opt:
            case "n":
                output = text_n
            case "y":
                output = text_y
            case _:
                output = f"{self.COLORS['yellow']}[INFO]{self.COLORS['clear']} {self.COLORS['green']}{player_name}{self.COLORS['clear']} didn't answer the offer, so the offer has been rejected. The contract has been renewed."

        return output


class LangPTBR:
    def __init__(self):
        self.COLORS:dict = {
            'clear': '\033[0m',
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
            }
        # Informações iniciais do jogador
        self.input_name: str = "Por favor, insira o nome do seu jogador: \n>>> "
        self.number: str = "Agora, insira o número do seu jogador: \n>>> "
        self.position: str = "Agora, escolha entre as seguintes posições: \n"
        self.nationality: str = "Ótima escolha! Só mais dois passos. Escolha entre as seguintes nacionalidades:\n"
        self.transfer_step: str = "Finalmente! A última pergunta. Escolha entre as seguintes etapas de transferência: \n"

        # Sistema
        self.value_error: str = "[ERRO] Por favor, insira um número válido. Se você inseriu uma letra, símbolo ou número decimal, tente novamente."
        self.successful: str = f"{self.COLORS['yellow']}[INFO]{self.COLORS['clear']} Seu jogador foi criado com sucesso! Agora, vamos prosseguir com a simulação.\n"

    # Sistema
    def selectionInfo(self, selection: str):
        return f'{self.COLORS["yellow"]}[INFO]{self.COLORS["clear"]} {self.COLORS["green"]}{selection}{self.COLORS["clear"]} foi selecionado com sucesso.'

    def balanceInfo(self, total_salary: int):
        return f'{self.COLORS["yellow"]}[INFO]{self.COLORS["clear"]} O saldo atual é {self.COLORS["red"]}R${total_salary}M{self.COLORS["clear"]}.'

    # Sistema - transferências
    def firstTransfer(self, player_name: str, team: str):
        return f"{self.COLORS['blue']}[REVELADO]{self.COLORS['clear']} {self.COLORS['green']}{player_name}{self.COLORS['clear']} foi visto por um olheiro do {self.COLORS['red']}{team}{self.COLORS['clear']}, e agora ele faz parte do time com um futuro brilhante pela frente."

    def registerTransfer(self, player_name: str, team: str, year: int, salary: int):
        return f'{self.COLORS["blue"]}[TRANSFERÊNCIA]{self.COLORS["clear"]} {self.COLORS["green"]}{player_name}{self.COLORS["clear"]} foi transferido para {self.COLORS["red"]}{team}{self.COLORS["clear"]} aos {self.COLORS["red"]}{year}{self.COLORS["clear"]} anos por {self.COLORS["red"]}R${salary}M{self.COLORS["clear"]}/ano. Boa sorte!'

    def registerRenewal(self, player_name, previous_team, year, salary):
        return f'{self.COLORS["blue"]}[RENOVAÇÃO]{self.COLORS["clear"]} {self.COLORS["green"]}{player_name}{self.COLORS["clear"]} renovou seu contrato com {self.COLORS["red"]}{previous_team}{self.COLORS["clear"]} em {self.COLORS["red"]}{year}{self.COLORS["clear"]} por {self.COLORS["red"]}R${salary}M{self.COLORS["clear"]}/ano. Lealdade é raro hoje em dia!'

    # Simular textos de transferências
    def renewOffer(self, player_name: str, team: str, year: int, offer_salary: int, previous_team: str, renewal_salary: int):
        text_offer = f'{self.COLORS["red"]}[OFERTA]{self.COLORS["clear"]} {self.COLORS["green"]}{player_name}{self.COLORS["clear"]} recebeu uma oferta de contrato do {self.COLORS["red"]}{team}{self.COLORS["clear"]} aos {self.COLORS["red"]}{year}{self.COLORS["clear"]} anos com um salário anual de {self.COLORS["red"]}R${offer_salary}M{self.COLORS["clear"]}. No entanto, o técnico do {self.COLORS["red"]}{previous_team}{self.COLORS["clear"]} fez uma oferta de renovação de {self.COLORS["red"]}R${renewal_salary}M{self.COLORS["clear"]}/ano. Para renovar o contrato, digite {self.COLORS["red"]}n{self.COLORS["clear"]}. Para aceitar a oferta, digite {self.COLORS["red"]}y{self.COLORS["clear"]}.'
        return text_offer

    def renewOfferOpt(self, player_name: str, opt: str):
        text_n: str = f"{self.COLORS['yellow']}[INFO]{self.COLORS['clear']} {self.COLORS['green']}{player_name}{self.COLORS['clear']} recusou a oferta. O contrato foi renovado."

        text_s: str = f"{self.COLORS['yellow']}[INFO]{self.COLORS['clear']} {self.COLORS['green']}{player_name}{self.COLORS['clear']} aceitou a oferta, assim o contrato anterior foi encerrado."

        output: str

        match opt:
            case "n":
                output = text_n
            case "y":
                output = text_s
            case _:
                output = f"{self.COLORS['yellow']}[INFO]{self.COLORS['clear']} {self.COLORS['green']}{player_name}{self.COLORS['clear']} não respondeu à oferta, então a oferta foi rejeitada. O contrato foi renovado."

        return output

    def simpleOffer(self, player_name: str, team: str, offer_salary: int):
        text_offer = f'{self.COLORS["red"]}[OFERTA]{self.COLORS["clear"]} {self.COLORS["green"]}{player_name}{self.COLORS["clear"]} recebeu uma oferta de contrato do {self.COLORS["red"]}{team}{self.COLORS["clear"]} por {self.COLORS["red"]}R${offer_salary}M{self.COLORS["clear"]}/ano. Para aceitar a oferta, digite {self.COLORS["red"]}y{self.COLORS["clear"]}; para rejeitar a oferta, digite {self.COLORS["red"]}n{self.COLORS["clear"]}.'
        return text_offer

    def simpleOfferOpt(self, player_name: str, opt: str):
        text_s: str = f"{self.COLORS['yellow']}[INFO]{self.COLORS['clear']} {self.COLORS['green']}{player_name}{self.COLORS['clear']} aceitou a oferta, e o contrato anterior foi encerrado."

        text_n: str = f"{self.COLORS['yellow']}[INFO]{self.COLORS['clear']} {self.COLORS['green']}{player_name}{self.COLORS['clear']} recusou a oferta. O contrato foi renovado."

        output: str

        match opt:
            case "y":
                output = text_s
            case "n":
                output = text_n
            case _:
                output = f"{self.COLORS['yellow']}[INFO]{self.COLORS['clear']} {self.COLORS['green']}{player_name}{self.COLORS['clear']} não respondeu à oferta, então a oferta foi rejeitada. O contrato foi renovado."

        return output