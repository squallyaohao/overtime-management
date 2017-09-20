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
    
    def mousePressEvent(self,event):
        button = event.button()
        if button == Qt.LeftButton:
            self.setSelectionBehavior(QAbstractItemView.SelectItems)
            super(QTableWidget,self).mousePressEvent(event)
        elif button == Qt.RightButton:
            self.setSelectionBehavior(QAbstractItemView.SelectRows)
            super(QTableWidget,self).mousePressEvent(event)