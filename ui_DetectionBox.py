# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\abrown2\.qgis2\python\plugins\ResponseRatio\ui_DetectionBox.ui'
#
# Created: Thu Oct 24 12:52:49 2013
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_DetectionBox(object):
    def setupUi(self, DetectionBox):
        DetectionBox.setObjectName(_fromUtf8("DetectionBox"))
        DetectionBox.resize(307, 246)
        self.buttonBox = QtGui.QDialogButtonBox(DetectionBox)
        self.buttonBox.setGeometry(QtCore.QRect(20, 200, 241, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Help|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(DetectionBox)
        self.label.setGeometry(QtCore.QRect(30, 40, 261, 71))
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(DetectionBox)
        self.label_2.setGeometry(QtCore.QRect(30, 150, 121, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(DetectionBox)
        self.label_3.setGeometry(QtCore.QRect(40, 10, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit = QtGui.QLineEdit(DetectionBox)
        self.lineEdit.setGeometry(QtCore.QRect(40, 170, 51, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_4 = QtGui.QLabel(DetectionBox)
        self.label_4.setGeometry(QtCore.QRect(30, 120, 81, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(DetectionBox)
        self.label_5.setGeometry(QtCore.QRect(110, 120, 51, 21))
        self.label_5.setAutoFillBackground(True)
        self.label_5.setFrameShape(QtGui.QFrame.Box)
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.retranslateUi(DetectionBox)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DetectionBox.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DetectionBox.reject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("helpRequested()")), DetectionBox.open)
        QtCore.QMetaObject.connectSlotsByName(DetectionBox)

    def retranslateUi(self, DetectionBox):
        DetectionBox.setWindowTitle(_translate("DetectionBox", "DetectionBox", None))
        self.label.setText(_translate("DetectionBox", "DetectionBox has detected that your target field has negative values for samples below detection. For the robustness of the technique, it is recommended that these are changed to be half the detection limit for that element", None))
        self.label_2.setText(_translate("DetectionBox", "Replacement Value", None))
        self.label_3.setText(_translate("DetectionBox", "Detection Limit Alteration Needed", None))
        self.label_4.setText(_translate("DetectionBox", "Value detected", None))

