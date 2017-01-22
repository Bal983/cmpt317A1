#libraries
import networkx as graphLibrary
from collections import deque

#functions
def depthFirstSearch(graphToSearch, startNode, endNode):
    print("DFS called");
    print "Start Node: " + str(startNode) + "; End Node: " + str(endNode);

    #setting up the variables needed to do the search
    currentNode = startNode;
    toVisitStack = [currentNode];
    nodesVisited = [];
    
    #adding a counter for call comparison purposes
    counter = 0;

    #the actual searching loop
    while( len(toVisitStack) != 0 ):
        #this print statement just prints the stack of nodes we need to visit for debugging purposes
        print "Stack of nodes to visit: " + str(toVisitStack);
        counter += 1;
        
        #we are currently going to visit the last item added onto the stack
        currentNode = toVisitStack.pop();
        #then we need to add the current node into the list of nodes we have already visisted
        nodesVisited.append(currentNode);

        #nodes to add is simply a list of all of the neighbors of the current node
        nodesToAdd = list(graphLibrary.all_neighbors(graphToSearch, currentNode));
        
        #the first bit of heuristical logic, if one of the current neighbors are the node we are looking for, we instantly move there
        if endNode in nodesToAdd:
            currentNode = endNode;
            nodesVisited.append(currentNode);
            break;

        #We still aren't at the location, but we don't want duplicates, so we check if anything in nodesVisited is a node we are considering to add, if we find a duplicate we remove it.
        for item in nodesVisited:
            if item in nodesToAdd:
                nodesToAdd.remove(item);
    
        #then we add all of the neighbors onto the stack
        toVisitStack.extend(nodesToAdd);

    print "Number of nodes explored: " + str(counter);
    print
    return currentNode

def breadthFirstSearch(graphToSearch, startNode, endNode):
    print("BFS called");
    print "Start Node: " + str(startNode) + "; End Node: " + str(endNode);

    #setting up the variables needed to do the search
    currentNode = startNode;
    toVisitQueue = deque([currentNode]);
    nodesVisited = [];
    
    #adding a counter for call comparison purposes
    counter = 0;

    #the actual searching loop
    while (len(toVisitQueue) != 0):
        #this print statement just prints the queue of nodes we need to visit for debugging purposes
        print "Stack of nodes to visit: " + str(toVisitQueue);
        counter += 1;
        
        #we are currently going to visit the first item in the queue
        currentNode = toVisitQueue.popleft();
        #then we need to add the current node into the list of nodes we have already visisted
        nodesVisited.append(currentNode);
    
        #nodes to add is simply a list of all of the neighbors of the current node
        nodesToAdd = list(graphLibrary.all_neighbors(graphToSearch, currentNode));
        
        #the first bit of heuristical logic, if one of the current neighbors are the node we are looking for, we instantly move there
        if endNode in nodesToAdd:
            currentNode = endNode;
            nodesVisited.append(currentNode);
            break;

        #We still aren't at the location, but we don't want duplicates, so we check if anything in nodesVisited is a node we are considering to add, if we find a duplicate we remove it.
        for item in nodesVisited:
            if item in nodesToAdd:
                nodesToAdd.remove(item);
    
        #then we add all of the neighbors into the stack
        toVisitQueue.extend(nodesToAdd);

    print "Number of Nodes explored: " + str(counter);
    print
    return currentNode

def aStarSearch(graphToSearch, startNode):
    print("A* search called");
