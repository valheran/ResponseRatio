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
from ui_responseratio import Ui_ResponseRatio

from qgis.core import *
#import Utility functions
import RR_utilities as utils

class ResponseRatioDialog(QtGui.QDialog, Ui_ResponseRatio):
	tarLayer = 0
	tarField = 0
	calcButton = 0
	eleList = 0 
	
	def __init__(self):
			QtGui.QDialog.__init__(self)
			# Set up the user interface from Designer.
			self.ui = Ui_ResponseRatio()
			self.ui.setupUi(self)
			#rename combo box variable
			ResponseRatioDialog.tarLayer = self.ui.targetLayer
			ResponseRatioDialog.tarField = self.ui.targetField
			ResponseRatioDialog.calcButton = self.ui.calcButton
			ResponseRatioDialog.eleList = self.ui.listWidget
			#refresh Target Element combo box when Data Layer combo box changes
			ResponseRatioDialog.tarLayer.currentIndexChanged.connect(self.reloadFields)
			#load Data Layer Combo box
			self.manageGui()
			
	def manageGui(self):
			
			ResponseRatioDialog.tarLayer.clear()
			ResponseRatioDialog.tarLayer.addItems(utils.getVectorLayerNames())
			
	def reloadFields(self):
			
			layer = utils.getVectorLayerByName(ResponseRatioDialog.tarLayer.currentText())
			
			ResponseRatioDialog.tarField.clear()
			ResponseRatioDialog.tarField.addItems(utils.getFieldNames(layer))
			
#	def addEleList(self):
		#adds elements to the list to keep track of whats been calculated