# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imageDialog.ui'
#
# Created: Tue May 13 16:47:21 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Img_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(845, 490)
        self.imageLabel = QtGui.QLabel(Dialog)
        self.imageLabel.setGeometry(QtCore.QRect(90, 40, 671, 341))
        self.imageLabel.setText(_fromUtf8(""))
        self.imageLabel.setObjectName(_fromUtf8("imageLabel"))
        self.BackButton = QtGui.QPushButton(Dialog)
        self.BackButton.setGeometry(QtCore.QRect(80, 430, 85, 27))
        self.BackButton.setObjectName(_fromUtf8("BackButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.BackButton.setText(QtGui.QApplication.translate("Dialog", "Back", None, QtGui.QApplication.UnicodeUTF8))

