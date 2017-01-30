#_______________libraries______________
import car
import graphImplementation
import time
import datetime
import sys
import assignPackages

#_______________functions_______________
def testing():
    print

def main():
    # These values change the performance and complexity of the problem
    graphSize               = 20            # graphSize^2 = M
    numberOfCars            = 2              # N
    numberOfPackages        = 8              # K
    numberOfGraphs          = 1              # This will probably remain 1
    usingOptimal            = False           #use the optimal Algorithm, very slow

    #Graph reduction settings
    isMinimumSpanningTree   = False         # If true, the tree will be minimum spanning
    performGraphReduction   = True          # The graph will perform the reduction algorithm
    reductionFactor         = 1            # The % of nodes that will be chosen for edge reduction    ( 0.0 , 1.0 )
    additionalRandomness    = True          # Makes the graph reduction function have a chance to not remove an edge
                                            # this makes the degree of selected nodes unlikely to have the same degree
    randomFactor            = 0.5           # The strength of the additional randomness   0.0 = No difference,   1.0 = Edges can never be removed
    minimumDegree           = 2             # The algorithm will strive to have the minimum degree be 2
    
    # These values are used for the test log entry - adjust before running tests
    codeVersion             = "5f85d88"         # The first 7 characters of the run's GitHub revision code
    teamMember              = "David"           # The name of the person running this test
    if usingOptimal:
        packageAssignmentMethod = "Logical        "  # The method used to assign packages
    else:
        packageAssignmentMethod = "Pseudo-Logical"  # The method used to assign packages

    pathfindingMethod       = "A* Search"       # The method used to pathfind
    currentDatetime = datetime.datetime.now()

    #Generating a list of graphs to use
    sys.stdout.write("Creating graph........................")
    graphImplementation.makeGraphList( graphSize )
    print "Done!"
    for graph in graphImplementation.graphs:
        print graphImplementation.printGraphStats(graph)
        
    numberOfEdgesPreReduction = graphImplementation.graphLibrary.number_of_edges(graph)
        
    print #handy statement just to add a newline
    
    #Reducing all of the graphs by the above options
    sys.stdout.write("Reducing graph........................\n")
    for graph in graphImplementation.graphs:
        if(performGraphReduction):
            if(isMinimumSpanningTree):
                graphImplementation.minimumSpanningTree(graph)
                continue
            elif(additionalRandomness):
                graphImplementation.reduceGraphRand(graph, reductionFactor, minimumDegree, randomFactor)
                continue
            else:
                graphImplementation.reduceGraph(graph, reductionFactor, minimumDegree)
    print "Done!"
    
    numberOfEdgesPostReduction = graphImplementation.graphLibrary.number_of_edges(graph)

    
    print #handy statement just to add a newline
    
    startTime = time.time()

    #for each graph we generated, we set up random locations and then get those packages.
    for currentGraph in graphImplementation.graphs:
        if (currentGraph != None):  #error check just in case there is a null (none) graph (a creation function failed)
            #calculating difficulty addition
            difficultyAddition = 1
            if(performGraphReduction):
                sys.stdout.write("Calculating difficulty addition.......")
                difficultyAddition += reductionFactor + (numberOfEdgesPreReduction/numberOfEdgesPostReduction)
                sys.stdout.write("done\n")
                print difficultyAddition
            
            sys.stdout.write("Creating car and package objects......")
            objectList = graphImplementation.createObjects(numberOfCars, numberOfPackages, currentGraph, difficultyAddition)
            print "Done!"
            print #handy statement just to add a newline
            
            #Note: objectList is a list of two lists formatted as follows:
                #cars: the list of garage numbers that exist on the map
                #packages: the list of package objects, each object knows its drop off/pickup locations
            cars = objectList[0]
            packages = objectList[1]
            
            # Assign the packages to cars
            sys.stdout.write("Assigning packages to cars............")
            if usingOptimal:
                assignPackages.startSearchTree(cars, packages)
            else:
                assignPackages.pseudoLogicalAssignment(cars, packages)
            print "Done!"
            print #handy statement just to add a newline

            # Initialize timer
            grandTotal = 0


            # Call a search method for each car on the map
            print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            for car in cars:
                carTotal = 0
                print "CAR " + str(car.identifier) + " IS BEGINNING ROUTE WITH " + str(len(car.packageList)) + " PACKAGES"
                print "\tGarage Location: " + str(car.currentLocation)
                carTotal += car.useAStar(currentGraph)
                grandTotal += carTotal
                print
                print "CAR " + str(car.identifier) + " FINISHED"
                print "CAR used gas: " + str(carTotal)
                print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            endTime = time.time()

            print "The grand total (total path lengths) was: " + str(grandTotal)
            print "\tAnd the total real time taken was: " + str(endTime - startTime)

    print "All packages delivered!"


    # Print diagnostic information at very end of simulation
    print "=========================================================================="
    print "IMPORTANT EXECUTION LOG - COPY TO TESTING SPREADSHEET"
    print "--------------------------------------------------------------------------"

    #adding a heading that shows what each thing is
    sys.stdout.write("Time                \t")
    sys.stdout.write("Code Version\t")
    sys.stdout.write("Team Member\t")
    sys.stdout.write("Cars\t")
    sys.stdout.write("Packages\t")
    sys.stdout.write("Graph Size\t")
    sys.stdout.write("Reduced?\t")
    sys.stdout.write("Assignment Method\t")
    sys.stdout.write("Pathfinding Method\t")
    sys.stdout.write("Total time\t     ")
    sys.stdout.write("\"Gas\" Usage\n")  
    
    # Shouldn't need to alter these directly
    sys.stdout.write(currentDatetime.strftime("%d-%b-%Y %I:%M %p") + "\t")
    sys.stdout.write(codeVersion + "\t        ")
    sys.stdout.write(teamMember + "\t        ")
    sys.stdout.write(str(numberOfCars) + "\t")
    sys.stdout.write(str(numberOfPackages) + "\t        ")
    sys.stdout.write(str(graphSize) + "\t        ")
    sys.stdout.write(str(performGraphReduction) + "\t        ")
    sys.stdout.write(packageAssignmentMethod + "\t        ")
    sys.stdout.write(pathfindingMethod + "\t        ")
    sys.stdout.write(str(endTime - startTime) + "\t     ")
    sys.stdout.write(str(grandTotal) + "\t")
    
    print
    print "=========================================================================="
    
        # Print diagnostic information at very end of simulation
    print "=========================================================================="
    print "EXTRA EXECUTION LOG - COPY TO TESTING SPREADSHEET"
    print "--------------------------------------------------------------------------"

    #adding a heading that shows what each thing is
    sys.stdout.write("Time                \t")
    sys.stdout.write("Code Version\t")
    sys.stdout.write("Team Member\t")
    sys.stdout.write("Cars\t")
    sys.stdout.write("Packages\t")
    sys.stdout.write("Graph Size\t")
    sys.stdout.write("Graphs\t")
    sys.stdout.write("Min Tree\t")
    sys.stdout.write("Reduced?\t")
    sys.stdout.write("Reduction Factor\t")
    sys.stdout.write("Additional Random?\t")
    sys.stdout.write("Random Factor\t")
    sys.stdout.write("MinDegree\t")
    sys.stdout.write("Assignment Method\t")
    sys.stdout.write("Pathfinding Method\t")
    sys.stdout.write("Total time\t     ")
    sys.stdout.write("\"Gas\" Usage\n")  
    
    # Shouldn't need to alter these directly
    sys.stdout.write(currentDatetime.strftime("%d-%b-%Y %I:%M %p") + "\t")
    sys.stdout.write(codeVersion + "\t        ")
    sys.stdout.write(teamMember + "\t        ")
    sys.stdout.write(str(numberOfCars) + "\t")
    sys.stdout.write(str(numberOfPackages) + "\t        ")
    sys.stdout.write(str(graphSize) + "\t        ")
    sys.stdout.write(str(numberOfGraphs) + "\t")
    sys.stdout.write(str(isMinimumSpanningTree) + "\t        ")
    sys.stdout.write(str(performGraphReduction) + "\t        ")
    sys.stdout.write(str(reductionFactor) + "\t                ")
    sys.stdout.write(str(additionalRandomness) + "\t                ")
    sys.stdout.write(str(randomFactor) + "\t        ")
    sys.stdout.write(str(minimumDegree) + "\t        ")
    sys.stdout.write(packageAssignmentMethod + "\t        ")
    sys.stdout.write(pathfindingMethod + "\t        ")
    sys.stdout.write(str(endTime - startTime) + "\t     ")
    sys.stdout.write(str(grandTotal) + "\t")
    
    print
    print "=========================================================================="
    
    if ( graphSize <= 10):
        graphImplementation.makeAllFigures( "White" )
    
if __name__ == "__main__":
    main()
