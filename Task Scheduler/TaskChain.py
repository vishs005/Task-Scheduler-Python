
from Task import Task

class TaskChain(object):
	
	def __init__(self,taskList = []):
		self.tasks = taskList
		self.totalDuration = 0
		
	
