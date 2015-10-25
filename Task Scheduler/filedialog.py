from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_mainLayout(object):
    def setupUi(self, mainLayout):
        mainLayout.setObjectName(_fromUtf8("mainLayout"))
        mainLayout.resize(598, 335)
        mainLayout.setTabPosition(QtGui.QTabWidget.North)
        mainLayout.setTabShape(QtGui.QTabWidget.Rounded)
        mainLayout.setElideMode(QtCore.Qt.ElideLeft)

        self.basic_tab = QtGui.QWidget()
        self.file_button = QtGui.QPushButton(self.basic_tab)
        QtCore.QObject.connect(self.file_button, QtCore.SIGNAL("clicked()"), self.choose_file)

    def choose_file(self):
        file_name = QtGui.QFileDialog.getOpenFileName(self, "Open Data File", "", "CSV data files (*.csv)")

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mainLayout = QtGui.QTabWidget()
    ui = Ui_mainLayout()
    ui.setupUi(mainLayout)
    mainLayout.show()
    sys.exit(app.exec_())
