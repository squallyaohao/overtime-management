#coding=utf-8
#this file define the actual interface of the program and internal actions and slots

import sys,os,os.path
from PyQt4 import QtCore
from PyQt4 import QtGui
from ui_mainwindow import Ui_MainWindow
import department,member
import pandas as pd


class UI_ApplyOvertime(Ui_MainWindow):
    def __init__(self,parent=None):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)

if __name__ =='__main__':
    app = QtGui.QApplication(sys.argv) 
    ui = UI_ApplyOvertime()
    ui.show()
sys.exit(app.exec_()) 