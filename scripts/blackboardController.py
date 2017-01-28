#_______________libraries______________
import car
import graphImplementation
import time
import datetime
import sys

#_______________functions_______________
def testing():
    print

def main():
    # These values change the performance and complexity of the problem
    graphSize               = 1000          # graphSize^2 = M
    numberOfCars            = 10            # N
    numberOfPackages        = 100           # K
    numberOfGraphs          = 1             # This will probably remain 1
    
    # These values are used for the test log entry - adjust before running tests
    codeVersion             = "f5572fe"     # The first 7 characters of the run's GitHub revision code
    teamMember              = "David"       # The name of the person running this test
    packageAssignmentMethod = "Arbitrary"   # The method used to assign packages
    pathfindingMethod       = "A* Search"   # The method used to pathfind
    currentDatetime = datetime.datetime.now()
    
    #Generating a list of graphs to use
    sys.stdout.write("Creating graph........................")
    graphImplementation.makeGraphList( graphSize )
    print "Done!"

    #for each graph we generated, we set up random locations and then get those packages.
    for currentGraph in graphImplementation.graphs:
        if (currentGraph != None):  #error check just in case there is a null (none) graph (a creation function failed)
            sys.stdout.write("Creating car and package objects......")
            objectList = graphImplementation.createObjects(numberOfCars, numberOfPackages, currentGraph)
            print "Done!"
            
            #Note: objectList is a list of two lists formatted as follows:
                #cars: the list of garage numbers that exist on the map
                #packages: the list of package objects, each object knows its drop off/pickup locations
            cars = objectList[0]
            packages = objectList[1]
            
            # Assign the packages to cars
            sys.stdout.write("Assigning packages to cars............")
            assignPackages(currentGraph, cars, packages)
            print "Done!"
            
            # Initialize timer
            grandTotal = 0
            startTime = time.time()
            
            # Call a search method for each car on the map
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
        
    # Print diagnostic information at very end of simulation
    print "=========================================================================="
    print "EXECUTION LOG - COPY TO TESTING SPREADSHEET"
    print "--------------------------------------------------------------------------"
    
    # Shouldn't need to alter these directly
    sys.stdout.write(currentDatetime.strftime("%d-%b-%Y %I:%M %p") + "\t") 
    sys.stdout.write(codeVersion + "\t")                              
    sys.stdout.write(teamMember + "\t")                               
    sys.stdout.write(str(numberOfCars) + "\t")                             
    sys.stdout.write(str(numberOfPackages) + "\t")
    sys.stdout.write(str(graphSize) + "\t")
    sys.stdout.write(str(numberOfGraphs) + "\t")
    sys.stdout.write("Arbitrary" + "\t")                                    
    sys.stdout.write("A* Search" + "\t")                                    
    sys.stdout.write(str(endTime - startTime) + "\t")                      
    sys.stdout.write(str(grandTotal) + "\t")
    print
    print "=========================================================================="

#logic for assigning packages to cars in a smart way will eventually go here
#Note: package difficulty is being calculated at the point of package creation access it using package.difficulty
def assignPackages( graph, cars, packages):

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
    # For now, just assign the packages in an arbitrary way
    while packages:
        for car in cars:
            if packages:
                car.packageList.append(packages.pop())
            else: 
                break
            

if __name__ == "__main__":
    main()
