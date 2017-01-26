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
        
    def testing( self ):
        print
        print "-------------------------"
        print "testing the package file"
        
    if __name__ == "__main__":
        testing( None )
