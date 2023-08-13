from logic.game import SoccerPLayer, CareerSimulator, TEAMS

class Tests:
    def __init__(self):
        pass
    def testJsonReader(self):
        # Read JSON file
        if TEAMS == []:
            print("[ERROR] Please, load the JSON file first.")
            return
        else:
            print("[RESOLVED] JSON file loaded successfully.",f"\n JSON RESULT:\n{TEAMS}")

    def testGameStart(self):
        s = CareerSimulator()
        print(s.startGame())

t = Tests()
t.testGameStart()
        