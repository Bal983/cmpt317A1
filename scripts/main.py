#libraries
import networkx as graphLibrary
import graphFile
import search

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

currentLocation = garageNode;

#calling DFS on the graph
#this first call gets the package
currentLocation = search.depthFirstSearch(mainGraph, currentLocation, packagePickupNode);
#this second call delivers the package
currentLocation = search.depthFirstSearch(mainGraph, currentLocation, packageDropoffNode);
#this final call goes home
currentLocation = search.depthFirstSearch(mainGraph, currentLocation, garageNode);

if(currentLocation == garageNode):
    print "success!"

#calling BFS on the graph
#search.breadthFirstSearch(mainGraph, garageNode);

#calling A* on the graph
#search.aStarSearch(mainGraph, garageNode);

graphFile.drawGraph(mainGraph, 'white');
