# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data_Alert_dockwidget_base.ui'
#
# Created: Tue Sep 29 12:29:50 2015
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_dataAlertDockWidgetBase(object):
    def setupUi(self, dataAlertDockWidgetBase):
        dataAlertDockWidgetBase.setObjectName(_fromUtf8("dataAlertDockWidgetBase"))
        dataAlertDockWidgetBase.resize(350, 548)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.endButton = QtGui.QPushButton(self.dockWidgetContents)
        self.endButton.setGeometry(QtCore.QRect(240, 480, 75, 23))
        self.endButton.setObjectName(_fromUtf8("endButton"))
        self.startButton = QtGui.QPushButton(self.dockWidgetContents)
        self.startButton.setGeometry(QtCore.QRect(30, 480, 75, 23))
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.textBrowser = QtGui.QTextBrowser(self.dockWidgetContents)
        self.textBrowser.setGeometry(QtCore.QRect(15, 110, 321, 351))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.upper = QtGui.QLineEdit(self.dockWidgetContents)
        self.upper.setGeometry(QtCore.QRect(120, 10, 113, 20))
        self.upper.setObjectName(_fromUtf8("upper"))
        self.left = QtGui.QLineEdit(self.dockWidgetContents)
        self.left.setGeometry(QtCore.QRect(20, 40, 113, 20))
        self.left.setObjectName(_fromUtf8("left"))
        self.right = QtGui.QLineEdit(self.dockWidgetContents)
        self.right.setGeometry(QtCore.QRect(220, 40, 113, 20))
        self.right.setObjectName(_fromUtf8("right"))
        self.lower = QtGui.QLineEdit(self.dockWidgetContents)
        self.lower.setGeometry(QtCore.QRect(120, 70, 113, 20))
        self.lower.setObjectName(_fromUtf8("lower"))
        dataAlertDockWidgetBase.setWidget(self.dockWidgetContents)

        self.retranslateUi(dataAlertDockWidgetBase)
        QtCore.QMetaObject.connectSlotsByName(dataAlertDockWidgetBase)

    def retranslateUi(self, dataAlertDockWidgetBase):
        dataAlertDockWidgetBase.setWindowTitle(_translate("dataAlertDockWidgetBase", "UVI Alert", None))
        self.endButton.setText(_translate("dataAlertDockWidgetBase", "End", None))
        self.startButton.setText(_translate("dataAlertDockWidgetBase", "Start", None))

