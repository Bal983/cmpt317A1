#_______________libraries_______________
import blackboardController
import graphImplementation
import search
import car

#_______________functions______________
def testAll():
    blackboardController.testing()
    graphImplementation.testing( 10 )
    search.testing()
    car.testing()