import math,random
from agent import *
from car import *
import heapq, operator
from collections import Counter
import copy

class BeamSearchAgent(Agent):

  def __init__(self):
    self.lastPositions = []
    self.dc = None
    self.chosenAction = []
    self.chosenActionIndex = 1
    self.plannedActions = []
    self.stateHistory = []

  def getAction(self, gameState):

    carState = gameState.data.agentStates[0].car.getPosAndOrient()
    (center_x, center_y), Orient = carState
    Orient = Orient/3.14*180
    self.stateHistory.append(((int(center_x), int(center_y)), int(Orient)))
    #print 'stateHistory'
    #for i in self.stateHistory:
    #  print i

    if len(self.plannedActions) > 0:
      action = self.plannedActions.pop(0)
      # print 'plannedActions', self.plannedActions
      #print action
      return action

    beamSearch = 20
    depth = 50
    firstX = 10
    gameStateListNextLevel = []
    level = 1

    legalMoves = gameState.getLegalActions()
    legalMoves = [x for x in legalMoves if x != (0,0)]
    gameStateList = []
    for action in legalMoves:
      gameStateList.append((gameState, [action]))

    if len(gameStateList) > beamSearch:
      random.shuffle(gameStateList)

      scores = []
      for state, action in gameStateList:
        scoreTemp = self.evaluationFunction(state, action[-1])
        scores.append(scoreTemp)

      idx = zip(*heapq.nlargest(beamSearch, enumerate(scores), key=operator.itemgetter(1)))[0]

      gameStateListTemp = []
      for i in idx:
        gameStateListTemp.append(gameStateList[i])

      gameStateList = gameStateListTemp

    #print 'before while'
    #for s in gameStateList:
    #  print s[0].data.agentStates[0].car.getPosAndOrient(), s[1]

    # threshold = 0.005
    duplicateFlag = 1
    gameStateListBackup = copy.deepcopy(gameStateList)

    while 1:

      if len(gameStateList) > 0:
        gameState, actionHistory = gameStateList.pop(0)
      else:
        if len(gameStateListNextLevel) == 0:
          # threshold /= 2
          duplicateFlag = 0
          gameStateList = copy.deepcopy(gameStateListBackup)
          #print len(gameStateListNextLevel)
          #print '123123123s'
          #print threshold
          #print len(gameStateListBackup)
        else:
          duplicateFlag = 1
          gameStateList = gameStateListNextLevel
          gameStateListBackup = copy.deepcopy(gameStateList)
          #print 'gameStateListBackup'
          #print len(gameStateListBackup)
          gameStateListNextLevel = []

        if len(gameStateList) > beamSearch:
          random.shuffle(gameStateList)

          scores = []
          for state, action in gameStateList:
            scoreTemp = self.evaluationFunction(state, action[-1])
            scores.append(scoreTemp)

          idx = zip(*heapq.nlargest(beamSearch, enumerate(scores), key=operator.itemgetter(1)))[0]

          gameStateListTemp = []
          for i in idx:
            gameStateListTemp.append(gameStateList[i])

          gameStateList = gameStateListTemp


        gameState, actionHistory = gameStateList.pop(0)

      if len(actionHistory) == depth:
        gameStateList.append((gameState, actionHistory))
        break

      actionPrev = actionHistory[-1]

      newState = gameState.generateSuccessor(actionPrev)
      if newState.isWin():
        self.plannedActions = actionHistory
        # self.plannedActions = [x for x in self.plannedActions if x != (0,0)]
        action = self.plannedActions.pop(0)
        #print 'isWin'
        #print action
        return action
      
      carNewState = newState.data.agentStates[0].car.getPosAndOrient()
      (newcenter_x, newcenter_y), newOrient = carNewState
      newOrient = newOrient/3.14*180
      carNewState = ((int(newcenter_x), int(newcenter_y)), int(newOrient))
      #if carNewState in self.stateHistory:
      #  print '___________________'
      #  continue
      
      if duplicateFlag == 1:
        for carPrevState in self.stateHistory:
          if carNewState == carPrevState:
            newState = None
            break

      #(newcenter_x, newcenter_y), newOrient = carNewState
      #for (precenter_x, precenter_y), prevOrient in self.stateHistory:
      #  x = abs(newcenter_x - precenter_x) < threshold * abs(precenter_x)
      #  y = abs(newcenter_y - precenter_y) < threshold * abs(precenter_y)
      #  theta = abs(newOrient - prevOrient) < threshold * abs(prevOrient)
        #if x == True and y == True and theta == True:
        #  print '---------'
        #  print carNewState, actionPrev
        #  print '========='
          # newState = None

      if newState == None:
        continue

      legalMoves = newState.getLegalActions()
      legalMoves = [x for x in legalMoves if x != (0,0)]
      if len(actionHistory)%10 == 0:
        for action in legalMoves:
          gameStateListNextLevel.append((newState, actionHistory + [action]))
      elif actionPrev in legalMoves:
        gameStateListNextLevel.append((newState, actionHistory + [actionPrev]))
      else:
        for action in legalMoves:
          gameStateListNextLevel.append((newState, actionHistory + [action]))

      #print 'next level'
      #for s in gameStateListNextLevel:
      #  print s[0].data.agentStates[0].car.getPosAndOrient(), s[1]


    # print len(gameStateList)
    #for s in gameStateList:
    #  print s[0].data.agentStates[0].car.getPosAndOrient(), s[1]

    scores = []
    for state, action in gameStateList:
      scoreTemp = self.evaluationFunction(state, action[-1])
      scores.append(scoreTemp)
    bestScore = max(scores)

    bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
    chosenIndex = random.choice(bestIndices) # Pick randomly among the best
    #print 'best state'
    #print gameStateList[chosenIndex][0].data.agentStates[0].car.getPosAndOrient()
    action = gameStateList[chosenIndex][1][0]
    self.plannedActions = gameStateList[chosenIndex][1]

    # plannedActionsNonStop = [x for x in self.plannedActions if x != (0,0)]

    # print 'plannedActionsNonStop', plannedActionsNonStop

    self.plannedActions = self.plannedActions[0:firstX]
    # if len(self.plannedActions) == 0:
    #  self.plannedActions = [(0,0)]

    # print self.plannedActions 
    # input('')

    self.plannedActions.pop(0)

    #print 'bestMove'
    #print action
    return action

  def evaluationFunction(self, state, action):
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
      return numInPark*100 + 1.0/dist + 0.1/orientDiff# - angle/180*math.pi



