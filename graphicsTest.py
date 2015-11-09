from graphicsUtils import *
from obstacle import *
from car import *

if __name__ == '__main__':
  begin_graphics(1200, 600)
  clear_screen()
  LeftBlock = RecObstacle(300, 480, 150, 100, 0)
  g = polygon(LeftBlock.getVertices(), formatColor(1, 1, 1))
  RightBlock = RecObstacle(800, 480, 150, 100, 0)
  g = polygon(RightBlock.getVertices(), formatColor(1, 1, 1))
  car = Car(70, 25, 120, 60, 8, 500, 400, 3.14)
  g = polygon(car.getVertices(), formatColor(1, 1, 1))
  circle((150, 150), 20, formatColor(0.7, 0.3, 0.0), None, endpoints=[15, - 15])
  sleep(2)
