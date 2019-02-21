#coding=utf-8

import sys,os
from PyQt4 import QtCore
from PyQt4 import QtGui


class Warning(QtGui.QMessageBox):
    def __init__(self,msg,parent=None):
        super(Warning,self).__init__(QtGui.QMessageBox.Warning,u'警告',msg,QtGui.QMessageBox.Ok,parent=parent)
        self.show()
        
class Info(QtGui.QMessageBox):
    def __init__(self,msg,parent=None):
        super(Info,self).__init__(QtGui.QMessageBox.Information,u'提示',msg,QtGui.QMessageBox.Ok,parent=parent)
        self.show()
        
class confirm(QtGui.QMessageBox):
    def __init__(self,msg,parent=None):
        super(confirm,self).__init__(QtGui.QMessageBox.Question,u'确认',msg,QtGui.QMessageBox.Ok|QtGui.QMessageBox.Cancel,parent=parent)
        self.show()






if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    box = Warning('dada')   
    box.show()
    app.exec_()
        