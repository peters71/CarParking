from game import *
from actions import *
import sys
import os
import layout
import graphicsDisplay

class ClassicGameRules:
  def newGame(self, layout, agents, display):
    initState = GameState()
    initState.initialize(layout)
    game = Game(agents, display)
    game.state = initState
    return game


class CarRules:
  def getLegalActions(state):
    return [Directions.FORWARD, Directions.BACKWARD, Directions.LEFT, Directions.RIGHT, Directions.RLEFT, Directions.RRIGHT, Directions.STOP] 
  getLegalActions = staticmethod(getLegalActions)

  def applyAction(state, action):
    carState = state.data.agentStates[0]
    carState.car.generateSuccessor(action)
  applyAction = staticmethod(applyAction)
  
def default(str):
  return str + ' [Default: %default]'


def parseAgentArgs(str):
  if str == None: return {}
  pieces = str.split(',')
  opts = {}
  for p in pieces:
    if '=' in p:
      key, val = p.split('=')
    else:
      key, val = p, 1
    opts[key] = val
  return opts

def readCommand(argv):
  from optparse import OptionParser
  usageStr = """
  USAGE:    python carParking.py <options>
  """
  parser = OptionParser(usageStr)

  parser.add_option('-d', '--driver', dest='driver', 
                    help=default('the agent TYPE in the driverAgent module to use'), 
		    metavar='TYPE', default='KeyboardAgent')
  parser.add_option('-l', '--layout', dest='layout',
                    help=default('the LAYOUT_FILE from which to load the map layout'),
                    metavar='LAYOUT_FILE', default='small')

  options, otherjunk = parser.parse_args(argv)
  if len(otherjunk) != 0:
    raise Exception('Command line input not understood: ' + str(otherjunk))

  args = dict()
  args['display'] = graphicsDisplay.carParkingGraphics()

  # Choose a layout
  args['layout'] = layout.getLayout( options.layout )
  if args['layout'] == None: raise Exception("The layout " + options.layout + " cannot be found")
  
  # Choose a driver agent
  driverType = loadAgent(options.driver)
  args['driver'] = driverType()
  
  return args

def loadAgent(driver):
  # Looks through all pythonPath Directories for the right module,
  pythonPathStr = os.path.expandvars("$PYTHONPATH")
  if pythonPathStr.find(';') == -1:
    pythonPathDirs = pythonPathStr.split(':')
  else:
    pythonPathDirs = pythonPathStr.split(';')
  pythonPathDirs.append('.')

  for moduleDir in pythonPathDirs:
    if not os.path.isdir(moduleDir): continue
    moduleNames = [f for f in os.listdir(moduleDir) if f.endswith('gents.py') or f=='submission.py']
    for modulename in moduleNames:
      try:
        module = __import__(modulename[:-3])
      except ImportError:
        continue
      if driver in dir(module):
	return getattr(module, driver)
  raise Exception('The agent ' + driver + ' is not specified in any *Agents.py.')
															  

def runGames(layout, driver, display):
  rules=ClassicGameRules()
  agents = [driver]
  game = rules.newGame(layout, agents, display)
  game.run()


if __name__ == '__main__':
  args = readCommand(sys.argv[1:])
  runGames(**args)
  pass
