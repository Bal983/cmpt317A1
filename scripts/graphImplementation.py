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
    
    #after we generate all the graphs, #print all of the stats
    for graph in graphs:
        printGraphStats( graph )      
    
#a grid graph by default is such that each node has an edge between each coordinate neighbor.
#technical the graphs can be size n by m, but n by n is more visually pleasing and doesn't take away from the searches.
def createGridGraph ( size ):
    #print "Forming a grid graph of size " + str(size) + "."
    G = graphLibrary.grid_2d_graph(size, size, periodic=False, create_using=None)
    #print "Here's the stats of the grid graph:"
    graphs.append(G)

#given a graph it will use the networkx features to #print the stats of a graph, for testing purposes
def printGraphStats( toPrint ):
    print ("Standard library stats:")
    #print (graphLibrary.info(toPrint))
    #print

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
def drawGraph( graph, colour):
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
def createObjects( numberOfGarages, numberOfPackages, graph):
    #defining empty lists for the two groups of objects we want to return
    carList = list()
    packageList = list()
    
    #generating x car objects with a random garage location
    for x in range( 0, numberOfGarages ):
        garageLocation = random.randrange(0, len(list(graph.nodes())))
        carList.append( Car(x, list(graph.nodes())[garageLocation]) )
        
    #generating x package objects with random pickup/dropoff locations
    #limitation: pickup and dropoff location are never the same
    for x in range( 0, numberOfPackages ):
        pickupLocation = random.randrange( 0, len(list(graph.nodes())) )
        dropoffLocation = random.randrange( 0, len(list(graph.nodes())) )
        
        while( pickupLocation == dropoffLocation ):
            dropoffLocation = random.randrange( 0, len(list(graph.nodes())) )
            
        packageList.append( Package(x, list(graph.nodes())[pickupLocation], list(graph.nodes())[dropoffLocation]) )

    return [carList, packageList]

def removeRandomEdges( graph ):
    #put the code that removes random edges here.
    print "removeRandomEdges was called"

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
