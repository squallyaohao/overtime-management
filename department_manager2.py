#coding=utf-8
#this file define the actual interface of the program and internal actions and slots

import sys,os,os.path
from PyQt4 import QtCore
from PyQt4 import QtGui
from ui_department_manager2 import Ui_MainWindow
from ui_querytable import Ui_QueryTable
import xml.etree.ElementInclude as ET
import department,member
import pandas as pd
import excelUtility

overtimetablehead = [u'日期',u'姓名',u'加班项目',u'加班展项',u'加班时长',u'加班餐',u'加班描述']
depdict = {0:'三维动画',1:'投标动画',2:'二维动画',3:'平面设计',4:'编导'}


class DepartmentManager(Ui_MainWindow):
    def __init__(self,parent=None,xmlpath=''):
        super(Ui_MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.department = department.Department(xmlpath)
        self.dep = self.department.getDepName()
        self.dep_line.setCurrentIndex(self.dep)
        self.tabWidget.setCurrentIndex(0)
        curDate = QtCore.QDate.currentDate()
        self.query_fromdate.setDate(curDate)
        self.query_todate.setDate(curDate)
        self.projectDict = {}
        self.allMembers = []
        self.getAllProject()
        self.getAllMembers()
        #intialize all widgets
        self.drawList('project_list',self.projectDict)
        self.drawList('member_list',self.allMembers)
        self.drawComboBox('query_member',self.allMembers)
        self.drawComboBox('query_project',self.projectDict.keys())
        self.query_overtime_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        #set up connections
        self.setConnections()
        
        
        
    def setConnections(self):
        self.connect(self.dep_edit,QtCore.SIGNAL('clicked()'),self.editDepartment)
        self.connect(self.dep_line,QtCore.SIGNAL('currentIndexChanged(int)'),self.confirmDepartment)
        self.connect(self.add_project_btn,QtCore.SIGNAL('clicked()'),self.addProject)
        self.connect(self.delete_project_btn,QtCore.SIGNAL('clicked()'),self.deleteProject)
        self.connect(self.add_subproject_btn,QtCore.SIGNAL('clicked()'),self.addSubproject)
        self.connect(self.delete_subproject_btn,QtCore.SIGNAL('clicked()'),self.deleteSubproject)
        self.connect(self.project_name,QtCore.SIGNAL('returnPressed()'),self.addProject)
        self.connect(self.subproject_name,QtCore.SIGNAL('returnPressed()'),self.addSubproject)
        self.connect(self.add_member_btn,QtCore.SIGNAL('clicked()'),self.addMember)
        
        self.query_project.currentIndexChanged.connect(self.showSubprojectComobox)
        self.connect(self.query,QtCore.SIGNAL('clicked()'),self.showQueryResult)
        self.connect(self.save_excel,QtCore.SIGNAL('clicked()'),self.saveExcel)
        self.project_list.itemClicked.connect(self.showSubproject)
        #self.connect(self.project_list,QtCore.SIGNAL('doubleClicked()'),self.showSubproject)
 
        
    def editDepartment(self):
        self.dep_line.setEnabled(True)
        
        
    def confirmDepartment(self):
        index = self.dep_line.currentIndex()
        self.department.setDepName(index)
        self.dep_line.setEnabled(False)
        
    
    def addProject(self):
        project = self.project_name.text()
        if project not in self.projectDict.keys() and project is not None:
            projectdict = {}
            projectdict[unicode(project)]=''
            success = self.department.addProject(projectdict)
            if success:
                newItem = QtGui.QListWidgetItem(project)
                self.project_list.addItem(newItem)
                self.projectDict[unicode(project)]=[]            
                self.project_name.setText('')
 
 

    def addSubproject(self):
        curProjectItem = self.project_list.currentItem()
        subproject = self.subproject_name.text()
        if curProjectItem is not None :
            curProject = curProjectItem.text()
            if subproject is not None and subproject not in self.projectDict[unicode(curProject)]:            
                projectdict = {}
                projectdict[unicode(curProject)]=unicode(subproject)
                success = self.department.addProject(projectdict)
                if success:
                    newItem = QtGui.QListWidgetItem(subproject)
                    self.subproject_list.addItem(newItem)
                    self.subproject_name.setText('')
                    self.projectDict[unicode(curProject)].append(unicode(subproject))
            
                
    def addTask(self):
        pass
    
    
    def addMember(self):
        newMemberName = self.member_name_line.text()
        newMemberTitle = self.member_title_line.text()
        if newMemberName is not None and newMemberTitle is not None and unicode(newMemberName) not in self.allMembers:
            member = [unicode(newMemberName),depdict[self.dep].decode('utf-8'),unicode(newMemberTitle)]
            success = self.department.addMember(member)
            if success:
                newItem = QtGui.QListWidgetItem(newMemberName)
                self.member_list.addItem(newItem)
                self.member_name_line.setText('')
                self.allMembers.append(unicode(newMemberName))
            
            
    
    
    def deleteProject(self):
        curItem = self.project_list.currentItem()
        curRow = self.project_list.currentRow()
        print curItem
        if curItem is not None:
            project = curItem.text()
            projectdict = {}
            projectdict['project']=unicode(project)
            success = self.department.deleteProject(projectdict)
            if success:
                self.project_list.takeItem(curRow)
                self.showSubproject()
            
    
    
    
    def deleteSubproject(self):
        curProjectItem = self.project_list.currentItem()
        curSubprojectItem = self.subproject_list.currentItem()
        curSubprojectIndex = self.subproject_list.currentRow()
        if curSubprojectItem is not None:
            curProject= curProjectItem.text()
            curSubproject = curSubprojectItem.text()
            projectdict = {}
            projectdict['project'] = unicode(curProject)
            projectdict['subproject'] = unicode(curSubproject)
            success = self.department.deleteProject(projectdict)
            if success:
                self.subproject_list.takeItem(curSubprojectIndex)
                self.projectDict[unicode(curProject)].remove(unicode(curSubproject))
    
    

    def drawList(self,listname='',l={}):
        listWidget = self.findChild(QtGui.QListView,listname)        
        for key in l.keys():
            item = QtGui.QListWidgetItem(key)
            listWidget.addItem(item)

            
    def drawList(self,listname='',l=[]):
        listWidget = self.findChild(QtGui.QListView,listname) 
        listWidget.clear()
        for temp in l:
            item = QtGui.QListWidgetItem(temp)
            listWidget.addItem(item)
            
            
    def drawComboBox(self,widgetname='',l=[]):
        comboBox = self.findChild(QtGui.QComboBox,widgetname)
        comboBox.clear()
        comboBox.addItem('*')
        if len(l)>0:
            for temp in l:
                comboBox.addItem(temp)
                
                
    def drawTable(self,tablename='',tableheader=[],tablelist=[]):
        tableWidget = self.findChild(QtGui.QTableWidget,tablename)
        numRows = len(tablelist)
        numCols = len(tableheader)
        print tablelist
        tableWidget.setRowCount(numRows)
        tableWidget.setColumnCount(numCols)        
        tableWidget.setHorizontalHeaderLabels(tableheader)
        tableWidget.setColumnWidth(numCols-1,100)
        textFont = QtGui.QFont('Hei',11)
        for i,row in enumerate(tablelist):
            for j,col in enumerate(row):
                item = QtGui.QTableWidgetItem(unicode(col))
                item.setTextAlignment(0x0004|0x0080)
                item.setFont(textFont)
                tableWidget.setItem(i,j,item)


            
    def showSubproject(self):
        currentProject = self.project_list.currentItem().text()
        subproject_list = self.projectDict[unicode(currentProject)]
        self.drawList('subproject_list',subproject_list)
        
    def showSubprojectComobox(self):
        curProject = self.query_project.currentText()
        if curProject != '*':
            curSubproject = self.projectDict[unicode(curProject)]
            self.drawComboBox('query_subproject',curSubproject)      
        else:
            self.drawComboBox('query_subproject',[])
        
        
    
    def getAllProject(self):
        self.projectDict = self.department.getProjectsFromServer('project')
        
        
    def getAllMembers(self):
        self.allMembers = self.department.getAllMembersFromServer('members')
        
        
    def showQueryResult(self):
        query_member = unicode(self.query_member.currentText())
        query_fromdate = unicode(self.query_fromdate.text())
        query_todate = unicode(self.query_todate.text())
        query_project = unicode(self.query_project.currentText())
        query_subproject = unicode(self.query_subproject.currentText())
        result = self.department.queryOvertime(table='overtime', date=(query_fromdate,query_todate), member=query_member, 
                                     project=query_project,subproject=query_subproject 
                                     )
        if result is not None:
            self.drawTable(tablename='query_overtime_table',tableheader=overtimetablehead,tablelist=result)
        
        
    
    def saveExcel(self):
        path = QtGui.QFileDialog.getSaveFileName(caption = 'Save Excel',filter="Excel File (*.xls *.xlsx)")
        if path is not None:
            curTable = []
            curTable.append(overtimetablehead)
            rows = self.query_overtime_table.rowCount()
            cols = self.query_overtime_table.columnCount()
            for i in range(0,rows):
                temp = []
                for j in range(0,cols):
                    item = self.query_overtime_table.item(i,j)               
                    t = item.text()
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
        
        
        
        
        
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    path = sys.argv[0]
    cwd = os.path.dirname(path)
    xmlPath = cwd + '''\department.xml'''
    print xmlPath
    manager = DepartmentManager(xmlpath=xmlPath)
    manager.show()
    app.exec_()