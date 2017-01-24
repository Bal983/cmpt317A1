#_______________libraries_______________
import search

#_______________functions_______________
#given a garage location, a list of packagePickupNodes and a list of packageDropoffNode
    #find each package in the list and then deliver it.
    #Then go home.
    #note:
    #Uses the Depth first search algorithm with basic heuristics
def useDFS( graphToSearch, garageNode, packagePickupNodes, packageDropoffNodes ):
    #calling DFS on the graph
    currentLocation = garageNode[0]

    for x in range ( 0, len(packagePickupNodes) ):
        print "Package number " + str(x)
        
        #the first call gets a package
        currentLocation = search.depthFirstSearch( graphToSearch, currentLocation, packagePickupNodes[x] )
        
        #the second call delivers that package
        currentLocation = search.depthFirstSearch( graphToSearch, currentLocation, packageDropoffNodes[x] )

    #this final call goes home
    print "Done, going home!"
    currentLocation = search.depthFirstSearch( graphToSearch, currentLocation, garageNode )
    
#given a garage location, a packagePickupNode and a packageDropoffNode, find the package, move to pick it up
#deliver the package, and then go home. Uses the Breadth first search algorithm with no heuristics
def useBFS( graphToSearch, garageNode, packagePickupNodes, packageDropoffNodes ):
    
    #calling BFS on the graph
    currentLocation = garageNode[0]

    for x in range ( 0, len(packagePickupNodes) ):
        print "Package number " + str(x)
        
        #the first call gets a package
        currentLocation = search.breadthFirstSearch( graphToSearch, currentLocation, packagePickupNodes[x] )
        
        #the second call delivers that package
        currentLocation = search.breadthFirstSearch( graphToSearch, currentLocation, packageDropoffNodes[x] )

    #this final call goes home
    print "Done, going home!"
    currentLocation = search.breadthFirstSearch( graphToSearch, currentLocation, garageNode )

def useAStar( graphToSearch, garageNode, packagePickupNodes, packageDropoffNodes ):
    #calling A* on the graph
    currentLocation = garageNode[0]

    for x in range ( 0, len(packagePickupNodes) ):
        print "Package number " + str(x)
        
        #the first call gets a package
        currentLocation = search.aStarSearch( graphToSearch, currentLocation, packagePickupNodes[x] )
        
        #the second call delivers that package
        currentLocation = search.aStarSearch( graphToSearch, currentLocation, packageDropoffNodes[x] )

    #this final call goes home
    print "Done, going home!"
    currentLocation = search.aStarSearch( graphToSearch, currentLocation, garageNode )
    
def testing():
    print "testing the car file"
    
if __name__ == "__main__":
    testing()