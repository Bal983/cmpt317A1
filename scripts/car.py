# _______________libraries_______________
import search

class Car:
    
    # _______________attributes______________
    
    # id - a numeric identifier for the car
    # garageLocation - the coordinates of the garage location i.e. where the car starts and ends its route
    # packageList - a list of packages for the car to pick up and deliver
    # currentLocation - the coordinates where the car currently is, initially at the garage
    def __init__(self, id, garageLocation, packageList=list()):
        self.id = id
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
            print "Delivering package id " + str(package.id)
            
            # the first call gets a package
            self.currentLocation = search.depthFirstSearch(graphToSearch, self.currentLocation, package.pickupLocation)
            
            # the second call delivers that package
            self.currentLocation = search.depthFirstSearch(graphToSearch, self.currentLocation, package.dropoffLocation)
    
        # this final call goes home
        print "Done, going home!"
        self.currentLocation = search.depthFirstSearch(graphToSearch, self.currentLocation, self.garageLocation)
        
    # given a garage location, a packagePickupNode and a packageDropoffNode, find the package, move to pick it up
    # deliver the package, and then go home. Uses the Breadth first search algorithm with no heuristics
    def useBFS(self, graphToSearch, garageNode, packagePickupNodes, packageDropoffNodes):
        
        # calling BFS on the graph
        currentLocation = garageNode[0]
    
        for x in range (0, len(packagePickupNodes)):
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
            print "Package number " + str(x)
            
            # the first call gets a package
            currentLocation = search.aStarSearch(graphToSearch, currentLocation, packagePickupNodes[x])
            
            # the second call delivers that package
            currentLocation = search.aStarSearch(graphToSearch, currentLocation, packageDropoffNodes[x])
    
        # this final call goes home
        print "Done, going home!"
        currentLocation = search.aStarSearch(graphToSearch, currentLocation, garageNode)
        
    def testing():
        print "testing the car file"
        
    if __name__ == "__main__":
        testing()
