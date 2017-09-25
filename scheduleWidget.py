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

        
        startPos = 1400*0.2
        barWidth = 1400*0.5
        barHeight = 25*0.7
        barYStart = 25*0.3
        item = scheduleBar(QRect(startPos,barYStart,barWidth,barHeight))
        self.schedule.setCellWidget(0,0, item)
    
    def synchronize(self,x):
        self.scrollBar1.setValue(x)
        self.scrollBar2.setValue(x)
        
        
        


class scheduleBar(QWidget):
    def __init__(self,rect,parent=None):
        super(QWidget,self).__init__(parent)
        self.rect = rect
        
        
    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)
        p.setBrush(Qt.green)
        p.drawRect(self.rect)
        p.end()
        
        