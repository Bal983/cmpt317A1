#_______________libraries______________
import heapq

#_______________functions______________

#logic for assigning packages to cars in a smart way will eventually go here
#Note: package difficulty is being calculated at the point of package creation access it using package.difficulty
def pseudoLogicalAssignment( graph, CARS, PACKAGES):
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
    currentBest = (0, list())
    
    for car in CARS:
        for package in PACKAGES:
            tempPACKAGES = PACKAGES
            tempPACKAGES.remove(package)
            
            car.packageList.append(package)
            possibleBest = searchTree( CARS, tempPACKAGES, getDifficulty(car, package) + package.difficulty)
            if possibleBest[0] < currentBest[0]:
                currentBest = possibleBest
            
            car.packageList.remove(package)
    
    

#Note:   the depth (d) of this tree will be the number of packages we are going to delivers
#        the width of each layer will be (n*k)^d
def searchTree(CARS, PACKAGES, currentDifficulty):
    while PACKAGES:
        None