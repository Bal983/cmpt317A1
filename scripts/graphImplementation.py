#libraries
import networkx as graphLibrary
import matplotlib.pyplot as plot
import random
import math
from car import Car
from package import Package

# Member Variables
graphs = []                 #A list of graphs that the graphFile manages

#functions
#a helper function that calls a number of the graph creation functions.
def makeGraphList( size ):
    #add more functions here if we want to test with a longer list of graphs.
    createGridGraph ( size )

#a grid graph by default is such that each node has an edge between each coordinate neighbor.
#technical the graphs can be size n by m, but n by n is more visually pleasing and doesn't take away from the searches.
def createGridGraph ( size ):
    graphs.append(graphLibrary.grid_2d_graph(size, size, periodic=False, create_using=None))

#given a graph it will use the networkx features to #print the stats of a graph, for testing purposes
def printGraphStats( toPrint ):
    print ("Standard library stats:")
    print (graphLibrary.info(toPrint))

#for each graph in the graphs[] list, we create a window for it and call drawGraph.
def makeAllFigures( color ):
    count = 0
    for graph in graphs:
        count = count + 1
        plot.figure(count)
        if(graph.number_of_nodes() > 0):
            drawGraph ( graph , color)
    #showing the graphs, will pause the scripts until the plot windows are closed.
    plot.show();

#drawGraph takes a graph and a colour, defines plot to have the limits (plus a small border) of the number of nodes per size, and then draws it.
#Note; this function will currently only work if the name of the node is named in the same way a coordinate would appear.
def drawGraph( graph, colour ):
    #getting the size
    size = math.sqrt(len(list(graph.nodes())))
    #creating the axis
    plot.ylim([-1,(size)])
    plot.xlim([-1,(size)])
    pos = dict( (node, node) for node in graph.nodes() )
    #drawing the graph
    graphLibrary.draw_networkx(graph, pos, node_color=colour, width=2.0, linewidth=2.0, font_size=10, node_size=800)

#given a graph, a number of garages and a number of packages, we will generate a number of points.
#note: it will generate points such that packagePickupNumber[location] is related to packageDropoffNumber[location]
def createObjects( numberOfGarages, numberOfPackages, graph, difficultyAddition):
    #defining empty lists for the two groups of objects we want to return
    carList = list()
    packageList = list()

    maxRange = len(list(graph.nodes()))
    #generating x car objects with a random garage location
    for x in range( 0, numberOfGarages ):
        garageLocation = random.randrange(0, maxRange)
        carList.append( Car(x, list(graph.nodes())[garageLocation], difficultyAddition) )
        #print "Car " + str(x) + " has been created"

    #generating x package objects with random pickup/dropoff locations
    #limitation: pickup and dropoff location are never the same
    for x in range( 0, numberOfPackages ):
        pickupLocation = random.randrange( 0, maxRange )
        dropoffLocation = random.randrange( 0, maxRange )

        while( pickupLocation == dropoffLocation ):
            dropoffLocation = random.randrange( 0, maxRange )

        packageList.append( Package(x, list(graph.nodes())[pickupLocation], list(graph.nodes())[dropoffLocation], difficultyAddition) )
        #print "Package " + str(x) + " has been created"

    return [carList, packageList]

def createDefinedObjects( graph ):
    carList = list()
    packageList = list()

    #creating cars
    carList.append( Car(0, (0, 0)))
    carList.append( Car(1, (99, 99)))

    #creating packages
    packageList.append( Package(0, (1, 0), (2, 0)))
    packageList.append( Package(1, (1, 1), (2, 1)))
    packageList.append( Package(2, (1, 2), (2, 2)))
    packageList.append( Package(3, (1, 3), (2, 3)))
    packageList.append( Package(4, (98, 97), (97, 97)))
    packageList.append( Package(5, (98, 98), (97, 98)))
    packageList.append( Package(6, (98, 99), (97, 99)))

    return [carList, packageList]

def removeRandomEdges( graph ):
    #put the code that removes random edges here.
    print "removeRandomEdges was called"
    
def minimumSpanningTree(G):
    print "Making a minimum spanning tree."
    reduceGraph(G , 1.0 , 1.0)
    print "Remaining edges"
    
# reduces the connected of a graph by selecting a percentage of the nodes and destroying
# the edges if a minimum degree is maintained
# reductionFactor :float in (0.0 , 1.0 )
# minimumDegree   :int in [0 , inf)
def reduceGraph(graph, reductionFactor, minimumDegree):
    print "Trimming " + str(reductionFactor * 100) + "% of the nodes in " + str( graph )
    print "Minimum Degree of " + str(minimumDegree) + " will be preserved."
    graphLibrary.info ( graph )
    originalNodes = graph.nodes()
    # Take a random sample of the nodes according to the parameters
    sample = random.sample(originalNodes, int(reductionFactor * len(originalNodes)))
    # Remove all edges that don't break the degree rule
    edgeCountOrig = len(graph.edges())
    print "Starting edge count: " + str (edgeCountOrig)
    for node in sample:
        edges = graph.edges(node)
        for edge in edges:
            valid = graph.degree(edge[0]) > minimumDegree and graph.degree(edge[1]) > minimumDegree
            if(valid):
                graph.remove_edge(edge[0], edge[1])
                if( not graphLibrary.is_connected( graph )) :
                    graph.add_edge(edge[0],edge[1])
    edgeCountFinal = len(graph.edges())
    print "Final edge count: " + str(edgeCountFinal)
    print "Final reduction percentage :" + str( ( float (edgeCountFinal)/ float (edgeCountOrig )))

# reduces the connected of a graph by selecting a percentage of the nodes and destroying
# the edges if a minimum degree is maintained. Addition: pseudo-random defects compared to standard result
# reductionFactor :float in (0.0 , 1.0 )
# minimumDegree   :int in [0 , inf)
# rand            :float in (0.0 , 1.0 ) : likelihood for a removal to be executed
def reduceGraphRand(graph, reductionFactor, minimumDegree, randomFactor):
    print "Trimming " + str(reductionFactor * 100) + "% of the nodes in " + str( graph )
    print "Minimum Degree of " + str(minimumDegree) + " will be preserved."
    graphLibrary.info ( graph )
    originalNodes = graph.nodes()
    # Take a random sample of the nodes according to the parameters
    sample = random.sample(originalNodes, int(reductionFactor * len(originalNodes)))
    # Remove all edges that don't break the degree rule
    edgeCountOrig = len(graph.edges())
    print "Starting edge count: " + str (edgeCountOrig)
    for node in sample:
        edges = graph.edges(node)
        for edge in edges:
            valid = graph.degree(edge[0]) > minimumDegree and graph.degree(edge[1]) > minimumDegree
            if(valid):
                graph.remove_edge(edge[0], edge[1])
                if( not graphLibrary.is_connected( graph )) :
                    graph.add_edge(edge[0],edge[1])
    edgeCountFinal = len(graph.edges())
    print "Starting edge count: " + str(edgeCountFinal)
    print "Final reduction percentage :" + str( ( float (edgeCountFinal)/ float (edgeCountOrig )))

def testing( size ):
    print
    print "-------------------------"
    print "Testing the graphImplementation file"
    #testing the mackGraphList method, should create a defined amount of graphs of size size
    makeGraphList( size )

    #this method will draw all of the above graphs with node colour red.
    makeAllFigures( "red" )

if __name__ == "__main__":
    testing( 5 )
