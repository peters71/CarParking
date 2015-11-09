class Directions:
  FORWARD = (0, 10)
  BACKWARD = (0, -10)
  LEFT = (-0.2, 4)
  RIGHT = (0.2, 4)
  RLEFT = (-0.2, -4)
  RRIGHT = (0.2, -4)
  STOP = (0, 0)

class Actions:
  def getPossibleActions(state):
    return [Directions.FORWARD, Directions.BACKWARD, Directions.LEFT, Direction.RIGHT]
  getPossibleActions = staticmethod(getPossibleActions)

  def getLegalActions(state):
    return [Directions.FORWARD, Directions.BACKWARD, Directions.LEFT, Direction.RIGHT]
  getLegalActions = staticmethod(getLegalActions)
