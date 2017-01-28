#_______________libraries_______________
import car
import graphImplementation

#_______________functions_______________
def testing():
    print
    ##print
    #print "-------------------------"
    #print "testing the blackboardController"

def main():
    graphSize = 1000         #note, sizes over about 200 start to get slow on Bryton's computer.
    numberOfCars = 50       #if you want to generate more cars change this number
    numberOfPackages = 100   #if you want to generate more packages change this number
    
    print "Number of cars (N): " + str(numberOfCars)
    print "Number of packages (K): " + str(numberOfPackages)
    
    #Generating a list of graphs to show
    
    graphImplementation.makeGraphList( graphSize )
    print "Graph has been created"

    #for each graph we generated, we set up random locations and then get those packages.
    #Note: objectList is a list of two lists formatted as follows:
        #cars: the list of garage numbers that exist on the map
        #packages: the list of package objects, each object knows its drop off/pickup locations
    for currentGraph in graphImplementation.graphs:
        if (currentGraph != None):  #error check just in case there is a null (none) graph (a creation function failed)
            #print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

            objectList = graphImplementation.createObjects(numberOfCars, numberOfPackages, currentGraph)
            print "Objects created"

            #after we get the integers, we have to get the specific nodes and tell the user
            cars = objectList[0]
            packages = objectList[1]
            
            #logic for assigning packages to cars in a smart way will eventually go here
            #Note: package difficulty is being calculate at the point of package creation
                #access it using package.difficulty
            
            #for now, simply give each car a package in no particular order until there are no packages left
            while packages:
                for car in cars:
                    if packages:
                        car.packageList.append(packages.pop())
                    else: 
                        break
            
            for car in cars:
                print "CAR " + str(car.identifier) + " IS BEGINNING ROUTE WITH " + str(len(car.packageList)) + " PACKAGES"
                print "\tGarage Location: " + str(car.currentLocation)
                car.useAStar(currentGraph)
                print
                print "CAR " + str(car.identifier) + " FINISHED"
                print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

    print "All packages delivered!"
    
    if ( graphSize <= 10):
        graphImplementation.makeAllFigures( "White" )
    
if __name__ == "__main__":
    main()
