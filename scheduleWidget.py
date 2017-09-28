#coding=utf-8

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import scheduleWidgetSuper
import random,copy
import department_manager


class scheduleWidget(scheduleWidgetSuper.Ui_Form):
    def __init__(self,parent=None):
        super(scheduleWidgetSuper.Ui_Form,self).__init__(parent)
        self.setupUi(self)
        
        self.scrollBar1 = self.period1.horizontalScrollBar()
        self.scrollBar2 = self.period2.horizontalScrollBar()
        self.scrollBar3 = self.schedule.horizontalScrollBar()
        
        self.setConnections()
        self.setUpTables()
        self.drawTree()
        self.expandItem()
        self.collapsItem()
        
        self.itemList=[]


    
    def synchronize(self,x):
        self.scrollBar1.setValue(x)
        self.scrollBar2.setValue(x)
        
        
    def setUpTables(self):
        self.period1.setColumnCount(14)
        for i in range(14):
            self.period1.setColumnWidth(i,100)
            
        self.period2.setColumnCount(14)
        for i in range(14):
            self.period2.setColumnWidth(i,100)        
            
        self.schedule.setColumnCount(14)
        for i in range(14):
            self.schedule.setColumnWidth(i,100)
            
        rowCounts = self.schedule.rowCount()
        for i in range(rowCounts):
            self.schedule.setSpan(i,0,1,14)           
        
        
    def drawSchedule(self,row_index,start_date,end_date,progress):
        cellWidth = self.schedule.columnWidth(0)*self.schedule.columnSpan(0,0)
        rowHeight = self.schedule.rowHeight(row_index)
        rect = QRect(0,0,cellWidth,rowHeight)
        item = scheduleBar(rect,start_date,end_date,Qt.green,progress)
        self.schedule.setCellWidget(row_index,0,item)


       
    def drawTree(self):
        headItem = self.entry_list.headerItem()
        headItem.setSizeHint(0,QSize(100,50))
        iterator = QTreeWidgetItemIterator(self.entry_list)
        i=0
        while iterator.value() is not None:
            item = iterator.value()            
            item.setSizeHint(0,QSize(100,30))
            start_date = i/10.0
            end_date = (i+1)/10.0
            progress = random.uniform(0,1.0)
            self.drawSchedule(i,start_date,end_date,progress)
            data = QVariant(i)
            item.setData(0,Qt.UserRole,data)
            #item.setExpanded(True)
            #self.entry_list.itemExpanded.emit(item)
            i = i+1
            iterator = iterator.__iadd__(1)

    
    def expandItem(self):
        iterator = QTreeWidgetItemIterator(self.entry_list)
        while iterator.value() is not None:
            item = iterator.value()            
            item.setExpanded(True)
            #self.entry_list.itemExpanded.emit(item)
            iterator = iterator.__iadd__(1)
    
    
    def collapsItem(self):
        iterator = QTreeWidgetItemIterator(self.entry_list)
        while iterator.value() is not None:
            item = iterator.value()            
            item.setExpanded(False)
            #self.entry_list.itemExpanded.emit(item)
            iterator = iterator.__iadd__(1)        
            
    
    def collapsSchedule(self,item):
        self.entry_list.selectAll()
        sl = self.entry_list.selectedIndexes()
        self.entry_list.clearSelection()
        showList =[]
        for s in sl:
            item = self.entry_list.itemFromIndex(s)
            row_index = item.data(0,Qt.UserRole).toInt()[0]
            showList.append(row_index)
        
        rowCount = self.schedule.rowCount()
        for row in range(rowCount):
            self.schedule.hideRow(row)
        for row in showList:
            self.schedule.showRow(row)
        
        

    def setConnections(self):
        self.scrollBar3.valueChanged.connect(self.synchronize)
        self.entry_list.itemExpanded.connect(self.collapsSchedule)
        self.entry_list.itemCollapsed.connect(self.collapsSchedule)


class scheduleBar(QWidget):
    def __init__(self,rect,startPos,endPos,color,progress,parent=None):
        super(QWidget,self).__init__(parent)
        self.startPos = startPos
        self.endPos = endPos
        self.progress = progress
        rectLeft = rect.left()
        rectWidth = rect.width()
        rectTop = rect.top()
        rectHeight = rect.height()
        barLeft = rectLeft + rectWidth*startPos
        barWidth = rectWidth * (endPos - startPos)
        barTop = rectTop + rectHeight*0.25
        barHeight = rectHeight*0.5
        self.rect = rect
        self.bar = QRect(barLeft,barTop,barWidth,barHeight)
        self.color = color
        progressBarWidth = barWidth*(progress)
        self.progressBar = QRect(barLeft,barTop,progressBarWidth,barHeight)      

    def __getitem__(self):
        return scheduleBar(self.rect, self.startPos, self.endPos, self.color, self.progress, 
                          )
        
    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)
        p.setBrush(self.color)        
        p.drawRect(self.bar)
        p.setBrush(Qt.blue)
        p.drawRect(self.progressBar)
        startLineTopx = self.bar.left()
        startLineTopy = self.rect.top()
        startLineBottomx = self.bar.left()
        startLineBottomy = self.rect.bottom()
        endLineTopx = endLineBottomx = self.bar.right()
        endLineTopy = self.rect.top() 
        endLineBottomy = self.rect.bottom()
        pen = QPen()
        pen.setColor(Qt.black)
        pen.setStyle(Qt.SolidLine)
        pen.setWidth(5)
        p.setPen(pen)
        p.drawLine(startLineTopx,startLineTopy,startLineBottomx,startLineBottomy)
        p.drawLine(endLineTopx,endLineTopy, endLineBottomx,endLineBottomy)
        p.end()
        
        