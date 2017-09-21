#coding=utf-8

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import scheduleWidgetSuper


class scheduleWidget(scheduleWidgetSuper.Ui_Form):
    def __init__(self,parent=None):
        super(scheduleWidgetSuper.Ui_Form,self).__init__(parent)
        self.setupUi(self)
        
        

        
        
        scrollBar1 = self.period1.horizontalScrollBar()
        scrollBar2 = self.period2.horizontalScrollBar()
        headItem = self.entry_list.headerItem()
        headItem.setSizeHint(0,QSize(100,50))
        iterator = QTreeWidgetItemIterator(self.entry_list)
        while iterator.value() is not None:
            iterator.value().setSizeHint(0,QSize(100,30))
            iterator = iterator.__iadd__(1)

        #leftHeader1 = QTableWidgetItem('1')
        #leftHeader1.setText('fdafdsa')
        #leftHeader1.setSizeHint(QSize(100,50))
        #self.entry_list.setHorizontalHeaderItem(0,leftHeader1)
