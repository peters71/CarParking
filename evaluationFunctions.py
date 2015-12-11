import math

class EvaluationFunction:
    @staticmethod
    def evaluateParking(state, action):
        gameState = state.generateSuccessor(action)
        if state.isWin():
            return 99999
        car = gameState.data.agentStates[0].car
        park = gameState.data.layout.getParkingSpace()
        centerCar, orientCar = car.getPosAndOrient()
        centerObs, orientObs = park.getCenterAndOrient()
        dist = ((centerCar[0] - centerObs[0])**2 + (centerCar[1] - centerObs[1])**2)**0.5
        angle = math.atan((centerCar[1] - centerObs[1])/(centerCar[0] - centerObs[0]))
        orientDiff = min([abs(orientCar - orientObs - 3.14159), abs(orientCar - orientObs), abs(orientCar - orientObs + 3.14159)])
        numInPark = 0
        for v in car.getVertices():
            if park.contains(v):
                numInPark += 1
        if numInPark == 0: 
            return -dist/250 - min(abs(angle - orientCar), abs(angle - orientCar - 3.14159), abs(angle - orientCar + 3.14159))
        else:
            return numInPark*100 + 1.0/dist + 0.1/(orientDiff + 0.01)# - angle/180*math.pi

    @staticmethod
    def evaluateMiddle(state, action, middleState):
        gameState = state.generateSuccessor(action)
        car = gameState.data.agentStates[0].car
        car2 = middleState.data.agentStates[0].car
        centerCar, orientCar = car.getCenterAndOrient()
        centerObs, orientObs = car2.getCenterAndOrient()
        dist = ((centerCar[0] - centerObs[0])**2 + (centerCar[1] - centerObs[1])**2)**0.5
        angle = math.atan((centerCar[1] - centerObs[1])/(centerCar[0] - centerObs[0]))
        orientDiff = min([abs(orientCar - orientObs - 3.14159), abs(orientCar - orientObs), abs(orientCar - orientObs + 3.14159)])
        return -dist/250 - min(abs(angle - orientCar), abs(angle - orientCar - 3.14159), abs(angle - orientCar + 3.14159)) - 0.5 * min(abs(orientObs - orientCar), abs(orientObs - orientCar - 3.14159), abs(orientObs - orientCar + 3.14159))

