#_______________imports_______________

#_______________class_______________
class Package:
    
    # _______________attributes______________
    
    # identifier - a numeric identifier for the package
    # pickupLocation - the coordinates where the package is picked up
    # dropoffLocation - the coordinates where the package is dropped off
    def __init__(self, identifier, pickupLocation, dropoffLocation):
        self.identifier = identifier
        self.pickupLocation = pickupLocation
        self.dropoffLocation = dropoffLocation
        self.calculateDifficulty( pickupLocation, dropoffLocation)        
        
    def calculateDifficulty(self, pickupLocation, dropoffLocation ):
        pickupLocationX = pickupLocation[0]
        pickupLocationY = pickupLocation[1]
        dropoffLocationX = dropoffLocation[0]
        dropoffLocationY = dropoffLocation[1]
        self.difficulty = abs(pickupLocationX - dropoffLocationX) + abs(pickupLocationY - dropoffLocationY)
    
    def testing( self ):
        print
        print "-------------------------"
        print "testing the package file"
        
    if __name__ == "__main__":
        testing( None )
