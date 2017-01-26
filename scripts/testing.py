#_______________libraries_______________
import blackboardController
import graphImplementation
import search
from car import Car
from package import Package

#_______________functions______________
def testAll():
    blackboardController.testing()
    graphImplementation.testing( 5 )
    search.testing()
    Car.testing( Car( 0, None, None ) )
    Package.testing( Package( 0, None, None ) )
    
    
if __name__ == "__main__":
    testAll()