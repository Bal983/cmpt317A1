__author__ = """Aric Hagberg (hagberg@lanl.gov)"""
#    Copyright (C) 2004-2015
#    Aric Hagberg <hagberg@lanl.gov>
#    Dan Schult <dschult@colgate.edu>
#    Pieter Swart <swart@lanl.gov>
#    All rights reserved.
#    BSD license.

#Imports
try:
    import math
    from ast import literal_eval    #additional library to fix a string interpretat
    import matplotlib.pyplot as plt
    import graphFile
    from networkx.generators.classic import empty_graph, complete_graph, grid_graph

except:
    raise
import networkx as nx
import random

#functions
def minimumSpanningTree( G ):
    trim(G , 1.0 , 1.0)
    
def trim( G , minDegree , likelyHood):
    #All edges retrieved from the graph
    print("Trimming" + str(G))
    print ("Nodes :" + str(G.nodes(True)))
    for n in G.nodes():
         print("Processing node: " + str(n))
         #Each edge is initially valid to remove
         neighbours = nx.to_edgelist(G,n)
         print("List of edges attached to " + str(n) + " : " + str( neighbours))
         edgesToNeighbours = []
         for e in neighbours:
             # edgesToNeighbours.append( (e[0],e[1],))
             if(G.degree(n) > minDegree):
                 #The edges to be processed
                 for adjacent in edgesToNeighbours:
                    #valid = (G.degree(adjacent) > minDegree  or   G.degree(n) > minDegree)
                    # Both nodes must meet the criteria
                    valid = (G.degree(n) > minDegree or G.degree(adjacent[1]))
                    print( (likelyHood) >= random.random() )

                    if(valid):

                        print("removing" + str())

                        G.remove_edge(e )
                        print ("Nodes :" + str(G.nodes(False)))
                        
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
#Another grid, but this one can be anysize
try:
    import matplotlib.pyplot as pltGrid
except:
    raise
N = 10
G=nx.grid_2d_graph(N,N)
pos = dict( (n, n) for n in G.nodes() )
labels = dict( ((i, j), i * 10 + j) for i, j in G.nodes() )
nx.draw_networkx(G, pos=pos, labels=labels)

pltGrid.axis('off')
pltGrid.show()

N = 3#input("Enter dimensions for grid plot.")
G=nx.grid_2d_graph(N,N)
trim( G , 1.0 , 1.0)
minimumSpanningTree(G)
pos = dict( (n, n) for n in G.nodes() )
labels = dict( ((i, j), i * 10 + j) for i, j in G.nodes() )
nx.draw_networkx(G, pos=pos, labels=labels)
pltGrid.axis('off')
pltGrid.show()