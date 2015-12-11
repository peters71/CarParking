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
        if (centerObs[1] > centerCar[1]) and (angle < 0):
            angle = -angle
        if (centerObs[1] < centerCar[1]) and (angle > 0):
            angle = -angle
        orientDiff1 = abs(orientCar - angle)
        orientDiff2 = abs(orientCar - orientObs)
        numInPark = 0
        for v in car.getVertices():
            if park.contains(v):
                numInPark += 1
        if numInPark == 0: 
            return -dist/250 - orientDiff1
        else:
            return numInPark*100 - dist - (orientDiff2 + 0.01)

    @staticmethod
    def evaluateMiddle(state, action, middleState):
        gameState = state.generateSuccessor(action)
        car = gameState.data.agentStates[0].car
        car2 = middleState.data.agentStates[0].car
        centerCar, orientCar = car.getCenterAndOrient()
        centerObs, orientObs = car2.getCenterAndOrient()
        dist = ((centerCar[0] - centerObs[0])**2 + (centerCar[1] - centerObs[1])**2)**0.5
        angle = math.atan((centerCar[1] - centerObs[1])/(centerCar[0] - centerObs[0]))
        if (centerObs[1] > centerCar[1]) and (angle < 0):
            angle = -angle
        if (centerObs[1] < centerCar[1]) and (angle > 0):
            angle = -angle
        orientDiff1 = abs(angle - orientCar)
        orientDiff2 = abs(orientObs - orientCar)
        return -dist/250 -  orientDiff1 - orientDiff2

