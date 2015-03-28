# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\abrown2\.qgis2\python\plugins\ResponseRatio\ui_responseratio.ui'
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

class Ui_ResponseRatio(object):
    def setupUi(self, ResponseRatio):
        ResponseRatio.setObjectName(_fromUtf8("ResponseRatio"))
        ResponseRatio.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(ResponseRatio)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Help|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.targetLayer = QtGui.QComboBox(ResponseRatio)
        self.targetLayer.setGeometry(QtCore.QRect(20, 100, 131, 21))
        self.targetLayer.setObjectName(_fromUtf8("targetLayer"))
        self.targetField = QtGui.QComboBox(ResponseRatio)
        self.targetField.setGeometry(QtCore.QRect(20, 160, 131, 21))
        self.targetField.setObjectName(_fromUtf8("targetField"))
        self.label = QtGui.QLabel(ResponseRatio)
        self.label.setGeometry(QtCore.QRect(30, 80, 101, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(ResponseRatio)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 121, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(ResponseRatio)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.calcButton = QtGui.QPushButton(ResponseRatio)
        self.calcButton.setGeometry(QtCore.QRect(40, 200, 75, 23))
        self.calcButton.setObjectName(_fromUtf8("calcButton"))
        self.listWidget = QtGui.QListWidget(ResponseRatio)
        self.listWidget.setGeometry(QtCore.QRect(240, 30, 141, 191))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.label_4 = QtGui.QLabel(ResponseRatio)
        self.label_4.setGeometry(QtCore.QRect(250, 10, 111, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(ResponseRatio)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ResponseRatio.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ResponseRatio.reject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("helpRequested()")), ResponseRatio.open)
        QtCore.QMetaObject.connectSlotsByName(ResponseRatio)

    def retranslateUi(self, ResponseRatio):
        ResponseRatio.setWindowTitle(_translate("ResponseRatio", "ResponseRatio", None))
        self.label.setText(_translate("ResponseRatio", "Data Layer", None))
        self.label_2.setText(_translate("ResponseRatio", "Target Element", None))
        self.label_3.setText(_translate("ResponseRatio", "Response Ratio Calculator", None))
        self.calcButton.setText(_translate("ResponseRatio", "Calculate", None))
        self.label_4.setText(_translate("ResponseRatio", "Elements Calculated", None))

