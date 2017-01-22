#libraries
import networkx as graphLibrary
import matplotlib.pyplot as plot
import random
from networkx.generators.classic import empty_graph, complete_graph, grid_graph

# Member Variables
graphs = []                 #A list of graphs that the graphFile manages

#functions
def makeGraphList( size ):
    completeRandomGraph( size )
    randomGridGraph ( size )
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

def randomGridGraph ( size):
    print "Forming a random grid graph of size " + str(size) + "."
    G = graphLibrary.complete_graph(size)
    print "Here's the stats of random grid graph:"
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

    graph.nodes(data=True);

def makeAllFigures( color):
    plot.figure(0)
    count = 0
    
    for graph in graphs:
        plot.title("Graph #:" + (str)(count+1))
        count = count +1
        plot.figure(count)

    drawGraph (graph , color , 10 , 10)

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

def drawGraph( graph, colour, width, height):
    #creating the axis
    plot.ylim([0,height])
    plot.xlim([0,width])
    
    #setting some options
    plot.title("Initial Graph")
      
    #getting the positions
    #pos = graphLibrary.get_node_attributes(graph, 'pos')
      
    #drawing the graph
    graphLibrary.draw_networkx(graph, node_color=colour,)

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


