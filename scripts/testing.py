#_______________libraries_______________
import blackboardController
import graphImplementation
import search
import car

#_______________functions______________
def testAll():
    blackboardController.testing()
    graphImplementation.testing( 5 )
    search.testing()
    car.testing()
    
if __name__ == "__main__":
    testAll()