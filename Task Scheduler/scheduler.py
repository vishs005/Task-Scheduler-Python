#!/usr/bin/python

from __future__ import print_function
import sys
from Task 	import Task
from Graph 	import Graph
from TaskChain 	import TaskChain
from Resource 	import Resource
from Slot 	import Slot
from pychartdir import *
from datetime import datetime
#from PIL import Image

# ---- Declaring global variable
taskList = []
adjacencyList = {}
graph = Graph(adjacencyList)
criticalPaths = []
taskChains = []
resources = []
globalFreeSlots = []

resourceFileName = None
taskFileName = None
dependencyFileName = None

# ---- Get data from UI
def scheduleTasks(resFName,taskFName,depFName):
	global resourceFileName,taskFileName,dependencyFileName
	global taskList, adjacencyList,graph,criticalPaths,taskChains,resources,globalFreeSlots
	
	taskList = []
	adjacencyList = {}
	graph = Graph(adjacencyList)
	criticalPaths = []
	taskChains = []
	resources = []
	globalFreeSlots = []
	
	resourceFileName = resFName
	taskFileName = taskFName
	dependencyFileName = depFName
	
	importTasks() 
	findCriticalPaths()
	findAndSortTaskChains()		
	allocateResources()

	maxEndDay = -1
	for taskChain in taskChains:
		for id in taskChain.tasks:
    			t = getTaskFromId(id)
			if t.endDay > maxEndDay:
				maxEndDay = t.endDay
	
	for resource in resources:
		for slot in resource.freeSlots:
			print(resource.name," ",slot.start,"-",slot.end)
	print("Minimum number of days required to complete all tasks : ",maxEndDay)
    
	drawGraph(maxEndDay)

	
# ---- Read data from files 
def importTasks():

# ---  Read tasks from files.	
	global taskList,resourceFileName,taskFileName,dependencyFileName
	global resources
	fptasks = open(taskFileName,"r")#"tasks.txt","r")

	for line in fptasks.readlines():		
		newTask = Task()
		t = line.split(",")	
		newTask.name = t[1]		
		newTask.id = int(t[0])
		newTask.duration = int(t[2])
		adjacencyList[newTask.id] = []
		taskList.append(newTask)	
	fptasks.close()			

#---- Read resources
	fpresources = open(resourceFileName,"r")#("resources.txt","r")
	
	for line in fpresources.readlines():
		r = line.strip().split(",")
		newResource = Resource(int(r[0]),r[1])
		resources += [newResource]
				
	fpresources.close()

# ---- Read depedencies and create predecessor list -----
	fpdependencies = open(dependencyFileName,"r")#("dependencies.txt","r")	

	for line in fpdependencies.readlines():
		line = line.rstrip()
		print(line)		
		x = line.split(",")
		if(len(x)>1):
			task = getTaskFromId(int(x[0]))
			for i in range(1,len(x)):
				task.predecessors.append(int(x[i]))
		"""if len(x) >1:			
			z = x[1]		
			for task in taskList:
				if task.id == int(x[0]):			 					
					y = z.strip().split(",")	
					for b in y:
						task.predecessors.append(int(b))"""								
				#print(x[0],task.predecessor)
	fpdependencies.close()


# ---- Create successor list ----
	for succTask in taskList:
		#succTask = getTaskFromId()
		for predId in succTask.predecessors:
			task = getTaskFromId(predId)
			task.successors.append(succTask.id)
 			adjacencyList[task.id] = task.successors
 			

# -- Print id, predecessor, successor	
"""for task in taskList:	
	print(task.id,task.predecessors,task.successors)"""
	
# -- Main Functionality implementation

def getTaskFromId(id):
	for task in taskList:
		if task.id == id:
			return task 
	return None


# -- find all critical paths 
def findCriticalPaths():
	
	noPredTasks = []
	noSuccTasks = []
	noPredSuccTasks = []
	global criticalPaths
	for task in taskList:
		if len(task.predecessors) == 0 and len(task.successors) == 0:
			
			noPredSuccTasks.append(task.id)
			
		# -- find no predecessor tasks
		elif len(task.predecessors) == 0:
			noPredTasks.append(task.id)
		
		# -- find no successor tasks	 
		elif len(task.successors) == 0:
			noSuccTasks.append(task.id)
	
	
	print (noPredTasks)
	print (noSuccTasks)
	# -- find a path between each pair
	for id1 in noPredTasks:
		for id2 in noSuccTasks:
			criticalPaths += graph.find_all_paths(id1,id2)	
	
 	# -- add remaining tasks
 	
 	for id1 in noPredSuccTasks:
 		singleNodeList = [id1]
 		criticalPaths += [singleNodeList]
 	
 	print  (criticalPaths)	 

def getTotalPathDuration(path):
	
	duration = 0
	for id in path:
		task = getTaskFromId(id)	
		duration +=task.duration
	return duration

def findAndSortTaskChains():
	
	global taskChains
	
	for path in criticalPaths:
		#print (path)
		taskChain = TaskChain(path)
		taskChain.totalDuration = getTotalPathDuration(path)
		taskChains += [taskChain]
	
	
	# -- Sort the chains in descending order.
	taskChains.sort(key = lambda x:x.totalDuration, reverse = True)
	
	
	# -- Initialize the start days for all tasks.
	for taskChain in taskChains:
		t = getTaskFromId(taskChain.tasks[0]) 
		t.startDay = 1
		t.endDay = t.startDay + t.duration - 1
		for i,id in enumerate(taskChain.tasks):
			if  i > 0:
				t = getTaskFromId(id)
				prev = getTaskFromId(taskChain.tasks[i-1])
				if t.startDay == -1 or t.startDay <= prev.endDay:
					t.startDay = prev.endDay + 1
					t.endDay = t.startDay + t.duration -1
		
			 
	"""for taskChain in taskChains:
		for i,id in enumerate(taskChain.tasks):
			t = getTaskFromId(id) 
			print(t.id," ",t.name," ",t.startDay," ",t.endDay," ",t.resourceOnTask  )

	for taskChain in taskChains:
		print(taskChain.tasks)"""
		  
# -- Only thing remaining 	
def allocateResources():
	
	global globalFreeSlots,resources
	for resource in resources:
		for freeSlot in resource.freeSlots:
			globalFreeSlots += [freeSlot]
	
	# -- sort the global free slots
	globalFreeSlots.sort(key = lambda x:(x.start,x.slotDuration),reverse = False)
	
	for taskChain in taskChains:
		for id in taskChain.tasks:
			task = getTaskFromId(id)			
			if task.resourceOnTask == None:
				getSuitableSlotDuration(task,False)
				
				if task.resourceOnTask == None:
					getSuitableSlotDuration(task,True)

 	for t in taskList:
		#t = getTaskFromId(id)
		print(t.id," ",t.name," ",t.startDay," ",t.endDay)
		if(t.resourceOnTask!=None):
    			print(t.resourceOnTask.name)	

					

def adjustSuccessors(task):
	if(len(task.successors) == 0):
		return None
	else:	
		for succId in task.successors:
			succTask = getTaskFromId(succId)
			if succTask.startDay <= task.endDay:
				succTask.startDay = task.endDay + 1
				succTask.endDay = succTask.startDay + succTask.duration -1 	
				adjustSuccessors(succTask)
						
					
def getSuitableSlotDuration(task,flag):
	global globalFreeSlots	
	for freeSlot in globalFreeSlots:
		maxPredEndDay = getMaxPredEndDay(task)
		
		if task.duration<=freeSlot.slotDuration and freeSlot.start > maxPredEndDay:
			if(not flag and (task.startDay < freeSlot.start or task.endDay> freeSlot.end)):
				continue
			task.resourceOnTask = freeSlot.resourceOnSlot
			if flag == True:	
				task.startDay = freeSlot.start
				task.endDay = task.startDay + task.duration-1
				adjustSuccessors(task) 
			if task.startDay - freeSlot.start>0:	
				remFreeSlot1 = Slot(freeSlot.start, task.startDay-1)
				remFreeSlot1.resourceOnSlot = freeSlot.resourceOnSlot
				globalFreeSlots.append(remFreeSlot1)
				#remFreeSlot1.resourceOnSlot.freeSlots.remove(freeSlot)
				remFreeSlot1.resourceOnSlot.freeSlots.append(remFreeSlot1)
							
			if freeSlot.end - task.endDay>0:	
				remFreeSlot2 = Slot(task.endDay+1, freeSlot.end)
				remFreeSlot2.resourceOnSlot = freeSlot.resourceOnSlot
				globalFreeSlots.append(remFreeSlot2)
				#remFreeSlot2.resourceOnSlot.freeSlots.remove(freeSlot)
				remFreeSlot2.resourceOnSlot.freeSlots.append(remFreeSlot2)
						
			freeSlot.resourceOnSlot.freeSlots.remove(freeSlot)
			globalFreeSlots.remove(freeSlot) 
			updateFreeSlots()			
			globalFreeSlots.sort(key = lambda x:(x.start,x.slotDuration),reverse = False)
			
			return		
	return

# --- In case if multiple free slots are existing one after other for same resource. -----					
def updateFreeSlots():
	global resources,globalFreeSlots	
	for resource in resources:
		#addedFreeSlots, freeSlotsToRemove
		i = 0
		#while i<len(resource.freeSlots)-1:
		for i in range(len(resource.freeSlots)-1):	
			if(resource.freeSlots[i].end + 1== resource.freeSlots[i+1].start):
				print(i)				
				globalFreeSlots.remove(resource.freeSlots[i+1])
 				globalFreeSlots.remove(resource.freeSlots[i])
				
				resource.freeSlots[i].end == resource.freeSlots[i+1].end
				resource.freeSlots[i].duration == resource.freeSlots[i].duration + resource.freeSlots[i+1].duration	 
				resource.freeSlots.remove(resource.freeSlots[i+1])
				globalFreeSlots.append(resource.freeSlots[i])
			#i+=1	

	
def getMaxPredEndDay(task):
	maxPredEndDay = -1	
	for predId in task.predecessors:
		pred = getTaskFromId(predId)
		if(maxPredEndDay<pred.endDay):
			maxPredEndDay = pred.endDay
	return maxPredEndDay	
	
def drawGraph(maxDuration):
    refDate = chartTime(2012,1,1)
    labels = []
    startDate = []#refDate, refDate + 14 * 24 * 60 * 60  , refDate + 2*14 * 24 * 60 * 60]
    endDate = []#refDate + 14 * 24 * 60 * 60, refDate + 2*14 * 24*60*60, refDate + 3*14 * 24 * 60*60]
    for t in taskList:
	    #t = getTaskFromId(id)
		if(not t == None):
			if(t.resourceOnTask == None):
				res = ""
			else:
				res = "("+t.resourceOnTask.name+")"	
			labels.append(t.name+res)        
		startDate.append(refDate + (t.startDay - 1)*24*60*60)
        	endDate.append(refDate + (t.endDay - 1)*24*60*60)
    
    c = XYChart(620, 280, 0xccffcc, 0x000000, 1)

    c.addTitle("Time Scheduling", "timesbi.ttf", 15, 0xffffff).setBackground(0x006000)
    c.setPlotArea(140, 55, 460, 200, 0xffffff, 0xeeeeee, LineColor, 0xc0c0c0, 0xc0c0c0).setGridWidth(2, 1, 1, 1)
    
    c.swapXY()

    c.yAxis().setDateScale(refDate, refDate + maxDuration*24*60*60, 24*60*60*7)
    c.yAxis().setMultiFormat(StartOfMonthFilter(), "<*font=arialbd.ttf*>{value|mmm d}",StartOfDayFilter(), "-{value|d}")

    c.setYAxisOnRight()
    c.xAxis().setLabels(labels)

    c.xAxis().setReverse()

    c.xAxis().setTickOffset(0.5)
    plannedColor = 0x0000aa

    c.addBoxLayer(startDate, endDate, plannedColor, "Planned").setBorderColor(SameAsMainColor)

    b = c.addLegend(595, 60, 0, "arialbd.ttf", 8)
    b.setAlignment(TopRight)
    b.setBackground(0x80808080, -1, 2)

    # Output the chart
    c.makeChart("layergantt.png")
    
def main():
	importTasks() 
	findCriticalPaths()
	findAndSortTaskChains()		
	allocateResources()
	
	global resources	
	maxEndDay = -1
	for taskChain in taskChains:
		for id in taskChain.tasks:
    			t = getTaskFromId(id)
			if t.endDay > maxEndDay:
				maxEndDay = t.endDay
	
	for resource in resources:
		for slot in resource.freeSlots:
			print(resource.name," ",slot.start,"-",slot.end)
	print("Minimum number of days required to complete all tasks : ",maxEndDay)
    
	drawGraph(maxEndDay)

	img = Image.open("layergantt.png")
    	img.show()

#main()

