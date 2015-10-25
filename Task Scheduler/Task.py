
class Task(object):
	
	def __init__(self,id=-1, name1=""):
		self.name = name1
		self.predecessors = []
		self.id = id
		self.duration = 0		
		self.successors = []
		self.startDay = -1
		self.endDay = -1 
		self.resourceOnTask = None
	
