#_______________libraries______________
import car
import graphImplementation
import time
import datetime
import sys
import heapq
import numpy

#_______________functions_______________
def testing():
    print

def main():
    # These values change the performance and complexity of the problem
    graphSize               = 10            # graphSize^2 = M
    numberOfCars            = 1             # N
    numberOfPackages        = 1             # K
    numberOfGraphs          = 1             # This will probably remain 1

    #Graph reduction settings
    isMinimumSpanningTree   = False         # If true, the tree will be minimum spanning
    performGraphReduction   = True          # The graph will perform the reduction algorithm
    reductionFactor         = 0.5           # The % of nodes that will be chosen for edge reduction    ( 0.0 , 1.0 )
    additionalRandomness    = True          # Makes the graph reduction function have a chance to not remove an edge
                                            # this makes the degree of selected nodes unlikely to have the same degree
    ignoreChance            = 0.5           # The strength of the additional randomness   0.0 = No difference,   1.0 = Edges can never be removed
    minimumDegree           = 2             # The algorithm will strive to have the minimum degree be 2
    
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
    
    sys.stdout.write("Reducing graph........................")
    for graph in graphImplementation.graphs:
        graphImplementation.reduceGraph(graph, reductionFactor, minimumDegree)

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

            for car in cars:
                print car.totalDifficulty
                print len(car.packageList)

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
def assignPackages( graph, CARS, PACKAGES):
    #step one, sort the list of packages based on their difficulties
    minHeap = []
    for package in PACKAGES:
        heapq.heappush(minHeap, (-1 * package.difficulty, package))

    #note, in this case, the gScores will be the difficulty from any car at its current position to the package pickup location
    #the heuristic is simply the difficulty rating of the package, which is calculated at the time of package construction
    #so the fScore will be the difficulty to deliver the package + the difficulty to get to the package.
    difficultyPerCar = dict()

    while minHeap:
        currentNode = heapq.heappop(minHeap)    #note, current node will be a tuple formated (package difficulty, package)

        difficultyPerCar.clear()   #ensuring that the dictionary is cleared
        #this loop will calculate the current gScore for every car
        for car in CARS:
            difficultyPerCar[car] = getDifficulty(car, currentNode[1]) + car.totalDifficulty

        bestCost = min(difficultyPerCar.items(), key=lambda x: x[1])

        bestCost[0].packageList.append(currentNode[1])
        bestCost[0].totalDifficulty += difficultyPerCar[bestCost[0]]

def getDifficulty(car, package):
    if(len(car.packageList) == 0):
        return abs(car.garageLocation[0] - package.pickupLocation[0]) + abs(car.garageLocation[1] - package.pickupLocation[1])
    else:
        return abs(car.packageList[-1].dropoffLocation[0] - package.pickupLocation[0]) + abs(car.packageList[-1].dropoffLocation[1] - package.pickupLocation[1])

if __name__ == "__main__":
    main()
