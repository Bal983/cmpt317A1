# libraries
import networkx as graphLibrary
import heapq
import numpy
import sys
from collections import deque
from test.test_threaded_import import done


# functions
def depthFirstSearchRevised(graphToSearch, startNode, endNode):
    print "------------------------------------------------------------"
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
    
    print "Number of nodes explored: " + str(counter);
    return currentNode

def breadthFirstSearchRevised(graphToSearch, startNode, endNode):
    print "------------------------------------------------------------"
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
    
    print "Number of nodes explored: " + str(counter);
    return currentNode

def perfectWorldDistance(start, dest):
    if(start is None or dest is None):
        print "this is very bad"
        return
    xdiff = dest[0] - start[0]
    ydiff = dest[1] - start[1]
    return abs(xdiff) + abs(ydiff)
 
def aStarSearch(graphToSearch, startNode, endNode, heuristic):
    print "------------------------------------------------------------"
    print("A* search called");
    print "Start Node: " + str(startNode) + "; End Node: " + str(endNode);
    print "Difficulty of this delivery is: " + str(heuristic(startNode, endNode))

    openSet , closedSet = set(), set()
    openSet.add(startNode)
    
    # Stores the best way to get to a specific node
    cameFromMap = dict()

    # Costs to reach particular nodes
    gScores = dict()            #the score to get to that place from your starting location
    heuristicScores = dict()    #the score of the heuristic
    fScores = dict()            #the heuristic score added onto the gScore
    
    #Note: heuristicScores[node] is just fScore[node] - gScore[node]
    #if we run into memory issues, one thing we might be able to do is eliminate the heursticScores map
    #and pass around both the fScores and the gScores map
    
    fScores[startNode] = heuristic(startNode, endNode)
    heuristicScores[startNode] = fScores[startNode]
    gScores[startNode] = 0

    minHeap = []
    heapq.heappush(minHeap, (sys.maxint, startNode))

    while openSet:
        # Current node is the best scoring node in the fScore dictionary
        currentNode = getBestNode(minHeap, heuristicScores)[1]
                
        if(currentNode == endNode):
            return reconstructPath(cameFromMap , currentNode)
        
        print currentNode
        
        openSet.remove(currentNode)
        closedSet.add(currentNode)
        
        neighbors = set(graphLibrary.all_neighbors(graphToSearch, currentNode))
        
        # Check for unvisited neighbors
        for neighbor in neighbors:            
            if(neighbor in closedSet):
                continue
            
            ##### Hardcoded 1 cost for any edge for now but can add a cost function easily
            neighborScore = gScores[currentNode] + 1
            
            # add the node to the open list if not already in
            if(neighbor not in openSet):
                openSet.add(neighbor)

            # # If this path to the neighbor isn't better than the known one, skip
            elif neighborScore >= gScores[neighbor]:
                continue

            cameFromMap[neighbor] = currentNode
            gScores[neighbor] = neighborScore #the cost that we calculated from this node is the cheapest
            heuristicScores[neighbor] = heuristic(neighbor , endNode)
            neighborFScore = neighborScore + heuristicScores[neighbor]
            fScores[neighbor] = neighborFScore
            heapq.heappush(minHeap, (neighborFScore, neighbor))

def getBestNode( minHeap, heuristicScores):
    #if there is one (or zero) items in the heap, there can't be any ties.
    if(len(minHeap) <= 1 ):
        return heapq.heappop(minHeap)
    
    tieNodes = []
    
    #Note: in this algorithm our "nodes" are actually tuples where
    # the first element of the tuple is the f score and the second element is the node.
    
    #we know forsure we want the root of the heap, so we get that, and it is the best node
    tieNodes.append(heapq.heappop(minHeap))
    bestNode = tieNodes[0]
    
    #while we can peek at the heap and there are ties (with the fScores) in the heap
    #we have to pop the tie elements off.
    while(len(minHeap) >= 1 and minHeap[0][0] == tieNodes[0][0]):
        tieNodes.append(heapq.heappop(minHeap))
       
    #now we search through the list of tied elements and find the one with the best utility score 
    for node in tieNodes:
        if(heuristicScores[node[1]] < heuristicScores[bestNode[1]]):
            bestNode = node
    
    #then we remove the best element from the list of ties, and re add the remaining elements to the heap.
    tieNodes.remove(bestNode)
    for node in tieNodes:
        heapq.heappush(minHeap, (node[0], node[1]))

    return bestNode

def reconstructPath(cameFromMap , goalNode):
    path = [goalNode]
    current = goalNode
    while current in cameFromMap:
        current = cameFromMap[current]
        path.append(current)
    return path
    
def testing():
    print
    print "-------------------------"
    print "testing the search file"
    
if __name__ == "__main__":
    testing()
    
