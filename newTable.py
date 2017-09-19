#coding=utf-8


from PyQt4.QtCore import *
from PyQt4.QtGui import *



class NewTable(QTableWidget):
    def __init__(self,parent=None):
        super(QTableWidget,self).__init__(parent)
        self.tableName =''
        
        
    def setTableName(self,name):
        self.tableName = name
        
        
    def getTableName(self):
        return self.tableName