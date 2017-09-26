#coding=utf-8

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import scheduleWidgetSuper


class scheduleWidget(scheduleWidgetSuper.Ui_Form):
    def __init__(self,parent=None):
        super(scheduleWidgetSuper.Ui_Form,self).__init__(parent)
        self.setupUi(self)
        
        
        self.period1.setColumnCount(14)
        for i in range(14):
            self.period1.setColumnWidth(i,100)
            
        self.period2.setColumnCount(14)
        for i in range(14):
            self.period2.setColumnWidth(i,100)        
            
        self.schedule.setColumnCount(14)
        for i in range(14):
            self.schedule.setColumnWidth(i,100)        
        self.schedule.setSpan(0,0,1,14)
            
        
        self.scrollBar1 = self.period1.horizontalScrollBar()
        self.scrollBar2 = self.period2.horizontalScrollBar()
        self.scrollBar3 = self.schedule.horizontalScrollBar()
        
      
        headItem = self.entry_list.headerItem()
        headItem.setSizeHint(0,QSize(100,50))
        iterator = QTreeWidgetItemIterator(self.entry_list)
        while iterator.value() is not None:
            iterator.value().setSizeHint(0,QSize(100,30))
            iterator = iterator.__iadd__(1)

        self.scrollBar3.valueChanged.connect(self.synchronize)

        
        rowStartX = self.schedule.columnViewportPosition(0) 
        rowStartY = self.schedule.rowViewportPosition(0)
        cellWidth = self.schedule.columnWidth(0)*self.schedule.columnSpan(0,0)
        rowHeight = self.schedule.rowHeight(0)
        rect = QRect(rowStartX,rowStartY,cellWidth,rowHeight)
        item = scheduleBar(rect,0.2,0.7,Qt.red)
        self.schedule.setCellWidget(0,0, item)
    
    def synchronize(self,x):
        self.scrollBar1.setValue(x)
        self.scrollBar2.setValue(x)
        
        
        


class scheduleBar(QWidget):
    def __init__(self,rect,startPos,endPos,color,parent=None):
        super(QWidget,self).__init__(parent)
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
        
    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)
        p.setBrush(self.color)        
        p.drawRect(self.bar)
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
        
        