import math
from carParking import CarRules
from agent import AgentState
import copy
from collections import Counter
from twoStepAgents import TwoStepAgent

class GameState:

  def getLegalActions_Middle(self, index=0):
    if self.isLose(): return []
    actionSet = []
    for action in CarRules.getLegalActions(self):
      state = GameState(self)
      CarRules.applyAction(state, action)
      if not state.isLose():
        actionSet.append(action)
    return actionSet

  def getLegalActions(self, index=0):
    if self.isWin() or self.isLose(): return []
    actionSet = []
    for action in CarRules.getLegalActions(self):
      state = GameState(self)
      CarRules.applyAction(state, action)
      if not state.isLose():
        actionSet.append(action)
    return actionSet

  def generateSuccessor_Middle(self, action, agentIndex=0):
    # if self.isWin() or self.isLose(): raise Exception('Can\'t generate a successor of a terminal state.')
    state = GameState(self)
    CarRules.applyAction(state, action)

    # Book keeping
    self.data._agentMoved = agentIndex
    return state

  def generateSuccessor(self, action, agentIndex=0):
    if self.isWin() or self.isLose(): raise Exception('Can\'t generate a successor of a terminal state.')
    state = GameState(self)
    CarRules.applyAction(state, action)

    # Book keeping
    self.data._agentMoved = agentIndex
    return state

  def getCarPosition(self):
    return self.data.getPosition()
 
  def isWin(self):
    vertices = self.data.agentStates[0].car.getVertices()
    allIn = 1
    for vertice in vertices:
      if not self.data.layout.goldenParkingSpace.contains(vertice):
        allIn = 0
    if allIn == 1:
      return 1
    return 0

  def isLose(self):
    vertices = self.data.agentStates[0].car.getVertices()
    for vertice in vertices:
      if vertice[0] < 0 or vertice[0] > self.data.layout.getWidth() or vertice[1] < 0 or vertice[1] > self.data.layout.getHeight():
        #print 'Lose! (out of boundry)'
        return 1
      for recObstacles in self.data.layout.recObstacles:
        if recObstacles.contains(vertice):
          #print 'Lose! (car in obstacles)'
          return 1
        for v in recObstacles.getVertices():
          if self.data.agentStates[0].car.contains(v):
            #print 'Lose! (obstacles in car)'
            return 1

    return 0


## Helper methods:

  def __init__(self, prevState = None):
    if prevState != None:
      self.data = GameStateData(prevState.data)
    else:
      self.data = GameStateData()

  def deepCopy(self):
    state = GameState(self)
    state.data = self.data.deepCopy()
    return state

  def __hash__(self):
    return hash(self.data)

  def __str__(self):
    return str(self.data)

  def initialize(self, layout):
    self.data.initialize(layout)

class GameStateData:
  
  def __init__(self, prevState=None):
    if prevState != None:
      self.agentStates = self.copyAgentStates(prevState.agentStates)
      self.layout = prevState.layout
      self.score = prevState.score
    self._agentMoved = None
    self._lose = False
    self._win = False

  def getPosition(self):
    return self.agentStates[0].getPosAndOrient()

  def deepCopy(self):
    state = GameStateData(self)
    state.layout = self.layout.deepCopy()
    return state

  def copyAgentStates(self, agentStates):
      copied = []
      for agentState in agentStates:
        copied.append(agentState.duplicate())
      return copied
  
  def __eq__(self, other):
    if other == None: return False
    if not self.carState == other.agentState: return False 
    if not self.score == other.score: return False

  def __hash__(self):
    return

  def initialize(self, layout):
    self.layout = layout
    self.score = 0
    self.scoreChange = 0
    self.agentStates = []
    for carInit in layout.carInits:
      self.agentStates.append(AgentState(carInit))

class Game:
  """
  Manages the control flow, soliciting actions from agents. 
  """

  def __init__(self, agents, display):
    self.agentCrashed = False
    self.agents = agents
    self.display = display
    ## self.rules = rules
    self.gameOver = False
    self.moveHistory = []
    self.agentTimeout = False
    self.display = display

  def getProgress(self):
    """
    if self.gameOver:
      return 1.0
    else:
      return self.rules.getProgress(self)
    """

  def run(self):
    self.display.initialize(self.state.data)

    agentIndex = 0
    numAgents = len(self.agents)
    move_time = 0

    while not self.isGameOver(self.state):
      agent = self.agents[agentIndex]
      move_time += 1
      observation = self.state.deepCopy()

      # Solicit an action
      action = None
      action = agent.getAction(observation)
      # print action

      # Execute the action
      self.moveHistory.append(action)
      self.state = self.state.generateSuccessor(action, agentIndex )

      # wait = input("continue")

      # Change the display
      if isinstance(agent, TwoStepAgent):
        self.display.drawMiddleState(agent.middleState)

      self.display.update(self.state.data)
      
      # if agentIndex == numAgents + 1: self.numMoves += 1
      # Next agent
      # agentIndex = (agentIndex + 1) % numAgents

   ## self.display.finish()
    if self.state.isWin():
      print "Win!"
    elif self.state.isLose():
      print "Lose..."

    print "Total %d Time" % move_time

    actionHistory = Counter(self.moveHistory)
    move_time -= actionHistory[(0,0)]

    print "Move %d Times" % move_time
    print actionHistory
    print '----------------------------------------'
    # print [x for i,x in enumerate(self.moveHistory) if x != (0,0)]
    print self.moveHistory

  def isGameOver(self, gameState):
    if gameState.isWin() or gameState.isLose():
      return 1
    return 0
