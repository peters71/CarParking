import math
from car import Car
class Agent:
  def __init__(self, index=0):
    self.index = index

  def getAction(self, state):
    raiseNotDefined()

"""
class Configuration:
  ## A Configuration holds the position of the car 

  def __init__(self, posAndOrient):
    self.posAndOrient = posAndOrient

  def getPosAndOrient(self):
    return self.posAndOrient

  def __hash__(self):
    x = hash(self.posAndOrient[0])
    y = hash(self.posAndOrient[2])
    return hash(x + 13 * y)

  def __str__(self):
    return "(pos, orient) = ("+str(self.posAndOrient[0]) + ", "+str(self.posAndOrient[1]) + ")"

  def generateSuccessor(self, action, L):
    x, y = self.posAndOrient[0]
    theta = self.posAndOrient[1]
    phi = action[0]
    ds = action[1]
    dx = ds * math.cos(theta)
    dy = ds * math.sin(theta)
    dtheta = ds * math.tan(phi) / L
    return Configuration(((x + dx, y + dy), theta + dtheta))
"""
class AgentState:
  """
  AgentState hold the state of a car (configuration)
  """

  def __init__(self, carInit):
    self.car = Car(*carInit)
    
  def getPosAndOrient(self):
    return self.car.getPosAndOrient()


