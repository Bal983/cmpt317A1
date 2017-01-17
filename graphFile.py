#libraries
import networkx as graphLibrary
import matplotlib.pyplot as plot

#functions
def initGraph( graph ):
    #adding the nodes to make a 3 by 3 graph
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


def drawGraph( graph ):
    #creating the axis
    plot.ylim([0,5]);
    plot.xlim([0,5]);
    
    #setting some options
    plot.title("Initial Graph");
    
    #getting the positions
    pos = graphLibrary.get_node_attributes(graph, 'pos');
    
    #drawing the graph
    graphLibrary.draw_networkx(graph, pos, font_size=12, node_color='white', node_size=600, width=2.0);
    plot.show();

#setting up staticGraph
staticGraph = graphLibrary.Graph();
initGraph(staticGraph);

#testing the graph
print("Here is a list of the graphs nodes");
print(list(staticGraph.nodes()));

print("Here is a list of the graphs edges");
print(list(staticGraph.edges()));

drawGraph( staticGraph );

