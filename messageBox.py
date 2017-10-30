#coding=utf-8

import sys,os
from PyQt4 import QtCore
from PyQt4 import QtGui


class Warning(QtGui.QMessageBox):
    def __init__(self,msg,parent=None):
        super(Warning,self).__init__(QtGui.QMessageBox.Warning,u'警告',msg,QtGui.QMessageBox.Ok,parent=parent)
        self.show()
        






if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    box = Warning('dada')   
    box.show()
    app.exec_()
        