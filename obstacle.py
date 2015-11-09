import math

class Obstacle:
  def __init__(self, index=0):
    self.index = index
  
  def isColliding(self, car):
    raiseNotDefined()


class RecObstacle(Obstacle):
  def __init__(self, center_x, center_y, length, width, orientation=0):
    self.center_x = center_x
    self.center_y = center_y
    self.length = length
    self.width = width
    self.orientation = orientation

  def getSize(self):
    return (self.length, self.width)
  
  def getCenterAndOrient(self):
    return (self.center, self.orientation)

  def getVertices(self):
    dx1 = self.length * math.cos(self.orientation)/2
    dy1 = self.length * math.sin(self.orientation)/2
    dx2 = self.width * math.sin(self.orientation)/2
    dy2 = self.width * math.cos(self.orientation)/2
    V = [(self.center_x - dx1 + dx2, self.center_y - dy1 - dy2),
         (self.center_x - dx1 - dx2, self.center_y - dy1 + dy2),
	 (self.center_x + dx1 - dx2, self.center_y + dy1 + dy2),
	 (self.center_x + dx1 + dx2, self.center_y + dy1 - dy2)]
    return V

  def contains(self, vertice):
    x, y = vertice
    x = x - self.center_x
    y = y - self.center_y
    x_ = math.cos(self.orientation) * x + math.sin(self.orientation) * y
    y_ = - math.sin(self.orientation) * x + math.cos(self.orientation) * y

    if (2 * abs(x_) < self.length) and (2 * abs(y_) < self.width):
      return 1
    else:
      return 0

  def scale(self, wl, ww):
    self.length = self.length * wl
    self.width = self.width*wl

class SquareObstacle(RecObstacle):
  def __init__(self, center_x, center_y, length, orientation=0):
    self.center = center
    self.length = length
    self.width = length
    self.orientation = orientation
   


