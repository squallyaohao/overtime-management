# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Dev\overtime-management\ui_tablewindow.ui'
#
# Created: Mon Sep 11 18:56:01 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

import sys    
from PyQt4 import QtCore, QtGui
from ui_tablewindow import Ui_Form

class Ui_QueryTable(Ui_Form):
    def __init__(self,parent=None):
        super(Ui_Form,self).__init__(parent)
        self.setupUi(self)

        
        
        


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    table = Ui_QueryTable()
    table.show()
    app.exec_()