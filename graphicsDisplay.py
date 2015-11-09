from graphicsUtils import *
import math, time

BACKGROUND_COLOR = formatColor(0,0,0)

class carParkingGraphics:
  def __init__(self):
    print "Initializing"

  def initialize(self, state):
    self.startGraphics(state)
    self.drawStaticObjects(state)
    self.drawAgentObjects(state)

  def startGraphics(self, state):
    self.layout = state.layout
    layout = self.layout
    self.width = layout.getWidth()
    self.height = layout.getHeight()
    self.make_window(self.width, self.height)
    self.currentState = layout

  def make_window(self, width, height):
    screen_width = width
    screen_height = height
    begin_graphics(screen_width, screen_height, BACKGROUND_COLOR, "Project Car Parking")

  def drawStaticObjects(self, state):
    layout = self.layout
    self.drawRecObstacles(layout.recObstacles)
    self.drawParkingSpace(layout.parkingSpace)
    self.drawGoldenParkingSpace(layout.goldenParkingSpace)
    refresh()

  def drawAgentObjects(self, state):
    self.agentImages = []
    for index, agent in enumerate(state.agentStates):
      image = self.drawCar(agent.car)
      self.agentImages.append((agent, image))
    refresh()

  def drawRecObstacles(self, recObstacles):
    for recObstacle in recObstacles:
      polygon(recObstacle.getVertices(), formatColor(1, 1, 1))


  def drawParkingSpace(self, parkingSpace):
    polygon(parkingSpace.getVertices(), formatColor(0, 1, 0))

  def drawGoldenParkingSpace(self, goldenParkingSpace):
    polygon(goldenParkingSpace.getVertices(), formatColor(1, 1, 0))

  def drawCar(self, car):
    return polygon(car.getVertices(), formatColor(1, 0, 0))

  def update(self, newState):
    agentIndex = newState._agentMoved
    agentIndex = 0
    agentState = newState.agentStates[agentIndex]
    prevState, prevImage = self.agentImages[agentIndex]
    self.moveCar(agentState, prevImage)

  def moveCar(self, agentState, image):
      moVe_to(image, *agentState.car.getVertices())

    
