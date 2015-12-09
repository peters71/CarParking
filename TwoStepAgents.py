import math,random
from agent import *
from car import *
import heapq, operator
from collections import Counter
import copy

class TwoStepAgent(Agent):

	def __init__(self):
		self.lastPositions = []
		self.dc = None
		self.chosenAction = []
		self.chosenActionIndex = 1
		self.plannedActions = []
		self.stateHistory = []

		self.destinationStateList = []

	def getAction(self, gameState):

		(dest_center_x, dest_center_y), dest_orient = gameState.data.layout.getParkingSpace().getCenterAndOrient()
		print (dest_center_x, dest_center_y), dest_orient

		input('hold')

		return (0,0)

