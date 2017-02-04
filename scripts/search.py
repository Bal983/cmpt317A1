# libraries
import networkx as graphLibrary
import heapq
import numpy
import sys
from collections import deque
from test.test_threaded_import import done
from Queue import PriorityQueue


# functions
def depthFirstSearchRevised(graphToSearch, startNode, endNode):
    print("Revised DFS called");
    print "Start Node: " + str(startNode) + "; End Node: " + str(endNode);
    
    #we use sets instead of lists so we don't have to use our own code to 
    #compare the neighbors list to the visited list
    #both sets start by containing the startNode
    visited, stack = set(), [startNode]
    counter = 0
    
    currentNode = startNode
    
    while stack:
        counter += 1
        
        # the vertex is now the top item of the stack
        currentNode = stack.pop()
        
        # neighbors is a set of all the neighbors of the current node
        neighbors = set(graphLibrary.all_neighbors(graphToSearch, currentNode))
        
        # if the endnode is in the neighbors, we "move" there instantly and abandon the rest of the algorithm
        if endNode in neighbors:
            counter += 1
            currentNode = endNode
            break
        
        # otherwise, we have to continue searching
        if currentNode not in visited:
            visited.add(currentNode)
            stack.extend(neighbors - visited)
    
    return (currentNode, counter)

def breadthFirstSearchRevised(graphToSearch, startNode, endNode):
    print("Revised BFS called");
    print "Start Node: " + str(startNode) + "; End Node: " + str(endNode);
    
    # we use sets instead of lists so we don't have to use our own code to compare the neighbors list to the visited list
    # both sets start by containing the startNode
    visited, queue = set(), [startNode]
    counter = 0
    currentNode = startNode
    
    while queue:
        currentNode = queue.pop(0)
        counter += 1
        
        neighbors = set(graphLibrary.all_neighbors(graphToSearch, currentNode))
        
        # if the endnode is in the neighbors, we "move" there instantly and abandon the rest of the algorithm
        if endNode in neighbors:
            counter += 1
            currentNode = endNode
            break
        
        # otherwise, we have to continue searching.
        if currentNode not in visited:
            visited.add(currentNode)
            queue.extend(neighbors - visited)
    
    return (currentNode, counter)

def perfectWorldDistance(start, dest):
    if(start is None or dest is None):
        print "this is very bad"
        return
    xdiff = dest[0] - start[0]
    ydiff = dest[1] - start[1]
    return abs(xdiff) + abs(ydiff)
 
def aStarSearch(graphToSearch, startNode, endNode, heuristic):
    print("A* search called");
    print "Start Node: " + str(startNode) + "; End Node: " + str(endNode);
    print "Difficulty of this delivery is: " + str(heuristic(startNode, endNode))
    
    # Stores the best way to get to a specific node
    cameFromMap = dict()

    # Costs to reach particular nodes
    gScores = dict()            #the score to get to that place from your starting location
    
    gScores[startNode] = 0

    openPriorityQueue = PriorityQueue()
    closedSet = set()
    openPriorityQueue._put((heuristic(startNode , endNode), startNode))

    while openPriorityQueue:
        # Current node is the best scoring node in the fScore dictionary
        currentNode = getBestNode(openPriorityQueue, gScores)[1]
                
        if(currentNode == endNode):
            return reconstructPath(cameFromMap , currentNode)
        
        closedSet.add(currentNode)
        
        neighbors = set(graphLibrary.all_neighbors(graphToSearch, currentNode))
        
        # Check for unvisited neighbors
        for neighbor in neighbors:            
            if(neighbor in closedSet):
                continue
            
            # Hardcoded 1 cost for any edge for now but can add a cost function easily
            neighborScore = gScores[currentNode] + 1
            
            if neighbor not in gScores or neighborScore < gScores[neighbor]:
                gScores[neighbor] = neighborScore
                openPriorityQueue._put((neighborScore + heuristic(neighbor , endNode), neighbor ))
                cameFromMap[neighbor] = currentNode

def getBestNode( priorityQueue, gScores):
    x = PriorityQueue()
    x.get
    
    #if there is one (or zero) items in the heap, there can't be any ties.
    if(priorityQueue.qsize() <= 1 ):
        return priorityQueue._get()
    
    tieNodes = []
    
    #Note: in this algorithm our "nodes" are actually tuples where
    # the first element of the tuple is the f score and the second element is the node.
    
    #we know forsure we want the root of the heap, so we get that, and it is the best node
    tieNodes.append(priorityQueue._get())
    bestNode = tieNodes[0]
    
    #we have to pop elements off until we don't get a tie
    while(priorityQueue.qsize() >= 1):
        temp = priorityQueue._get()
        if (temp[0] == tieNodes[0][0]):
            tieNodes.append(temp)
        else:
            priorityQueue._put(temp)
            break
       
    #now we search through the list of tied elements and find the one with the best utility score 
    for node in tieNodes:
        if(node[0]-gScores[node[1]] < bestNode[0]-gScores[bestNode[1]]):
            bestNode = node
    
    #then we remove the best element from the list of ties, and re add the remaining elements to the heap.
    tieNodes.remove(bestNode)
    for node in tieNodes:
        priorityQueue._put((node[0], node[1]))

    return bestNode

def reconstructPath(cameFromMap , goalNode):
    path = [goalNode]
    current = goalNode
    while current in cameFromMap:
        current = cameFromMap[current]
        path.append(current)
    return path
    
if __name__ == "__main__":
    testing()
