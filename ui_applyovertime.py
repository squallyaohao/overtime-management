#coding=utf-8
#this file define the actual interface of the program and internal actions and slots

import sys,os,os.path
from PyQt4 import QtCore
from PyQt4 import QtGui
from ui_membermainwindow import Ui_MemberMainWindow
from ui_querytable import Ui_QueryTable
import xml.etree.ElementInclude as ET
import department,member
import pandas as pd
import excelUtility



class UI_ApplyOvertime(Ui_MemberMainWindow):
    def __init__(self,parent=None,xmlpath=''):
        super(Ui_MemberMainWindow,self).__init__(parent)
        self.setupUi(self)
        
        self.member = member.Member(xmlpath)
        name = self.member.getName()
        dep  = self.member.getDepartment()
        self.name_line.setText(name)
        self.dep_line.setCurrentIndex(dep)
        curDate = QtCore.QDate.currentDate()
        self.apply_date.setDate(curDate)
        self.query_fromdate.setDate(curDate)
        self.query_todate.setDate(curDate)
        self.apply_date.setEnabled(False)
    
        self.member.getProjectsFromServer(table='project')
        projectList = self.member.getAllProjects()
        for pro in projectList:
            self.apply_project.addItem(pro)
            self.query_project.addItem(pro)
        self.tabWidget.setCurrentIndex(0)
        
        self.result_window = Ui_QueryTable()
        
        self.setConnections()
        

        
    def setConnections(self):    
        self.connect(self.name_edit,QtCore.SIGNAL("clicked()"),self.editName)
        self.connect(self.name_line,QtCore.SIGNAL("returnPressed()"),self.confirmName)
        self.connect(self.dep_edit,QtCore.SIGNAL('clicked()'),self.editDepartment)
        self.connect(self.dep_line,QtCore.SIGNAL('currentIndexChanged(int)'),self.confirmDepartment)
        self.connect(self.apply_overtime,QtCore.SIGNAL('clicked()'),self.applyForOvertime)
        self.connect(self.query,QtCore.SIGNAL('clicked()'),self.showQueryResult)
        self.result_window.updateSignal.connect(self.updateServer)
        
        
        
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
        des = unicode(self.desc.toPlainText())
        print des
        self.member.applyOvertime('overtime', date, duration, project, 
                                 meal,des )
        
    
    def showQueryResult(self):
        query_dates = (unicode(self.query_fromdate.text()),unicode(self.query_todate.text()))
        query_project = unicode(self.query_project.currentText())
        result = self.member.queryOvertime(table='overtime', date=query_dates, project=query_project)
        projectlist = self.member.getAllProjects()
        if len(result)>0:
            self.result_window.drawTable(result,projectlist)
            self.result_window.show()
        else:
            messagebox = QtGui.QMessageBox(2,QtCore.QString(u'提示'),QtCore.QString(u'没有查询到相关记录'),QtGui.QMessageBox.Yes | QtGui.QMessageBox.Cancel)
            messagebox.exec_()
            

    def updateServer(self):
        curTable = self.result_window.getTableData()
        success  = self.member.updateServer('overtime',curTable)
        if success:
            messagebox = QtGui.QMessageBox(2,QtCore.QString(u'提示'),QtCore.QString(u'加班记录已更新成功！'),QtGui.QMessageBox.Yes | QtGui.QMessageBox.Cancel)
            messagebox.exec_()
            
                            

if __name__ =='__main__':
    app = QtGui.QApplication(sys.argv) 
    #app.setStyle(QtGui.QStyleFactory.create('Plasitc'))
    path = sys.argv[0]
    cwd = os.path.dirname(path)
    xmlPath = cwd + '''\member.xml'''
    ui = UI_ApplyOvertime(xmlpath = xmlPath)
    ui.show()
sys.exit(app.exec_()) 