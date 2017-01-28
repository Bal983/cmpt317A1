# _______________libraries_______________
import search

class Car:

    # _______________attributes______________
    
    # identifier - a numeric identifier for the car
    # garageLocation - the coordinates of the garage location i.e. where the car starts and ends its route
    # packageList - a list of packages for the car to pick up and deliver
    # currentLocation - the coordinates where the car currently is, initially at the garage
    def __init__(self, identifier, garageLocation):
        self.identifier = identifier
        self.garageLocation = garageLocation
        self.packageList = [] 
        self.currentLocation = garageLocation
    
    # _________________methods_______________
    # given a map (graph) to search
        # find each package in the list and then deliver it.
        # Then go home.
        # note: Uses the Depth first search algorithm with basic heuristics
    def useDFS(self, graphToSearch):
        for package in self.packageList:
            print "------------------------------------------------------------"
            print "working with package id " + str(package.identifier)
            print
            
            #the first call gets a package
            print "getting the package"
            print "Car " + str(self.identifier) + " picked up package ID " + str(package.identifier)
            self.currentLocation = search.depthFirstSearchRevised(graphToSearch, self.currentLocation, package.pickupLocation)
            
            print
            
            #the second call delivers that package
            print "delivering the package"
            print "Car " + str(self.identifier) + " dropped off package ID " + str(package.identifier)
            self.currentLocation = search.depthFirstSearchRevised(graphToSearch, self.currentLocation, package.dropoffLocation)

        # this final call goes home
        print "Car " + str(self.identifier) + " returning to garage"
        self.currentLocation = search.depthFirstSearchRevised(graphToSearch, self.currentLocation, self.garageLocation)
        
    # given a garage location, a packagePickupNode and a packageDropoffNode, find the package, move to pick it up
    # deliver the package, and then go home. Uses the Breadth first search algorithm with no heuristics
    def useBFS(self, graphToSearch):
        for package in self.packageList:
            #print "------------------------------------------------------------"
            #print "working with package id " + str(package.identifier)
            #print "\tPackage has pickpup point: " + str(package.pickupLocation)
            #print "\tPackage has dropoff point: " + str(package.dropoffLocation)
            #print
            
            # the first call gets a package
            #print "getting the package"
            self.currentLocation = search.breadthFirstSearchRevised(graphToSearch, self.currentLocation, package.pickupLocation)
            
            #print
            
            # the second call delivers that package
            #print "delivering the package"
            self.currentLocation = search.breadthFirstSearchRevised(graphToSearch, self.currentLocation, package.dropoffLocation)
    
        # this final call goes home
        #print
        #print "------------------------------------------------------------"
        #print "Done, going home!"
        self.currentLocation = search.breadthFirstSearchRevised(graphToSearch, self.currentLocation, package.pickupLocation)
    
    def useAStar(self, graphToSearch):

        for package in self.packageList:

            # the first call gets a package
            print "Car " + str(self.identifier) + " picked up package ID " + str(package.identifier)
            print("NONE?")
            print(self.currentLocation)
            self.currentLocation = search.aStarSearch(graphToSearch, self.currentLocation, package.pickupLocation, search.perfectWorldDistance)

            print

            # the second call delivers that package
            print "Car " + str(self.identifier) + " dropped off package ID " + str(package.identifier)
            self.currentLocation = search.aStarSearch(graphToSearch, self.currentLocation, package.dropoffLocation, search.perfectWorldDistance)

        # this final call goes home
            print "Car " + str(self.identifier) + " returning to garage"
            self.currentLocation = search.aStarSearch(graphToSearch, self.currentLocation, self.garageLocation, search.perfectWorldDistance)
        
    def testing( self ):
        print
        #print "-------------------------"
        ##print "testing the car file"
        
    if __name__ == "__main__":
        testing( None )
