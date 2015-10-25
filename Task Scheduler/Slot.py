
class Slot(object):
	def __init__(self,startDay = 1,endDay = 1000):
		self.start = startDay
		self.end = endDay
		self.slotDuration = self.end - self.start + 1
		self.resourceOnSlot = None
