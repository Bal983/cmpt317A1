#_______________libraries_______________
import car
import graphImplementation

#_______________functions_______________
def testing():
    print "testing the blackboardController"

def main():
    #Generating a list of graphs to show
    size = 10
    graphImplementation.makeGraphList( size )
    graphImplementation.makeAllFigures( "White" )

    #for each graph we generated, we set up random locations and then get those packages.
    #Note: pointsList is a list of three lists formatted as follows:
        #garageNumbers: the list of garage numbers that exist on the map
        #packagePickupNumbers: the list of package pickup locations
        #packageDropoffNumbers: the list of package drop off locations
        #packagePickupNumbers[x] corresponds to packageDropoffNumbers[x]
    for currentGraph in graphImplementation.graphs:
        if (currentGraph != None):  #error check just in case there is a null (none) graph (a creation function failed)
            print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            print len(list(currentGraph.nodes()))

            numberOfCars = 1;       #if you want to generate more cars change this number
            numberOfPackages = 2;   #if you want to generate more packages change this number
            pointsList = graphImplementation.createPoints(numberOfCars, numberOfPackages, currentGraph)

            #after we get the integers, we have to get the specific nodes and tell the user
            garageNodeNumbers = pointsList[0]
            packagePickupNodeNumbers = pointsList[1]
            packageDropoffNodeNumbers = pointsList[2]
        
            #creating empty lists, not needed but makes the code more readable
            garageNodes = list()
            packagePickupNodes = list()
            packageDropoffNodes = list()
        
            #now setting up these lists
            for x in garageNodeNumbers:
                garageNodes.append( list(currentGraph.nodes())[x] )
            
            for x in packagePickupNodeNumbers:
                packagePickupNodes.append( list(currentGraph.nodes())[x] )
            
            for x in packageDropoffNodeNumbers:
                packageDropoffNodes.append( list(currentGraph.nodes())[x] )
        
            print "Garage Locations: " + str(garageNodes)
            print "Package Pickup Locations: " + str(packagePickupNodes)
            print "Package Drop-off Locations: " + str(packageDropoffNodes)

            print "Doing a DFS search on the above locations, this will pick up and drop off the packages and then go home"
            car.useDFS(currentGraph, garageNodes, packagePickupNodes, packageDropoffNodes)

            print "Doing a BFS search on the above locations, this will pick up and drop off the packages and then go home"
            car.useBFS(currentGraph, garageNodes, packagePickupNodes, packageDropoffNodes)
        
    print "Done!"
    
if __name__ == "__main__":
    main()
