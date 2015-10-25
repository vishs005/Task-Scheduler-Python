# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SaveFiles.ui'
#
# Created: Tue May 13 13:33:27 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class SaveFiles_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(322, 220)
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(59, 29, 211, 161))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.SaveTasksButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.SaveTasksButton.setObjectName(_fromUtf8("SaveTasksButton"))
        self.verticalLayout.addWidget(self.SaveTasksButton)
        self.SaveDependenciesButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.SaveDependenciesButton.setObjectName(_fromUtf8("SaveDependenciesButton"))
        self.verticalLayout.addWidget(self.SaveDependenciesButton)
        self.SaveResourcesButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.SaveResourcesButton.setObjectName(_fromUtf8("SaveResourcesButton"))
        self.verticalLayout.addWidget(self.SaveResourcesButton)
        self.BackButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.BackButton.setObjectName(_fromUtf8("BackButton"))
        self.verticalLayout.addWidget(self.BackButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.SaveTasksButton.setText(QtGui.QApplication.translate("Dialog", "Save Tasks", None, QtGui.QApplication.UnicodeUTF8))
        self.SaveDependenciesButton.setText(QtGui.QApplication.translate("Dialog", "Save Dependencies", None, QtGui.QApplication.UnicodeUTF8))
        self.SaveResourcesButton.setText(QtGui.QApplication.translate("Dialog", "Save Resources", None, QtGui.QApplication.UnicodeUTF8))
        self.BackButton.setText(QtGui.QApplication.translate("Dialog", "Back", None, QtGui.QApplication.UnicodeUTF8))

