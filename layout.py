import os
import json
import random
import copy

from obstacle import *
from car import *

VISIBILITY_MATRIX_CACHE = {}

class Layout:
  """
  A Layout manages the static information about the game board.
  """
  
  def __init__(self, worldName):
    self.loadData(worldName)

  def loadData(self, worldName):
    layoutFileName = worldName + '.json'
    layoutDir = 'layouts'
    layoutPath = os.path.join(layoutDir, layoutFileName)
    layoutFile = open(layoutPath)
    self.data = json.load(layoutFile)
    layoutFile.close()
    self.recObstacles = [RecObstacle(*args) for args in self.data['recObstacles']]
    self.parkingSpace = RecObstacle(*self.data['parkingSpace'])
    self.goldenParkingSpace = copy.deepcopy(self.parkingSpace)
    self.goldenParkingSpace.scale(0.8, 0.9)
    self.carInits = self.data['carInit']
    
  def getWidth(self):
    return self.data['size'][0]

  def getHeight(self):
    return self.data['size'][1]

  def getRecObstacles(self):
    return self.recObstacles

  def getParkingSpace(self):
    return self.parkingSpace

  def deepCopy(self):
    return copy.deepcopy(self)

  
def getLayout(name, back = 2):
    print "Getting layout"
    return Layout(name)
