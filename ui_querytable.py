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

tablehead = [u'日期',u'姓名',u'加班项目',u'加班展项',u'加班时长',u'加班餐',u'加班描述']


class Ui_QueryTable(Ui_Form):
    updateSignal = QtCore.pyqtSignal(name='updateServer')
    def __init__(self,parent=None):    
        super(Ui_Form,self).__init__(parent)
        self.setupUi(self)
        self.connect(self.pushButton,QtCore.SIGNAL('clicked()'),self.saveExcel)
        self.connect(self.pushButton_2,QtCore.SIGNAL('clicked()'),self.updateQuery)
        self.numRows = 0
        self.numCols = 0
        
                
    #show query result    
    def drawTable(self,result,projectlist):
        numRows = len(result)
        numCols = len(tablehead)
        self.numRows = numRows
        self.numCols = numCols
        self.tableWidget.setRowCount(numRows)
        self.tableWidget.setColumnCount(numCols)
        self.tableWidget.setHorizontalHeaderLabels(tablehead)
        #self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        textFont = QtGui.QFont('Hei',11)
        #start draw table
        for i,row in enumerate(result):
            for j,col in enumerate(row):
                if j != 2:
                    item = QtGui.QTableWidgetItem(unicode(col))
                    item.setTextAlignment(0x0004|0x0080)
                    item.setFont(textFont)
                    if j<2:
                        item.setFlags(QtCore.Qt.ItemIsEditable)                    
                    self.tableWidget.setItem(i,j, item) 
                else:
                    comboItem = QtGui.QComboBox()
                    comboItem.addItem(col)
                    for pro in projectlist:
                        if col != pro:
                            comboItem.addItem(pro)
                    comboItem.setCurrentIndex(0)
                    self.tableWidget.setCellWidget(i,j,comboItem)
        self.calcTotalDuration()
        
        
    
    def calcTotalDuration(self):
        total = 0
        numRows = self.numRows
        for i in range(numRows):
            dur = int(self.tableWidget.item(i,4).text())
            total = total + dur
        self.totaltime.setText(str(total))
                
                
                
    #save query result to an excel    
    def saveExcel(self):
        path = QtGui.QFileDialog.getSaveFileName(caption = 'Save Excel',filter="Excel File (*.xls *.xlsx)")
        if path is not None:
            curTable = []
            curTable.append(tablehead)
            rows = self.numRows
            cols = self.numCols
            for i in range(0,rows):
                temp = []
                for j in range(0,cols):
                    item = self.tableWidget.item(i,j)
                    if j!=2:                 
                        t = item.text()
                        temp.append(unicode(t))
                    else:
                        comboItem = self.tableWidget.cellWidget(i,j)
                        t = comboItem.currentText()
                        temp.append(unicode(t))
                curTable.append(temp)        
            #catch error if IOError
            error = excelUtility.exportToExcel(path,curTable)
            if isinstance(error,IOError):
                messagebox = QtGui.QMessageBox(2,QtCore.QString(u'错误'),QtCore.QString(u'保存文件失败，请检查文件名称或是否处于打开状态！'),QtGui.QMessageBox.Yes | QtGui.QMessageBox.Cancel)
                messagebox.exec_()    
            if error == 1:
                messagebox = QtGui.QMessageBox(1,QtCore.QString(u''),QtCore.QString(u'文件保存成功！'),QtGui.QMessageBox.Yes)
                messagebox.exec_() 
        else:
            messagebox = QtGui.QMessageBox(2,QtCore.QString(u'错误'),QtCore.QString(u'未指定文件保存路径！'),QtGui.QMessageBox.Yes | QtGui.QMessageBox.Cancel)
            messagebox.exec_()                
        
                
            
    def updateQuery(self):
        self.updateSignal.emit()


        
    def getTableData(self):
        curTable = []
        rows = self.numRows
        cols = self.numCols
        for i in range(rows):
            temp = []
            for j in range(cols):
                if j!=2:
                    value = self.tableWidget.item(i,j).text()
                    temp.append(unicode(value))
                else:
                    value = self.tableWidget.cellWidget(i,j).currentText()
                    temp.append(unicode(value))
            curTable.append(temp)
        return curTable
    
        


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    table = Ui_QueryTable()
    table.show()
    app.exec_()