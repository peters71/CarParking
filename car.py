import math

class Car:
  def __init__(self, wheelbase, d, length, width, bumper, center_x, center_y, orientation=0):
    self.wheelbase = wheelbase
    self.d = d
    self.length = length
    self.width = width
    self.bumper = bumper
    self.center_x = center_x
    self.center_y = center_y
    self.orientation = orientation

  def getSize(self):
    return (self.length, self.size)

  def getPosAndOrient(self):
    return ((self.center_x, self.center_y), self.orientation)

  def getVertices(self):
    x1 = self.center_x - self.d * math.cos(self.orientation)
    y1 = self.center_y - self.d * math.sin(self.orientation)
    x2 = self.center_x + (self.length - self.d) * math.cos(self.orientation)
    y2 = self.center_y + (self.length - self.d) * math.sin(self.orientation)
    dx = self.width * math.sin(self.orientation)/2
    dy = self.width * math.cos(self.orientation)/2
    V = [(x1 + dx, y1 - dy), (x1 - dx, y1 + dy),
         (x2 - dx, y2 + dy), (x2 + self.bumper * math.cos(self.orientation), y2 + self.bumper * math.sin(self.orientation)), (x2 + dx, y2 - dy)]
    return V

  def generateSuccessor(self, action):
    theta = self.orientation
    phi = action[0]
    ds = action[1]
    dx = ds * math.cos(theta)
    dy = ds * math.sin(theta)
    dtheta = ds * math.tan(phi) / self.wheelbase
    
    self.center_x += dx
    self.center_y += dy
    self.orientation += dtheta
    

