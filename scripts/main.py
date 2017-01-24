#_______________libraries_______________
import networkx as graphLibrary
import search
import graphFile

#_______________functions_______________
#given a garage location, a packagePickupNode and a packageDropoffNode, find the package, move to pick it up
#deliver the package, and then go home. Uses the Depth first search algorithm with basic heuristics
def useDFS(graphToSearch, garageNode, packagePickupNode, packageDropoffNode):

    #calling DFS on the graph
    currentLocation = garageNode

    #this first call gets the package
    currentLocation = search.depthFirstSearch(graphToSearch, currentLocation, packagePickupNode)

    #this second call delivers the package
    currentLocation = search.depthFirstSearch(graphToSearch, currentLocation, packageDropoffNode)

    #this final call goes home
    currentLocation = search.depthFirstSearch(graphToSearch, currentLocation, garageNode)

#given a garage location, a packagePickupNode and a packageDropoffNode, find the package, move to pick it up
#deliver the package, and then go home. Uses the Breadth first search algorithm with no heuristics
def useBFS(graphToSearch, garageNode, packagePickupNode, packageDropoffNode):
    #calling BFS on the graph
    currentLocation = garageNode

    #this first call gets the package
    currentLocation = search.breadthFirstSearch(graphToSearch, currentLocation, packagePickupNode)
    
    #this second call delivers the package
    currentLocation = search.breadthFirstSearch(graphToSearch, currentLocation, packageDropoffNode)

    #this final call goes home
    currentLocation = search.breadthFirstSearch(graphToSearch, currentLocation, garageNode)

#_______________main_______________
#Generating a list of functions to show
size = 10

graphFile.makeGraphList( size )           #5 is the size of the non preset graphs, can be changed.

#setting up the random points
#note; pointsList will be an array of size 3(for now), where the first item is the randomly generated location of the garage
    #the second item is the randomly generated location of the packages pickup location
    #and the third item is the randomly generated location of the packages drop-off location. These numbers will be integers.
for graph in graphFile.graphs:
    if (graph != None):
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        print len(list(graph.nodes()))

        pointsList = graphFile.createPoints(1, 1, graph)

        #after we get the integers, we have to get the specific nodes and tell the user
        garageNode = list(graph.nodes())[pointsList[0]]
        packagePickupNode = list(graph.nodes())[pointsList[1]]
        packageDropoffNode = list(graph.nodes())[pointsList[2]]
        print "Garage Location: " + str(garageNode)
        print "Package Pickup Location: " + str(packagePickupNode)
        print "Package Drop-off Location: " + str(packageDropoffNode)

        print "Doing a DFS search on the above locations, this will pick up and drop off one package and then go home"
        useDFS(graph, garageNode, packagePickupNode, packageDropoffNode)

        print "Doing a BFS search on the above locations, this will pick up and drop off one package and then go home"
        useBFS(graph, garageNode, packagePickupNode, packageDropoffNode)
        
print "Done!"
