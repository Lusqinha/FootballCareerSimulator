from random import randint
import json
from logic.randomizer import RandomSupplies

# Exceptions

class PositionException(Exception):
    def __init__(self):
        super().__init__("[ERROR] The position you provided is not valid. Please, try again.")
        
class NationalityException(Exception):
    def __init__(self):
        super().__init__("[ERROR] The nationality you provided is not valid. Please, try again.")
        
class TransferStepException(Exception):
    def __init__(self):
        super().__init__("[ERROR] The transfer step you provided is not valid. Please, try again.")

TEAMS = []

with open("logic/data/teams.json", "r") as file:
    TEAMS = json.load(file)

# Colors
COLORS = {
            'clear': '\033[0m',
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
            
}

# Positions, nationalities and transfer steps
POSITIONS = ["goalkeeper", "defender", "midfielder", "striker"]
NATIONALITIES = ["european", "south american", "african", "asian", "north american"]
TRANSFER_STEPS = [2, 3]

# Max ages
MAX_AGES = {
    2: 38,
    3: 42
}



""" This class will be used to create a soccer player object.
    The soccer player object will have the following attributes:
        - name
        - number
        - position
        - nationality
        - apps (appearances)
        - goals (reduce for goalkeepers and defenders, increase for strikers)
        - assists (increase for midfielders and strikers)
        - yellow cards (increase for defenders and midfielders)
        - red cards (increase for defenders and midfielders)
        - clean sheets (for goalkeepers)
        - League titles
        - Champions League titles
        - World Cup titles
        - Ballon d'Ors
        - Puskas Awards
    
    The soccer player will list the teams he has played for and the years he played for them, like the example below:
        [{
            "team": "Real Madrid",
            "year": 09,
            "salary": 100 # in millions per year
        },
        {
            "team": "Manchester United",
            "year": 10,
            "salary": 150 # in millions per year
        }]
"""
class SoccerPLayer:
    def __init__(self, name:str, number:str, position:str, nationality:str, transfer_step=2):
        # Basic attributes
        self.name:str = name
        self.number:str = number
        self.position:str = position
        self.nationality:str = nationality
        self.age:int = 18
        self.retirement_age:int = MAX_AGES[transfer_step]
        
        # Transfer attributes
        self.transfer_step:int = transfer_step
        self.total_transfers:int = 0
        self.transfer_history:list = []
        self.total_salary:int = 0
        
        # Only declared, not initialized
        self.apps:int
        self.goals:int
        self.assists:int
        self.yellow_cards:int
        self.red_cards:int
        self.clean_sheets:int
        self.league_titles:int
        self.champions_league_titles:int
        self.world_cup_titles:int
        self.ballon_dors:int
        self.puskas_awards:int
        
            
    # This method will be used to update the player's Transfer History. Provide the team, year and salary in millions per year.
    def registerTransference(self, team:str, year:int, salary:int):
        if self.total_transfers == 0:
            print(f"{COLORS['blue']}[REVEAL]{COLORS['clear']} {COLORS['green']}{self.name}{COLORS['clear']} has been seen by a scout of {COLORS['red']}{team}{COLORS['clear']}, now he is part of the team and a shining future awaits him.")
        self.transfer_history.append({
            "team": team,
            "year": year,
            "salary": salary
        })
        self.total_transfers += 1
        self.age += self.transfer_step
        self.total_salary += salary*self.transfer_step
        print(f'{COLORS["blue"]}[TRANSFER]{COLORS["clear"]} {COLORS["green"]}{self.name}{COLORS["clear"]} has been transferred to {COLORS["red"]}{team}{COLORS["clear"]} at {COLORS["red"]}{year}{COLORS["clear"]} for {COLORS["red"]}{salary}M{COLORS["clear"]} per year. Good luck!')
        # Print total salary
        print(f'{COLORS["yellow"]}[INFO]{COLORS["clear"]} The current balance is {COLORS["red"]}€{self.total_salary}M{COLORS["clear"]}.')
    
    def registerRenewal(self, salary:int=0):
        if salary == 0:
            salary = self.transfer_history[-1]["salary"]
            
        self.transfer_history.append({
            "team": self.transfer_history[-1]["team"],
            "year": self.transfer_history[-1]["year"],
            "salary": salary
        })
        self.total_transfers += 1
        self.age += self.transfer_step
        self.total_salary += salary*self.transfer_step
        print(f'{COLORS["blue"]}[RENEW]{COLORS["clear"]} {COLORS["green"]}{self.name}{COLORS["clear"]} has renewed his contract with {COLORS["red"]}{self.transfer_history[-1]["team"]}{COLORS["clear"]} at {COLORS["red"]}{self.transfer_history[-1]["year"]}{COLORS["clear"]} for {COLORS["red"]}{salary}M{COLORS["clear"]} per year. You are a loyal player!')
        # Print total salary
        print(f'{COLORS["yellow"]}[INFO]{COLORS["clear"]} The current balance is {COLORS["red"]}{self.total_salary}M{COLORS["clear"]}.')
    # Return the player's transfer history
    def getTransferHistory(self):
        return self.transfer_history
    
    # Return the value of the player's salary in millions
    def setTotalSalary(self):
        for transfer in self.transfer_history:
            self.total_salary += transfer["salary"]
        return self.total_salary
    
    
    
# This class will be used to simulate a career of a soccer player.   
class CareerSimulator:
    def __init__(self):
        self.player:SoccerPLayer
        self.gameTitle:str = f"""{COLORS['red']}
  ██████  ▒█████   ▄████▄   ▄████▄  ▓█████  ██▀███        ▄████▄   ▄▄▄       ██▀███  ▓█████ ▓█████  ██▀███         ██████  ██▓ ███▄ ▄███▓
▒██    ▒ ▒██▒  ██▒▒██▀ ▀█  ▒██▀ ▀█  ▓█   ▀ ▓██ ▒ ██▒     ▒██▀ ▀█  ▒████▄    ▓██ ▒ ██▒▓█   ▀ ▓█   ▀ ▓██ ▒ ██▒     ▒██    ▒ ▓██▒▓██▒▀█▀ ██▒
░ ▓██▄   ▒██░  ██▒▒▓█    ▄ ▒▓█    ▄ ▒███   ▓██ ░▄█ ▒     ▒▓█    ▄ ▒██  ▀█▄  ▓██ ░▄█ ▒▒███   ▒███   ▓██ ░▄█ ▒     ░ ▓██▄   ▒██▒▓██    ▓██░
  ▒   ██▒▒██   ██░▒▓▓▄ ▄██▒▒▓▓▄ ▄██▒▒▓█  ▄ ▒██▀▀█▄       ▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██▀▀█▄  ▒▓█  ▄ ▒▓█  ▄ ▒██▀▀█▄         ▒   ██▒░██░▒██    ▒██ 
▒██████▒▒░ ████▓▒░▒ ▓███▀ ░▒ ▓███▀ ░░▒████▒░██▓ ▒██▒ ██▓ ▒ ▓███▀ ░ ▓█   ▓██▒░██▓ ▒██▒░▒████▒░▒████▒░██▓ ▒██▒ ██▓ ▒██████▒▒░██░▒██▒   ░██▒
▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ░▒ ▒  ░░ ░▒ ▒  ░░░ ▒░ ░░ ▒▓ ░▒▓░ ▒▓▒ ░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░░░ ▒░ ░░░ ▒░ ░░ ▒▓ ░▒▓░ ▒▓▒ ▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ░  ░
░ ░▒  ░ ░  ░ ▒ ▒░   ░  ▒     ░  ▒    ░ ░  ░  ░▒ ░ ▒░ ░▒    ░  ▒     ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ░  ░ ░ ░  ░  ░▒ ░ ▒░ ░▒  ░ ░▒  ░ ░ ▒ ░░  ░      ░
░  ░  ░  ░ ░ ░ ▒  ░        ░           ░     ░░   ░  ░   ░          ░   ▒     ░░   ░    ░      ░     ░░   ░  ░   ░  ░  ░   ▒ ░░      ░   
      ░      ░ ░  ░ ░      ░ ░         ░  ░   ░       ░  ░ ░            ░  ░   ░        ░  ░   ░  ░   ░       ░        ░   ░         ░   
                  ░        ░                          ░  ░                                                    ░                                  
        {COLORS['clear']}"""
        
        self.msgGoodLuck:str = f"""{COLORS['green']}
   ▄██████▄   ▄██████▄   ▄██████▄  ████████▄        ▄█       ███    █▄   ▄████████    ▄█   ▄█▄ 
  ███    ███ ███    ███ ███    ███ ███   ▀███      ███       ███    ███ ███    ███   ███ ▄███▀ 
  ███    █▀  ███    ███ ███    ███ ███    ███      ███       ███    ███ ███    █▀    ███▐██▀   
 ▄███        ███    ███ ███    ███ ███    ███      ███       ███    ███ ███         ▄█████▀    
▀▀███ ████▄  ███    ███ ███    ███ ███    ███      ███       ███    ███ ███        ▀▀█████▄    
  ███    ███ ███    ███ ███    ███ ███    ███      ███       ███    ███ ███    █▄    ███▐██▄   
  ███    ███ ███    ███ ███    ███ ███   ▄███      ███▌    ▄ ███    ███ ███    ███   ███ ▀███▄ 
  ████████▀   ▀██████▀   ▀██████▀  ████████▀       █████▄▄██ ████████▀  ████████▀    ███   ▀█▀ 
                                                   ▀                                 ▀         
        {COLORS['clear']}"""
               
        self.startGame()
        self.simulateCareer()
    
    def printSelection(self, toSelect:list):
        selector_string:str = f"" 
        pos_counter:int = 0
        for pos in toSelect:
            pos_counter += 1
            selector_string += f'[{COLORS["blue"]} {pos_counter} {COLORS["clear"]}] {COLORS["red"]}{str(pos).title()}{COLORS["clear"]} '
        selector_string += f'{COLORS["clear"]}'

        return selector_string
    
    def printSuccessfulSelection(self, selection:str):
        print(f'{COLORS["yellow"]}[INFO]{ COLORS["clear"]} {COLORS["green"]}{selection}{COLORS["clear"]} has been successfully selected.')
    
    def matchPosition(self, position:int):
        match position:
            case 1:
                position = POSITIONS[0]
            case 2:
                position = POSITIONS[1]
            case 3:
                position = POSITIONS[2]
            case 4:
                position = POSITIONS[3]
            case _:
                raise PositionException
            
    def matchNationalities(self, nationality:int):
        match nationality:
            case 1:
                nationality = NATIONALITIES[0]
            case 2:
                nationality = NATIONALITIES[1]
            case 3:
                nationality = NATIONALITIES[2]
            case 4:
                nationality = NATIONALITIES[3]
            case 5:
                nationality = NATIONALITIES[4]
            case _:
                raise NationalityException
                
    def matchTransferStep(self, transfer_step:int):
        match transfer_step:
            case 1:
                transfer_step = TRANSFER_STEPS[0]
            case 2:
                transfer_step = TRANSFER_STEPS[1]
            case _:
                raise TransferStepException
           
    def startGame(self):
        print(str(self.gameTitle))
        try:
            positions_string:str = self.printSelection(POSITIONS)
            nationality_string:str = self.printSelection(NATIONALITIES)
            transfer_step_string:str = self.printSelection(TRANSFER_STEPS)
            
            # User declarations
            name:str = str(input("Please, insert the name of your player: \n>>> ")).title()
            self.printSuccessfulSelection(name)
            
            number:int = int(input("Please, insert the number of your player: \n>>> "))
            self.printSuccessfulSelection(number)
            
            position:int = int(input(f"Now, choose between the following positions: \n{positions_string}\n>>> "))
            self.matchPosition(position)
            self.printSuccessfulSelection(POSITIONS[position-1])
            
            nationality:int = int(input(f"Wow! Nice choice, only two more steps. Choose between the following nationalities:\n{nationality_string} \n>>> "))
            self.matchNationalities(nationality)
            self.printSuccessfulSelection(NATIONALITIES[nationality-1])
            
            transfer_step = int(input(f"Finally! The last question. Choose between the following transfer steps: \n{transfer_step_string} \n>>> "))
            self.matchTransferStep(transfer_step)
            self.printSuccessfulSelection(TRANSFER_STEPS[transfer_step-1])

            # Create the player
            self.player = SoccerPLayer(
                name, 
                number,
                position,
                nationality
            )          
            
        except ValueError:
            print("[ERROR] Please, insert a valid number, if you inserted a letter, symbol or decimal number, please, try again.")
            return False
        except PositionException as e:
            print(e)
            return False
        except NationalityException as e:
            print(e)
            return False
        except TransferStepException as e:
            print(e)
            return False

        else:
            print(f"{COLORS['yellow']}[INFO]{COLORS['clear']} Your player has been successfully created! Now, we will proceed with the simulation.\n ")
            print(self.msgGoodLuck)
    
    def simulateTransfer(self):
        
        rs = RandomSupplies(TEAMS)
        
        first_team:bool = True if self.player.total_transfers == 0 else False
        renewal_offer:bool = True if self.player.total_transfers > 0 and randint(1,11) >= 5 else False
        renewal_salary:int = 0
        prime:bool = True if self.player.age >= 25 and self.player.age <= 32 else False
        
        # Randomize a team
        team:str = rs.randomTeam()
        
        offer_salary:int
        
        year:int
        
        # Select year according to the transfer step and age
        if first_team:
            year:int = self.player.age
            offer_salary:int = 0
            self.player.registerTransference(team, year, offer_salary)
        else:
            year:int = self.player.age
            prev_salary:int = self.player.transfer_history[-1]["salary"]
            
            offer_salary = rs.randomSalary(prime, prev_salary)
            
            opt:str = "" 
               
            # TODO: Quando fora do prime, baixar o salário de renovação, evitando o viés de alta constante   
            if renewal_offer:
                
                renewal_salary = rs.randomSalary(prime, prev_salary, renew=True, offer_value=offer_salary)
            
                print(f'{COLORS["red"]}[OFFER]{COLORS["clear"]} {COLORS["green"]}{self.player.name}{COLORS["clear"]} has been offered a contract by {COLORS["red"]}{team}{COLORS["clear"]} at {COLORS["red"]}{year}{COLORS["clear"]} for {COLORS["red"]}{offer_salary}M{COLORS["clear"]} per year. But, the manager of {COLORS["red"]}{self.player.transfer_history[-1]["team"]}{COLORS["clear"]} has offered a renewal of {COLORS["red"]}{renewal_salary}M{COLORS["clear"]} per year. If you want to renew the contract, type {COLORS["red"]}n{COLORS["clear"]}, if you want to accept the offer, type {COLORS["red"]}y{COLORS["clear"]}.')
                opt = str(input(">>> ")).lower()
                if opt == "n":
                    print(f"{COLORS['yellow']}[INFO]{COLORS['clear']} {COLORS['green']}{self.player.name}{COLORS['clear']} has rejected the offer. The contract has been renewed.")
                    
                    self.player.registerRenewal(renewal_salary)
                elif opt == "y":
                    print(f"{COLORS['yellow']}[INFO]{COLORS['clear']} {COLORS['green']}{self.player.name}{COLORS['clear']} has  accepted the offer, so the previous contract has been terminated.")
                    self.player.registerTransference(team, year, offer_salary)
                else:
                    print(f"{COLORS['yellow']}[INFO]{COLORS['clear']} {COLORS['green']}{self.player.name}{COLORS['clear']} don't answer the offer, so the offer has been rejected. The contract has been renewed.")
                    self.player.registerRenewal(renewal_salary)
            else:
                
                print(f'{COLORS["red"]}[OFFER]{COLORS["clear"]} {COLORS["green"]}{self.player.name}{COLORS["clear"]} has been offered a contract by {COLORS["red"]}{team}{COLORS["clear"]} at {COLORS["red"]}{year}{COLORS["clear"]} for {COLORS["red"]}{offer_salary}M{COLORS["clear"]} per year. If you want to accept the offer, type {COLORS["red"]}y{COLORS["clear"]}, if you want to reject the offer, type {COLORS["red"]}n{COLORS["clear"]}.')
                opt = str(input(">>> ")).lower()
                
                if opt == "y":
                    print(f"{COLORS['yellow']}[INFO]{COLORS['clear']} {COLORS['green']}{self.player.name}{COLORS['clear']} has accepted the offer, so the previous contract has been terminated.")
                    self.player.registerTransference(team, year, offer_salary)

                elif opt == "n":
                    print(f"{COLORS['yellow']}[INFO]{COLORS['clear']} {COLORS['green']}{self.player.name}{COLORS['clear']} has rejected the offer. The contract has been renewed.")
                    # Renew the contract
                    self.player.registerRenewal(renewal_salary)
                else:
                    print(f"{COLORS['yellow']}[INFO]{COLORS['clear']} {COLORS['green']}{self.player.name}{COLORS['clear']} don't answer the offer, so the offer has been rejected. The contract has been renewed.")
                    # Renew the contract
                    self.player.registerRenewal(renewal_salary)
                    
            ans:bool = True if opt == "y" else False
            return ans
        
        # Register the transfer
        
    def simulateCareer(self):
        while self.player.age <= self.player.retirement_age:
            self.simulateTransfer()
