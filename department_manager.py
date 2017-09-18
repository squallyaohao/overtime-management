#coding=utf-8
#this file define the actual interface of the program and internal actions and slots

import sys,os,os.path
from PyQt4 import QtCore
from PyQt4 import QtGui
from ui_department_manager3 import Ui_MainWindow
from ui_querytable import Ui_QueryTable
import xml.etree.ElementInclude as ET
import department as department
import ui_newProjectDialog,ui_newSubprojectDialog,ui_newTaskDialog
import member
import pandas as pd
import excelUtility
import datetime
from db_structure import *

overtimetablehead = [u'日期',u'姓名',u'加班项目',u'加班展项',u'加班时长',u'加班餐',u'加班描述']
depdict = {0:u'三维动画',1:u'投标动画',2:u'二维动画',3:u'平面设计',4:u'编导'}
category = {u'动画':0,u'游戏':1}


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
        self.subprojectDict = {}
        self.taskDict = {}
        self.allMembers = {}
        self.projectTree = {}
        self.getAllProject()
        self.getAllSubproject()
        self.getAllTask()
        self.getAllMembers()
        self.buildTreeHierarchy()
        self.tree_project.setColumnCount(1)
        self.tree_project.setHeaderLabel(u'项目名称')
        self.drawProjectTree()
        projectList = self.projectDict.keys()
        self.drawComboBox('query_project', projectList)
        self.query_overtime_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        #set up connections
        self.setConnections()
        
        
    def getAllProject(self):
        self.projectDict = self.department.getProjectsFromServer()

        
    def getAllSubproject(self):
        self.subprojectDict = self.department.getSubprojectFromServer()

        
    def getAllTask(self):
        self.taskDict = self.department.getTaskFromeServer()

        
    def getAllMembers(self):
        self.allMembers = self.department.getMembersFromServer()
        
        

    def buildTreeHierarchy(self):
        for task in self.taskDict.keys():
            pass
            
            
            
        
        
    def setConnections(self):
        self.connect(self.dep_edit,QtCore.SIGNAL('clicked()'),self.editDepartment)
        self.connect(self.dep_line,QtCore.SIGNAL('currentIndexChanged(int)'),self.confirmDepartment)
        self.connect(self.query_project,QtCore.SIGNAL('currentIndexChanged(int)'),self.showSubprojectComobox)
        
        self.connect(self.btn_add_project,QtCore.SIGNAL('clicked()'),self.addProject)
        self.connect(self.btn_add_subproject,QtCore.SIGNAL('clicked()'),self.addSubproject)
        self.connect(self.btn_add_task,QtCore.SIGNAL('clicked()'),self.addTask)
        
        
        self.connect(self.add_member_btn,QtCore.SIGNAL('clicked()'),self.addMember)        
        self.connect(self.query,QtCore.SIGNAL('clicked()'),self.showQueryResult)
        self.connect(self.save_excel,QtCore.SIGNAL('clicked()'),self.saveExcel)        
        self.tree_project.itemDoubleClicked.connect(self.showInfo)
        
 
        
    def editDepartment(self):
        self.dep_line.setEnabled(True)
        
        
    def confirmDepartment(self):
        index = self.dep_line.currentIndex()
        self.department.setDepName(index)
        self.dep_line.setEnabled(False)
        
    
    def addProject(self):
        tempDict,ok = newProjectDialog.newProject()       
        project_subprojects = ''
        if tempDict[u'项目名称'] not in self.projectTree.keys() and tempDict[u'项目名称'] != '':
            success = self.department.addProject(tempDict)
            if success:
                root = self.tree_project.topLevelItem(0)
                newItem = newTreeWidgetItem(root)
                newItem.setText(0,tempDict[u'项目名称'])
                newItem.setLevel(1)
                self.getAllProject()




    def addSubproject(self):
        tempDict,ok = newSubprojectDialog.newSubproject(projectDict=self.projectDict)
        subproject = tempDict[u'subproject']
        subproject_tasks = ''
        project = tempDict[u'project']
        if project != '' :
            subproject_list = self.projectDict[project][u'subprojects'].split(';')
            if (subproject != '') and (subproject not in subproject_list):
                subproject_vars = [subproject,tempDict[u'category'],project,tempDict[u'start_date'],tempDict[u'finish_date'],subproject_tasks,tempDict[u'description']]
                newSubprojectDict = self.department.addSubproject(subproject_vars)
                if newSubprojectDict:
                    self.projectDict[project][u'subprojects'] = self.projectDict[project][u'subprojects'] + subproject + ";"
                    self.department.updateServer(table=u'project', varsList=[(u'subprojects',self.projectDict[project][u'subprojects'])], 
                                                conditionsList=[(u'project',project)])
                    itemIter = QtGui.QTreeWidgetItemIterator(self.tree_project)
                    while itemIter.value() is not None:
                        if unicode(itemIter.value().text(0)) == project:
                            newItem = newTreeWidgetItem(itemIter.value())
                            newItem.setText(0,subproject)
                            newItem.setLevel(2)
                            break
                        else:
                            itemIter = itemIter.__iadd__(1)
                    self.getAllProject()
                    self.getAllSubproject()
                    self.showSubprojectInfo(project)
                    
            
                
    def addTask(self):
        tempDict,ok = newTaskDialog.newTask(projectDict=self.projectDict)
        task = tempDict[u'task']
        project = tempDict[u'project']
        subproject = tempDict[u'subproject']
        department = depdict[self.dep]
        progress = str(0.0)
        membersList = ''
        if project != '' and subproject != '':
            tasks_list = self.subprojectDict[subproject][u'tasks'].split(';')
            print tasks_list
            if task != '' and task not in tasks_list:
                task_vars = [task,department,project,subproject,tempDict[u'start_date'],tempDict[u'finish_date'],progress,membersList,tempDict[u'description']]
                print task_vars
                newTaskDict = self.department.addTask(task_vars)
                if newTaskDict:
                    self.taskDict[task] = newTaskDict
                    self.subprojectDict[subproject][u'tasks'] = self.subprojectDict[subproject][u'tasks'] + task + ";"
                    self.department.updateServer(table=u'subproject',varsList = [(u'tasks',self.subprojectDict[subproject]['tasks'])],
                                                 conditionsList = [(u'subproject',subproject)])
                    self.getAllProject()
                    self.getAllSubproject()
                    self.getAllTask()
                    self.showTaskInfo(subproject)
                    



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
            subproject = self.taskDict[unicode(curTask)]['subproject']
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
        

        


    def drawProjectTree(self):
        root = newTreeWidgetItem(self.tree_project)
        root.setText(0,u'全部项目')
        root.setLevel(0)
        for project in self.projectDict.keys():
            projectItem = newTreeWidgetItem(root)
            projectItem.setText(0,project)
            projectItem.setLevel(1)
            #subprojectList = self.projectDict[project][u'subprojects'].split(';')
            #if subprojectList is not None:
                #for subproject in subprojectList:
                    #if subproject != '':
                        #subprojectItem =  newTreeWidgetItem(projectItem)
                        #subprojectItem.setText(0,subproject)
                        #subprojectItem.setLevel(2)
        self.tree_project.addTopLevelItem(root)

            
    


        
    def showSubprojectComobox(self):
        curProject = self.query_project.currentText()
        if curProject != '*':
            curSubproject = self.projectDict[unicode(curProject)][u'subprojects'].split(';')[:-1]
            self.drawComboBox('query_subproject',curSubproject)      
        else:
            self.drawComboBox('query_subproject',[])    

            
            
    def drawComboBox(self,widgetname='',l=[]):
        comboBox = self.findChild(QtGui.QComboBox,widgetname)
        comboBox.clear()
        comboBox.addItem('*')
        if len(l)>0:
            for temp in l:
                comboBox.addItem(temp)


                
    def showInfo(self,item):
        level = item.getLevel()
        if level == 0:
            self.showProjectInfo()
        elif level == 1:
            project = unicode(item.text(0))
            self.showSubprojectInfo(unicode(project))
        elif level == 2:
            subproject = unicode(item.text(0))
            self.showTaskInfo(unicode(subproject))

                
    def showProjectInfo(self):
        self.label_tables.setText(u'项目详情')
        self.table_prodetail.clear()
        
        rows = len(self.projectDict.keys())
        self.table_prodetail.setRowCount(rows)
        self.table_prodetail.setColumnCount(len(projectTableHeader))
        self.table_prodetail.setHorizontalHeaderLabels(projectTableHeader)
        
        for i,row in enumerate(self.projectDict.keys()):
            item = QtGui.QTableWidgetItem(row)
            self.table_prodetail.setItem(i,0, item)
            infolist = projectTableList[1:]
            for j,col in enumerate(infolist):
                item = QtGui.QTableWidgetItem(unicode(self.projectDict[row][col]))
                item.setTextAlignment(QtCore.Qt.AlignHCenter)
                self.table_prodetail.setItem(i,j+1,item)

    
    
    
    def showSubprojectInfo(self,project):
        self.label_tables.setText(u'展项详情: '+project)
        self.table_prodetail.clear()
        drawDict = {}
        for subproject in self.subprojectDict.keys():
            if self.subprojectDict[subproject][u'project'] == project:
                drawDict[subproject] = self.subprojectDict[subproject]
        rows = len(drawDict.keys())
        self.table_prodetail.setRowCount(rows)
        self.table_prodetail.setColumnCount(len(subprojectTableHeader))
        self.table_prodetail.setHorizontalHeaderLabels(subprojectTableHeader)        
    
        for i,row in enumerate(drawDict.keys()):
            item = QtGui.QTableWidgetItem(row)
            self.table_prodetail.setItem(i,0,item)
            infolist = subprojectTableList[1:]
            for j,col in enumerate(infolist):
                item = QtGui.QTableWidgetItem(unicode(drawDict[row][col]))
                item.setTextAlignment(QtCore.Qt.AlignHCenter)
                self.table_prodetail.setItem(i,j+1,item)
 
 

    def showTaskInfo(self,subproject):
        self.label_tables.setText(u'任务详情: '+subproject)
        self.table_prodetail.clear()
        drawDict = {}
        for task in self.taskDict.keys():
            if self.taskDict[task][u'subproject'] == subproject:
                drawDict[task] = self.taskDict[task]                
        rows = len(drawDict.keys())
        self.table_prodetail.setRowCount(rows)
        self.table_prodetail.setColumnCount(len(tasksTableHeader))
        self.table_prodetail.setHorizontalHeaderLabels(tasksTableHeader)        
        for i,row in enumerate(drawDict.keys()):
            item = QtGui.QTableWidgetItem(row)
            self.table_prodetail.setItem(i,0,item)
            infolist = [u'start_date',u'finish_date',u'progress',u'members',u'description']
            for j,col in enumerate(infolist):
                item = QtGui.QTableWidgetItem(unicode(drawDict[row][col]))
                item.setTextAlignment(QtCore.Qt.AlignHCenter)
                self.table_prodetail.setItem(i,j+1,item)

    
                
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




              

class newTreeWidgetItem(QtGui.QTreeWidgetItem):
    def __init__(self,parent=None):
        super(QtGui.QTreeWidgetItem,self).__init__(parent)
        self.level = 0
        
    def setLevel(self,level):
        self.level = level
        
    def getLevel(self):
        return self.level
        
    




class newProjectDialog(ui_newProjectDialog.Ui_Dialog):
    def __init__(self,parent):
        super(ui_newProjectDialog.Ui_Dialog,self).__init__(parent)
        self.setupUi(self)
        
                
    @staticmethod
    def newProject(parent=None):
        dialog = newProjectDialog(parent)
        result = dialog.exec_()
        newProjectDict = {}
        project = unicode(dialog.project_name.text()) 
        project_start_date = unicode(dialog.start_date.text())
        project_end_date = unicode(dialog.finish_date.text())
        product_pm = unicode(dialog.product_PM.text())
        script_pm = unicode(dialog.script_PM.text())
        design_pm = unicode(dialog.design_PM.text())
        flash_pm = unicode(dialog.flash_PM.text())
        ani_pm = unicode(dialog.ani_PM.text())
        post_pm = unicode(dialog.post_PM.text())
        software_pm = unicode(dialog.software_PM.text())
        hardware_pm = unicode(dialog.hardware_PM.text())
        project_desc = unicode(dialog.project_desc.toPlainText())
        newProjectDict[u'项目名称'] = project
        newProjectDict[u'起始时间'] = project_start_date
        newProjectDict[u'结束时间'] = project_end_date
        newProjectDict[u'项目说明'] = project_desc
        newProjectDict[u'项目经理'] = product_pm
        newProjectDict[u'脚本负责'] = script_pm
        newProjectDict[u'平面负责'] = design_pm
        newProjectDict[u'二维负责'] = flash_pm
        newProjectDict[u'三维负责']= ani_pm
        newProjectDict[u'后期负责'] = post_pm
        newProjectDict[u'软件负责'] = software_pm
        newProjectDict[u'硬件负责'] = hardware_pm
        return (newProjectDict,result==QtGui.QDialog.Accepted)



    
    
    
class newSubprojectDialog(ui_newSubprojectDialog.Ui_Dialog):
    def __init__(self,parent=None,projectDict={}):
        super(ui_newSubprojectDialog.Ui_Dialog,self).__init__(parent)
        self.setupUi(self)
        projectList = projectDict.keys()
        for pro in projectList:
            self.projectCombo.addItem(pro)
    
    @staticmethod
    def newSubproject(parent=None,projectDict={}):
        dialog = newSubprojectDialog(parent,projectDict)
        result = dialog.exec_()
        newSubprojectDict = {}
        subproject = unicode(dialog.subproject_name.text()) 
        project = unicode(dialog.projectCombo.currentText())
        subproject_start_date = unicode(dialog.start_date.text())
        subproject_end_date = unicode(dialog.finish_date.text())
        subproject_category = unicode(dialog.category.currentText())
        script = unicode(dialog.script.text())
        ani = unicode(dialog.animation.text())
        post = unicode(dialog.postproduct.text())
        software = unicode(dialog.software.text())
        hardware = unicode(dialog.hardware.text())
        subproject_desc = unicode(dialog.subproject_desc.toPlainText())
        newSubprojectDict[u'展项名称'] = subproject
        newSubprojectDict[u'项目名称'] = project
        newSubprojectDict[u'展项类型'] = subproject_category
        newSubprojectDict[u'起始时间'] = subproject_start_date
        newSubprojectDict[u'结束时间'] = subproject_end_date
        newSubprojectDict[u'展项说明'] = subproject_desc
        newSubprojectDict[u'脚本负责'] = script      
        newSubprojectDict[u'三维负责']= ani
        newSubprojectDict[u'后期负责'] = post
        newSubprojectDict[u'软件负责'] = software
        newSubprojectDict[u'硬件负责'] = hardware
        return (newSubprojectDict,result==QtGui.QDialog.Accepted)        
        
        
        

class newTaskDialog(ui_newTaskDialog.Ui_Dialog):
    def __init__(self,parent=None,projectDict={}):
        super(ui_newTaskDialog.Ui_Dialog,self).__init__()
        self.setupUi(self)
        self.projectDict = projectDict
        projectList = self.projectDict.keys()
        for pro in projectList:
            self.projectCombo.addItem(pro)
        self.showSubprojects()
        self.projectCombo.currentIndexChanged.connect(self.showSubprojects)
        
    def showSubprojects(self):
        project = unicode(self.projectCombo.currentText())
        subprojects = self.projectDict[project][u'subprojects'].split(';')
        self.subprojectCombo.clear()
        for subpro in subprojects:
            if subpro != '':
                self.subprojectCombo.addItem(subpro)
        
    @staticmethod
    def newTask(parent=None,projectDict={}):
        dialog = newTaskDialog(parent,projectDict)
        result = dialog.exec_()
        newTaskDict = {}
        task = unicode(dialog.task_name.text())
        project = unicode(dialog.projectCombo.currentText())
        subproject = unicode(dialog.subprojectCombo.currentText())
        task_start_date = unicode(dialog.start_date.text())
        task_end_date = unicode(dialog.finish_date.text())
        task_desc = unicode(dialog.task_desc.toPlainText())
        newTaskDict[u'任务名称'] = task
        newTaskDict[u'项目名称'] = project
        newTaskDict[u'展项名称'] =subproject 
        newTaskDict[u'起始时间'] = task_start_date
        newTaskDict[u'结束时间'] = task_end_date
        newTaskDict[u'任务说明'] = task_desc
        return (newTaskDict,result==QtGui.QDialog.Accepted)
        
        
                
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    path = sys.argv[0]
    cwd = os.path.dirname(path)
    xmlPath = cwd + '''\department.xml'''
    manager = DepartmentManager(xmlpath=xmlPath)
    manager.show()
    app.exec_()