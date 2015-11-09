from agent import Agent
from actions import Directions
import random

class KeyboardAgent(Agent):
  """
  An agent controlled by the keyboard.
  """
  # NOTE: Arrow keys also work.
  WEST_KEY  = 'a' 
  EAST_KEY  = 'd' 
  NORTH_KEY = 'w' 
  SOUTH_KEY = 's'
  RLEFT_KEY = 'j'
  RRIGHT_KEY = 'l'
  STOP_KEY = 'q'

  def __init__( self, index = 0 ):
    
    self.lastMove = Directions.STOP
    self.index = index
    self.keys = []
    
  def getAction( self, state):
    from graphicsUtils import keys_waiting
    from graphicsUtils import keys_pressed
    keys = keys_waiting() + keys_pressed()
    if keys != []:
      self.keys = keys
    self.keys = keys
    legal = state.getLegalActions(self.index)
    move = self.getMove(legal)
    
    if (self.STOP_KEY in self.keys) and Directions.STOP in legal: move = Directions.STOP

    if move not in legal:
      move = random.choice(legal)
      
    self.lastMove = move
    return move

  def getMove(self, legal):
    move = Directions.STOP
    if   (self.NORTH_KEY in self.keys or 'Up' in self.keys) and Directions.FORWARD in legal:   move = Directions.FORWARD
    if   (self.SOUTH_KEY in self.keys or 'Down' in self.keys) and Directions.BACKWARD in legal: move = Directions.BACKWARD
    if   (self.WEST_KEY in self.keys or 'Left' in self.keys) and Directions.LEFT in legal:   move = Directions.LEFT
    if   (self.EAST_KEY in self.keys or 'Right' in self.keys) and Directions.RIGHT in legal: move = Directions.RIGHT
    if   (self.RLEFT_KEY in self.keys):   move = Directions.RLEFT
    if   (self.RRIGHT_KEY in self.keys):   move = Directions.RRIGHT

    return move
  
"""
class KeyboardAgent2(KeyboardAgent):
  # NOTE: Arrow keys also work.
  WEST_KEY  = 'j' 
  EAST_KEY  = "l" 
  NORTH_KEY = 'i' 
  SOUTH_KEY = 'k'
  STOP_KEY = 'u'

  def getMove(self, legal):
    move = Directions.STOP
    if   (self.NORTH_KEY in self.keys) and Directions.NORTH in legal:   move = Directions.FORWARD
    if   (self.SOUTH_KEY in self.keys) and Directions.SOUTH in legal: move = Directions.BACKWARD
    if   (self.WEST_KEY in self.keys) and Directions.WEST in legal:   move = Directions.LEFT
    if   (self.EAST_KEY in self.keys) and Directions.EAST in legal: move = Directions.RIGHT

    return move

"""
  
  
