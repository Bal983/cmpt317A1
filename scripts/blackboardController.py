#_______________libraries_______________
import car
import graphImplementation

#_______________functions_______________
def testing():
    print
    print "-------------------------"
    print "testing the blackboardController"

def main():
    #Generating a list of graphs to show
    size = 200
    graphImplementation.makeGraphList( size )
    
    if ( size <= 10):
        graphImplementation.makeAllFigures( "White" )

    #for each graph we generated, we set up random locations and then get those packages.
    #Note: objectList is a list of two lists formatted as follows:
        #cars: the list of garage numbers that exist on the map
        #packages: the list of package objects, each object knows its drop off/pickup locations
    for currentGraph in graphImplementation.graphs:
        if (currentGraph != None):  #error check just in case there is a null (none) graph (a creation function failed)
            print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            print len(list(currentGraph.nodes()))

            numberOfCars = 1       #if you want to generate more cars change this number
            numberOfPackages = 2   #if you want to generate more packages change this number
            objectList = graphImplementation.createObjects(numberOfCars, numberOfPackages, currentGraph)

            #after we get the integers, we have to get the specific nodes and tell the user
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
            
            for car in cars:
                print "Car " + str(car.identifier) + " is now delivering its " + str(len(car.packageList)) + " packages"
                car.useDFS(currentGraph)
                print
                print "Car " + str(car.identifier) + " is now done delivering its " + str(len(car.packageList)) + " packages"
                print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

    print "Done!"
    
if __name__ == "__main__":
    main()
