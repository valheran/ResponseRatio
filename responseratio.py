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


# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.utils import *
from qgis.gui import *
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from responseratiodialog import ResponseRatioDialog
from ui_responseratio import Ui_ResponseRatio as ui_input
import os.path
#import Utility functions
import RR_utilities as utils


class ResponseRatio:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'responseratio_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = ResponseRatioDialog()

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/responseratio/icon.png"),
            "Response Ratio", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&RR Calculator", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&RR Calculator", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
        # show the dialog
		self.dlg.__init__()
		self.dlg.show()
        # Run the dialog event loop
		
		self.dlg.calcButton.clicked.connect(self.calc)
		
		result = self.dlg.exec_()
        # See if OK was pressed
		if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code)
			pass
	
    def calc(self):
		#initiate class
		layerName = ResponseRatioDialog.tarLayer.currentText()
		fieldName = ResponseRatioDialog.tarField.currentText()
		listItem = ''
		calculator = utils.resRatio(layerName, fieldName)
#		background has been calculated, now need to create new attribute, then populate with response ratios

		calculator.addField()
		calculator.popField()
		
		listItem = str(calculator.NewFieldName) + str("  ") + str(calculator.background)
		#self.dlg.eleList.addItem(calculator.NewFieldName)
		self.dlg.eleList.addItem(listItem)
		#debugging output
		result = str(calculator.background)
		#iface.messageBar().pushMessage("background calc", result, level=QgsMessageBar.INFO)
		message = str('background used_') + str(result)
		QgsMessageLog.logMessage(message)
