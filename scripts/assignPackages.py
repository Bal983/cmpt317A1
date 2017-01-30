#_______________libraries______________
import heapq
from Finder.Files import packages
import copy
from pip._vendor.pyparsing import _MAX_INT
import sys

#_______________functions______________
currentBest = (0, dict())
currentSolution = (0, dict())

#logic for assigning packages to cars in a smart way will eventually go here
#Note: package difficulty is being calculated at the point of package creation access it using package.difficulty
def pseudoLogicalAssignment( CARS, PACKAGES):
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

#calculates the difficulty for one car to pick up a package
def getDifficulty(car, package):
    if(len(car.packageList) == 0):
        return abs(car.garageLocation[0] - package.pickupLocation[0]) + abs(car.garageLocation[1] - package.pickupLocation[1])
    else:
        return abs(car.packageList[-1].dropoffLocation[0] - package.pickupLocation[0]) + abs(car.packageList[-1].dropoffLocation[1] - package.pickupLocation[1])
    
    
def startSearchTree( CARS, PACKAGES ):
    print
    
    carDict = dict()
    for car in CARS:
        carDict[car] = list()
    
    #a "solution" is a touple such that the first item is an integer marking the difficulty
    # and the second item is a dictionary keyed on cars that stores a list of pacakges.    
    
    global currentBest
    global currentSolution
    
    currentBest = (_MAX_INT, carDict)
    currentSolution = (0, copy.copy(carDict))
    
    searchTree( CARS, PACKAGES, 1)
    
    goingHomeDistance = 0
    for car in CARS:
        car.packageList.extend(currentBest[1][car])
        if currentBest[1][car]:
            goingHomeDistance += abs(currentBest[1][car][-1].dropoffLocation[0] - car.garageLocation[0]) + abs(currentBest[1][car][-1].dropoffLocation[1] - car.garageLocation[1])
    
    currentBest = (currentBest[0] + goingHomeDistance, currentBest[1])
    print "final", currentBest
    
    return currentBest[0]


#Note:   the depth (d) of this tree will be the number of packages we are going to delivers
#        the width of each layer will be (n*k)^d
def searchTree(CARS, PACKAGES, indent):
    global currentBest
    global currentSolution
    
    #note: at some point we should probably figure out how to factor in going home distance.
    if len(PACKAGES) == 0 and currentSolution[0] < currentBest[0]:
        #print"\t" * indent,  "At Leaf"
        newDict = dict()
        for car in CARS:
            newDict[car] = list()
            newDict[car] = copy.copy(currentSolution[1][car])
        currentBest = (copy.copy(currentSolution[0]), newDict)
        #print currentBest[0], "\t", currentBest[1]
    else:
        for car in CARS:
            #print "\t" * indent, "Car" , car.identifier
            for package in PACKAGES:     
                #print "\t" * indent, "Package", package.identifier
                #copies the list of PACKAGES
                tempPACKAGES = list(PACKAGES)
                tempPACKAGES.remove(package)
                
                currentDifficulty = revisedGetDifficulty(car, package) + package.difficulty
                #print "\t" * indent, currentDifficulty
                
                if (currentSolution[0] + currentDifficulty) >= currentBest[0]:
                    #print "\t" * indent,  "Skipped"
                    continue
                
                #this may prove to be problematic.
                currentSolution[1][car].append(package)
                currentSolution = (currentSolution[0] + currentDifficulty, currentSolution[1])
                #print "\t" * indent, currentSolution[0]
            
                #print "\t" * indent, "Recursing"
                searchTree(CARS, tempPACKAGES, indent+1)
                
                #this may prove to be problematic.
                currentSolution[1][car].remove(package)
                currentSolution = (currentSolution[0] - currentDifficulty, currentSolution[1])          

def revisedGetDifficulty(car, package):
    global currentSolution
    if(len(currentSolution[1][car]) == 0):
        return abs(car.garageLocation[0] - package.pickupLocation[0]) + abs(car.garageLocation[1] - package.pickupLocation[1])
    else:
        return abs(currentSolution[1][car][-1].dropoffLocation[0] - package.pickupLocation[0]) + abs(currentSolution[1][car][-1].dropoffLocation[1] - package.pickupLocation[1])
    

                
                
                
                
                
                
                
                
