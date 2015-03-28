# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ResponseRatio
                                 A QGIS plugin
 Calculates response ratios
                             -------------------
        begin                : 2013-10-22
        copyright            : (C) 2013 by dfgdfgdf
        email                : dfgdfgdfg
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


def name():
    return "RR Calculator"


def description():
    return "Calculates response ratios"


def version():
    return "Version 0.1"


def icon():
    return "icon.png"


def qgisMinimumVersion():
    return "2.0"

def author():
    return "dfgdfgdf"

def email():
    return "dfgdfgdfg"

def classFactory(iface):
    # load ResponseRatio class from file ResponseRatio
    from responseratio import ResponseRatio
    return ResponseRatio(iface)
