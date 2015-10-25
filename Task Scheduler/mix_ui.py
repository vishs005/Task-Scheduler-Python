import sys
import os
from PyQt4 import QtGui,QtCore
from AddNewTask_ui import *
from scheduler_ui import *
from LoadFiles_ui import *
from SaveFiles_ui import *	
from scheduler import *
from imageDialog_ui import *
from Task import *

taskName = None
taskDuration = None
isAdded = False
taskList = []

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class saveFDialog(QtGui.QDialog):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)  	
		self.ui = SaveFiles_Dialog()
		self.ui.setupUi(self)
		self.ui.SaveTasksButton.clicked.connect(self.SaveTasksClicked)
		self.ui.SaveDependenciesButton.clicked.connect(self.SaveDependenciesButtonClicked)
		self.ui.SaveResourcesButton.clicked.connect(self.SaveResourcesButtonClicked)
		self.ui.BackButton.clicked.connect(self.BackButtonClicked)
	def SaveTasksClicked(self):
			filename = QtGui.QFileDialog.getSaveFileName(self, "Save file", os.getcwd(), ".txt")
			print filename	        
			fp=open("tasks_test.txt")
			output= []
			for line in fp:
				print line
				output.append(line)
			fp.close()
			f=open(filename,"w")
			f.writelines(output)
			f.close()
	
	def SaveDependenciesButtonClicked(self):
			filename = QtGui.QFileDialog.getSaveFileName(self, "Save file", os.getcwd(), ".txt")
			print filename	        
			fp=open("dependencies_test.txt")
			output= []
			for line in fp:
				print line
				output.append(line)
			fp.close()
			f=open(filename,"w")
			f.writelines(output)
			f.close()	

	def SaveResourcesButtonClicked(self):
			filename = QtGui.QFileDialog.getSaveFileName(self, "Save file", os.getcwd(), ".txt")
			print filename	        
			fp=open("resources_test.txt")
			output= []
			for line in fp:
				print line
				output.append(line)
			fp.close()
			f=open(filename,"w")
			f.writelines(output)
			f.close()
		
	def BackButtonClicked(self):
			self.done(1)

class loadFDialog(QtGui.QDialog):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)  	
		self.ui = LoadFiles_Dialog()
		self.ui.setupUi(self)
		self.ui.LoadTasks.clicked.connect(self.LoadTasksClicked)
		self.ui.LoadDependenciesButton.clicked.connect(self.LoadDependenciesButtonClicked)
		self.ui.LoadResourcesButton.clicked.connect(self.LoadResourcesButtonClicked)
		self.ui.BackButton.clicked.connect(self.BackButtonClicked)
	def LoadTasksClicked(self):
			str1 = QtGui.QFileDialog.getOpenFileName(self, "Open Tasks", os.getcwd())
			fp = open(str1)
			output= []
			for line in fp:
				output.append(line)
			fp.close()
			f=open("tasks_test.txt","w")	
			f.writelines(output)
			f.close()
	
	def LoadDependenciesButtonClicked(self):
			str1 = QtGui.QFileDialog.getOpenFileName(self, "Open Dependencies", os.getcwd())
			fp=open(str1)
			output= []
			for line in fp:
				output.append(line)
			fp.close()
			f=open("dependencies_test.txt","w")	
			f.writelines(output)
			f.close()	

	def LoadResourcesButtonClicked(self):
			str1 = QtGui.QFileDialog.getOpenFileName(self, "Open Resources", os.getcwd())
			fp=open(str1)
			output= []
			for line in fp:
				output.append(line)
			fp.close()
			f=open("resources_test.txt","w")	
			f.writelines(output)
			f.close()
		
	def BackButtonClicked(self):
			self.done(1)
		
class imgDialog(QtGui.QDialog):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)  	
		self.ui = Img_Dialog()
		self.ui.setupUi(self)
		myPixmap = QtGui.QPixmap(_fromUtf8('layergantt.png'))
		#myScaledPixmap = myPixmap.scaled(self.ui.imageLabel.size(), QtCore.Qt.KeepAspectRatio)
		self.ui.imageLabel.setPixmap(myPixmap)
		self.ui.BackButton.clicked.connect(self.BackButtonClicked)

	def BackButtonClicked(self):
		self.done(1)

class frmDialog(QtGui.QDialog):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)  	
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.AddTaskButton.clicked.connect(self.AddTaskButtonClicked)
		self.ui.CancelButton.clicked.connect(self.CancelButtonClicked) 	
   	 
  	def AddTaskButtonClicked(self):
		global taskName,taskDuration,isAdded
		if(not self.ui.TaskNameText.text() == "" and not self.ui.TaskDurationText.text() == ""):		
			taskName = self.ui.TaskNameText.text() 		
			taskName = (str(taskName)).strip()			
			taskDuration = self.ui.TaskDurationText.text()
			taskDuration = (str(taskDuration)).strip()
			isAdded = True	
			self.done(1)
	 				
    	def CancelButtonClicked(self):
		global isAdded
		isAdded = False
		self.done(1)

class frmMain(QtGui.QMainWindow):
  	def __init__(self, parent=None):
		self.count = 0    		
		self.resCount = 0		
		QtGui.QWidget.__init__(self, parent)
    		self.ui = Ui_MainWindow()
    		self.ui.setupUi(self)
    		
		#--------  Add Events ----------	
		self.ui.NewTaskButton.clicked.connect(self.NewTaskButtonClicked)
		self.ui.TaskListWidget.itemClicked.connect(self.TaskWidgetItemClicked)	
		self.ui.DependencyListWidget.itemClicked.connect(self.DependencyWidgetItemClicked)		
		self.ui.CreateGraphButton.clicked.connect(self.CreateGraphButtonClicked) 	
		self.ui.QuitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
		self.ui.AddResourceButton.clicked.connect(self.AddResourceButtonClicked)
		self.ui.DeleteResourceButton.clicked.connect(self.DeleteResourceButtonClicked)		 	
		self.ui.EditButton.clicked.connect(self.EditButtonClicked)		
		self.ui.DeleteButton.clicked.connect(self.DeleteButtonClicked)	
		self.ui.LoadFilesButton.clicked.connect(self.LoadFilesButtonClicked)	
		self.ui.SaveFilesButton.clicked.connect(self.SaveFilesButtonClicked)
       	 	
		#-------  Initialize files -----
		f = open('tasks_test.txt','w')
		f.close()
		f = open('dependencies_test.txt','w')
		f.close()
		f = open('resources_test.txt','w')
		f.close()  

	def SaveFilesButtonClicked(self):
		Dialog3 = saveFDialog()
		Dialog3.show()
    		ret = Dialog3.exec_()
	
	def LoadFilesButtonClicked(self):
		global taskList		
		Dialog2 = loadFDialog()
		Dialog2.show()
    		ret = Dialog2.exec_()

		self.ui.TaskListWidget.clear()
		taskList = []
		f = open('tasks_test.txt')
		for line in f:
			line = line.rstrip("\n")
			x = line.split(",")
			task = Task(int(x[0]),x[1])
			task.duration = int(x[2])
			preds = self.getPredecessorsFromFile(task.id)
			task.predecessors = preds			
			taskList.append(task)
						
			self.ui.TaskListWidget.addItem(line)					
		f.close()
		self.populateDependencyList()
		for task in taskList:
			print(str(task.id)+" "+task.name)
			print(task.predecessors)		
		self.ui.ResourceListWidget.clear()
		f = open('resources_test.txt')
		temp = None		
		for line in f:
			line = line.rstrip("\n")			
			temp = line			
			self.ui.ResourceListWidget.addItem(line)					
		f.close()
		if(not temp == None):	
			temp = temp.split(",")
			self.resCount = int(temp[0])
		else:
			self.resCount = 0
	def getPredecessorsFromFile(self,taskId):
		f = open('dependencies_test.txt')
		predList = []		
		for line in f:
			line = line.rstrip("\n")
			x = line.split(",")
			tid = int(x[0])
			if tid == taskId:
				for i in range(1,len(x)):
					predList.append(int(x[i]))	
										
		f.close()
		return predList	

	def EditButtonClicked(self):
		#---- Edit entries in file tasks ----
		currentTaskLine = str(self.ui.TaskListWidget.currentItem().text())		
		if not currentTaskLine == "":
			self.ui.TaskListWidget.clear()
			CTL = currentTaskLine.split(",")
			f = open('tasks_test.txt')
			output = []
			for line in f:
				line = line.rstrip("\n")			
				x = line.split(",")
   				if CTL[1] == x[1]:
					#print(line+","+str(predTaskId))					
     		   			output.append(x[0]+","+str(self.ui.NameText.text())+","+str(self.ui.DurationText.text())+"\n")
				else:
					output.append(x[0]+","+x[1]+","+x[2]+"\n")
			f.close()			
			f = open('tasks_test.txt', 'w')
			f.writelines(output)
			f.close()
			for line in output:
				line = line.rstrip("\n")				
				x = line.split(",")
				self.ui.TaskListWidget.addItem(x[0]+","+x[1]+","+x[2])	
		#---- Edit entries in file dependencies---
	
	def DeleteButtonClicked(self):
		#---- Delete Entries in file tasks ----
		global taskList		
		currentTaskLine = str(self.ui.TaskListWidget.currentItem().text())		
		if not currentTaskLine == "":
			self.ui.TaskListWidget.clear()
			#self.count = 0
			CTL = currentTaskLine.split(",")
			f = open('tasks_test.txt')
			output = []
			for line in f:
				line = line.rstrip("\n")			
				x = line.split(",")
   				if not CTL[1] == x[1]:
					#print(line+","+str(predTaskId))						
     		   			output.append(x[0]+","+x[1]+","+x[2]+"\n")					
			f.close()			
			f = open('tasks_test.txt', 'w')
			f.writelines(output)
			f.close()
			for line in output:
				line = line.rstrip("\n")				
				x = line.split(",")
				self.ui.TaskListWidget.addItem(x[0]+","+x[1]+","+x[2])
		#---- Create New task list ----
			taskList = []
			f = open('tasks_test.txt')
			for line in f:
				line = line.rstrip("\n")
				x = line.split(",")
				task = Task(int(x[0]),x[1])
				task.duration = int(x[2])
				preds = self.getPredecessorsFromFile(task.id)
				task.predecessors = preds			
				taskList.append(task)
						
				#self.ui.TaskListWidget.addItem(line)					
			f.close()
		#---- Delete Entries in file dependencies---

			self.ui.DependencyListWidget.clear()
			#CTL
			f = open('dependencies_test.txt')
			output1 = []
			for line in f:
				line = line.rstrip("\n")			
				x = line.split(",")
   				if not int(CTL[0]) == int(x[0]):
					#print(line+","+str(predTaskId)
					str1 = ""	
					for i in range(0,len(x)):
						if not int(x[i]) == int(CTL[0]): 
     		   					str1=str1+str(x[i])+","
					str1= str1.rstrip(",")
					output1.append(str1+"\n")					
			f.close()
			f = open('dependencies_test.txt', 'w')
			f.writelines(output1)
			f.close()
			self.populateDependencyList()

	
  	def NewTaskButtonClicked(self):	
    		Dialog = frmDialog(self)
    		Dialog.show()
    		ret = Dialog.exec_()
    		global taskName,taskDuration,isAdded,taskList
		if(isAdded):    		
			self.count+=1
			self.ui.TaskListWidget.addItem(str(self.count)+","+taskName+","+taskDuration)
			self.populateDependencyList()			
			task = Task(self.count,taskName)
			task.duration = int(taskDuration)
			taskList.append(task) 			
			
			f = open('tasks_test.txt','a') 
			f.write(str(self.count)+","+taskName+","+taskDuration+"\n") 
			f.close()
			f1 = open('dependencies_test.txt','a') 
			f1.write(str(self.count)+"\n") 
			f1.close()

	def TaskWidgetItemClicked(self):
		self.populateDependencyList()
		currentItem = str(self.ui.TaskListWidget.currentItem().text())
		t = currentItem.split(",")	
		selectedTaskId = int(t[0])
		print selectedTaskId		
		task = self.getTaskFromId(selectedTaskId)
					
		if(not task == None):
			self.ui.NameText.setText(task.name)
			self.ui.DurationText.setText(str(task.duration))			
			for predId in task.predecessors:
				# find name corresponding to predId in dependency list
				predTask = self.getTaskFromId(predId)					
				if not predTask == None:				
					predName = predTask.name
								
					for ind in range(self.ui.DependencyListWidget.count()):
						itemD = self.ui.DependencyListWidget.item(ind)
						if((str(itemD.text())).strip() == predName):				
							itemD.setBackground(QtGui.QColor('yellow'))				
					
		
		#find the predecessor task ids. Find thier corresponding names and 

	def DependencyWidgetItemClicked(self):
		self.ui.DependencyListWidget.currentItem().setBackground(QtGui.QColor('yellow'))	
		taskListCurrentSelected = str(self.ui.TaskListWidget.currentItem().text())	
		tlcs = 	taskListCurrentSelected.split(",")	
		taskId = int(tlcs[0])
		task = self.getTaskFromId(taskId)		
		#print taskId 			
		dependencyListCurrentSelected = (str(self.ui.DependencyListWidget.currentItem().text())).strip()
		predTaskId = self.getIdFromTaskName(dependencyListCurrentSelected) 
		predTask = self.getTaskFromId(predTaskId)
		
		#print predTaskId
		if(predTaskId>0 and not predTask == None and not task ==None and predTaskId not in task.predecessors):		
			# add the predTaskId in dependencies.txt corresponding to taskId
			f = open('dependencies_test.txt')
			output = []
			for line in f:
				line = line.rstrip("\n")				
				x = line.split(",")
				#print(x[0]+"-"+str(taskId))
   				if taskId == int(x[0]):
					#print(line+","+str(predTaskId))
     		   			output.append(line+","+str(predTaskId)+"\n")
					task.predecessors.append(predTaskId)					
					flag = True
				else:
					output.append(line+"\n")
			f.close()
			f = open('dependencies_test.txt', 'w')
			f.writelines(output)
			f.close()	

	def getIdFromTaskName(self,taskName1):
		global taskList	
		for task in taskList:
			#print task.id
			if task.name == taskName1:
				return task.id
		return 0
	
	def getTaskFromId(self,taskId):
		global taskList
		for task in taskList:
			#print task.id
			if task.id == taskId:
				return task
		return None
	def CreateGraphButtonClicked(self):
		scheduleTasks("resources_test.txt","tasks_test.txt","dependencies_test.txt")		
		Dialog1 = imgDialog()
		Dialog1.show()
    		ret = Dialog1.exec_()	

	def AddResourceButtonClicked(self):
		if( not self.ui.ResourceText.text() == ""):
			self.resCount+=1			
			fp = open("resources_test.txt","a")
			fp.write(str(self.resCount)+","+str(self.ui.ResourceText.text())+"\n")
			fp.close()
			self.ui.ResourceListWidget.addItem(str(self.resCount)+","+str(self.ui.ResourceText.text()))	 	
			self.ui.ResourceText.clear()	
		
	def DeleteResourceButtonClicked(self):
		currentResName = str(self.ui.ResourceListWidget.currentItem().text())		
		if not currentResName == "":
			self.ui.ResourceListWidget.clear()
			self.resCount = 0
			CRN = currentResName.split(",")
			f = open('resources_test.txt')
			output = []
			for line in f:
				line = line.rstrip("\n")			
				x = line.split(",")
   				if not CRN[1] == x[1]:
					#print(line+","+str(predTaskId))
					self.resCount+=1
     		   			output.append(str(self.resCount)+","+x[1]+"\n")					
			f.close()
			f = open('resources_test.txt', 'w')
			f.writelines(output)
			f.close()
			for line in output:
				line = line.rstrip("\n")				
				x = line.split(",")
				self.ui.ResourceListWidget.addItem(x[0]+","+x[1])
				
	#def QuitButtonClicked(self):
		
	
	def populateDependencyList(self):
		self.ui.DependencyListWidget.clear()	
		if(not self.ui.TaskListWidget.currentItem() == None):
			#self.ui.TaskListWidget.currentItem().setBackground(QtGui.QColor('yellow'))		
		 	temp = str(self.ui.TaskListWidget.currentItem().text())		
			t = temp.split(",")	
			selectedTask = t[1]					
			for i in range(0,len(self.ui.TaskListWidget)):	
				item = str(self.ui.TaskListWidget.item(i).text())
				t = item.split(",")	
				currTask = t[1]
				if(not currTask == selectedTask):	
					self.ui.DependencyListWidget.addItem(currTask)	 						
    	
if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  MainWindow = frmMain()
  MainWindow.show()
  sys.exit(app.exec_())


