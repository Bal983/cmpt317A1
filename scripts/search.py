# libraries
import networkx as graphLibrary
import heapq
import numpy
import sys
from collections import deque
from test.test_threaded_import import done

# functions

# depreciated function
def depthFirstSearch(graphToSearch, startNode, endNode):
    # print "------------------------------------------------------------"
    # print("DFS called");
    # print "Start Node: " + str(startNode) + "; End Node: " + str(endNode);

    # setting up the variables needed to do the search
    currentNode = startNode;
    toVisitStack = [currentNode];
    nodesVisited = [];
    
    # adding a counter for call comparison purposes
    counter = 0;

    # the actual searching loop
    while(len(toVisitStack) != 0):
        # this print statement just prints the stack of nodes we need to visit for debugging purposes
        counter += 1;
        
        # we are currently going to visit the last item added onto the stack
        currentNode = toVisitStack.pop();
        
        # then we need to add the current node into the list of nodes we have already visisted
        nodesVisited.append(currentNode);

        # get the list of neighbors
        neighborsList = list(graphLibrary.all_neighbors(graphToSearch, currentNode))
        
        # the first bit of heuristical logic, if one of the current neighbors are the node we are looking for, we instantly move there
        if endNode in neighborsList:
            currentNode = endNode;
            nodesVisited.append(currentNode);
            break;

        # nodes to add is simply a list of all of the neighbors of the current node
        for node in neighborsList:
            if node not in nodesVisited:
                toVisitStack.append(node)

    # print "Number of nodes explored: " + str(counter);
    # print
    return currentNode

# as the function name suggests, this is the revised DFS

# improved depth first search that makes use of sets, should be no more efficient, but the bug doesn't appear until much
# large sizes of the graph.

def depthFirstSearchRevised(graphToSearch, startNode, endNode):
    # print("Revised DFS called");
    # print "Start Node: " + str(startNode) + "; End Node: " + str(endNode);
    
    # we use sets instead of lists so we don't have to use our own code to compare the neighbors list to the visited list
    # both sets start by containing the startNode
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
    
    # print "Number of nodes explored: " + str(counter);
    return currentNode
            

# depreciated function
def breadthFirstSearch(graphToSearch, startNode, endNode):
    # print "------------------------------------------------------------"
    # print("BFS called");
    # print "Start Node: " + str(startNode) + "; End Node: " + str(endNode);

    # setting up the variables needed to do the search
    currentNode = startNode;
    toVisitQueue = deque([currentNode]);
    nodesVisited = [];
    
    # adding a counter for call comparison purposes
    counter = 0;

    # the actual searching loop
    while (len(toVisitQueue) != 0):
        counter += 1;
        
        # we are currently going to visit the first item in the queue
        currentNode = toVisitQueue.popleft();

        # then we need to add the current node into the list of nodes we have already visisted
        nodesVisited.append(currentNode);
    
        # nodes to add is simply a list of all of the neighbors of the current node
        neighborsList = list(graphLibrary.all_neighbors(graphToSearch, currentNode))
        
        # the first bit of heuristical logic, if one of the current neighbors are the node we are looking for, we instantly move there
        if endNode in neighborsList:
            currentNode = endNode;
            nodesVisited.append(currentNode);
            break;

        # We still aren't at the location, but we don't want duplicates, so we check if anything in nodesVisited is a node we are considering to add, if we find a duplicate we remove it.
        for item in nodesVisited:
            if item in neighborsList:
                neighborsList.remove(item);
    
        # then we add all of the neighbors into the stack
        toVisitQueue.extend(neighborsList);

    # print "Number of Nodes explored: " + str(counter);
    # print
    return currentNode

def breadthFirstSearchRevised(graphToSearch, startNode, endNode):
    # print("Revised BFS called");
    # print "Start Node: " + str(startNode) + "; End Node: " + str(endNode);
    
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
    
    # print "Number of nodes explored: " + str(counter);
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
     #
     print heuristic(startNode, endNode)


     openList , closedList = set() , set()

     openList.add(startNode)
     # Stores the best way to get to a specific node
     cameFromMap = dict()

     # Costs to reach particular nodes
     gScores = dict()

     fScores = dict()

     currentNode = startNode
     #
     fScores[currentNode] = heuristic(startNode, endNode)
     gScores[startNode] = 0

     minHeapF = []
     heapq.heappush(minHeapF, (sys.maxint, startNode))

     # not efficient
     while not openList :

         # Current node is the best scoring node in the fScore dictionary
         currentNode = heapq.heappop(minHeap)

         if(current == endNode):
            return reconstructPath(cameFromMap , current)
         openSet.remove(currentNode)
         closedSet.add(currentNode)
         # Check for unvisited neighbors

         for neighbor in currentNode.neighbors :

             if(neighbors in closedList):
                continue
             ##### Hardcoded 1 cost for any edge for now but can add a cost function easily
             neighborScore = gScore[startNode] + 1
             # add the node to the open list if not already in
             if(neighbor not in openList):
                 openList.add(neighbor)

             # # If this path to the neighbor isn't better than the known one, skip
             elif neighborScore >= gScore[neighbor]:
                continue

             cameFromMap[neighbor] = currentNode
             gScores[neighbor] = neighborScore
             fScores[neighbor] = neighborScore + heuristic(neighbor , endNode)


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
    
