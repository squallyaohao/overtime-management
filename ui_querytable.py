# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Dev\overtime-management\ui_tablewindow.ui'
#
# Created: Mon Sep 11 18:56:01 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

import sys    
from PyQt4 import QtCore, QtGui
from ui_tablewindow import Ui_Form
import excelUtility

tablehead = ['日期','姓名','加班项目','加班时长','加班餐']


class Ui_QueryTable(Ui_Form):
    updateSignal = QtCore.pyqtSignal(name='updateServer')
    def __init__(self,parent=None):    
        super(Ui_Form,self).__init__(parent)
        self.setupUi(self)
        self.connect(self.pushButton,QtCore.SIGNAL('clicked()'),self.saveExcel)
        self.connect(self.pushButton_2,QtCore.SIGNAL('clicked()'),self.updateQuery)
        
    #show query result    
    def drawTable(self,result):
        numRows = len(result)
        numCols = len(result[0])
        self.tableWidget.setRowCount(numRows)
        self.tableWidget.setColumnCount(numCols)
        self.tableWidget.setHorizontalHeaderLabels(['Date','Name','Project','Duration','Meal'])
        #self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        textFont = QtGui.QFont('Hei',11)
        #start draw table
        for i,row in enumerate(result):
            for j,col in enumerate(row):
                item = QtGui.QTableWidgetItem(unicode(col))
                item.setTextAlignment(0x0004|0x0080	)
                item.setFont(textFont)
                self.tableWidget.setItem(i,j, item)   
                
                
    #save query result to an excel    
    def saveExcel(self):
        list = []
        list.append(tablehead)
        rows = self.tableWidget.rowCount()
        cols = self.tableWidget.columnCount()
        for i in range(0,rows):
            temp = []
            for j in range(0,cols):
                item = self.tableWidget.item(i,j)
                t = item.text()
                temp.append(unicode(t))
            list.append(temp)        
        #catch error if IOError
        error = excelUtility.exportToExcel(r'c:\aaa.xlsx',list)
        if isinstance(error,IOError):
            messagebox = QtGui.QMessageBox(2,QtCore.QString(u'错误'),QtCore.QString(u'保存文件失败，请检查文件是否处于打开状态！'),QtGui.QMessageBox.Yes | QtGui.QMessageBox.Cancel)
            messagebox.exec_()    
        if error == 1:
            messagebox = QtGui.QMessageBox(1,QtCore.QString(u''),QtCore.QString(u'文件保存成功！'),QtGui.QMessageBox.Yes)
            messagebox.exec_() 
            
            
    def updateQuery(self):
        self.updateSignal.emit()
        pass
        
    def getTableData(self):
        print 'getData'
        list = []
        return list
        pass
        


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    table = Ui_QueryTable()
    table.show()
    app.exec_()