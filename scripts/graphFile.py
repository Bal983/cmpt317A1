#libraries
import networkx as graphLibrary
import matplotlib.pyplot as plot
import random
import math
from networkx.generators.classic import empty_graph, complete_graph, grid_graph

# Member Variables
graphs = []                 #A list of graphs that the graphFile manages

#functions
def makeGraphList( size ):
    #completeRandomGraph( size*size )    #size here specifies the number of nodes, so if we want a 5 sided grid graph, we want 25 nodes so we square it here
    gridGraph ( size )                  #in grid graph, size represents the number of nodes in each dimension.
    presetGraph()
    
def presetGraph():
    print "Creating the preset 4 by 4 graph:"
    
    G = graphLibrary.Graph()
    initPresetGraph1(G)
    
    print "Here's the stats of preset graph:"
    printGraphStats(G)
    graphs.append(G)
    
def completeRandomGraph(size):
    print "Forming a random complete graph of size " + str(size) + "."
  
    G = graphLibrary.complete_graph(size)
    
    print "Here's the stats of random complete graph:"
    printGraphStats(G)
    graphLibrary.random_layout(G)
    graphs.append(G)

def gridGraph ( size ):
    print "Forming a grid graph of size " + str(size) + "."
    G = graphLibrary.grid_2d_graph(size, size, periodic=False, create_using=None)
    print "Here's the stats of the grid graph:"
    printGraphStats(G)
    graphLibrary.random_layout(G)
    graphs.append(G)

def printGraphStats( toPrint ):
    print("Standard library stats:")
    print (graphLibrary.info(toPrint))
    print

def initPresetGraph1( graph ):
    #adding the nodes to make a 4 by 4 graph
    graph.add_node("1,1", pos=(1,1));
    graph.add_node("1,2", pos=(1,2));
    graph.add_node("1,3", pos=(1,3));
    graph.add_node("1,4", pos=(1,4));
    graph.add_node("2,1", pos=(2,1));
    graph.add_node("2,2", pos=(2,2));
    graph.add_node("2,3", pos=(2,3));
    graph.add_node("2,4", pos=(2,4));
    graph.add_node("3,1", pos=(3,1));
    graph.add_node("3,2", pos=(3,2));
    graph.add_node("3,3", pos=(3,3));
    graph.add_node("3,4", pos=(3,4));
    graph.add_node("4,1", pos=(4,1));
    graph.add_node("4,2", pos=(4,2));
    graph.add_node("4,3", pos=(4,3));
    graph.add_node("4,4", pos=(4,4));

    #adding some edges into the graph
    graph.add_edge("2,2", "3,2");
    graph.add_edge("2,2", "1,2");
    graph.add_edge("2,2", "2,1");
    graph.add_edge("2,2", "2,3");
    graph.add_edge("2,1", "3,1");
    graph.add_edge("3,1", "3,2");
    graph.add_edge("3,2", "3,3");
    graph.add_edge("2,3", "1,3");
    graph.add_edge("1,3", "1,2");
    graph.add_edge("1,2", "1,1");
    graph.add_edge("1,3", "1,4");
    graph.add_edge("2,3", "2,4");
    graph.add_edge("3,3", "3,4");
    graph.add_edge("3,3", "4,3");
    graph.add_edge("3,2", "4,2");
    graph.add_edge("4,2", "4,1");
    graph.add_edge("4,3", "4,4");
    graph.add_edge("3,4", "4,4");

def makeAllFigures( color):
    count = 0
    
    for graph in graphs:
        count = count + 1
        plot.figure(count)
        drawGraph (graph , color )
        
    #showing the graphs, will pause the scripts
    plot.show();

def createPoints( numberOfPackages, numberOfGarages, graph):
    #generating random locations for the garage and the package
    garageNumber = random.randrange(0, len(list(graph.nodes())));
    packagePickupNumber = random.randrange(0, len(list(graph.nodes())));
    packageDropoffNumber = random.randrange(0, len(list(graph.nodes())));
        
    while ((packageDropoffNumber == packagePickupNumber)):
        packageDropoffNumber = random.randrange(1, len(list(graph.nodes())));

    return [garageNumber, packagePickupNumber, packageDropoffNumber]

def drawGraph( graph, colour):
    #creating the axis
    plot.ylim([-0.5,1.5])
    plot.xlim([-0.5,1.5])
    
    edgeSize = math.sqrt(int(len(graph.nodes())))
    
    positions = dict()
    
    #generating the positions
    for node in graph.nodes():
        nodeAsString = str(node)
        nodeAsString = nodeAsString.replace("(","")
        nodeAsString = nodeAsString.replace(")","")
        nodeAsString = nodeAsString.replace(" ","")
        print nodeAsString
    
    #drawing the graph
    graphLibrary.draw_networkx(graph, node_color=colour, width=2.0, linewidth=2.0, font_size=14, node_size=800)

def testing():
    makeGraphList( 10 )
    #setting up staticGraph
    staticGraph = graphLibrary.Graph();
    initPresetGraph1(staticGraph);
    #plot.figure(2):
    #testing the graph
    makeAllFigures("red")
    for i in range(0,3):
        createPoints( 1, 1, graphs[i]);
        drawGraph (graphs[i, "green"], 50, 50)
    drawGraph(staticGraph , "purple" , 10 , 10);


