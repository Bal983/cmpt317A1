#libraries
import networkx as graphLibrary
import matplotlib.pyplot as plot
import random
import math
import graphFile
from ast import literal_eval    #additional library to fix a string interpretation issue
from networkx.generators.classic import empty_graph, complete_graph, grid_graph

# Member Variables
graphs = []                 #A list of graphs that the graphFile manages
#functions
def makeGraphList( size ):
    graphs = []
    presetGraph()
    gridGraph ( size )                  #in grid graph, size represents the number of nodes in each dimension.

def presetGraph():
    print "Creating the preset 4 by 4 graph:"
    G = graphLibrary.Graph()
    initPresetGraph1(G)
    print "Here's the stats of preset graph:"
    printGraphStats(G)
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
    print(graphLibrary.info(toPrint))
    print()

def initPresetGraph1( graph ):
    #adding the nodes to make a 4 by 4 graph
    graph.add_node("(1, 1)", pos=(1,1));
    graph.add_node("(1, 2)", pos=(1,2));
    graph.add_node("(1, 3)", pos=(1,3));
    graph.add_node("(1, 4)", pos=(1,4));
    graph.add_node("(2, 1)", pos=(2,1));
    graph.add_node("(2, 2)", pos=(2,2));
    graph.add_node("(2, 3)", pos=(2,3));
    graph.add_node("(2, 4)", pos=(2,4));
    graph.add_node("(3, 1)", pos=(3,1));
    graph.add_node("(3, 2)", pos=(3,2));
    graph.add_node("(3, 3)", pos=(3,3));
    graph.add_node("(3, 4)", pos=(3,4));
    graph.add_node("(4, 1)", pos=(4,1));
    graph.add_node("(4, 2)", pos=(4,2));
    graph.add_node("(4, 3)", pos=(4,3));
    graph.add_node("(4, 4)", pos=(4,4));

    #adding some edges into the graph
    graph.add_edge("(2, 2)", "(3, 2)");
    graph.add_edge("(2, 2)", "(1, 2)");
    graph.add_edge("(2, 2)", "(2, 1)");
    graph.add_edge("(2, 2)", "(2, 3)");
    graph.add_edge("(2, 1)", "(3, 1)");
    graph.add_edge("(3, 1)", "(3, 2)");
    graph.add_edge("(3, 2)", "(3, 3)");
    graph.add_edge("(2, 3)", "(1, 3)");
    graph.add_edge("(1, 3)", "(1, 2)");
    graph.add_edge("(1, 2)", "(1, 1)");
    graph.add_edge("(1, 3)", "(1, 4)");
    graph.add_edge("(2, 3)", "(2, 4)");
    graph.add_edge("(3, 3)", "(3, 4)");
    graph.add_edge("(3, 3)", "(4, 3)");
    graph.add_edge("(3, 2)", "(4, 2)");
    graph.add_edge("(4, 2)", "(4, 1)");
    graph.add_edge("(4, 3)", "(4, 4)");
    graph.add_edge("(3, 4)", "(4, 4)");

def makeAllFigures( color ):
    count = 0

    for graph in graphs:
        count = count + 1
        plot.figure(count)
        if(graph.number_of_nodes() > 0):
            drawGraph ( graph , color)


    #showing the graphs, will pause the scripts
    plot.show();

def drawGraph( graph, colour):
    #getting the size
    size = math.sqrt(len(list(graph.nodes())))
    #creating the axis
    plot.ylim([-0.5,(size+1.5)])
    plot.xlim([-0.5,(size+1.5)])


    pos = {}
    for node in graph:
        nodeAsString = str(node)
        pos[nodeAsString] = literal_eval(nodeAsString)
    print pos

    #graphLibrary.set_node_attributes(graph,'pos',pos)

    #drawing the graph
    print (str(pos))
    graphLibrary.draw_networkx(graph, pos, node_color=colour, width=2.0, linewidth=2.0, font_size=10, node_size=800)

def createPoints( numberOfPackages, numberOfGarages, graph):
    #generating random locations for the garage and the package
    garageNumber = random.randrange(0, len(list(graph.nodes())));
    packagePickupNumber = random.randrange(0, len(list(graph.nodes())));
    packageDropoffNumber = random.randrange(0, len(list(graph.nodes())));

    while ((packageDropoffNumber == packagePickupNumber)):
        packageDropoffNumber = random.randrange(1, len(list(graph.nodes())));

    return [garageNumber, packagePickupNumber, packageDropoffNumber]

def testing():
    makeGraphList( 10 )
    #testing the graph
    makeAllFigures("red")
    graphFile.graphs[0] = gridGraph(17)
