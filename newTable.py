#coding=utf-8


from PyQt4.QtCore import *
from PyQt4.QtGui import *



class NewTable(QTableWidget):
    myReturnPressed = pyqtSignal(int,int)
    def __init__(self,parent=None):
        super(QTableWidget,self).__init__(parent)
        self.tableName =''
        self.columnsWidth = []

        
    def setTableName(self,name):
        self.tableName = name
        
        
    def getTableName(self):
        return self.tableName
    
    def mousePressEvent(self,event):
        button = event.button()
        pos = event.pos()
        index = self.indexAt(pos)
        item = self.itemFromIndex(index)
        if button == Qt.LeftButton:
            self.setSelectionBehavior(QAbstractItemView.SelectItems)
            self.setItemSelected(item,True)
            super(QTableWidget,self).mousePressEvent(event)

        elif button == Qt.RightButton:
            self.setSelectionBehavior(QAbstractItemView.SelectRows)
            super(QTableWidget,self).mousePressEvent(event)
         
    def keyPressEvent(self,e):
        super(NewTable,self).keyPressEvent(e)
        if e.key() == Qt.Key_Return:
            curIndex = self.selectedIndexes()
            if len(curIndex)>0:
                curIndex = curIndex[0]
            else:
                curIndex = self.currentIndex()
            curWidget = self.cellWidget(curIndex.row(),curIndex.column())
            print type(curWidget)
            if curWidget is not None:
                if isinstance(curWidget,QComboBox):
                    value = curWidget.currentText()
                    self.removeCellWidget(curIndex.row(), curIndex.column())
                    item = QTableWidgetItem(value)
                    item.setTextAlignment(Qt.AlignHCenter)
                    self.setItem(curIndex.row(), curIndex.column(), item)
                elif isinstance(curWidget,QSlider):
                    value = curWidget.value()
                    self.removeCellWidget(curIndex.row(), curIndex.column())
                elif isinstance(curWidget,QCalendarWidget):
                    date = curWidget.selectedDate().toString('yyyy-MM-dd')
                    self.removeCellWidget(curIndex.row(), curIndex.column())
                    item = QTableWidgetItem(date)
                    item.setTextAlignment(Qt.AlignHCenter)                    
                    self.setItem(curIndex.row(), curIndex.column(), item)
                    self.setRowHeight(curIndex.row(),30)
                    self.setColumnWidth(curIndex.column(),self.columnsWidth[curIndex.column()])
                elif isinstance(curWidget,QLineEdit):
                    value = curWidget.text()
                    item = QTableWidgetItem(value)
                    item.setTextAlignment(Qt.AlignHCenter)                    
                    self.setItem(curIndex.row(), curIndex.column(), item)
            self.myReturnPressed.emit(curIndex.row(),curIndex.column())


                    
