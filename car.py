import math

class Car:
# wheel base is the distance between front and back wheels, d is the distance between the back wheel and the back of the car, bumper is the length of the protrusion in the front of the car(The triangle)
# The center of the car is defined as the middle point of the two back wheels
  def __init__(self, wheelbase, d, length, width, bumper, center_x, center_y, orientation=0):
    self.geometry = CarGeometry(wheelbase, d, length, width, bumper)
    self.center_x = center_x
    self.center_y = center_y
    self.orientation = orientation

  def getSize(self):
    return (self.geometry.length, self.geometry.width)

  def getPosAndOrient(self):
    return ((self.center_x, self.center_y), self.orientation)

  def getVertices(self):
    x1 = self.center_x - self.geometry.d * math.cos(self.orientation)
    y1 = self.center_y - self.geometry.d * math.sin(self.orientation)
    x2 = self.center_x + (self.geometry.length - self.geometry.d) * math.cos(self.orientation)
    y2 = self.center_y + (self.geometry.length - self.geometry.d) * math.sin(self.orientation)
    dx = self.geometry.width * math.sin(self.orientation)/2
    dy = self.geometry.width * math.cos(self.orientation)/2
    V = [(x1 + dx, y1 - dy), (x1 - dx, y1 + dy),
         (x2 - dx, y2 + dy), (x2 + self.geometry.bumper * math.cos(self.orientation), y2 + self.geometry.bumper * math.sin(self.orientation)), (x2 + dx, y2 - dy)]
    return V

  def update(self, action):
    theta = self.orientation
    phi = action[0]
    ds = action[1]
    dx = ds * math.cos(theta)
    dy = ds * math.sin(theta)
    dtheta = ds * math.tan(phi) / self.geometry.wheelbase
    
    self.center_x += dx
    self.center_y += dy
    self.orientation += dtheta

  def contains(self, v):
    # The true center of the car with speed bumper considered
    center_x_ = self.center_x + ((self.geometry.length + self.geometry.bumper)*1.0/2 - self.geometry.d) * math.cos(self.orientation)
    center_y_ = self.center_y + ((self.geometry.length + self.geometry.bumper)*1.0/2 - self.geometry.d) * math.sin(self.orientation)

    x, y = v
    x = x - center_x_
    y = y - center_y_
    x_ = math.cos(self.orientation) * x + math.sin(self.orientation) * y
    y_ = - math.sin(self.orientation) * x + math.cos(self.orientation) * y

    if (2 * abs(x_) < self.geometry.length + self.geometry.bumper) and (2 * abs(y_) < self.geometry.width):
        return 1
    else:
        return 0

# The copiedCar is used when searching, the only difference from car is that it they refer to a same geometry and thus save space
class CopiedCar(Car):
  def __init__(self, car):
    self.geometry = car.geometry 
    self.center_x = car.center_x
    self.center_y = car.center_y
    self.orientation = car.orientation

class CarGeometry:
  def __init__(self, wheelbase, d, length, width, bumper):
    self.wheelbase = wheelbase
    self.d = d
    self.length = length
    self.width = width
    self.bumper = bumper

  







