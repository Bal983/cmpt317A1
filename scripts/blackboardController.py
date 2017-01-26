#_______________libraries_______________
import car
import graphImplementation

#_______________functions_______________
def testing():
    print
    print "-------------------------"
    print "testing the blackboardController"

def main():
    # Value for M
    graphSize = 1000         #note, sizes over about 200 start to get slow on Bryton's computer.
    # Value for N
    numberOfCars = 10      
    # Value for K
    numberOfPackages = 100   
    
    print "Number of cars: " + str(numberOfCars)
    print "Number of packages: " + str(numberOfPackages)
    print "-------------------------"
    
    #Generating a list of graphs to show
    graphImplementation.makeGraphList( graphSize )

    #for each graph we generated, we set up random locations and then get those packages.
    #Note: objectList is a list of two lists formatted as follows:
        #cars: the list of garage numbers that exist on the map
        #packages: the list of package objects, each object knows its drop off/pickup locations
    for currentGraph in graphImplementation.graphs:
        if (currentGraph != None):  #error check just in case there is a null (none) graph (a creation function failed)
            print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            
            objectList = graphImplementation.createObjects(numberOfCars, numberOfPackages, currentGraph)
            cars = objectList[0]
            packages = objectList[1]
            
            #logic for assigning packages to cars in a smart way will eventually go here
            
            #for now, simply give each car a package in no particular order until there are no packages left
            while packages:
                for car in cars:
                    if packages:
                        car.packageList.append(packages.pop())
                    else: 
                        break
            
            # Run the DFS method on each car
            for car in cars:
                #print "Car " + str(car.identifier) + " is now delivering its " + str(len(car.packageList)) + " packages"
                #print "\tGarage Location: " + str(car.currentLocation)
                car.start()
                #print
                #print "Car " + str(car.identifier) + " is now done delivering its " + str(len(car.packageList)) + " packages"
                #print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

    print "Parent thread done!"
    
    if ( graphSize <= 10):
        graphImplementation.makeAllFigures( "White" )
    
if __name__ == "__main__":
    main()
