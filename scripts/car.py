# _______________libraries_______________
import search

class Car:

    # _______________attributes______________
    
    # identifier - a numeric identifier for the car
    # garageLocation - the coordinates of the garage location i.e. where the car starts and ends its route
    # packageList - a list of packages for the car to pick up and deliver
    # currentLocation - the coordinates where the car currently is, initially at the garage
    def __init__(self, identifier, garageLocation, packageList=list()):
        self.identifier = identifier
        self.garageLocation = garageLocation
        self.packageList = packageList 
        self.currentLocation = garageLocation
    
    # _________________methods_______________
    # given a map (graph) to search
        # find each package in the list and then deliver it.
        # Then go home.
        # note:
        # Uses the Depth first search algorithm with basic heuristics
    def useDFS(self, graphToSearch):
        for package in self.packageList:
            print "------------------------------------------------------------"
            print "working with package id " + str(package.identifier)
            print
            
            # the first call gets a package
            print "getting the package"
            self.currentLocation = search.depthFirstSearchRevised(graphToSearch, self.currentLocation, package.pickupLocation)
            
            print
            
            # the second call delivers that package
            print "delivering the package"
            self.currentLocation = search.depthFirstSearchRevised(graphToSearch, self.currentLocation, package.dropoffLocation)
    
        # this final call goes home
        print
        print "------------------------------------------------------------"
        print "Done, going home!"
        self.currentLocation = search.depthFirstSearchRevised(graphToSearch, self.currentLocation, self.garageLocation)
        
    # given a garage location, a packagePickupNode and a packageDropoffNode, find the package, move to pick it up
    # deliver the package, and then go home. Uses the Breadth first search algorithm with no heuristics
    def useBFS(self, graphToSearch, garageNode, packagePickupNodes, packageDropoffNodes):
        # calling BFS on the graph
        currentLocation = garageNode[0]
    
        for x in range (0, len(packagePickupNodes)):
            print "------------------------------------------------------------"
            print "Package number " + str(x)
            
            # the first call gets a package
            currentLocation = search.breadthFirstSearch(graphToSearch, currentLocation, packagePickupNodes[x])
            
            # the second call delivers that package
            currentLocation = search.breadthFirstSearch(graphToSearch, currentLocation, packageDropoffNodes[x])
    
        # this final call goes home
        print "Done, going home!"
        currentLocation = search.breadthFirstSearch(graphToSearch, currentLocation, garageNode)
    
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
