from Slot	import Slot

class Resource(object): 
	def __init__(self, resId, resName): # take the dura
		self.name = resName
		self.id	= resId
		freeSlot = Slot()
		freeSlot.resourceOnSlot = self
		self.freeSlots=[]
		self.freeSlots.append(freeSlot)
