import networkx as graphLibrary

def initGraph( staticGraph ):
    #adding the nodes to make a 3 by 3 graph
    staticGraph.add_node("1,1");
    staticGraph.add_node("1,2");
    staticGraph.add_node("1,3");
    staticGraph.add_node("2,1");
    staticGraph.add_node("2,2");
    staticGraph.add_node("2,3");
    staticGraph.add_node("3,1");
    staticGraph.add_node("3,2");
    staticGraph.add_node("3,3");

    #adding some edges into the graph
    staticGraph.add_edge("2,2", "3,2");
    staticGraph.add_edge("2,2", "1,2");
    staticGraph.add_edge("2,2", "2,1");
    staticGraph.add_edge("2,2", "2,3");
    staticGraph.add_edge("1,1", "2,1");
    staticGraph.add_edge("2,1", "3,1");
    staticGraph.add_edge("3,1", "3,2");
    staticGraph.add_edge("3,2", "3,3");
    staticGraph.add_edge("3,3", "2,3");
    staticGraph.add_edge("2,3", "1,3");
    staticGraph.add_edge("1,3", "1,2");
    staticGraph.add_edge("1,2", "1,1");


#setting up staticGraph
staticGraph = graphLibrary.Graph();
initGraph(staticGraph);

#testing the graph
print("Here is a list of the graphs nodes");
print(list(staticGraph.nodes()));

print("Here is a list of the graphs edges");
print(list(staticGraph.edges()));
