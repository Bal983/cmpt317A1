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
    trim(G , 1.0 , 1.0)
    print "Remaining edges"
def gatherLegalSample(graph, reductionFactor, minimumDegree):
    originalNodes = graph.nodes()
    sample = random.sample(originalNodes, int(reductionFactor * len(originalNodes)))
    for node in sample:
        edges = G.edges(node)
        for edge in edges:
            valid = G.degree(edge[0]) > minimumDegree and G.degree(edge[1]) > minimumDegree
            if(valid):
                G.remove_edge(edge[0],edge[1])

def trim(G , minDegree , percent):
    # All edges retrieved from the graph
    print("Graph has the following nodes: " + str (G.edges()))
    print("Trimming " + str(percent) + " of the nodes" + str(G))
    sample = random.sample(G.nodes)
    print ()

    print ("Nodes :" + str(G.nodes(True)))
    for n in G.nodes():
         print("Processing node: " + str(n))
         # Each edge is initially valid to remove
         neighbours = nx.to_edgelist(G, n)
         print("List of edges attached to " + str(n) + " : " + str(neighbours))



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

N = 10  # input("Enter dimensions for grid plot.")
G = nx.grid_2d_graph(N, N)
# trim(G , 2.0 , 1.0)
gatherLegalSample(G, .5, 2)

# minimumSpanningTree(G)

pos = dict((n, n) for n in G.nodes())
labels = dict(((i, j), i * 10 + j) for i, j in G.nodes())
nx.draw_networkx(G, pos=pos, labels=labels)
pltGrid.axis('off')
pltGrid.show()
