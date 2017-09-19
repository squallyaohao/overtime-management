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
        #self.department.projectDict = {}
        #self.department.subprojectDict = {}
        #self.department.taskDict = {}
        #self.department.allMembers = {}
        #self.getAllProject()
        #self.getAllSubproject()
        #self.getAllTask()
        #self.getAllMembers()
        #self.buildTreeHierarchy()
        self.tree_project.setColumnCount(1)
        self.tree_project.setHeaderLabel(u'项目名称')
        self.drawProjectTree()
        self.drawMemberList()
        memberIdList = self.department.allMembers.keys()
        memberIdList.sort()
        memberList = []
        for memberId in memberIdList:
            memberList.append(self.department.allMembers[memberId][u'姓名'])
        self.drawComboBox('query_member',memberList)
        projectIdList = self.department.projectDict.keys()
        projectIdList.sort()
        projectList = []
        for projectId in projectIdList:
            projectList.append(self.department.projectDict[projectId][u'项目名称'])
        self.drawComboBox('query_project', projectList)
        self.query_overtime_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        #set up connections
        self.setConnections()
        
        
    #def getAllProject(self):
        #self.department.projectDict = self.department.getProjectsFromServer()

        
    #def getAllSubproject(self):
        #self.department.subprojectDict = self.department.getSubprojectFromServer()

        
    #def getAllTask(self):
        #self.department.taskDict = self.department.getTaskFromeServer()

        
    #def getAllMembers(self):
        #self.department.allMembers = self.department.getMembersFromServer()
        
        

    #def buildTreeHierarchy(self):
        #self.department.hierTree = self.department.buildTreeHierarchy()

        
    #def getHierTree(self):
        #self.department.hierTree = self.department.getHierTree()
                 
        
    def setConnections(self):
        self.connect(self.dep_edit,QtCore.SIGNAL('clicked()'),self.editDepartment)
        self.connect(self.dep_line,QtCore.SIGNAL('currentIndexChanged(int)'),self.confirmDepartment)
        self.connect(self.query_project,QtCore.SIGNAL('currentIndexChanged(int)'),self.showSubprojectComobox)
        
        self.connect(self.btn_add_project,QtCore.SIGNAL('clicked()'),self.addProject)
        self.connect(self.btn_add_subproject,QtCore.SIGNAL('clicked()'),self.addSubproject)
        self.connect(self.btn_add_task,QtCore.SIGNAL('clicked()'),self.addTask)
        self.connect(self.delete_2,QtCore.SIGNAL('clicked()'),self.delete)
        self.connect(self.btn_save,QtCore.SIGNAL('clicked()'),self.saveTable)
        self.connect(self.btn_exportExcel,QtCore.SIGNAL('clicked()'),self.exportProjectToExcel)
                
        self.connect(self.add_member_btn,QtCore.SIGNAL('clicked()'),self.addMember)        
        self.connect(self.query,QtCore.SIGNAL('clicked()'),self.showQueryResult)
        self.connect(self.save_excel,QtCore.SIGNAL('clicked()'),self.exportOvertimeToExcel)        
        self.tree_project.itemDoubleClicked.connect(self.showInfo)
        

        
 
        
    def editDepartment(self):
        self.dep_line.setEnabled(True)
        
        
    def confirmDepartment(self):
        index = self.dep_line.currentIndex()
        self.department.setDepName(index)
        self.dep_line.setEnabled(False)
        
    
    def addProject(self):
        tempDict,ok = newProjectDialog.newProject()       
        if tempDict[u'项目名称'] != '':
            tempDict[u'完成度'] = str(0)
            tempDict[u'项目状态'] = u'进行中'
            success = self.department.addProject(tempDict)
            if success[0] == 1:
                root = self.tree_project.topLevelItem(0)
                newItem = newTreeWidgetItem(root)
                newItem.setText(0,success[1][u'项目名称'])
                newItem.setLevel(1)
                newItem.setId(success[1][u'项目编号'])
                self.getHierTree()
            elif success[0] == 2:
                print '添加项目失败'
            else :
                print '该项目已存在'
            


    def addSubproject(self):
        tempDict,projectId,ok = newSubprojectDialog.newSubproject(projectDict=self.department.projectDict)
        subproject = tempDict[u'展项名称']
        project = tempDict[u'项目名称']
        tempDict[u'完成度'] = str(0)
        tempDict[u'展项状态'] = u'进行中'        
        if project != '' and subproject != '':
            success = self.department.addSubproject(tempDict,projectId)
            if success[0] == 1:
                itemIter = QtGui.QTreeWidgetItemIterator(self.tree_project)
                while itemIter.value() is not None:
                    if unicode(itemIter.value().text(0)) == project:
                        newItem = newTreeWidgetItem(itemIter.value())
                        newItem.setText(0,success[1][u'展项名称'])
                        newItem.setLevel(2)
                        newItem.setId(success[1][u'展项编号'])
                        self.getHierTree()
                        self.showSubprojectInfo(projectId)
                        break
                    else:
                        itemIter = itemIter.__iadd__(1)
            elif success[0] == 2:
                print '添加展项失败'
            else:
                print '展项已存在'            
                    
            
                
    def addTask(self):
        tempDict,projectId,subprojectId,ok = newTaskDialog.newTask(projectDict=self.department.projectDict,subprojectDict=self.department.subprojectDict)
        task = tempDict[u'任务名称']
        project = tempDict[u'项目名称']
        subproject = tempDict[u'展项名称']
        tempDict[u'完成度'] = str(0)
        tempDict[u'任务状态'] = u'进行中'
        tempDict[u'参与人员'] = ''
        if project != '' and subproject != '' and task != '':
            success = self.department.addTask(tempDict,projectId,subprojectId)
            if success[0] == 1:
                itemIter = QtGui.QTreeWidgetItemIterator(self.tree_project)
                while itemIter.value() is not None:
                    if unicode(itemIter.value().text(0)) == subproject:
                        newItem = newTreeWidgetItem(itemIter.value())
                        newItem.setText(0,success[1][u'任务名称'])
                        newItem.setLevel(3)
                        newItem.setId(success[1][u'任务编号'])
                        self.showTaskInfo(subprojectId)
                        break
                    else:
                        itemIter = itemIter.__iadd__(1)
            elif success[0] == 2:
                print '添加任务失败'
            else:
                print '任务已存在'
                    



    def addMember(self):
        newMemberName = self.member_name_line.text()
        newMemberTitle = self.member_title_line.text()
        if newMemberName != '' and newMemberTitle !='':
            memberDict = {}
            memberDict[u'姓名'] = unicode(newMemberName)
            memberDict[u'职务'] = unicode(newMemberTitle)
            memberDict[u'部门'] = depdict[self.dep]
            success = self.department.addMember(memberDict)
            if success[0] == 1:
                newItem = QtGui.QListWidgetItem(newMemberName)
                self.member_list.addItem(newItem)
                self.member_name_line.setText('')
                self.member_title_line.setText('')
                self.drawMemberList
            else :
                print '添加成员失败'
        else:
            print '该成员已存在'

        
    
    def delete(self):
        curSelected = self.tree_project.currentItem()
        parentItem = curSelected.parent()
        if parentItem is not None:
            itemId = curSelected.getId()
            level = curSelected.getLevel()
            parentItem.removeChild(curSelected)
            if level == 1:
                self.department.deleteProject(itemId)
            elif level == 2:
                self.department.deleteSubproject(itemId)
            else:
                self.department.deleteTask(itemId)
            
    
    
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
            project = self.department.subprojectDict[unicode(curSubproject)]['project']
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
            subproject = self.department.taskDict[unicode(curTask)]['subproject']
            success = self.department.deleteTask(taskDict,subproject)
            if success:
                self.task_list.takeItem(curRow)
                self.getAllProject()
                self.getAllSubproject()
                self.getAllTask()
                self.showSubproject()
                self.showTasks()
 
 
 
    def drawMemberList(self):
        for member in self.department.allMembers.keys():
            name = self.department.allMembers[member][u'姓名']
            item = QtGui.QListWidgetItem(name)
            self.member_list.addItem(item)
 
            
            
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
    


    def exportProjectToExcel(self):
        self.saveExcel(self.table_prodetail)
    
    
    def exportOvertimeToExcel(self):
        self.saveExcel(self.query_overtime_table)


    def saveExcel(self,table):
        #table = self.findChild(QtGui.QTableWidget, tableName)
        path = QtGui.QFileDialog.getSaveFileName(caption = 'Save Excel',filter="Excel File (*.xls *.xlsx)")
        if path is not None:
            curTable = []
            rows = table.rowCount()
            cols = table.columnCount()
            labels = []
            for col in range(cols):
                item = table.horizontalHeaderItem(col)
                labels.append(unicode(item.text()))
            curTable.append(labels)
            for i in range(0,rows):
                temp = []
                for j in range(0,cols):
                    item = table.item(i,j)               
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
        projectIdList = self.department.hierTree.keys()
        projectIdList.sort()
        for projectId in projectIdList:
            projectItem = newTreeWidgetItem(root)
            projectItem.setText(0,self.department.projectDict[projectId][u'项目名称'])
            projectItem.setLevel(1)
            projectItem.setId(projectId)
            subproIdList = self.department.hierTree[projectId].keys()
            subproIdList.sort()
            for subproId in subproIdList:            
                subprojectItem =  newTreeWidgetItem(projectItem)
                subprojectItem.setText(0,self.department.subprojectDict[subproId][u'展项名称'])
                subprojectItem.setLevel(2)
                subprojectItem.setId(subproId)
                taskList = self.department.hierTree[projectId][subproId]
                for task in taskList:
                    taskItem = newTreeWidgetItem(subprojectItem)
                    taskItem.setText(0,self.department.taskDict[task][u'任务名称'])
                    taskItem.setLevel(3)
                    taskItem.setId(task)
        self.tree_project.addTopLevelItem(root)

            

        
    def showSubprojectComobox(self):
        curProject = self.query_project.currentText()
        if curProject != '*':
            curProjectId = ''
            for projectId in self.department.projectDict.keys():
                if self.department.projectDict[projectId][u'项目名称'] == unicode(curProject):
                    curProjectId = projectId
                    break
            subprojectIdList = self.department.hierTree[curProjectId].keys()
            subprojectList = []
            for subprojectId in subprojectIdList:
                subprojectList.append(self.department.subprojectDict[subprojectId][u'展项名称'])
                self.drawComboBox('query_subproject',subprojectList)
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
            projectId = item.getId()
            self.showSubprojectInfo(projectId)
        elif level == 2:
            subprojectId = item.getId()
            self.showTaskInfo(subprojectId)



                
    def showProjectInfo(self):
        self.label_tables.setText(u'项目详情')
        self.table_prodetail.clear()        
        rows = len(self.department.projectDict.keys())
        self.table_prodetail.setTableName(u'project')
        self.table_prodetail.setRowCount(rows)
        self.table_prodetail.setColumnCount(len(self.department.proTabHeader))
        self.table_prodetail.setHorizontalHeaderLabels(self.department.proTabHeader)
        projectList = self.department.projectDict.keys()
        projectList.sort()
        for i,row in enumerate(projectList):
            for j,col in enumerate(self.department.proTabHeader):
                item = QtGui.QTableWidgetItem(unicode(self.department.projectDict[row][col]))
                item.setTextAlignment(QtCore.Qt.AlignHCenter)
                if j==0:
                    item.setFlags(QtCore.Qt.ItemIsEditable)                
                self.table_prodetail.setItem(i,j,item)

    
    
    
    def showSubprojectInfo(self,projectId):
        print projectId
        projectName = self.department.projectDict[projectId][u'项目名称']
        self.label_tables.setText(projectName +u' 展项详情: ')
        self.table_prodetail.clear()
        subprojectIdList = self.department.hierTree[projectId].keys()
        subprojectIdList.sort()
        rows = len(subprojectIdList)
        self.table_prodetail.setTableName(u'subproject')
        self.table_prodetail.setRowCount(rows)
        self.table_prodetail.setColumnCount(len(self.department.subproTabHeader))
        self.table_prodetail.setHorizontalHeaderLabels(self.department.subproTabHeader)        
    
        for i,row in enumerate(subprojectIdList):
            for j,col in enumerate(self.department.subproTabHeader):
                item = QtGui.QTableWidgetItem(unicode(self.department.subprojectDict[row][col]))
                item.setTextAlignment(QtCore.Qt.AlignHCenter)
                if j==0:
                    item.setFlags(QtCore.Qt.ItemIsEditable)
                self.table_prodetail.setItem(i,j,item)
 
 

    def showTaskInfo(self,subprojectId):
        subprojectName = self.department.subprojectDict[subprojectId][u'展项名称']
        self.label_tables.setText(subprojectName + u' 任务详情: ')
        self.table_prodetail.clear()
        projectId = subprojectId[0:3]
        taskIdList = self.department.hierTree[projectId][subprojectId]
        rows = len(taskIdList)
        self.table_prodetail.setTableName(u'task')
        self.table_prodetail.setRowCount(rows)
        self.table_prodetail.setColumnCount(len(self.department.taskTabHeader))
        self.table_prodetail.setHorizontalHeaderLabels(self.department.taskTabHeader)        
        for i,row in enumerate(taskIdList):
            for j,col in enumerate(self.department.taskTabHeader):
                item = QtGui.QTableWidgetItem(unicode(self.department.taskDict[row][col]))
                item.setTextAlignment(QtCore.Qt.AlignHCenter)
                if j==0:
                    item.setFlags(QtCore.Qt.ItemIsEditable)                
                self.table_prodetail.setItem(i,j,item)


    
                
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



    def saveTable(self):
        tableName = self.table_prodetail.getTableName()
        numRows = self.table_prodetail.rowCount()
        numCols = self.table_prodetail.columnCount()
        rows= []
        for i in range(numRows):
            row = []
            for j in range(numCols):
                item = self.table_prodetail.item(i,j)
                row.append(unicode(item.text()))
            rows.append(row)
        self.department.saveTable(tableName,rows)

            
        

              

class newTreeWidgetItem(QtGui.QTreeWidgetItem):
    def __init__(self,parent=None):
        super(QtGui.QTreeWidgetItem,self).__init__(parent)
        self.level = 0
        self.Id = ''
        
    def setLevel(self,level):
        self.level = level
        
    def setId(self,Id=''):
        self.Id = Id
        
    def getLevel(self):
        return self.level
        
    def getId(self):
        return self.Id




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
            projectId = QtCore.QVariant(projectDict[pro][u'项目编号'])
            self.projectCombo.addItem(projectDict[pro][u'项目名称'],projectId)
    
    @staticmethod
    def newSubproject(parent=None,projectDict={}):
        dialog = newSubprojectDialog(parent,projectDict)
        result = dialog.exec_()
        newSubprojectDict = {}
        subproject = unicode(dialog.subproject_name.text()) 
        project = unicode(dialog.projectCombo.currentText())
        index = dialog.projectCombo.currentIndex()
        subproject_start_date = unicode(dialog.start_date.text())
        subproject_end_date = unicode(dialog.finish_date.text())
        subproject_category = unicode(dialog.category.currentText())
        script = unicode(dialog.script.text())
        ani = unicode(dialog.animation.text())
        post = unicode(dialog.postproduct.text())
        software = unicode(dialog.software.text())
        hardware = unicode(dialog.hardware.text())
        subproject_desc = unicode(dialog.subproject_desc.toPlainText())
        projectId = unicode(dialog.projectCombo.itemData(index).toString())
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
        return (newSubprojectDict,projectId,result==QtGui.QDialog.Accepted)        
        
        
        

class newTaskDialog(ui_newTaskDialog.Ui_Dialog):
    def __init__(self,parent=None,projectDict={},subprojectDict={}):
        super(ui_newTaskDialog.Ui_Dialog,self).__init__()
        self.setupUi(self)
        self.projectDict = projectDict
        self.subprojectDict = subprojectDict
        projectList = self.projectDict.keys()
        for pro in projectList:
            projectId = QtCore.QVariant(self.projectDict[pro][u'项目编号'])
            self.projectCombo.addItem(projectDict[pro][u'项目名称'],projectId)
        self.showSubprojects()
        self.projectCombo.currentIndexChanged.connect(self.showSubprojects)
        
    def showSubprojects(self):
        projectIndex = self.projectCombo.currentIndex()
        projectId = unicode(self.projectCombo.itemData(projectIndex).toString())
        subprojectList = []
        for key in self.subprojectDict.keys():
            if key.startswith(projectId):
                subprojectList.append(key)
        self.subprojectCombo.clear()
        for subpro in subprojectList:
            subprojectId = QtCore.QVariant(self.subprojectDict[subpro][u'展项编号'])
            self.subprojectCombo.addItem(self.subprojectDict[subpro][u'展项名称'],subprojectId)
        
    @staticmethod
    def newTask(parent=None,projectDict={},subprojectDict={}):
        dialog = newTaskDialog(parent,projectDict,subprojectDict)
        result = dialog.exec_()
        newTaskDict = {}
        task = unicode(dialog.task_name.text())
        project = unicode(dialog.projectCombo.currentText())
        subproject = unicode(dialog.subprojectCombo.currentText())
        task_start_date = unicode(dialog.start_date.text())
        task_end_date = unicode(dialog.finish_date.text())
        task_desc = unicode(dialog.task_desc.toPlainText())
        projectIndex = dialog.projectCombo.currentIndex()
        subprojectIndex = dialog.subprojectCombo.currentIndex()
        projectId = unicode(dialog.projectCombo.itemData(projectIndex).toString())
        subprojectId = unicode(dialog.subprojectCombo.itemData(subprojectIndex).toString())
        newTaskDict[u'任务名称'] = task
        newTaskDict[u'项目名称'] = project
        newTaskDict[u'展项名称'] = subproject 
        newTaskDict[u'起始时间'] = task_start_date
        newTaskDict[u'结束时间'] = task_end_date
        newTaskDict[u'任务说明'] = task_desc
        print projectId
        print subprojectId
        return (newTaskDict,projectId,subprojectId,result==QtGui.QDialog.Accepted)
        
        
                
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    path = sys.argv[0]
    cwd = os.path.dirname(path)
    xmlPath = cwd + '''\department.xml'''
    manager = DepartmentManager(xmlpath=xmlPath)
    manager.show()
    app.exec_()