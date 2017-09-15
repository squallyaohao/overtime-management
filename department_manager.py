#coding=utf-8
#this file define the actual interface of the program and internal actions and slots

import sys,os,os.path
from PyQt4 import QtCore
from PyQt4 import QtGui
from ui_department_manager import Ui_MainWindow
from ui_querytable import Ui_QueryTable
import xml.etree.ElementInclude as ET
import department as department
import member
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
        self.project_start_date.setDate(curDate)
        self.project_end_date.setDate(curDate)
        self.subproject_start_date.setDate(curDate)
        self.subproject_end_date.setDate(curDate)
        self.task_start_date.setDate(curDate)
        self.task_end_date.setDate(curDate)
        self.projectDict = {}
        self.subprojectDict = {}
        self.tasksDict = {}
        self.allMembers = {}
        self.getAllProject()
        self.getAllSubproject()
        self.getAllTask()
        self.getAllMembers()
        #intialize all widgets
        self.drawList('project_list',self.projectDict)
        self.drawList('member_list',self.allMembers)
        self.drawComboBox('query_member',self.allMembers)
        self.drawComboBox('query_project',self.projectDict.keys())
        self.query_overtime_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        #set up connections
        self.setConnections()
        
        
    def getAllProject(self):
        self.projectDict = self.department.getProjectsFromServer()

        
    def getAllSubproject(self):
        self.subprojectDict = self.department.getSubprojectFromServer()

        
    def getAllTask(self):
        self.tasksDict = self.department.getTasksFromeServer()

        
    def getAllMembers(self):
        self.allMembers = self.department.getMembersFromServer()
            
        
        
    def setConnections(self):
        self.connect(self.dep_edit,QtCore.SIGNAL('clicked()'),self.editDepartment)
        self.connect(self.dep_line,QtCore.SIGNAL('currentIndexChanged(int)'),self.confirmDepartment)
        
        self.connect(self.add_project_btn,QtCore.SIGNAL('clicked()'),self.addProject)
        self.connect(self.project_name,QtCore.SIGNAL('returnPressed()'),self.addProject)
        self.connect(self.add_subproject_btn,QtCore.SIGNAL('clicked()'),self.addSubproject)
        self.connect(self.subproject_name,QtCore.SIGNAL('returnPressed()'),self.addSubproject)
        self.connect(self.add_task_btn,QtCore.SIGNAL('clicked()'),self.addTask)
        self.connect(self.task_name,QtCore.SIGNAL('returnPressed()'),self.addTask)
        
        self.connect(self.delete_project_btn,QtCore.SIGNAL('clicked()'),self.deleteProject)  
        self.connect(self.delete_subproject_btn,QtCore.SIGNAL('clicked()'),self.deleteSubproject)
        self.connect(self.delete_task_btn,QtCore.SIGNAL('clicked()'),self.deleteTask)
        
        
        self.connect(self.add_member_btn,QtCore.SIGNAL('clicked()'),self.addMember)        
        self.connect(self.query,QtCore.SIGNAL('clicked()'),self.showQueryResult)
        self.connect(self.save_excel,QtCore.SIGNAL('clicked()'),self.saveExcel)
        
        
        self.project_list.itemClicked.connect(self.showProjectInfo)
        self.subproject_list.itemClicked.connect(self.showSubprojectInfo)
        self.task_list.itemClicked.connect(self.showTaskInfo)
        self.project_list.itemClicked.connect(self.showSubproject)
        self.subproject_list.itemClicked.connect(self.showTasks)
        self.query_project.currentIndexChanged.connect(self.showSubprojectComobox)
        
        #self.connect(self.project_list,QtCore.SIGNAL('doubleClicked()'),self.showSubproject)
 
        
    def editDepartment(self):
        self.dep_line.setEnabled(True)
        
        
    def confirmDepartment(self):
        index = self.dep_line.currentIndex()
        self.department.setDepName(index)
        self.dep_line.setEnabled(False)
        
    
    def addProject(self):
        project = unicode(self.project_name.text())
        project_start_date = unicode(self.project_start_date.text())
        project_end_date = unicode(self.project_end_date.text())
        project_subprojects = ''
        project_desc = unicode(self.project_desc.toPlainText())
        if project not in self.projectDict.keys() and project is not None:
            project_vars = [project,project_start_date,project_end_date,project_subprojects,project_desc]
            newProjectDict = self.department.addProject(project_vars)
            if newProjectDict:
                newItem = QtGui.QListWidgetItem(project)
                self.project_list.addItem(newItem)
                self.projectDict[unicode(project)]=newProjectDict      
                self.project_name.setText('')



    def addSubproject(self):
        curProjectItem = self.project_list.currentItem()
        subproject = unicode(self.subproject_name.text())
        subproject_category = unicode(self.subproject_category.currentText())
        subproject_start_date = unicode(self.subproject_start_date.text())
        subproject_end_date = unicode(self.subproject_end_date.text())
        subproject_tasks = ''
        subproject_desc = unicode(self.subproject_desc.toPlainText())
        if curProjectItem is not None :
            curProject = curProjectItem.text()
            subproject_list = self.projectDict[unicode(curProject)][u'subprojects'].split(';')
            if (subproject is not None) and (subproject not in subproject_list):
                subproject_vars = [subproject,subproject_category,unicode(curProject),subproject_start_date,subproject_end_date,subproject_tasks,subproject_desc]
                newSubprojectDict = self.department.addSubproject(subproject_vars)
                if newSubprojectDict:
                    self.subproject_name.setText('')
                    self.subprojectDict[subproject] = newSubprojectDict
                    self.projectDict[unicode(curProject)][u'subprojects'] = self.projectDict[unicode(curProject)][u'subprojects'] + subproject + ";"
                    self.department.updateServer(table=u'project', varsList=[(u'subprojects',self.projectDict[unicode(curProject)][u'subprojects'])], 
                                                conditionsList=[(u'project',unicode(curProject))])
                    self.showSubproject()
                    
            
                
    def addTask(self):
        task = unicode(self.task_name.text())
        department = depdict[self.dep_line.currentIndex()].decode('utf-8')
        curProjectItem = self.project_list.currentItem()
        curSubprojectItem = self.subproject_list.currentItem()
        task_start_date = unicode(self.task_start_date.text())
        task_finish_date = unicode(self.task_end_date.text())
        progress = str(0)
        membersList = ''
        task_description = unicode(self.task_description.toPlainText())
        if curProjectItem is not None and curSubprojectItem is not None:
            curProject = curProjectItem.text()
            curSubproject = curSubprojectItem.text()
            tasks_list = self.subprojectDict[unicode(curSubproject)]['tasks'].split(';')
            if task is not None and task not in tasks_list:
                task_vars = [task,department,unicode(curProject),unicode(curSubproject),task_start_date,task_finish_date,progress,membersList,task_description]
                newTaskDict = self.department.addTask(task_vars)
                if newTaskDict:
                    self.task_name.setText('')
                    self.tasksDict[task] = newTaskDict
                    self.subprojectDict[unicode(curSubproject)][u'tasks'] = self.subprojectDict[unicode(curSubproject)][u'tasks'] + task + ";"
                    self.department.updateServer(table=u'subproject',varsList = [(u'tasks',self.subprojectDict[unicode(curSubproject)]['tasks'])],
                                                 conditionsList = [(u'subproject',unicode(curSubproject))])
                    self.showTasks()



    def addMember(self):
        newMemberName = self.member_name_line.text()
        newMemberTitle = self.member_title_line.text()
        memberId = '0'
        if newMemberName is not None and newMemberTitle is not None and unicode(newMemberName) not in self.allMembers.keys():
            member = [unicode(newMemberName),memberId,depdict[self.dep].decode('utf-8'),unicode(newMemberTitle)]
            newMemberDict = self.department.addMember(member)
            if newMemberDict:
                newItem = QtGui.QListWidgetItem(newMemberName)
                self.member_list.addItem(newItem)
                self.member_name_line.setText('')
                self.member_title_line.setText('')
                self.allMembers[unicode(newMemberName)] = newMemberDict

        
    
    
    def deleteProject(self):
        curProjectItem = self.project_list.currentItem()
        curRow = self.project_list.currentRow()
        if curProjectItem is not None:
            project = curProjectItem.text()
            projectdict = {}
            projectdict['project']=unicode(project)
            success = self.department.deleteProject(projectdict)
            if success:
                self.project_list.takeItem(curRow)
                self.subproject_list.clear()
                self.task_list.clear()
                self.getAllProject()
                self.getAllSubproject()
                self.getAllTask()
                self.showSubproject()
                self.showTasks()
 
 
    
    def deleteSubproject(self):
        curSubprojectItem = self.subproject_list.currentItem()
        curRow = self.subproject_list.currentRow()
        if curSubprojectItem is not None:
            curSubproject = curSubprojectItem.text()
            subprojectdict = {}
            subprojectdict['subproject'] = unicode(curSubproject)
            project = self.subprojectDict[unicode(curSubproject)]['project']
            success = self.department.deleteSubproject(subprojectdict,project)
            if success:
                self.subproject_list.takeItem(curRow)
                self.task_list.clear()
                self.getAllProject()
                self.getAllSubproject()
                self.getAllTask()
                self.showSubproject()
                self.showTasks()
                
    
    def deleteTask(self):
        curTaskItem = self.task_list.currentItem()
        curRow = self.task_list.currentRow()
        if curTaskItem is not None:
            curTask = curTaskItem.text()
            taskDict = {}
            taskDict['task'] = unicode(curTask)
            subproject = self.tasksDict[unicode(curTask)]['subproject']
            success = self.department.deleteTask(taskDict,subproject)
            if success:
                self.task_list.takeItem(curRow)
                self.getAllProject()
                self.getAllSubproject()
                self.getAllTask()
                self.showSubproject()
                self.showTasks()
 
            
            
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
        
            
    

    def showSubproject(self):
        currentProjectItem = self.project_list.currentItem()
        if currentProjectItem is not None:
            currentProject = currentProjectItem.text()
            subproject_list = self.projectDict[unicode(currentProject)][u'subprojects'].split(';')[:-1]
            self.drawList('subproject_list',subproject_list)
        else:
            self.subproject_list.clear()
        self.showTasks()

        
    def showTasks(self):
        currentSubprojectItem = self.subproject_list.currentItem()
        if currentSubprojectItem is not None:
            currentSubproject = currentSubprojectItem.text()
            tasks_list = self.subprojectDict[unicode(currentSubproject)]['tasks']
            if len(tasks_list)>0:
                tasks_list = tasks_list.split(';')[:-1]
                self.drawList('task_list',tasks_list)
            else:
                self.task_list.clear()
        else:
            self.task_list.clear()

        
    def showSubprojectComobox(self):
        curProject = self.query_project.currentText()
        if curProject != '*':
            curSubproject = self.projectDict[unicode(curProject)][u'subprojects'].split(';')[:-1]
            self.drawComboBox('query_subproject',curSubproject)      
        else:
            self.drawComboBox('query_subproject',[])    

    

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
                
                
                
    def showProjectInfo(self):
        pass
    
    
    
    def showSubprojectInfo(self):
        pass
    
    

    def showTaskInfo(self):
        curItem = self.task_list.currentItem()
        if curItem is not None:
            text = curItem.text()
            temp = self.tasksDict[unicode(text)]
            start_date = temp['start_date']
            end_date = temp['finish_date']
            desc = temp['description']
            self.task_start_date.setDate(QtCore.QDate(start_date))
            
    
                
    def drawTable(self,tablename='',tableheader=[],tablelist=[]):
        tableWidget = self.findChild(QtGui.QTableWidget,tablename)
        numRows = len(tablelist)
        numCols = len(tableheader)
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


            

        
        
    

        

        
        
    

        
        
        
        
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    path = sys.argv[0]
    cwd = os.path.dirname(path)
    xmlPath = cwd + '''\department.xml'''
    print xmlPath
    manager = DepartmentManager(xmlpath=xmlPath)
    manager.show()
    app.exec_()