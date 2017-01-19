#libraries
import networkx as graphLibrary
import graphFile
import search

#functions
def useDFS(garageNode, packagePickupNode, packageDropoffNode):
    #calling DFS on the graph
    currentLocation = garageNode;
    #this first call gets the package
    currentLocation = search.depthFirstSearch(mainGraph, currentLocation, packagePickupNode);
    #this second call delivers the package
    currentLocation = search.depthFirstSearch(mainGraph, currentLocation, packageDropoffNode);
    #this final call goes home
    currentLocation = search.depthFirstSearch(mainGraph, currentLocation, garageNode);

def useBFS(garageNode, packagePickupNode, packageDropoffNode):
    #calling BFS on the graph
    currentLocation = garageNode;
    #this first call gets the package
    currentLocation = search.breadthFirstSearch(mainGraph, currentLocation, packagePickupNode);
    #this second call delivers the package
    currentLocation = search.breadthFirstSearch(mainGraph, currentLocation, packageDropoffNode);
    #this final call goes home
    currentLocation = search.breadthFirstSearch(mainGraph, currentLocation, garageNode);

#main
#setting up a graph
mainGraph = graphLibrary.Graph();
graphFile.initGraph(mainGraph);

#setting up the random points
#note; pointsList will be an array of size 3(for now), where the first item is the randomly generated location of the garage, the second item is the randomly generated location of the packages pickup location, and the third item is the randomly generated location of the packages dropoff location. These numbers will be integers.
pointsList = graphFile.createPoints(1, 1, mainGraph);

#after we get the integers, we have to get the specific nodes
garageNode = list(mainGraph.nodes())[pointsList[0]];
packagePickupNode = list(mainGraph.nodes())[pointsList[1]];
packageDropoffNode = list(mainGraph.nodes())[pointsList[2]];

print "Garage Location: " + str(garageNode);
print "Package Pickup Location: " + str(packagePickupNode);
print "Package Dropoff Location: " + str(packageDropoffNode);

useDFS(garageNode, packagePickupNode, packageDropoffNode);

useBFS(garageNode, packagePickupNode, packageDropoffNode);

graphFile.drawGraph(mainGraph, 'white');

