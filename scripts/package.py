#_______________imports_______________
from math import pow
#_______________class_______________
class Package:
    
    # _______________attributes______________
    
    # identifier - a numeric identifier for the package
    # pickupLocation - the coordinates where the package is picked up
    # dropoffLocation - the coordinates where the package is dropped off
    def __init__(self, identifier, pickupLocation, dropoffLocation, difficultyAddition):
        self.identifier = identifier
        self.pickupLocation = pickupLocation
        self.dropoffLocation = dropoffLocation
        self.calculateDifficulty( pickupLocation, dropoffLocation, difficultyAddition)        
        
    def calculateDifficulty(self, pickupLocation, dropoffLocation, difficultyAddition):
        pickupLocationX = pickupLocation[0]
        pickupLocationY = pickupLocation[1]
        dropoffLocationX = dropoffLocation[0]
        dropoffLocationY = dropoffLocation[1]
        self.difficulty = pow((abs(pickupLocationX - dropoffLocationX) + abs(pickupLocationY - dropoffLocationY)),difficultyAddition)
    
    def testing( self ):
        print
        print "-------------------------"
        print "testing the package file"
        
    if __name__ == "__main__":
        testing( None )
