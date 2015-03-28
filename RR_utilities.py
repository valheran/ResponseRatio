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
#Utility functions for the response Ratio plugin


import locale

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from qgis.core import *
from qgis.gui import *
import processing
from detectiondialog import DetectionBoxDialog 

def getVectorLayerNames():
    layerMap = QgsMapLayerRegistry.instance().mapLayers()
    layerNames = []
    for name, layer in layerMap.iteritems():
        if layer.type() == QgsMapLayer.VectorLayer:
            layerNames.append(unicode(layer.name()))
    return sorted(layerNames, cmp=locale.strcoll)


def getVectorLayerByName(layerName):
    layerMap = QgsMapLayerRegistry.instance().mapLayers()
    for name, layer in layerMap.iteritems():
        if layer.type() == QgsMapLayer.VectorLayer and layer.name() == layerName:
            if layer.isValid():
                return layer
            else:
                return None

def getFieldNames(layer):
    fields = layer.pendingFields()
    fieldNames = []
    for field in fields:
        fieldNames.append(unicode(field.name()))
    return sorted(fieldNames, cmp=locale.strcoll)
	
#original functions
#def getFieldNames(layer, fieldTypes):
#   fields = layer.pendingFields()
#   fieldNames = []
#    for field in fields:
#       if field.type() in fieldTypes and not field.name() in fieldNames:
#            fieldNames.append(unicode(field.name()))
#    return sorted(fieldNames, cmp=locale.strcoll)

class resRatio:

	values = []
	background = 0.00000
	layer = 0        	#layer selected in dialog box
	index = 0			#field index of field selected in dialog box
	NewFieldName = '' 	#name of new field to be generated
	tarFieldName = '' 	#name of layer selected in dialog box
	testResult = 0
	Error = 0
	
	def __init__(self, layerName, fieldName):
		self.layerName = layerName
		self.fieldname = fieldName
		
		# initialise the target layer and field
		resRatio.layer = getVectorLayerByName(layerName)
		resRatio.index = self.layer.fieldNameIndex(fieldName)
		resRatio.tarFieldName = fieldName
		resRatio.background = 0.00000
		resRatio.values = []
		resRatio.Error = 0
		#Checkdata fancy
		#self.errorlooping() # will return false if no error found, return nothing if error found after correcting it
		#if self.errorlooping() :
		#	self.errorlooping()
		#else
		
		#checkdata
		if self.checkData():
			#checkdata has detected error, initiate dialog box
			self.errdlg = DetectionBoxDialog(resRatio.Error)
			#show dialog box to obtain replacement value
			self.errdlg.show()
			if self.errdlg.exec_() :
				#initiate error correction iterator
				#QgsMessageLog.logMessage('ok clicked utilities')
				self.errdlg.run()
				self.errCorrector(self.errdlg.repValue)
		else:
		# continue on
			pass
		#pull in data and calculate background
		self.pullData()
		resRatio.background = self.backCalc()
		
		
	def pullData(self):
		Index = resRatio.index 
		Layer = resRatio.layer
		
		request = QgsFeatureRequest()
		request.setFlags(QgsFeatureRequest.NoGeometry)
		request.setSubsetOfAttributes([Index])
	
				
		for f in Layer.getFeatures(request):
			try:
				value = float(f[Index])
			except TypeError:
				value = 0
				
			if value > 0 :	
				resRatio.values.append(value)   
	
	def backCalc(self):
		#Sort table
		tmp = resRatio.values
		tmp.sort()
		count = len(tmp)
		#Find index of the first quartile. This is a very crude method, and will err on the low side for the 1st quartile
	
		quartIndex = int(count/4)-1

		#Find Mean of first quartile
		i = 0
		sumQuart = 0
		while i <= quartIndex:
			sumQuart += tmp[i]
			i+=1
	
		meanQuart = sumQuart/(quartIndex + 1)
		#return mean of first quartile as the background value
		#QgsMessageLog.logMessage(str(meanQuart))
		return meanQuart;
		
	def rrCalc(self, origValue):
		self.origValue = origValue
		#QgsMessageLog.logMessage(str(origValue))
		#QgsMessageLog.logMessage(str(resRatio.background))
		#calculate the response ratio using the original assay value and the calculated background
		try:
			responseRatio = origValue / resRatio.background
		except TypeError:
			responseRatio = None
		#return the value of the response ratio
		return responseRatio;

	def addField(self):
		#taken directly from PyQgis cookbook
		#res = layer.dataProvider().addAttributes( [ QgsField("mytext", QVariant.String), QgsField("myint", QVariant.Int) ] )
		#get target layer
		Layer = resRatio.layer
		Index = resRatio.index
		
		resRatio.NewFieldName = str(resRatio.tarFieldName) + str('_RR')  
		#check capability?
		#'editing' commands were put in to forces the new column to 'exist' in the attribute table- 
		#previously there was a problem of the new column being 'invisible' to the remaining functions
		Layer.startEditing()
		Layer.beginEditCommand('add new RR attribute')
		Layer.dataProvider().addAttributes([QgsField(resRatio.NewFieldName, QVariant.Double, 'double', 20, 2)])
		Layer.endEditCommand()
		Layer.commitChanges()
		
	def popField(self):
		
		#get target layer and field
		Index = resRatio.index 
		NewIndex = resRatio.layer.fieldNameIndex(resRatio.NewFieldName)
		Layer = resRatio.layer
		NewField = resRatio.NewFieldName
		features = Layer.getFeatures()
				
		Layer.startEditing()
		for feat in features:
			featID = feat.id()
			attrs = self.rrCalc(feat.attributes()[Index])
			
			Layer.changeAttributeValue(featID, NewIndex, attrs)
				
		Layer.commitChanges()
		
		#attempt to do it with dictionary
		#taken directly from PyQgis cookbook
		#attrs = { 0 : QVariant("hello"), 1 : QVariant(123) }
		#layer.dataProvider().changeAttributeValues({ fid : attrs })
		
		#changeTable = {}
	
	#	for feat in features:
	#		changeTable[feat.id()] = { NewIndex : self.rrCalc(feat.attributes()[Index])}
		
	#	Layer.dataProvider().ChangeAttributeValues(changeTable)
	
	#function to check for -ve values, if found, value is returned in order to trigger error dialog
	def checkData(self):
		Index = resRatio.index 
		Layer = resRatio.layer
		error = False
		
		request = QgsFeatureRequest()
		request.setFlags(QgsFeatureRequest.NoGeometry)
		request.setSubsetOfAttributes([Index])
	
				
		for f in Layer.getFeatures(request):
			try:
				value = float(f[Index])
				if value < 0 :
				#is bad number, trigger detetction limit alteration dialog
					error = True
				break
			except TypeError:
				continue
		
		if error :
			resRatio.Error = value
			return True;
				
	def errCorrector(self, repValue) :
		self.repValue = repValue
		Index = resRatio.index 
		Layer = resRatio.layer
				
		request = QgsFeatureRequest()
		request.setFlags(QgsFeatureRequest.NoGeometry)
		request.setSubsetOfAttributes([Index])
					
		Layer.startEditing()
		for f in Layer.getFeatures(request):
			featID = f.id()
			try:
				value = float(f[Index])
				if value < 0 :
				#is bad number, replace with new number
					Layer.changeAttributeValue(featID, Index, repValue)
				
			except TypeError:
				continue 
		Layer.commitChanges()
		
	#def errorlooping(self) :
	#	somevar = True
	#	if self.checkData():
			#checkdata has detected error, initiate dialog box
	#		self.errdlg = DetectionBoxDialog(resRatio.Error)
			#show dialog box to obtain replacement value
	#		self.errdlg.show()
	#		if self.errdlg.exe_() :
				#initiate error correction iterator
	#			self.errCorrector(self.errdlg.repValue)	
	#		else:
	#			somevar = False
				
	#		return somevar;
		# continue on
		