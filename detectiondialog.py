# -*- coding: utf-8 -*-
#**************************************************************************************************
#	Response Ratio QGIS Script	
#	A Brown and B Byrne
#
#	A script designed to convert analytical data of a coherent (an comparable) set of geochemical
#	data (eg Soil survey) and convert the variables into response ratios, essentially expressing
#	it in terms of multiples of "background". This allows for the data to be viewed as 
#	"how anomalous" rather than an absolute value, and also means that values between elements
#	can be directly compared, or added together to give cumulative results
#	Background is determined as the mean of the 1st quartile, and Response Ratio (RR) is given by;
#
#		RR = assay/mean(Q1)
#
#	
#
#**************************************************************************************************


from PyQt4 import QtCore, QtGui
from ui_DetectionBox import Ui_DetectionBox

from qgis.core import *
#import Utility functions
import RR_utilities as utils

class DetectionBoxDialog(QtGui.QDialog, Ui_DetectionBox):
	lineInput = 0
	prevValue = 0
	repValue = 0
	def __init__(self, errorValue):
			QtGui.QDialog.__init__(self)
			# Set up the user interface from Designer.
			self.ui = Ui_DetectionBox()
			self.ui.setupUi(self)
			self.errorValue = errorValue
			#rename output label and input box
			
			DetectionBoxDialog.lineInput = self.ui.lineEdit
			DetectionBoxDialog.prevValue = self.ui.label_5
			#set the detected error value
			DetectionBoxDialog.prevValue.setText(str(errorValue))
			#refresh Target Element combo box when Data Layer combo box changes
			#DetectionBoxDialog.tarLayer.currentIndexChanged.connect(self.reloadFields)
			
			self.run()
			
	def run(self):
		#result = self.exec_()
		#if result == 1 :
			#QgsMessageLog.logMessage('ok clicked dialog')
			DetectionBoxDialog.repValue = self.lineInput.text()
		
			
