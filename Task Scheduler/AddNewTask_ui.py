# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddTaskDialog.ui'
#
# Created: Mon May 12 13:34:42 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(327, 176)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 40, 121, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 121, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.TaskNameText = QtGui.QLineEdit(Dialog)
        self.TaskNameText.setGeometry(QtCore.QRect(180, 40, 113, 27))
        self.TaskNameText.setObjectName(_fromUtf8("TaskNameText"))
        self.TaskDurationText = QtGui.QLineEdit(Dialog)
        self.TaskDurationText.setGeometry(QtCore.QRect(180, 80, 113, 27))
        self.TaskDurationText.setObjectName(_fromUtf8("TaskDurationText"))
        self.AddTaskButton = QtGui.QPushButton(Dialog)
        self.AddTaskButton.setGeometry(QtCore.QRect(30, 130, 85, 27))
        self.AddTaskButton.setObjectName(_fromUtf8("AddTaskButton"))
        self.CancelButton = QtGui.QPushButton(Dialog)
        self.CancelButton.setGeometry(QtCore.QRect(180, 130, 85, 27))
        self.CancelButton.setObjectName(_fromUtf8("CancelButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Enter Task Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Enter Task Duration", None, QtGui.QApplication.UnicodeUTF8))
        self.AddTaskButton.setText(QtGui.QApplication.translate("Dialog", "Add Task", None, QtGui.QApplication.UnicodeUTF8))
        self.CancelButton.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

