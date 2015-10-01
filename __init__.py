# -*- coding: utf-8 -*-
"""
/***************************************************************************
 dataAlert
                                 A QGIS plugin
 Alerts when new UVI data is added
                             -------------------
        begin                : 2015-09-28
        copyright            : (C) 2015 by Eric Ong
        email                : eric.ong@digitalglobe.com
        git sha              : $Format:%H$
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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load dataAlert class from file dataAlert.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .data_Alert import dataAlert
    return dataAlert(iface)
