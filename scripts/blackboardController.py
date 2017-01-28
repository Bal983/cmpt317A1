#_______________libraries_______________
import car
import graphImplementation
import time

#_______________functions_______________
def testing():
    print

def main():
    graphSize = 1000         #note, sizes over about 200 start to get slow on Bryton's computer.
    numberOfCars = 10        #if you want to generate more cars change this number
    numberOfPackages = 100   #if you want to generate more packages change this number
    
    print "Number of cars (N): " + str(numberOfCars)
    print "Number of packages (K): " + str(numberOfPackages)
    
    #Generating a list of graphs to show
    
    print "Creating graph....."
    graphImplementation.makeGraphList( graphSize )
    print "Graph has been created"

    #for each graph we generated, we set up random locations and then get those packages.
    #Note: objectList is a list of two lists formatted as follows:
        #cars: the list of garage numbers that exist on the map
        #packages: the list of package objects, each object knows its drop off/pickup locations
    for currentGraph in graphImplementation.graphs:
        if (currentGraph != None):  #error check just in case there is a null (none) graph (a creation function failed)
            print "Creating Objects"
            objectList = graphImplementation.createObjects(numberOfCars, numberOfPackages, currentGraph)
            print "Objects created"

            #after we get the integers, we have to get the specific nodes and tell the user
            cars = objectList[0]
            packages = objectList[1]
            
            #for now, simply give each car a package in no particular order until there are no packages left
            assignPackages(currentGraph, cars, packages)
            
            grandTotal = 0
            
            startTime = time.time()
            for car in cars:
                print "CAR " + str(car.identifier) + " IS BEGINNING ROUTE WITH " + str(len(car.packageList)) + " PACKAGES"
                print "\tGarage Location: " + str(car.currentLocation)
                grandTotal += car.useAStar(currentGraph)
                print
                print "CAR " + str(car.identifier) + " FINISHED"
                print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            endTime = time.time()

            print "The grand total (total path lengths) was: " + str(grandTotal)
            print "\tAnd the total real time taken was: " + str(endTime - startTime)

    print "All packages delivered!"
    
    if ( graphSize <= 10):
        graphImplementation.makeAllFigures( "White" )

#logic for assigning packages to cars in a smart way will eventually go here
#Note: package difficulty is being calculate at the point of package creation access it using package.difficulty
def assignPackages( graph, cars, packages):
    print "Assigning Packages"

    '''
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
    '''
    while packages:
        for car in cars:
            if packages:
                car.packageList.append(packages.pop())
            else: 
                break

if __name__ == "__main__":
    main()
