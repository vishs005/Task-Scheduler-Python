# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoadFiles.ui'
#
# Created: Tue May 13 04:31:25 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class LoadFiles_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(311, 218)
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 30, 191, 161))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.LoadTasks = QtGui.QPushButton(self.verticalLayoutWidget)
        self.LoadTasks.setObjectName(_fromUtf8("LoadTasks"))
        self.verticalLayout.addWidget(self.LoadTasks)
        self.LoadDependenciesButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.LoadDependenciesButton.setObjectName(_fromUtf8("LoadDependenciesButton"))
        self.verticalLayout.addWidget(self.LoadDependenciesButton)
        self.LoadResourcesButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.LoadResourcesButton.setObjectName(_fromUtf8("LoadResourcesButton"))
        self.verticalLayout.addWidget(self.LoadResourcesButton)
        self.BackButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.BackButton.setObjectName(_fromUtf8("BackButton"))
        self.verticalLayout.addWidget(self.BackButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.LoadTasks.setText(QtGui.QApplication.translate("Dialog", "Load Tasks File", None, QtGui.QApplication.UnicodeUTF8))
        self.LoadDependenciesButton.setText(QtGui.QApplication.translate("Dialog", "Load Dependencies File", None, QtGui.QApplication.UnicodeUTF8))
        self.LoadResourcesButton.setText(QtGui.QApplication.translate("Dialog", "Load Resources File", None, QtGui.QApplication.UnicodeUTF8))
        self.BackButton.setText(QtGui.QApplication.translate("Dialog", "Back", None, QtGui.QApplication.UnicodeUTF8))

