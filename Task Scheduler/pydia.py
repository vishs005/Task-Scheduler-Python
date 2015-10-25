from PyQt4 import QtCore, QtGui
 
########################################################################
class DialogDemo(QtGui.QWidget):
    """"""	
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        # super(DialogDemo, self).__init__()
        QtGui.QWidget.__init__(self)
 
        self.label = QtGui.QLabel("Python dialog box")
 
        # create the buttons
       
        fileDialogBtn =  QtGui.QPushButton("Open File Dialog")
  	
 
        #connect the buttons to the functions (signals to slots)
      
        fileDialogBtn.clicked.connect(self.openFileDialog)
        
 
        # layout widgets
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(fileDialogBtn)
        self.setLayout(layout)
 
        # set the position and size of the window
        self.setGeometry(100, 100, 400, 100)
 
        self.setWindowTitle("Dialog Demo")
 
    
    #----------------------------------------------------------------------
    def openFileDialog(self):
        """
        Opens a file dialog and sets the label to the chosen path
        """
        import os
        filename = QtGui.QFileDialog.getSaveFileName(self, "Save file", "", ".txt")
	#str1 = QtGui.QFileDialog.getOpenFileName(self, "Open File", os.getcwd())
	print filename	        
	fp=open("tasks.txt")
	output= []
	for line in fp:
		print line
		output.append(line)
	fp.close()
	f=open(filename,"w")
	f.writelines(output)
	f.close()
 	
 
    #----------------------------------------------------------------------
    def openDirectoryDialog(self):
        """
        Opens a dialog to allow user to choose a directory
        """
        flags = QtGui.QFileDialog.DontResolveSymlinks | QtGui.QFileDialog.ShowDirsOnly
        d = directory = QtGui.QFileDialog.getExistingDirectory(self,
                                                               "Open Directory",
                                                               os.getcwd(),
                                                               flags)
        self.label.setText(d)
 
   
    
   
#----------------------------------------------------------------------
if __name__ == "__main__":
    app = QtGui.QApplication([])
    form = DialogDemo()
    form.show()
    app.exec_()
