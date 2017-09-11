#coding=utf-8
#this file define the actual interface of the program and internal actions and slots

import sys,os,os.path
from PyQt4 import QtCore
from PyQt4 import QtGui
from ui_mainwindow import Ui_MainWindow
from ui_querytable import Ui_QueryTable
import xml.etree.ElementInclude as ET
import department,member
import pandas as pd



class UI_ApplyOvertime(Ui_MainWindow):
    def __init__(self,parent=None,xmlpath=''):
        super(Ui_MainWindow,self).__init__(parent)       
        self.setupUi(self)
        
        self.member = member.Member(xmlpath)
        name = self.member.getName()
        dep  = self.member.getDepartment()
        self.name_line.setText(name)
        self.dep_line.setCurrentIndex(dep)
        self.setConnections()
        self.member.updateProjects(table='project')
        projectList = self.member.getAllProjects()
        for pro in projectList:
            self.apply_project.addItem(pro)
                   
        
    def setConnections(self):    
        self.connect(self.name_edit,QtCore.SIGNAL("clicked()"),self.editName)
        self.connect(self.name_line,QtCore.SIGNAL("returnPressed()"),self.confirmName)
        self.connect(self.dep_edit,QtCore.SIGNAL('clicked()'),self.editDepartment)
        self.connect(self.dep_line,QtCore.SIGNAL('currentIndexChanged(int)'),self.confirmDepartment)
        self.connect(self.apply_overtime,QtCore.SIGNAL('clicked()'),self.applyForOvertime)
        self.connect(self.query,QtCore.SIGNAL('clicked()'),self.showQueryResult)
        
        
        
    def editName(self):
        self.name_line.setEnabled(True)
        
        
    def confirmName(self):
        name = unicode(self.name_line.text())
        self.member.setName(name)
        self.name_line.setEnabled(False)
        
    
    def editDepartment(self):
        self.dep_line.setEnabled(True)
        
    
    def confirmDepartment(self):
        index = self.dep_line.currentIndex()
        self.member.setDepartment(index)
        self.dep_line.setEnabled(False)
        
        
    def applyForOvertime(self):
        date = unicode(self.apply_date.text())
        duration = unicode(self.apply_duration.text())
        meal = unicode(self.apply_meal.text())
        project = unicode(self.apply_project.currentText())
        self.member.applyOvertime('overtime', date, duration, project, 
                                 meal, )
        
    
    def showQueryResult(self):
        query_dates = (unicode(self.query_fromdate.text()),unicode(self.query_todate.text()))
        query_project = unicode(self.query_project.currentText())
        result = self.member.queryOvertime(table='overtime', date=query_dates, project=query_project)
        if result is not None:
            numRows = len(result)
            numCols = len(result[0])
            self.result_window = Ui_QueryTable()
            self.result_window.tableWidget.setRowCount(numRows)
            self.result_window.tableWidget.setColumnCount(numCols)
            self.result_window.tableWidget.setHorizontalHeaderLabels(['Date','Name','Project','Duration','Meal'])
            self.result_window.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
            textFont = QtGui.QFont('Hei',11)  

            for i,row in enumerate(result):
                for j,col in enumerate(row):
                    item = QtGui.QTableWidgetItem(unicode(col))
                    item.setTextAlignment(0x0004|0x0080	)
                    item.setFont(textFont)
                    self.result_window.tableWidget.setItem(i,j, item)
            
        self.result_window.show()
                            
    
        
    
        

if __name__ =='__main__':
    app = QtGui.QApplication(sys.argv) 
    path = sys.argv[0]
    cwd = os.path.dirname(path)
    xmlPath = cwd + '''\member.xml'''
    print xmlPath
    ui = UI_ApplyOvertime(xmlpath = xmlPath)
    ui.show()
sys.exit(app.exec_()) 