import math,random
from agent import *
from car import *
from evaluationFunctions import EvaluationFunction

class SimpleSearchAgent(Agent):

  def __init__(self):
    self.lastPositions = []
    self.dc = None
    self.chosenAction = []
    self.chosenActionIndex = 1
    self.plannedActions = []

  def getAction(self, gameState):
    if len(self.plannedActions) > 0:
      action = self.plannedActions.pop(0)
      return action

    legalMoves = gameState.getLegalActions()
    gameStateList = []
    for action in legalMoves:
      gameStateList.append((gameState, [action]))
    depth = 25
    while 1:
      gameState, actionHistory = gameStateList.pop(0)

      if len(actionHistory) == depth:
        gameStateList.append((gameState, actionHistory))
        break

      actionPrev = actionHistory[-1]

      newState = gameState.generateSuccessor(actionPrev)
      if newState.isWin():
        self.plannedActions = actionHistory
        action = self.plannedActions.pop(0)
        return action
      
      legalMoves = newState.getLegalActions()
      if len(actionHistory)%10 == 0:
        for action in legalMoves:
          gameStateList.append((newState, actionHistory + [action]))
      elif actionPrev in legalMoves:
        gameStateList.append((newState, actionHistory + [actionPrev]))
      else:
        for action in legalMoves:
          gameStateList.append((newState, actionHistory + [action]))


    scores = []
    for state, action in gameStateList:
      scoreTemp = self.evaluationFunction(state, action[-1])
      scores.append(scoreTemp)
    bestScore = max(scores)

    bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
    chosenIndex = random.choice(bestIndices) # Pick randomly among the best
    action = gameStateList[chosenIndex][1][0]
    self.plannedActions = gameStateList[chosenIndex][1]
    self.plannedActions.pop(0)
    return action

  def evaluationFunction(self, state, action):
    return EvaluationFunction.evaluateParking(state, action)

  def searchAction(self, gameState):
    bestTotalCost = [float('+inf')]
    bestHistory = [None]
    def recurse(state, totalCost, history):
      if state.isWin():
        if totalCost < bestTotalCost[0]:
          bestTotalCost[0] = totalCost
          bestHistory[0] = history
          return
        if totalCost > 15:
          return
      actionPrev = history[-1]
      for action in state.getLegalActions():
        if action[0] == -actionPrev[0] and action[1] == -actionPrev[1]:
          continue
        newState = state.generateSuccessor(action)
        recurse(newState, totalCost + 1, history + [action])
      return
    recurse(gameState,0,[(0,0)])
    return bestHistory[0]



