__author__ = """Aric Hagberg (hagberg@lanl.gov)"""
#    Copyright (C) 2004-2015
#    Aric Hagberg <hagberg@lanl.gov>
#    Dan Schult <dschult@colgate.edu>
#    Pieter Swart <swart@lanl.gov>
#    All rights reserved.
#    BSD license.

# Imports
try:
    import math
    from ast import literal_eval  # additional library to fix a string interpretat
    import matplotlib.pyplot as plt
    import graphImplementation
    from networkx.generators.classic import empty_graph, complete_graph, grid_graph

except:
    raise
import networkx as nx
import random

# functions
def minimumSpanningTree(G):

    print "Making a minimum spanning tree."
    reduceGraph(G , 1.0 , 1.0)
    print "Remaining edges"
# reduces the connected of a graph by selecting a percentage of the nodes and destroying
# the edges if a minimum degree is maintained
# reductionFactor :float in (0.0 , 1.0 )
# minimumDegree   :int in [0 , inf)
def reduceGraph(graph, reductionFactor, minimumDegree):
    print "Trimming " + str(reductionFactor * 100) + "% of the nodes in " + str(G)
    print "Minimum Degree of " + str(minimumDegree) + " will be preserved."
    nx.info (graph)
    originalNodes = graph.nodes()
    # Take a random sample of the nodes according to the parameters
    sample = random.sample(originalNodes, int(reductionFactor * len(originalNodes)))
    # Remove all edges that don't break the degree rule
    edgeCountOrig = len(G.edges())
    print "Starting edge count: " + str (edgeCountOrig)
    for node in sample:
        edges = G.edges(node)
        for edge in edges:
            valid = G.degree(edge[0]) > minimumDegree and G.degree(edge[1]) > minimumDegree
            if(valid):

                G.remove_edge(edge[0], edge[1])
    edgeCountFinal = len(G.edges())
    print "Starting edge count: " + str(edgeCountFinal)
    print "Final reduction percentage :" + str( ( float (edgeCountFinal)/ float (edgeCountOrig )))
# reduces the connected of a graph by selecting a percentage of the nodes and destroying
# the edges if a minimum degree is maintained. Addition: pseudo-random defects compared to standard result
# reductionFactor :float in (0.0 , 1.0 )
# minimumDegree   :int in [0 , inf)
# rand            :float in (0.0 , 1.0 ) : likelihood for a removal to be executed
def reduceGraphRand(graph, reductionFactor, minimumDegree, randomFactor):
    print "Trimming " + str(reductionFactor * 100) + "% of the nodes in " + str(G)
    print "Minimum Degree of " + str(minimumDegree) + " will be preserved."
    nx.info (graph)
    originalNodes = graph.nodes()
    # Take a random sample of the nodes according to the parameters
    sample = random.sample(originalNodes, int(reductionFactor * len(originalNodes)))
    # Remove all edges that don't break the degree rule
    edgeCountOrig = len(G.edges())
    print "Starting edge count: " + str (edgeCountOrig)
    for node in sample:
        edges = G.edges(node)
        for edge in edges:
            valid = G.degree(edge[0]) > minimumDegree and G.degree(edge[1]) > minimumDegree
            if(valid):

                G.remove_edge(edge[0], edge[1])
    edgeCountFinal = len(G.edges())
    print "Starting edge count: " + str(edgeCountFinal)
    print "Final reduction percentage :" + str( ( float (edgeCountFinal)/ float (edgeCountOrig )))

'''
    # All edges retrieved from the graph

    sample = random.sample(G.nodes)
    print ()

    print ("Nodes :" + str(G.nodes(True)))
    for n in G.nodes():
         print("Processing node: " + str(n))
         # Each edge is initially valid to remove
         neighbours = nx.to_edgelist(G, n)
         print("List of edges attached to " + str(n) + " : " + str(neighbours))


'''
'''
G=nx.grid_2d_graph(4,4)  #4x4 grid

pos=nx.spring_layout(G,iterations=100)

plt.subplot(221)
nx.draw(G,pos,font_size=8)

plt.subplot(222)
nx.draw(G,pos,node_color='k',node_size=0,with_labels=True)

plt.subplot(223)
nx.draw(G,pos,node_color='g',node_size=250,with_labels=False,width=6)

plt.subplot(224)
H=G.to_directed()
nx.draw(H,pos,node_color='b',node_size=20,with_labels=False)

plt.savefig("four_grids.png")
plt.show()
'''
                        ######################
# Another grid, but this one can be anysize
try:
    import matplotlib.pyplot as pltGrid
except:
    raise
N = 10
G = nx.grid_2d_graph(N, N)
pos = dict((n, n) for n in G.nodes())
labels = dict(((i, j), i * 10 + j) for i, j in G.nodes())
nx.draw_networkx(G, pos=pos, labels=labels)

pltGrid.axis('off')
pltGrid.show()





N = 15  # input("Enter dimensions for grid plot.")
G = nx.grid_2d_graph(N, N)
minimumSpanningTree(G)
# minimumSpanningTree(G)

pos = dict((n, n) for n in G.nodes())
labels = dict(((i, j), i * 10 + j) for i, j in G.nodes())
nx.draw_networkx(G, pos=pos, labels=labels)
pltGrid.axis('off')
pltGrid.show()
