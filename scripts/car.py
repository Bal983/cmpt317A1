# _______________libraries_______________
import search
import threading

class Car (threading.Thread):

    # _______________attributes______________
    
    # identifier - a numeric identifier for the car
    # garageLocation - the coordinates of the garage location i.e. where the car starts and ends its route
    # packageList - a list of packages for the car to pick up and deliver
    # currentLocation - the coordinates where the car currently is, initially at the garage
    def __init__(self, identifier, garageLocation, graphToSearch):
        threading.Thread.__init__(self)
        self.identifier = identifier
        self.garageLocation = garageLocation
        self.packageList = [] 
        self.currentLocation = garageLocation
        self.graphToSearch = graphToSearch
    # _________________methods_______________
    # given a map (graph) to search
        # find each package in the list and then deliver it.
        # Then go home.
        # note: Uses the Depth first search algorithm with basic heuristics
    def run(self):
        print "CAR " + str(self.identifier) + " START: " + str(len(self.packageList)) + " packages"
        for package in self.packageList:
            #print "------------------------------------------------------------"
            #print "working with package id " + str(package.identifier)
            #print
            
            # the first call gets a package
            print "CAR " + str(self.identifier) + ": Package ID " + str(package.identifier) + " picked up"
            self.currentLocation = search.depthFirstSearchRevised(self.graphToSearch, self.currentLocation, package.pickupLocation)
            
            #print
            
            # the second call delivers that package
            print "CAR " + str(self.identifier) + ": Package ID " + str(package.identifier) + " dropped off"
            self.currentLocation = search.depthFirstSearchRevised(self.graphToSearch, self.currentLocation, package.dropoffLocation)
    
        # this final call goes home
        #print
        #print "------------------------------------------------------------"
        print "CAR " + str(self.identifier) + ": Driving Home"
        self.currentLocation = search.depthFirstSearchRevised(self.graphToSearch, self.currentLocation, self.garageLocation)
        print "CAR " + str(self.identifier) + " DONE"
        
    # given a garage location, a packagePickupNode and a packageDropoffNode, find the package, move to pick it up
    # deliver the package, and then go home. Uses the Breadth first search algorithm with no heuristics
    def useBFS(self, graphToSearch):
        for package in self.packageList:
            print "------------------------------------------------------------"
            print "working with package id " + str(package.identifier)
            print "\tPackage has pickpup point: " + str(package.pickupLocation)
            print "\tPackage has dropoff point: " + str(package.dropoffLocation)
            print
            
            # the first call gets a package
            print "getting the package"
            self.currentLocation = search.breadthFirstSearchRevised(graphToSearch, self.currentLocation, package.pickupLocation)
            
            print
            
            # the second call delivers that package
            print "delivering the package"
            self.currentLocation = search.breadthFirstSearchRevised(graphToSearch, self.currentLocation, package.dropoffLocation)
    
        # this final call goes home
        print
        print "------------------------------------------------------------"
        print "Done, going home!"
        self.currentLocation = search.breadthFirstSearchRevised(graphToSearch, self.currentLocation, package.pickupLocation)
    
    def useAStar(self, graphToSearch, garageNode, packagePickupNodes, packageDropoffNodes):
        # calling A* on the graph
        currentLocation = garageNode[0]
    
        for x in range (0, len(packagePickupNodes)):
            print "------------------------------------------------------------"
            print "Package number " + str(x)
            
            # the first call gets a package
            currentLocation = search.aStarSearch(graphToSearch, currentLocation, packagePickupNodes[x])
            
            # the second call delivers that package
            currentLocation = search.aStarSearch(graphToSearch, currentLocation, packageDropoffNodes[x])
    
        # this final call goes home
        print "Done, going home!"
        currentLocation = search.aStarSearch(graphToSearch, currentLocation, garageNode)
        
    def testing( self ):
        print
        print "-------------------------"
        print "testing the car file"
        
    if __name__ == "__main__":
        testing( None )
