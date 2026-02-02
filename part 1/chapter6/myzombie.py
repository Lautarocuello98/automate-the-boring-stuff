import zombiedice

class MyZombie:
    def __init__(self, name):
        #all zombies must have a name:
        self.name = name

    def turn(self, gameState):
        #game state is a dict with info about the current state of the game.
        diceRollResults = zombiedice.roll() #first roll
    
        shotgun = 0
        brains = 0
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']
            brains += diceRollResults['brains']
        

            if brains >= 4:
                break
        
            elif shotgun >= 2:
                break

            else:
                diceRollResults = zombiedice.roll()
            

zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 shotgun', minShotguns=1),
    MyZombie(name='Lili'),
    #add any other zombie players here
)
zombiedice.runWebGui(zombies=zombies, numGames=1000)