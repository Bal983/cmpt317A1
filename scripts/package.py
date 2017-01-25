class Package:
    
    # _______________attributes______________
    
    # id - a numeric identifier for the package
    # pickupLocation - the coordinates where the package is picked up
    # dropoffLocation - the coordinates where the package is dropped off
    def __init__(self, id, pickupLocation, dropoffLocation):
        self.id = id
        self.pickupLocation = pickupLocation
        self.dropoffLocation = dropoffLocation
