# -*- coding: utf-8 -*-
"""
/***************************************************************************
 dataAlertDockWidget
                                 A QGIS plugin
 Alerts when new UVI data is added
                             -------------------
        begin                : 2015-09-28
        git sha              : $Format:%H$
        copyright            : (C) 2015 by Eric Ong
        email                : eric.ong@digitalglobe.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt4 import QtGui, uic
from PyQt4.QtCore import *

#NEW STUFF*******
from PyQt4 import QtCore
import urllib2
import time
import json

from datetime import datetime

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'data_Alert_dockwidget_base.ui'))

class dataAlertDockWidget(QtGui.QDockWidget, FORM_CLASS):

    closingPlugin = pyqtSignal()

    def __init__(self, parent=None):
        """Constructor."""
        super(dataAlertDockWidget, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

#NEW STUFF*******
        #self.pool = QtCore.QThreadPool()

        QtCore.QObject.connect(self.startButton, QtCore.SIGNAL('clicked()'), self.getParameters)

    def getParameters(self):
        left = self.left.text()
        right = self.right.text()
        upper = self.upper.text()
        lower = self.lower.text()
        #if (-180 <= left and right <= 180) and (-90 <= lower and upper <= 90):
        #if left >= -180 and left < right and right <= 180 and right > left and upper <= 90 and upper > lower and \
         #       lower >=-90 and lower < upper:
            #self.pool.start(self.dataAlertTool(left, right, upper, lower))
        self.dataAlertTool(left, right, upper, lower)
        #else:
            #self.textBrowser.append('Please enter valid coordinates')

    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()

    def dataAlertTool(self, left, right, upper, lower):
        mins = 0

        sourcesURL = 'https://iipbeta.digitalglobe.com/insight-vector/api/vectors/sources?left='+str(left)+'&right='+str(right)\
                     +'&upper='+str(upper)+'&lower='+str(lower)

        header = {'Authorization': 'Bearer7be753ae-8b42-4307-a1a0-7d8b8700182b'}

        sources = urllib2.Request(sourcesURL, headers=header)

        try:
            sourcesResponse = urllib2.urlopen(sources)
            sourcesData = sourcesResponse.read()
            self.textBrowser.append('------ ' + str(datetime.now()) + ' ------')

        except urllib2.HTTPError, e:
            self.textBrowser.append("Encountered http error: " + str(e))
        except IOError, e:
            self.textBrowser.append("Encountered io error: " + str(e))

        decoded = json.loads(sourcesData)
        previous = dict(decoded)

        for key in decoded['data']:
            self.textBrowser.append('Number of ' + str(key['name']) + ' features: ' + str(key['count']))

        time.sleep(5)

        self.textBrowser.append('\n')

        while mins != 3:
            sourcesResponse3 = urllib2.urlopen(sources)
            sourcesData3 = sourcesResponse3.read()
            decoded2 = json.loads(sourcesData3)
            self.textBrowser.append('------ ' + str(datetime.now()) + ' -------')
            current = dict(decoded2)

            for (a, b) in zip(previous['data'], current['data']):
                if a['count'] < b['count']:
                    self.textBrowser.append('***ALERT: ' + str((b['count'])-(a['count'])) + ' new ' + a['name'] + ' feature(s)***')

            previous = dict(decoded2)

            mins += 1
            time.sleep(5)
