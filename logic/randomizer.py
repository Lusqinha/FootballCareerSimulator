from random import randint
import json

class RandomSupplies:
    def __init__(self, teams_json:list):
        
        self.teams_json = teams_json
            
        self.json_length = len(self.teams_json)
        
    def randomTeam(self):
        random_index:int = randint(0, self.json_length - 1)
        team = self.teams_json[random_index]["team_name"]
        return team, random_index
    
    def generateRenewOffer(self, prev_salary:int, prime:bool=False):
        if prime: # if in prime, increase salary with some percentage between 20% and 60%
            percentage = (randint(2, 6)*0.1)+1
            offer = randint(1,15) if prev_salary*percentage == 0.0 else round(prev_salary*percentage)
            
            return offer
        else: # if not in prime, the renewal offer is half of the previous salary
            percentage = (randint(2, 8)*0.1)+1
            offer = randint(1,15) if prev_salary*percentage == 0.0 else round(prev_salary*percentage)
            return round(offer/2)

    def randomSalary(self, prime:bool, prev_salary:int, renew:bool=False, offer_value:int=0):
        if prime: #
            if renew: 

                renew_offer = self.generateRenewOffer(prev_salary, prime)
                
                return renew_offer
                
            else: # use values based on M euros
                offer = randint(60, 130)
                return offer
        else:
            if renew: 
                renew_offer = self.generateRenewOffer(round(prev_salary/3), prime)
                
                return renew_offer
            
            else: # use values based on M euros
                offer = randint(10, 40)
                return offer
    
        
        
        


if __name__ == "__main__":
    r = RandomSupplies("logic/data/teams.json") # type: ignore
    print(r.randomTeam())