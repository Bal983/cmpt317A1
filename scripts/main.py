#libraries
import networkx as graphLibrary
import graphFile
import search

#main

#setting up a graph
graph = graphLibrary.Graph();
graphFile.initGraph(graph);

#calling DFS on the graph
search.depthFirstSearch(graph);

#calling BFS on the graph
search.breadthFirstSearch(graph);

#calling A* on the graph
search.aStarSearch(graph);
