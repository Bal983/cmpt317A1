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
        self.totalDifficulty = 0
    
    # _________________methods_______________
    # given a map (graph) to search
        # find each package in the list and then deliver it.
        # Then go home.
        # note: Uses the Depth first search algorithm with basic heuristics
    def useDFS(self, graphToSearch):
        for package in self.packageList:
            # the first call gets a package
            search.depthFirstSearchRevised(graphToSearch, self.currentLocation, package.pickupLocation)
            self.currentLocation = package.pickupLocation
            
            # the second call delivers that package
            search.depthFirstSearchRevised(graphToSearch, self.currentLocation, package.dropoffLocation)
            self.currentLocation = package.dropoffLocation

    
        # this final call goes home
        search.breadthFirstSearchRevised(graphToSearch, self.currentLocation, package.pickupLocation)
        self.currentLocation = self.garageLocation
        
        return 0
        
    # given a garage location, a packagePickupNode and a packageDropoffNode, find the package, move to pick it up
    # deliver the package, and then go home. Uses the Breadth first search algorithm with no heuristics
    def useBFS(self, graphToSearch):
        for package in self.packageList:
            # the first call gets a package
            search.breadthFirstSearchRevised(graphToSearch, self.currentLocation, package.pickupLocation)
            self.currentLocation = package.pickupLocation
            
            # the second call delivers that package
            search.breadthFirstSearchRevised(graphToSearch, self.currentLocation, package.dropoffLocation)
            self.currentLocation = package.dropoffLocation

    
        # this final call goes home
        search.breadthFirstSearchRevised(graphToSearch, self.currentLocation, package.pickupLocation)
        self.currentLocation = self.garageLocation
        
        return 0
    
    def useAStar(self, graphToSearch):
        totalTraveled = 0
        for package in self.packageList:

            # the first call gets a package
            print "Car " + str(self.identifier) + " picked up package ID " + str(package.identifier)
            pathTaken = search.aStarSearch(graphToSearch, self.currentLocation, package.pickupLocation, search.perfectWorldDistance)
            print "Path taken was : " + str(pathTaken)
            print "Path length was : " + str(len(pathTaken))
            self.currentLocation = package.pickupLocation
            totalTraveled += len(pathTaken)
            print

            # the second call delivers that package
            print "Car " + str(self.identifier) + " dropped off package ID " + str(package.identifier)
            pathTaken = search.aStarSearch(graphToSearch, self.currentLocation, package.dropoffLocation, search.perfectWorldDistance)
            print "Path taken was : " + str(pathTaken)
            print "Path length was : " + str(len(pathTaken))
            self.currentLocation = package.dropoffLocation
            totalTraveled += len(pathTaken)
            print

        # this final call goes home
        print "Car " + str(self.identifier) + " returning to garage"
        pathTaken = search.aStarSearch(graphToSearch, self.currentLocation, self.garageLocation, search.perfectWorldDistance)
        print "Path taken was : " + str(pathTaken)
        print "Path length was : " + str(len(pathTaken))
        self.currentLocation = self.garageLocation
        totalTraveled += len(pathTaken)
        
        return totalTraveled
        
    def testing( self ):
        print
        #print "-------------------------"
        ##print "testing the car file"
        
    if __name__ == "__main__":
        testing( None )
