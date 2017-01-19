#libraries
import networkx as graphLibrary

#functions
def depthFirstSearch(graphToSearch, startNode, endNode):
    print("DFS called");
    print "Start Node: " + str(startNode) + "; End Node: " + str(endNode);

    currentNode = startNode;
    toVisitStack = [currentNode];
    nodesVisited = [];
    counter = 0;

    while( len(toVisitStack) != 0 ):
        print "Stack of nodes to visit: " + str(toVisitStack);
        counter += 1;
        currentNode = toVisitStack.pop();
        nodesVisited.append(currentNode);

        nodesToAdd = list(graphLibrary.all_neighbors(graphToSearch, currentNode));
        if endNode in nodesToAdd:
            currentNode = endNode;
            nodesVisited.append(currentNode);
            break;

        for item in nodesVisited:
            if item in nodesToAdd:
                nodesToAdd.remove(item);
    
        toVisitStack.extend(nodesToAdd);

    print "Number of nodes explored: " + str(counter);
    print
    return currentNode

def breadthFirstSearch(graphToSearch, startNode):
    print("BFS called");

def aStarSearch(graphToSearch, startNode):
    print("A* search called");
