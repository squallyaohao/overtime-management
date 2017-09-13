#coding=utf-8
#this file define the actual interface of the program and internal actions and slots

import sys,os,os.path
from PyQt4 import QtCore
from PyQt4 import QtGui
from ui_department_manager import Ui_MainWindow
from ui_querytable import Ui_QueryTable
import xml.etree.ElementInclude as ET
import department,member
import pandas as pd
import excelUtility




class DepartmentManager(Ui_MainWindow):
    def __init__(self,parent=None,xmlpath=''):
        super(Ui_MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.department = department.Department(xmlpath)
        dep = self.department.getDepName()
        self.tabWidget.setCurrentIndex(0)
        self.projectDict = {}
        self.getAllProject()
        self.drawList('project_list',self.projectDict)
        #set up connections
        self.setConnections()
        
        
        
    def setConnections(self):
        self.connect(self.dep_edit,QtCore.SIGNAL('clicked()'),self.editDepartment)
        self.connect(self.dep_line,QtCore.SIGNAL('currentIndexChanged(int)'),self.confirmDepartment)
        self.connect(self.add_project_btn,QtCore.SIGNAL('clicked()'),self.addProject)
        self.connect(self.delete_project_btn,QtCore.SIGNAL('clicked()'),self.deleteProject)
        self.connect(self.add_subproject_btn,QtCore.SIGNAL('clicked()'),self.addSubproject)
        self.connect(self.delete_subproject,QtCore.SIGNAL('clicked()'),self.deleteSubproject)
        self.project_list.itemClicked.connect(self.showSubproject)
        #self.connect(self.project_list,QtCore.SIGNAL('doubleClicked()'),self.showSubproject)
 
        
    def editDepartment(self):
        self.dep_line.setEnabled(True)
        
        
    def confirmDepartment(self):
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
        pass
    
    

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

            
    def showSubproject(self):
        currentProject = self.project_list.currentItem().text()
        subproject_list = self.projectDict[unicode(currentProject)]
        self.drawList('subproject_list',subproject_list)
    
    def getAllProject(self):
        self.projectDict = self.department.getProjectsFromServer('project')
        
        
        
        
    
    
        
        
        
        
        
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    path = sys.argv[0]
    cwd = os.path.dirname(path)
    xmlPath = cwd + '''\department.xml'''
    print xmlPath
    manager = DepartmentManager(xmlpath=xmlPath)
    manager.show()
    app.exec_()