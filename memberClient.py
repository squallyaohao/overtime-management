#coding=utf-8
#this file define the actual interface of the program and internal actions and slots

import sys,os,os.path
from PyQt4 import QtCore
from PyQt4 import QtGui
from ui_memberClient import Ui_MainWindow
#from ui_querytable import Ui_QueryTable
#import xml.etree.ElementInclude as ET
import member
import ui_newProjectDialog,ui_newSubprojectDialog,ui_newTaskDialog,ui_newDailyDialog
import excelUtility
import datetime
from db_structure import *
import random
import datetime

overtimetablehead = [u'日期',u'姓名',u'加班项目',u'加班展项',u'加班时长',u'加班餐',u'加班描述']
depDict = {1:u'三维动画',2:u'投标动画',3:u'二维动画',4:u'平面设计',5:u'编导'}
category = {u'动画':0,u'游戏':1}
monthDict = {1:u'一月',2:u'二月',3:u'三月',4:u'四月',5:u'五月',6:u'六月',7:u'七月',8:u'八月',9:u'九月',10:u'十月',11:u'十一月',12:u'十二月'}



class MemberClient(Ui_MainWindow):
    def __init__(self,parent=None):
        super(Ui_MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.member = member.Member()
        self.dep = self.member.getDepName()
        self.memberName = self.member.getMemberName()
        self.line_welcom.setText(u'你好，'+self.memberName)
        #self.dep_line.setCurrentIndex(self.dep)
        curDate = QtCore.QDate.currentDate()
        self.apply_date.setDate(curDate)
        self.query_fromdate.setDate(curDate)
        self.query_todate.setDate(curDate)
        self.tree_project.setColumnCount(1)
        self.tree_project.setHeaderLabel(u'项目名称')
        #self.assigned_task.setHeaderLabel(u'任务列表')
        self.drawProjectTree()
        #self.drawMemberList()
        
        #initialize query_member combobox
        memberIdList = self.member.allMembers.keys()
        memberIdList.sort()
        memberList = []
        for memberId in memberIdList:
            memberList.append((self.member.allMembers[memberId][u'姓名'],memberId))
        #self.drawComboBox('query_member',memberList)
        self.drawComboBox('combo_scheduleMemberFilter',memberList)
        
        #initialize query_project combobox
        projectIdList = self.member.projectDict.keys()
        projectIdList.sort()
        projectList = []
        for projectId in projectIdList:
            projectList.append((self.member.projectDict[projectId][u'项目名称'],projectId))
        self.drawComboBox('query_project', projectList)
        self.drawComboBox('apply_project', projectList)
        self.drawComboBox('combo_scheduleProjectFilter', projectList)

        self.query_overtime_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        
        #self.table_prodetail.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        #self.table_prodetail.customContextMenuRequested.connect(self.showContextMenu)
        

        self.scrollBar1 = self.period1_table.horizontalScrollBar()
        self.scrollBar2 = self.period2_table.horizontalScrollBar()
        self.scrollBar3 = self.schedule_table.horizontalScrollBar()
        self.scrollBar4 = self.schedule_table.verticalScrollBar()
        self.scrollBar5 = self.entry_list.verticalScrollBar()
        
        self.setConnections()
        
        self.setUpTables()
        self.drawEntryTree()
        self.expandItem()
        #self.collapsItem()        
        
        #self.table_memberDaily.setTableName('daily')
        
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        
                               
        
    def setConnections(self):
        #self.connect(self.dep_edit,QtCore.SIGNAL('clicked()'),self.editDepartment)
        #self.connect(self.dep_line,QtCore.SIGNAL('currentIndexChanged(int)'),self.confirmDepartment)
        self.connect(self.query_project,QtCore.SIGNAL('currentIndexChanged(int)'),self.showSubprojectComobox)
        self.connect(self.apply_project,QtCore.SIGNAL('currentIndexChanged(int)'),self.showSubprojectComobox2)
        self.connect(self.combo_scheduleProjectFilter,QtCore.SIGNAL('currentIndexChanged(int)'),self.showScheduleSubprojectComobox)
        self.connect(self.combo_scheduleSubprojectFilter,QtCore.SIGNAL('currentIndexChanged(int)'),self.drawEntryTree)
        self.connect(self.combo_scheduleMemberFilter,QtCore.SIGNAL('currentIndexChanged(int)'),self.drawEntryTree)
        self.connect(self.check_scheduleShowDetail,QtCore.SIGNAL('stateChanged(int)'),self.showScheduleDetail)

        
        #self.connect(self.btn_add_project,QtCore.SIGNAL('clicked()'),self.addProject)
        #self.connect(self.btn_add_subproject,QtCore.SIGNAL('clicked()'),self.addSubproject)
        #self.connect(self.btn_add_task,QtCore.SIGNAL('clicked()'),self.addTask)
        #self.connect(self.delete_2,QtCore.SIGNAL('clicked()'),self.delete)
        #self.connect(self.btn_save,QtCore.SIGNAL('clicked()'),self.saveTable)
        #self.connect(self.btn_exportExcel,QtCore.SIGNAL('clicked()'),self.exportProjectToExcel)
        self.connect(self.table_prodetail,QtCore.SIGNAL('myReturnPressed(int,int)'),self.tableItemChange)
        #self.connect(self.table_memberDaily,QtCore.SIGNAL('myReturnPressed(int,int)'),self.tableItemChange2)
        #self.connect(self.btn_addDaily,QtCore.SIGNAL('clicked()'),self.addNewDailyRow)
        #self.connect(self.btn_delDaily,QtCore.SIGNAL('clicked()'),self.delDaily)
                

        self.connect(self.apply_overtime,QtCore.SIGNAL('clicked()'),self.applyForOvertime)
        self.connect(self.query,QtCore.SIGNAL('clicked()'),self.queryOvertime)                
        self.connect(self.save_excel,QtCore.SIGNAL('clicked()'),self.exportOvertimeToExcel)        
        self.tree_project.itemClicked.connect(self.showInfo)
        #self.table_prodetail.itemDoubleClicked.connect(self.changeTableValue)
        #self.table_memberDaily.itemDoubleClicked.connect(self.changeTableValue2)
        self.query_overtime_table.itemDoubleClicked.connect(self.changeTableValue)
        #self.member_list.itemClicked.connect(self.showMemberTasks)
        
        self.scrollBar3.valueChanged.connect(self.synchronizeHorizontalScrollBar)
        self.scrollBar4.valueChanged.connect(self.synchronizeVerticalScrollBar1)
        self.scrollBar5.valueChanged.connect(self.synchronizeVerticalScrollBar2)
        self.entry_list.itemExpanded.connect(self.collapsSchedule)
        self.entry_list.itemCollapsed.connect(self.collapsSchedule)
        self.period_combo.currentIndexChanged.connect(self.changePeriod)
        


    def synchronizeHorizontalScrollBar(self,x):
        self.scrollBar1.setValue(x)
        self.scrollBar2.setValue(x)
        

    def synchronizeVerticalScrollBar1(self,y):
        self.scrollBar5.setValue(y)


    def synchronizeVerticalScrollBar2(self,y):
        self.scrollBar4.setValue(y)
        

    def changePeriod(self):
        self.setUpTables()
        self.drawSchedule()
        
        
    def getDuration(self,period='Year'):
        left_date = QtCore.QDate.currentDate()
        right_date = QtCore.QDate.currentDate()
        for projectId in self.member.projectDict.keys():
            date = self.member.projectDict[projectId][u'起始时间']
            if type(date) == type(u''):
                temp = date.split('-')
                date = [int(temp[0]),int(temp[1]),int(temp[2])]
            elif isinstance(date,datetime.date):
                date = [date.year,date.month,date.day]
            else:
                date = [date.year(),date.month(),date.day()]
            start_date = QtCore.QDate(date[0],date[1],date[2])
            date = self.member.projectDict[projectId][u'结束时间']
            if type(date) == type(u''):
                temp = date.split('-')
                date = [int(temp[0]),int(temp[1]),int(temp[2])]
            elif isinstance(date,datetime.date):
                date = [date.year,date.month,date.day]
            else:
                date = [date.year(),date.month(),date.day()]            
            end_date = QtCore.QDate(date[0],date[1],date[2])
            if left_date > start_date:
                left_date = start_date
            if right_date < end_date:
                right_date = end_date
        self.left_date = QtCore.QDate(left_date.year(),left_date.month(),1)
        self.right_date = QtCore.QDate(right_date.year(),right_date.month(),right_date.daysInMonth())
        self.left_date = self.left_date.addMonths(-1)
        self.right_date = self.right_date.addMonths(1)
        if period == 'Year':
            left_year = self.left_date.year()
            right_year = self.right_date.year()
            years = []
            year = left_year
            while year<=right_year:
                years.append(year)
                year = year+1
            return years
        if period == 'Month':
            months = []
            date = date1 = self.left_date
            date2 = self.right_date
            while date<=date2:
                months.append(date)
                date = date.addMonths(1)
            return months
        if period == 'Week':
            weeks = []
            firstDayOfWeek = self.left_date.dayOfWeek()
            days = 7 - firstDayOfWeek
            firstWeekend = self.left_date.addDays(days)
            weekend = firstWeekend
            while weekend<self.right_date:
                weeks.append(weekend)
                weekend = weekend.addDays(7)
            weeks.append(self.right_date)
            return weeks
        if period == 'Day':
            pass
        
        
        
    def setUpTables(self):
        period = unicode(self.period_combo.currentText())
        self.schedule_table.setColumnCount(1)
        self.schedule_table.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        if period == u'月':
            defaultWidth = 3
            tableWidth = self.period1_table.geometry().width()
            Years = self.getDuration('Year')
            Months = self.getDuration('Month')
            self.period1_table.setColumnCount(len(Years))
            self.period2_table.setColumnCount(len(Months))
            totalDays = self.left_date.daysTo(self.right_date)
            totalWidth = defaultWidth * totalDays
            if totalWidth < tableWidth:
                defaultWidth = tableWidth/totalDays
                totalWidth = tableWidth
            
            labels = []
            for i in range(len(Years)):
                year = Years[i]
                firstDay = QtCore.QDate(year,1,1)
                lastDay = QtCore.QDate(year,12,31)
                if firstDay<=self.left_date:
                    firstDay = self.left_date
                if lastDay>=self.right_date:
                    lastDay = self.right_date
                daysInYear = firstDay.daysTo(lastDay)+1
                columnWidth = daysInYear*defaultWidth
                self.period1_table.setColumnWidth(i,columnWidth)
                labels.append(str(year)+u'年')
            self.period1_table.setHorizontalHeaderLabels(labels)
             
            labels = []
            for i in range(len(Months)):
                month = Months[i]
                daysInMonth = month.daysInMonth()
                columnWidth = daysInMonth*defaultWidth
                self.period2_table.setColumnWidth(i,columnWidth)
                labels.append(monthDict[month.month()])
            self.period2_table.setHorizontalHeaderLabels(labels)
            self.schedule_table.setColumnWidth(0,totalWidth)
            
        if period == u'周':
            defaultWidth = 7
            tableWidth = self.period1_table.geometry().width()
            Months = self.getDuration('Month')
            Weeks = self.getDuration('Week')
            self.period1_table.setColumnCount(len(Months))
            self.period2_table.setColumnCount(len(Weeks))
            totalDays = self.left_date.daysTo(self.right_date)
            totalWidth = defaultWidth * totalDays
            if totalWidth < tableWidth:
                defaultWidth = tableWidth/totalDays
                totalWidth = tableWidth
            
            labels = []
            for i in range(len(Months)):
                month = Months[i]
                daysInMonth = month.daysInMonth()
                columnWidth = daysInMonth*defaultWidth
                self.period1_table.setColumnWidth(i,columnWidth)
                labels.append(u'{0}年'.format(month.year())+monthDict[month.month()])
            self.period1_table.setHorizontalHeaderLabels(labels)
            
            labels = []
            for i in range(len(Weeks)):
                weekend = Weeks[i]
                daysInWeek = 7
                if i==0:
                    daysInWeek = self.left_date.daysTo(weekend)
                if i==len(Weeks)-1:
                    daysInMonth = self.right_date.dayOfWeek()
                columnWidth = daysInWeek * defaultWidth
                self.period2_table.setColumnWidth(i,columnWidth)
                labels.append(u'{0}日'.format(weekend.day()))
            self.period2_table.setHorizontalHeaderLabels(labels)       
            
            self.schedule_table.setColumnWidth(0,totalWidth)      
            
        if period == u'日':
            defaultWidth = 25
            tableWidth = self.period1_table.geometry().width()
            Weeks = self.getDuration('Week')
            self.period1_table.setColumnCount(len(Weeks))            
            totalDays = self.left_date.daysTo(self.right_date)
            self.period2_table.setColumnCount(totalDays)
            totalWidth = defaultWidth * totalDays
            if totalWidth < tableWidth:
                defaultWidth = tableWidth/totalDays
                totalWidth = tableWidth
                
            labels = []
            for i in range(len(Weeks)):
                weekend = Weeks[i]
                daysInWeek = 7
                if i==0:
                    daysInWeek = self.left_date.daysTo(weekend)
                if i==len(Weeks)-1:
                    daysInMonth = self.right_date.dayOfWeek()
                columnWidth = daysInWeek * defaultWidth
                self.period1_table.setColumnWidth(i,columnWidth)
                labels.append(u'{0}年{1}月{2}日'.format(weekend.year(),weekend.month(),weekend.day()))
            self.period1_table.setHorizontalHeaderLabels(labels) 
            
            labels = []
            daysInWeekDict = {1:u'一',2:u'二',3:u'三',4:u'四',5:u'五',6:u'六',7:u'日'}
            for i in range(totalDays):
                day = self.left_date.addDays(i)
                self.period2_table.setColumnWidth(i,defaultWidth)
                dayOfWeek = day.dayOfWeek()
                labels.append(daysInWeekDict[dayOfWeek])
            self.period2_table.setHorizontalHeaderLabels(labels)
            self.schedule_table.setColumnWidth(0,totalWidth) 
            
        period1_header = self.period1_table.horizontalHeader()
        period1_header.setResizeMode(QtGui.QHeaderView.Fixed)
        period1_header.setClickable(False)
        period2_header = self.period2_table.horizontalHeader()
        period2_header.setResizeMode(QtGui.QHeaderView.Fixed)
        period2_header.setClickable(False)

        


    def drawScheduleItem(self,row_index,start_date,end_date,progress,status,level,detail,showDetial):
        currentDate = QtCore.QDate.currentDate()
        daysToToday = self.left_date.daysTo(currentDate)
        totalDays = self.left_date.daysTo(self.right_date)
        start_date = self.left_date.daysTo(start_date)*1.0/totalDays
        end_date = self.left_date.daysTo(end_date)*1.0/totalDays
        cur_pos = daysToToday*1.0/totalDays
        progress = progress/100
        cellWidth = self.schedule_table.columnWidth(0)
        rowHeight = self.schedule_table.rowHeight(0)
        rect = QtCore.QRect(0,0,cellWidth,rowHeight)
        item = scheduleBar(rect,start_date,end_date,cur_pos,QtCore.Qt.green,progress,status,level,detail,showDetial)
        self.schedule_table.setCellWidget(row_index,0,item)    

   
    def drawNullItem(self,row_index):
       currentDate = QtCore.QDate.currentDate()
       daysToToday = self.left_date.daysTo(currentDate)
       totalDays = self.left_date.daysTo(self.right_date)
       cur_pos = daysToToday*1.0/totalDays
       cellWidth = self.schedule_table.columnWidth(0)
       rowHeight = self.schedule_table.rowHeight(0)
       rect = QtCore.QRect(0,0,cellWidth,rowHeight)
       item = nullItem(rect,cur_pos)
       self.schedule_table.setCellWidget(row_index,0,item)
    
    
    def drawSchedule(self):
        showDetial = self.check_scheduleShowDetail.isChecked()
        self.schedule_table.clear()
        self.schedule_table.setRowCount(0)
        iterator = QtGui.QTreeWidgetItemIterator(self.entry_list)
        while iterator.value() is not None:
            treeItem = iterator.value()
            row_index = treeItem.data(0,QtCore.Qt.UserRole).toInt()[0]
            self.schedule_table.insertRow(row_index)
            text = treeItem.text(0)
            level = treeItem.getLevel()
            Id = treeItem.getId()            
            cellWidth = self.schedule_table.columnWidth(0)
            rowHeight = self.schedule_table.rowHeight(row_index)            
            rect = QtCore.QRect(0,0,cellWidth,30)
            if level == 1:
                project = self.member.projectDict[Id]
                start_date = self.member.projectDict[Id][u'起始时间']
                end_date = self.member.projectDict[Id][u'结束时间']
                progress = float(self.member.projectDict[Id][u'完成度'])
                status = self.member.projectDict[Id][u'项目状态']
                detail = {}
                detail[u'项目说明'] = unicode(self.member.projectDict[Id][u'项目说明'])
            elif level == 2:
                subproject = self.member.subprojectDict[Id]
                start_date = self.member.subprojectDict[Id][u'起始时间']
                end_date = self.member.subprojectDict[Id][u'结束时间']
                progress = float(self.member.subprojectDict[Id][u'完成度'])
                status = self.member.subprojectDict[Id][u'展项状态']
                detail = {}
                detail[u'展项说明'] = unicode(self.member.subprojectDict[Id][u'展项说明'])
            elif level == 3:
                task = self.member.taskDict[Id]
                start_date = self.member.taskDict[Id][u'起始时间']
                end_date = self.member.taskDict[Id][u'结束时间']
                progress = float(self.member.taskDict[Id][u'完成度'])
                status = self.member.taskDict[Id][u'任务状态']
                detail = {}
                detail[u'参与人员'] = unicode(self.member.taskDict[Id][u'参与人员'])
                detail[u'任务说明'] = unicode(self.member.taskDict[Id][u'任务说明'])
            else:
                self.drawNullItem(row_index)
                iterator = iterator.__iadd__(1)
                continue
             
            if type(start_date)==type(u'string'):
                temp = start_date.split('-')
                start_date = QtCore.QDate(int(temp[0]),int(temp[1]),int(temp[2]))
            elif isinstance(start_date,datetime.date):
                start_date = QtCore.QDate(start_date.year,start_date.month,start_date.day)
            if type(end_date)==type(u'string'):
                temp = end_date.split('-')
                end_date = QtCore.QDate(int(temp[0]),int(temp[1]),int(temp[2]))
            elif isinstance(end_date,datetime.date):
                end_date = QtCore.QDate(end_date.year,end_date.month,end_date.day)
            
            self.drawScheduleItem(row_index, start_date, end_date, progress, status, level,detail,showDetial)
            iterator = iterator.__iadd__(1)

      
       
    def drawEntryTree(self):
        self.entry_list.clear()
        headItem = self.entry_list.headerItem()
        headItem.setSizeHint(0,QtCore.QSize(100,50))
        projectFilter = self.combo_scheduleProjectFilter.currentText()
        subprojectFilter = self.combo_scheduleSubprojectFilter.currentText()
        memberFilter = self.combo_scheduleMemberFilter.currentText()
        if memberFilter == QtCore.QString('*'):
            if projectFilter != QtCore.QString('*') and projectFilter != '':
                index = self.combo_scheduleProjectFilter.currentIndex()
                projectId = unicode(self.combo_scheduleProjectFilter.itemData(index).toString())
                projectIdList = [projectId]
            else:
                projectIdList = self.member.hierTree.keys()
                projectIdList.sort()
            i=0
            for projectId in projectIdList:
                projectItem = newTreeWidgetItem(self.entry_list)
                projectItem.setSizeHint(0,QtCore.QSize(100,30))
                font = QtGui.QFont()
                font.setPixelSize(17)
                projectItem.setFont(0,font)
                projectItem.setText(0,self.member.projectDict[projectId][u'项目名称'])
                projectItem.setLevel(1)
                projectItem.setId(projectId)
                data = QtCore.QVariant(i)
                projectItem.setData(0,QtCore.Qt.UserRole,data)
                i = i + 1
                if subprojectFilter != QtCore.QString('*') and subprojectFilter != '':
                    index = self.combo_scheduleSubprojectFilter.currentIndex()
                    subprojectId = unicode(self.combo_scheduleSubprojectFilter.itemData(index).toString())
                    subproIdList = [subprojectId]
                else:
                    subproIdList = self.member.hierTree[projectId].keys()
                    subproIdList.sort()
                for subproId in subproIdList:            
                    subprojectItem =  newTreeWidgetItem(projectItem)
                    subprojectItem.setSizeHint(0,QtCore.QSize(100,30))
                    font = QtGui.QFont()
                    font.setPixelSize(15)
                    subprojectItem.setFont(0,font)                
                    subprojectItem.setText(0,self.member.subprojectDict[subproId][u'展项名称'])
                    subprojectItem.setLevel(2)
                    subprojectItem.setId(subproId)
                    data = QtCore.QVariant(i)
                    subprojectItem.setData(0,QtCore.Qt.UserRole,data)
                    i = i + 1
                    taskList = self.member.hierTree[projectId][subproId]
                    taskList.sort()
                    for task in taskList:
                        taskItem = newTreeWidgetItem(subprojectItem)
                        taskItem.setSizeHint(0,QtCore.QSize(100,30))
                        font = QtGui.QFont()
                        font.setPixelSize(13)
                        taskItem.setFont(0,font)                    
                        taskItem.setText(0,self.member.taskDict[task][u'任务名称'])
                        taskItem.setLevel(3)
                        taskItem.setId(task)
                        data = QtCore.QVariant(i)
                        taskItem.setData(0,QtCore.Qt.UserRole,data)
                        i = i + 1
                self.tree_project.addTopLevelItem(projectItem)
                nullItem = newTreeWidgetItem(self.entry_list)
                nullItem.setSizeHint(0,QtCore.QSize(100,30))
                nullItem.setText(0,u'')
                nullItem.setLevel(0)
                data = QtCore.QVariant(i)
                nullItem.setData(0,QtCore.Qt.UserRole,data)
                self.tree_project.addTopLevelItem(nullItem)
                i=i+1
                
        else:
            index = self.combo_scheduleMemberFilter.currentIndex()
            memberID = unicode(self.combo_scheduleMemberFilter.itemData(index).toString())
            taskList = self.member.allMembers[memberID][u'任务'].split(';')[:-1]
            index = self.combo_scheduleProjectFilter.currentIndex()
            projectId = unicode(self.combo_scheduleProjectFilter.itemData(index).toString())
            index = self.combo_scheduleSubprojectFilter.currentIndex()
            subprojectId = unicode(self.combo_scheduleSubprojectFilter.itemData(index).toString())                
            memberTaskTree = {}            
            for task in taskList:
                projectId = task[0:3]
                subproId = task[0:6]
                if not memberTaskTree.has_key(projectId):
                    memberTaskTree[projectId]={}
                if not memberTaskTree[projectId].has_key(subproId):
                    memberTaskTree[projectId][subproId]=[]
                memberTaskTree[projectId][subproId].append(task)

            if projectFilter != QtCore.QString('*') and projectFilter != '':
                if not memberTaskTree.has_key(projectId):
                    memberTaskTree = {}
                elif subprojectFilter != QtCore.QString('*') and subprojectFilter != '':
                    if not memberTaskTree[projectId].has_key(subprojectId):
                        memberTaskTree = {}
                    else:
                        taskList = memberTaskTree[projectId][subprojectId]
                        memberTaskTree = {}
                        memberTaskTree[projectId] = {}
                        memberTaskTree[projectId][subprojectId] = taskList
                else:
                    subproDict = memberTaskTree[projectId]
                    memberTaskTree = {}
                    memberTaskTree[projectId] = subproDict
            
            projectIdList = memberTaskTree.keys()
            projectIdList.sort()
            i = 0
            for projectId in projectIdList:
                projectItem = newTreeWidgetItem(self.entry_list)
                projectItem.setSizeHint(0,QtCore.QSize(100,30))
                font = QtGui.QFont()
                font.setPixelSize(17)
                projectItem.setFont(0,font)
                projectItem.setText(0,self.member.projectDict[projectId][u'项目名称'])
                projectItem.setLevel(1)
                projectItem.setId(projectId)
                data = QtCore.QVariant(i)
                projectItem.setData(0,QtCore.Qt.UserRole,data)
                i = i + 1
                subproIdList = memberTaskTree[projectId].keys()
                subproIdList.sort()
                for subproId in subproIdList:            
                    subprojectItem =  newTreeWidgetItem(projectItem)
                    subprojectItem.setSizeHint(0,QtCore.QSize(100,30))
                    font = QtGui.QFont()
                    font.setPixelSize(15)
                    subprojectItem.setFont(0,font)                
                    subprojectItem.setText(0,self.member.subprojectDict[subproId][u'展项名称'])
                    subprojectItem.setLevel(2)
                    subprojectItem.setId(subproId)
                    data = QtCore.QVariant(i)
                    subprojectItem.setData(0,QtCore.Qt.UserRole,data)
                    i = i + 1
                    taskList = memberTaskTree[projectId][subproId]
                    taskList.sort()
                    for task in taskList:
                        taskItem = newTreeWidgetItem(subprojectItem)
                        taskItem.setSizeHint(0,QtCore.QSize(100,30))
                        font = QtGui.QFont()
                        font.setPixelSize(13)
                        taskItem.setFont(0,font)                    
                        taskItem.setText(0,self.member.taskDict[task][u'任务名称'])
                        taskItem.setLevel(3)
                        taskItem.setId(task)
                        data = QtCore.QVariant(i)
                        taskItem.setData(0,QtCore.Qt.UserRole,data)
                        i = i + 1
                self.tree_project.addTopLevelItem(projectItem)
                nullItem = newTreeWidgetItem(self.entry_list)
                nullItem.setSizeHint(0,QtCore.QSize(100,30))
                nullItem.setText(0,u'')
                nullItem.setLevel(0)
                data = QtCore.QVariant(i)
                nullItem.setData(0,QtCore.Qt.UserRole,data)
                self.tree_project.addTopLevelItem(nullItem)
                i=i+1
         
        self.expandItem()
        self.setUpTables()
        self.drawSchedule()


    def expandItem(self):
        iterator = QtGui.QTreeWidgetItemIterator(self.entry_list)
        while iterator.value() is not None:
            item = iterator.value()            
            item.setExpanded(True)
            iterator = iterator.__iadd__(1)
    
    
    def collapsItem(self):
        iterator = QtGui.QTreeWidgetItemIterator(self.entry_list)
        while iterator.value() is not None:
            item = iterator.value()            
            item.setExpanded(False)
            iterator = iterator.__iadd__(1)        
            
    
    def collapsSchedule(self,item):
        self.entry_list.selectAll()
        sl = self.entry_list.selectedIndexes()
        self.entry_list.clearSelection()
        showList =[]
        for s in sl:
            item = self.entry_list.itemFromIndex(s)
            row_index = item.data(0,QtCore.Qt.UserRole).toInt()[0]
            self.schedule_table.showRow(row_index)
            showList.append(row_index)
        
        rowCount = self.schedule_table.rowCount()
        for row in range(rowCount):
            self.schedule_table.hideRow(row)
        for row in showList:
            #scheduleBar = self.schedule_table.cellWidget(row,0)
            #scheduleBar.repaint()
            self.schedule_table.showRow(row)
    
    
    def showScheduleSubprojectComobox(self):        
        curProject = self.combo_scheduleProjectFilter.currentText()
        if curProject != '*':
            index = self.combo_scheduleProjectFilter.currentIndex()
            curProjectId = unicode(self.combo_scheduleProjectFilter.itemData(index).toString())        
            subprojectIdList = self.member.hierTree[curProjectId].keys()
            subprojectList = []            
            for subprojectId in subprojectIdList:
                subprojectList.append((self.member.subprojectDict[subprojectId][u'展项名称'],subprojectId))
            self.drawComboBox('combo_scheduleSubprojectFilter', subprojectList)
            self.drawEntryTree()
        else:
            self.drawComboBox('combo_scheduleSubprojectFilter', [])    
            self.drawEntryTree()
                
                
    def showScheduleDetail(self,checked):
        rows = self.schedule_table.rowCount()
        if checked>0:
            show = True
        else:
            show = False
        for row in range(rows):
            widget = self.schedule_table.cellWidget(row,0)
            if isinstance(widget,scheduleBar):
                widget.setShowDetial(show)
                widget.repaint()

            
  
    
    #def addProject(self):
        #tempDict,ok = newProjectDialog.newProject()       
        #if tempDict[u'项目名称'] != '' and ok:
            #tempDict[u'完成度'] = str(0)
            #tempDict[u'项目状态'] = u'进行中'
            #success = self.member.addProject(tempDict)
            #if success[0] == 1:
                #root = self.tree_project.topLevelItem(0)
                #newItem = newTreeWidgetItem(root)
                #font = QtGui.QFont()
                #font.setPixelSize(16)
                #newItem.setFont(0,font)                
                #newItem.setText(0,success[1][u'项目名称'])
                #newItem.setLevel(1)
                #newItem.setId(success[1][u'项目编号'])
                #self.drawEntryTree()
                #self.query_project.addItem(success[1][u'项目名称'])
                #self.combo_scheduleProjectFilter.addItem(success[1][u'项目名称'])
            #elif success[0] == 2:
                #print '添加项目失败'
            #else :
                #print '该项目已存在'
            


    #def addSubproject(self):
        #tempDict,projectId,ok = newSubprojectDialog.newSubproject(projectDict=self.member.projectDict)
        #subproject = tempDict[u'展项名称']
        #project = tempDict[u'项目名称']
        #tempDict[u'完成度'] = str(0)
        #tempDict[u'展项状态'] = u'进行中'        
        #if project != '' and subproject != '' and ok:
            #success = self.member.addSubproject(tempDict,projectId)
            #if success[0] == 1:
                #itemIter = QtGui.QTreeWidgetItemIterator(self.tree_project)
                #while itemIter.value() is not None:
                    #if unicode(itemIter.value().text(0)) == project:
                        #newItem = newTreeWidgetItem(itemIter.value())
                        #font = QtGui.QFont()
                        #font.setPixelSize(14)
                        #newItem.setFont(0,font)                         
                        #newItem.setText(0,success[1][u'展项名称'])
                        #newItem.setLevel(2)
                        #newItem.setId(success[1][u'展项编号'])
                        #self.member.getHierTree()
                        #self.showSubprojectInfo(projectId)
                        #break
                    #else:
                        #itemIter = itemIter.__iadd__(1)
                #self.drawEntryTree()
            #elif success[0] == 2:
                #print '添加展项失败'
            #else:
                #print '展项已存在'            
                    
            
                
    #def addTask(self):
        #tempDict,projectId,subprojectId,ok = newTaskDialog.newTask(projectDict=self.member.projectDict,subprojectDict=self.member.subprojectDict)
        #task = tempDict[u'任务名称']
        #project = tempDict[u'项目名称']
        #subproject = tempDict[u'展项名称']
        #tempDict[u'完成度'] = str(0)
        #tempDict[u'任务状态'] = u'进行中'
        #tempDict[u'参与人员'] = ''
        #tempDict[u'部门'] = depDict[self.dep]
        #if project != '' and subproject != '' and task != '' and ok:
            #success = self.member.addTask(tempDict,projectId,subprojectId)
            #if success[0] == 1:
                #itemIter = QtGui.QTreeWidgetItemIterator(self.tree_project)
                #while itemIter.value() is not None:
                    #if unicode(itemIter.value().text(0)) == subproject:
                        #newItem = newTreeWidgetItem(itemIter.value())
                        #font = QtGui.QFont()
                        #font.setPixelSize(12)
                        #newItem.setFont(0,font)                         
                        #newItem.setText(0,success[1][u'任务名称'])
                        #newItem.setLevel(3)
                        #newItem.setId(success[1][u'任务编号'])
                        #self.showTaskInfo(subprojectId)
                        #break
                    #else:
                        #itemIter = itemIter.__iadd__(1)
                #self.drawEntryTree()
            #elif success[0] == 2:
                #print '添加任务失败'
            #else:
                #print '任务已存在'
                    



    #def addMember(self):
        #newMemberName = self.member_name_line.text()
        #newMemberTitle = self.member_title_line.text()
        #if newMemberName != '' and newMemberTitle !='':
            #memberDict = {}
            #memberDict[u'姓名'] = unicode(newMemberName)
            #memberDict[u'职务'] = unicode(newMemberTitle)
            #memberDict[u'部门'] = depDict[self.dep]
            #success = self.member.addMember(memberDict)
            #if success[0] == 1:
                #newItem = QtGui.QListWidgetItem(newMemberName)
                #data = QtCore.QVariant(success[1][u'编号'])
                #newItem.setData(QtCore.Qt.UserRole, data)
                #self.member_list.addItem(newItem)
                #self.member_name_line.setText('')
                #self.member_title_line.setText('')
                #self.drawMemberList
                #self.query_member.addItem(memberDict[u'姓名'])
                #self.combo_scheduleMemberFilter.addItem(memberDict[u'姓名'])
            #else :
                #print '添加成员失败'
        #else:
            #print '该成员已存在'

        
    
    #def delete(self):
        #curSelected = self.tree_project.currentItem()
        #parentItem = curSelected.parent()
        #if parentItem is not None:
            #itemId = curSelected.getId()
            #level = curSelected.getLevel()
            #parentItem.removeChild(curSelected)
            #if level == 1:
                #self.member.deleteProject(itemId)                
            #elif level == 2:
                #self.member.deleteSubproject(itemId)
            #else:
                #self.member.deleteTask(itemId)
            #self.tree_project.clearSelection()
            #self.tree_project.setItemSelected(parentItem,True)
            #self.showInfo(parentItem)
            #self.drawEntryTree()
    
    
    #def deleteProject(self):
        #curProjectItem = self.project_list.currentItem()
        #curRow = self.project_list.currentRow()
        #if curProjectItem is not None:
            #project = curProjectItem.text()
            #projectdict = {}
            #projectdict['project']=unicode(project)
            #success = self.member.deleteProject(projectdict)
            #if success:
                #self.project_list.takeItem(curRow)
                #self.subproject_list.clear()
                #self.task_list.clear()
                #self.showSubproject()
                #self.showTasks()
 
 
    
    #def deleteSubproject(self):
        #curSubprojectItem = self.subproject_list.currentItem()
        #curRow = self.subproject_list.currentRow()
        #if curSubprojectItem is not None:
            #curSubproject = curSubprojectItem.text()
            #subprojectdict = {}
            #subprojectdict['subproject'] = unicode(curSubproject)
            #project = self.member.subprojectDict[unicode(curSubproject)]['project']
            #success = self.member.deleteSubproject(subprojectdict,project)
            #if success:
                #self.subproject_list.takeItem(curRow)
                #self.task_list.clear()
                #self.showSubproject()
                #self.showTasks()
                
    
    #def deleteTask(self):
        #curTaskItem = self.task_list.currentItem()
        #curRow = self.task_list.currentRow()
        #if curTaskItem is not None:
            #curTask = curTaskItem.text()
            #taskDict = {}
            #taskDict['task'] = unicode(curTask)
            #subproject = self.member.taskDict[unicode(curTask)]['subproject']
            #success = self.member.deleteTask(taskDict,subproject)
            #if success:
                #self.task_list.takeItem(curRow)
                #self.showSubproject()
                #self.showTasks()
 
 
 
    #def drawMemberList(self):
        #idlist = self.member.allMembers.keys()
        #idlist.sort()
        #for member in idlist:
            #name = self.member.allMembers[member][u'姓名']
            #memberId = self.member.allMembers[member][u'编号']
            #data = QtCore.QVariant(memberId)
            #item = QtGui.QListWidgetItem(name)
            #item.setData(QtCore.Qt.UserRole,data)
            #item.setText(name)
            #self.member_list.addItem(item)




    #def showMemberTasks(self,item):
        #self.assigned_task.clear()
        #self.table_memberDaily.setRowCount(0)
        #memberId = unicode(item.data(QtCore.Qt.UserRole).toString())
        #if self.member.allMembers[memberId].has_key(u'任务'):
            #taskList = self.member.allMembers[memberId][u'任务'].split(';')[:-1]
        #memberTaskTree = {}            
        #for task in taskList:
            #projectId = task[0:3]
            #subproId = task[0:6]
            #if not memberTaskTree.has_key(projectId):
                #memberTaskTree[projectId]={}
            #if not memberTaskTree[projectId].has_key(subproId):
                #memberTaskTree[projectId][subproId]=[]
            #memberTaskTree[projectId][subproId].append(task)        
            
        #for projectId in memberTaskTree:
            #projectItem = newTreeWidgetItem(self.assigned_task)
            #projectItem.setText(0,self.member.projectDict[projectId][u'项目名称'])
            #projectItem.setLevel(1)
            #projectItem.setId(projectId)
            #subproIdList = memberTaskTree[projectId].keys()
            #subproIdList.sort()
            #for subproId in subproIdList:            
                #subprojectItem =  newTreeWidgetItem(projectItem)           
                #subprojectItem.setText(0,self.member.subprojectDict[subproId][u'展项名称'])
                #subprojectItem.setLevel(2)
                #subprojectItem.setId(subproId)
                #taskList = memberTaskTree[projectId][subproId]
                #taskList.sort()
                #for task in taskList:
                    #taskItem = newTreeWidgetItem(subprojectItem)            
                    #taskItem.setText(0,self.member.taskDict[task][u'任务名称'])
                    #taskItem.setLevel(3)
                    #taskItem.setId(task)
            #self.assigned_task.addTopLevelItem(projectItem)
        #self.assigned_task.expandAll()
        #self.showMemberDaily()


    #def countDaily(self):
        #statistics = {u'调休':0,u'请假':0,u'出差':0,u'其他':0}
        #rows = self.table_memberDaily.rowCount()
        #for i in range(rows):
            #hours = float(self.table_memberDaily.item(i,1).text())
            #cate = unicode(self.table_memberDaily.item(i,2).text())
            #if cate == u'调休':
                #statistics[u'调休'] = statistics[u'调休'] + hours
            #elif cate == u'请假':
                #statistics[u'请假'] = statistics[u'请假'] + hours
            #elif cate == u'出差':
                #statistics[ u'出差'] = statistics[u'出差'] + hours
            #else:
                #statistics[u'其他'] = statistics[u'其他'] + hours
        #text = ''
        #for key in statistics:
            #text = text + key
            #text = text + str(statistics[key]) + u'小时  '
        #self.statistics.setText(text)
         
                   

    #def showMemberDaily(self):
        #self.table_memberDaily.setRowCount(0)
        #self.table_memberDaily.columnsWidth = []
        #listItem = self.member_list.currentItem()
        #memberId = unicode(listItem.data(QtCore.Qt.UserRole).toString())
        #memberDailyDict = self.member.dailyDict[memberId]
        #dateList = memberDailyDict.keys()
        #dateList.sort()
        #self.table_memberDaily.setRowCount(len(dateList))
        #for i,date in enumerate(dateList):
            #for j,key in enumerate(self.member.dailyTabHeader[1:]):
                #item = QtGui.QTableWidgetItem()
                #text = unicode(memberDailyDict[date][key])
                #item.setText(unicode(memberDailyDict[date][key]))
                #item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
                #if j == 0:
                    #item.setFlags(QtCore.Qt.ItemIsEditable)
                #self.table_memberDaily.setItem(i,j,item)
                #font = item.font()
                #size1 = font.pixelSize()
                #size2 = font.pointSize()
                #if size1>size2:
                    #size = size1
                    #letterSpacing = font.letterSpacing()
                #else:
                    #dpi = self.logicalDpiX()
                    #size = size2 * dpi / 72
                    #letterSpacing = font.wordSpacing()
                #contextWidth = len(text)*size + (len(text)-1)*letterSpacing + 10
                #columnWidth = self.table_prodetail.columnWidth(j)
                #if columnWidth<contextWidth:
                    #columnWidth = contextWidth
                #self.table_memberDaily.setColumnWidth(j,contextWidth)
                #self.table_memberDaily.columnsWidth.append(columnWidth)
        #self.countDaily()


    #def addNewDailyRow(self):
        #listItem = self.member_list.currentItem()
        #index = 0
        #if listItem is not None:
            #index = self.member_list.currentIndex().row()
        #newDailyDict,memberId,ok = newDailyDialog.newDaily(memberDict=self.member.allMembers,index=index)
        #if ok:
            #success = self.member.addNewDaily(newDailyDict)
            #if success:
                #date = newDailyDict[u'日期']
                #newDailyDict.pop(u'编号')
                #self.member.dailyDict[memberId][date] = newDailyDict
                #self.showMemberDaily()
    
    
    #def delDaily(self):
        #listItem = self.member_list.currentItem()
        #memberId = unicode(listItem.data(QtCore.Qt.UserRole).toString())        
        #curRow = self.table_memberDaily.currentRow()
        #dailyDict = {}
        #dailyDict[u'编号'] = memberId
        #for j,key in enumerate(self.member.dailyTabHeader[1:]): 
            #item = self.table_memberDaily.item(curRow,j)
            #dailyDict[key] = unicode(item.text())
        ##print dailyDict
        #success = self.member.delDaily(dailyDict)
        #if success:
            #self.table_memberDaily.removeRow(curRow)
            #date = dailyDict[u'日期']
            #self.member.dailyDict[memberId].pop(date)
            


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
        self.tree_project.clear()
        root = newTreeWidgetItem(self.tree_project)
        font = QtGui.QFont()
        font.setPixelSize(17)        
        root.setFont(0,font)
        root.setText(0,u'全部项目')
        root.setLevel(0)
        root.setExpanded(True)
        projectIdList = self.member.hierTree.keys()
        projectIdList.sort()
        for projectId in projectIdList:
            projectItem = newTreeWidgetItem(root)
            font = QtGui.QFont()
            font.setPixelSize(16)
            projectItem.setFont(0,font)
            projectItem.setText(0,self.member.projectDict[projectId][u'项目名称'])
            projectItem.setLevel(1)
            projectItem.setId(projectId)
            projectItem.setExpanded(True)
            subproIdList = self.member.hierTree[projectId].keys()
            subproIdList.sort()
            for subproId in subproIdList:            
                subprojectItem =  newTreeWidgetItem(projectItem)
                font = QtGui.QFont()
                font.setPixelSize(14)
                subprojectItem.setFont(0,font)
                subprojectItem.setText(0,self.member.subprojectDict[subproId][u'展项名称'])
                subprojectItem.setLevel(2)
                subprojectItem.setId(subproId)
                subprojectItem.setExpanded(True)
                taskList = self.member.hierTree[projectId][subproId]
                taskList.sort()
                for task in taskList:
                    taskItem = newTreeWidgetItem(subprojectItem)
                    font = QtGui.QFont()
                    font.setPixelSize(12)                    
                    taskItem.setFont(0,font)
                    taskItem.setText(0,self.member.taskDict[task][u'任务名称'])
                    taskItem.setLevel(3)
                    taskItem.setId(task)
                    taskItem.setExpanded(True)
        self.tree_project.addTopLevelItem(root)



    def showSubprojectComobox(self):
        curProject = self.query_project.currentText()
        if curProject != '*':            
            index = self.query_project.currentIndex()
            curProjectId = unicode(self.query_project.itemData(index).toString())
            subprojectIdList = self.member.hierTree[curProjectId].keys()
            subprojectList = []
            for subprojectId in subprojectIdList:
                subprojectList.append((self.member.subprojectDict[subprojectId][u'展项名称'],subprojectId))
            self.drawComboBox('query_subproject',subprojectList)
        else:
            self.drawComboBox('query_subproject',[])                

    def showSubprojectComobox2(self):
        curProject = self.apply_project.currentText()
        if curProject != '*':            
            index = self.apply_project.currentIndex()
            curProjectId = unicode(self.apply_project.itemData(index).toString())
            subprojectIdList = self.member.hierTree[curProjectId].keys()
            subprojectList = []
            for subprojectId in subprojectIdList:
                subprojectList.append((self.member.subprojectDict[subprojectId][u'展项名称'],subprojectId))
            self.drawComboBox('apply_subproject',subprojectList)
        else:
            self.drawComboBox('apply_subproject',[])              
            
    def drawComboBox(self,widgetname='',l=[]):
        comboBox = self.findChild(QtGui.QComboBox,widgetname)
        comboBox.clear()
        comboBox.addItem('*')
        if len(l)>0:
            for temp in l:
                data = QtCore.QVariant(temp[1])
                comboBox.addItem(temp[0],temp[1])


                
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
        self.table_prodetail.setRowCount(0)
        self.table_prodetail.setColumnCount(0)        
        self.label_tables.setText(u'项目详情')
        self.table_prodetail.clear()
        self.table_prodetail.setTextElideMode(QtCore.Qt.ElideNone)
        rows = len(self.member.projectDict.keys())
        self.table_prodetail.setTableName(u'project')
        self.table_prodetail.setRowCount(rows)
        self.table_prodetail.setColumnCount(len(self.member.proTabHeader))
        self.table_prodetail.setHorizontalHeaderLabels(self.member.proTabHeader)
        projectList = self.member.projectDict.keys()
        projectList.sort()
        for i,row in enumerate(projectList):
            for j,col in enumerate(self.member.proTabHeader):
                text = unicode(self.member.projectDict[row][col])
                item = QtGui.QTableWidgetItem(text)
                item.setTextAlignment(QtCore.Qt.AlignHCenter)
                font = item.font()
                size1 = font.pixelSize()
                size2 = font.pointSize()
                if size1>size2:
                    size = size1
                    letterSpacing = font.letterSpacing()
                else:
                    dpi = self.logicalDpiX()
                    size = size2 * dpi / 72
                    letterSpacing = font.wordSpacing()
                contextWidth = len(text)*size + (len(text)-1)*letterSpacing + 20
                columnWidth = self.table_prodetail.columnWidth(j)
                if columnWidth<contextWidth:
                    columnWidth = contextWidth                                   
                item.setFlags(QtCore.Qt.ItemIsEditable)
                self.table_prodetail.setColumnWidth(j,columnWidth)
                self.table_prodetail.columnsWidth.append(columnWidth)
                self.table_prodetail.setItem(i,j,item)
    
    
    
    def showSubprojectInfo(self,projectId):
        self.table_prodetail.setRowCount(0)
        self.table_prodetail.setColumnCount(0)        
        projectName = self.member.projectDict[projectId][u'项目名称']
        self.label_tables.setText(projectName +u' 展项详情: ')
        self.table_prodetail.clear()
        subprojectIdList = self.member.hierTree[projectId].keys()
        subprojectIdList.sort()
        rows = len(subprojectIdList)
        self.table_prodetail.setTextElideMode(QtCore.Qt.ElideNone)
        self.table_prodetail.setTableName(u'subproject')
        self.table_prodetail.setRowCount(rows)
        self.table_prodetail.setColumnCount(len(self.member.subproTabHeader))
        self.table_prodetail.setHorizontalHeaderLabels(self.member.subproTabHeader)        
        for i,row in enumerate(subprojectIdList):
            for j,col in enumerate(self.member.subproTabHeader):
                text = unicode(self.member.subprojectDict[row][col])
                item = QtGui.QTableWidgetItem(text)
                item.setTextAlignment(QtCore.Qt.AlignHCenter)
                font = item.font()
                size1 = font.pixelSize()
                size2 = font.pointSize()
                if size1>size2:
                    size = size1
                    letterSpacing = font.letterSpacing()
                else:
                    dpi = self.logicalDpiX()
                    size = size2 * dpi / 72
                    letterSpacing = font.wordSpacing()
                contextWidth = len(text)*size + (len(text)-1)*letterSpacing + 20
                columnWidth = self.table_prodetail.columnWidth(j)
                if columnWidth<contextWidth:
                    columnWidth = contextWidth
                self.table_prodetail.setColumnWidth(j,columnWidth)                                   
                item.setFlags(QtCore.Qt.ItemIsEditable)
                self.table_prodetail.columnsWidth.append(columnWidth)
                self.table_prodetail.setItem(i,j,item)
 
 

    def showTaskInfo(self,subprojectId):
        self.table_prodetail.setRowCount(0)
        self.table_prodetail.setColumnCount(0)
        subprojectName = self.member.subprojectDict[subprojectId][u'展项名称']
        self.label_tables.setText(subprojectName + u' 任务详情: ')
        self.table_prodetail.clear()
        projectId = subprojectId[0:3]
        taskIdList = self.member.hierTree[projectId][subprojectId]
        taskIdList.sort()
        rows = len(taskIdList)
        self.table_prodetail.setTextElideMode(QtCore.Qt.ElideNone)
        self.table_prodetail.setTableName(u'task')
        self.table_prodetail.setRowCount(rows)
        self.table_prodetail.setColumnCount(len(self.member.taskTabHeader))
        self.table_prodetail.setHorizontalHeaderLabels(self.member.taskTabHeader)
        for i,row in enumerate(taskIdList):
            for j,col in enumerate(self.member.taskTabHeader):
                text = unicode(self.member.taskDict[row][col])
                item = QtGui.QTableWidgetItem(text)
                item.setTextAlignment(QtCore.Qt.AlignHCenter)
                font = item.font()
                size1 = font.pixelSize()
                size2 = font.pointSize()
                if size1>size2:
                    size = size1
                    letterSpacing = font.letterSpacing()
                else:
                    dpi = self.logicalDpiX()
                    size = size2 * dpi / 72
                    letterSpacing = font.wordSpacing()
                contextWidth = len(text)*size + (len(text)-1)*letterSpacing + 20
                columnWidth = self.table_prodetail.columnWidth(j)
                if columnWidth<contextWidth:
                    columnWidth = contextWidth
                self.table_prodetail.setColumnWidth(j,columnWidth)                  
                item.setFlags(QtCore.Qt.ItemIsEditable)
                self.table_prodetail.columnsWidth.append(columnWidth)
                self.table_prodetail.setItem(i,j,item)
        
        
    def applyForOvertime(self):
        date = unicode(self.apply_date.text())
        name = unicode(self.memberName)
        duration = unicode(self.apply_duration.text())
        meal = unicode(self.apply_meal.text())
        project = unicode(self.apply_project.currentText())
        subproject = unicode(self.apply_subproject.currentText())
        desc = unicode(self.desc.toPlainText())
        success = self.member.applyOvertime('overtime', [date,name,project,subproject,duration,meal,desc])
        if not success:
            print 'failed'
            
            

    def queryOvertime(self):
        query_dates = (unicode(self.query_fromdate.text()),unicode(self.query_todate.text()))
        query_project = unicode(self.query_project.currentText())
        query_subproject = unicode(self.query_subproject.currentText())
        result = self.member.queryOvertime(table='overtime', date=query_dates, project=query_project, subproject=query_subproject)
        projectlist = self.member.projectDict.keys()
        if len(result)>0:
            header = [u'日期',u'姓名',u'项目',u'展项',u'时长',u'加班餐',u'备注']
            self.drawTable(tablename='query_overtime_table', tableheader=header, tablelist=result)
        else:
            messagebox = QtGui.QMessageBox(2,QtCore.QString(u'提示'),QtCore.QString(u'没有查询到相关记录'),QtGui.QMessageBox.Yes | QtGui.QMessageBox.Cancel)
            messagebox.exec_()
    
    
                
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
                if j==0:
                    item.setFlags(QtCore.Qt.ItemIsEditable)
                tableWidget.setItem(i,j,item)



    def tableItemChange(self,row_index,col_index):
        tableName = self.table_prodetail.getTableName()
        header = []
        if tableName == u'project':
            header = self.member.proTabHeader
        elif tableName == u'subproject':
            header = self.member.subproTabHeader
        else :
            header = self.member.taskTabHeader
        numCols = self.table_prodetail.columnCount()
        rows = []
        row = []
        for j in range(numCols):
            item = self.table_prodetail.item(row_index,j)
            row.append(unicode(item.text()))
        rows.append(row)
        self.member.saveTable(tableName,rows)
        if header[col_index] == u'完成度':
            taskId = row[0]
            self.updateProgress(taskId)
        if header[col_index].find(u'名称')>0:
            ID = row[0]
            value = self.table_prodetail.item(row_index,col_index).text()
            iterator =  QtGui.QTreeWidgetItemIterator(self.tree_project)
            while iterator.value() is not None:
                item  = iterator.value()
                if item.getId() == ID:
                    item.setText(0,value)
                iterator = iterator.__iadd__(1)                
        self.drawEntryTree()



    def tableItemChange2(self,row_index,col_index):
        listItem = self.member_list.currentItem()
        memberId = unicode(listItem.data(QtCore.Qt.UserRole).toString())
        cols = self.table_memberDaily.columnCount()
        item = self.table_memberDaily.item(row_index,col_index)
        value = unicode(item.text())
        tableHeader = self.member.dailyTabHeader[1:]
        varsList = [(tableHeader[col_index],value)]
        conditionList = []        
        for j,key in enumerate(tableHeader):
            if j == col_index:
                continue
            else:
                item = self.table_memberDaily.item(row_index,j)
                text = unicode(item.text())
                conditionList.append((key,text))
        conditionList.append((self.member.dailyTabHeader[0],memberId))
        sccess = self.member.updateDaily(varsList,conditionList)
        if sccess:
            date = unicode(self.table_memberDaily.item(row_index,0).text())
            self.member.dailyDict[memberId][date][tableHeader[col_index]]=value
        self.countDaily()    

    def updateProgress(self,taskId):
        projectId = taskId[0:3]
        self.member.updateProgress(projectId)
        


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
        self.member.saveTable(tableName,rows)
        self.drawEntryTree()

            
    

    #def showContextMenu(self,e):
        #table_name = self.table_prodetail.getTableName()
        #cur_row = self.table_prodetail.currentRow()
        #total_rows = self.table_prodetail.rowCount()
        #row_hight  = self.table_prodetail.rowHeight(0)
        #y = e.y()
        #if table_name == u'task' and cur_row>=0 and y<row_hight*total_rows:
            #taskId = unicode(self.table_prodetail.item(cur_row,0).text())
            #colIndex = self.member.taskTabHeader.index(u'参与人员')
            #item = self.table_prodetail.item(cur_row,colIndex)
            #curText = unicode(item.text())
            ##get current member list,use '[:-1]' beacuse string's 'split' method always keey the '' at the end of the returned list
            #assignedMember = curText.split(';')[:-1]
            #menu = QtGui.QMenu('任务分配')
            #submenu = menu.addMenu(u'任务指派给')
            #submenu2 = menu.addMenu(u'取消指派')
            #self.signalMap = QtCore.QSignalMapper(self)
            #self.signalMap2 = QtCore.QSignalMapper(self)
            
            ##build assign action list and filter all the member who are already participate
            ##compare the number of the current involved member and the total member,so we can know if there are still someones who can be assigned
            #if len(assignedMember) < len( self.member.allMembers.keys()):
                #for member in self.member.allMembers:
                    #name = self.member.allMembers[member][u'姓名']
                    #memberId = self.member.allMembers[member][u'编号']
                    #name_id = name + '(' + memberId + ')'
                    #if name_id not in assignedMember:
                        #action = QtGui.QAction(name_id,submenu)
                        #self.signalMap.setMapping(action,name_id)
                        #action.triggered.connect(self.signalMap.map)
                        #submenu.addAction(action)
            #else:
                #action = QtGui.QAction(u'空',submenu)
                #action.setDisabled(True)
                #submenu.addAction(action)
                
            ##build un-assign action list,if assignedMember is an empty list,that means no one is participating
            #if len(assignedMember) != 0: 
                #for name_id in assignedMember:              
                    #if name_id != '':
                        #action = QtGui.QAction(name_id,submenu2)
                        #self.signalMap2.setMapping(action,name_id)
                        #action.triggered.connect(self.signalMap2.map)
                        #submenu2.addAction(action)
            #else:
                #action = QtGui.QAction(u'空',submenu)
                #action.setDisabled(True)
                #submenu2.addAction(action)      
            #self.signalMap.mapped[QtCore.QString].connect(self.taskAssign)
            #self.signalMap2.mapped[QtCore.QString].connect(self.taskUnassign)
            #menu.exec_(QtGui.QCursor.pos())
        #else:
            #pass
              
              
    #def taskAssign(self,name):
        #cur_row = self.table_prodetail.currentRow()
        #taskId = unicode(self.table_prodetail.item(cur_row,0).text())
        #colIndex = self.member.taskTabHeader.index(u'参与人员')
        #item = self.table_prodetail.item(cur_row,colIndex)
        #curText = unicode(item.text())           
        #name = unicode(name)
        #success = self.member.assignTask(curText,name,taskId)
        #if success:
            #col = item.column()
            #columnwidth = self.table_prodetail.columnWidth(col)
            #font = item.font()
            #size1 = font.pixelSize()
            #size2 = font.pointSize()
            #if size1>size2:
                #size = size1
                #letterSpacing = font.letterSpacing()
            #else:
                #dpi = self.logicalDpiX()
                #size = size2 * dpi / 72
                #letterSpacing = font.wordSpacing()
            #curText = curText + name + ';'
            #contextWidth = len(curText)*size + (len(curText)-1)*letterSpacing + 10 
            #if columnwidth < contextWidth:
                #columnwidth = contextWidth
            #self.table_prodetail.setColumnWidth(col,columnwidth)
            #item.setText(curText)

                
        
    #def taskUnassign(self,name):
        #cur_row = self.table_prodetail.currentRow()
        #taskId = unicode(self.table_prodetail.item(cur_row,0).text())
        #colIndex = self.member.taskTabHeader.index(u'参与人员')
        #item = self.table_prodetail.item(cur_row,colIndex)
        #curText = unicode(item.text())
        #name =unicode(name)
        #success = self.member.unassignTask(curText,name,taskId)
        #if success:
            #curText = curText.replace(name+';','')
            #item.setText(curText)



    def changeTableValue(self,item):
        def connectSlider():
            value = slider.value()
            item.setText(str(value))        
        table_name = self.table_prodetail.getTableName()
        row = item.row()
        col = item.column()
        header = []
        if table_name == u'project':
            header = self.member.proTabHeader
        elif table_name == u'subproject':
            header = self.member.subproTabHeader
        else:
            header = self.member.taskTabHeader
        headerLabel = header[col]
        if headerLabel.find(u'状态')>=0:
            combo = QtGui.QComboBox(self.table_prodetail)
            combo.addItem(u'等待')
            combo.addItem(u'进行中')
            combo.addItem(u'暂停')
            combo.addItem(u'待审核')
            combo.addItem(u'通过')
            combo.addItem(u'已完成')
            self.table_prodetail.setCellWidget(row,col,combo)
        if headerLabel.find(u'展项类型')>=0:
            combo = QtGui.QComboBox(self.table_prodetail)
            combo.addItem(u'动画')
            combo.addItem(u'游戏')
            self.table_prodetail.setCellWidget(row,col,combo)
        if headerLabel.find(u'完成度')>=0:
            value = float(item.text())
            slider = QtGui.QSlider(self.table_prodetail)
            slider.setOrientation(QtCore.Qt.Horizontal)
            slider.setRange(0,100)
            slider.setValue(value)
            slider.valueChanged.connect(connectSlider)
            self.table_prodetail.setCellWidget(row,col,slider)
        if headerLabel.find(u'时间')>0 or headerLabel.find(u'日期')>=0:
            text = item.text().split('-')
            if len(text)>0:
                date = QtCore.QDate(int(text[0]),int(text[1]),int(text[2]))
                calendar = myCalendarWidget(self.table_prodetail)
                calendar.setSelectedDate(date)
            self.table_prodetail.setRowHeight(row,200)
            self.table_prodetail.setColumnWidth(col,250)
            self.table_prodetail.setCellWidget(row,col,calendar)


    def changeTableValue2(self,item):    
        table_name = self.table_memberDaily.getTableName()
        row = item.row()
        col = item.column()
        header = self.member.dailyTabHeader
        headerLabel = header[col+1]
        if headerLabel.find(u'事项')>=0:
            combo = QtGui.QComboBox(self.table_memberDaily)
            combo.addItem(u'调休')
            combo.addItem(u'请假')
            combo.addItem(u'出差')
            combo.addItem(u'其他')
            self.table_memberDaily.setCellWidget(row,col,combo)
        if headerLabel.find(u'时长')>=0:
            value = item.text()
            if value != '':
                valeu = float(value)
            else:
                value = 0
            spinbox = QtGui.QDoubleSpinBox(self.table_memberDaily)
            spinbox.setValue(float(value))
            spinbox.setRange(0.0,8.0)
            spinbox.setSingleStep(0.5)
            self.table_memberDaily.setCellWidget(row,col,spinbox)
        if headerLabel.find(u'日期')>=0:
            calendar = myCalendarWidget(self.table_memberDaily)
            self.table_memberDaily.setRowHeight(row,200)
            self.table_memberDaily.setColumnWidth(col,250)
            self.table_memberDaily.setCellWidget(row,col,calendar)
            
    def changeTableValue3(self,item):    
        table_name = self.table_memberDaily.getTableName()
        row = item.row()
        col = item.column()
        header = self.member.dailyTabHeader
        headerLabel = header[col+1]
        if headerLabel.find(u'事项')>=0:
            combo = QtGui.QComboBox(self.table_memberDaily)
            combo.addItem(u'调休')
            combo.addItem(u'请假')
            combo.addItem(u'出差')
            combo.addItem(u'其他')
            self.table_memberDaily.setCellWidget(row,col,combo)
        if headerLabel.find(u'时长')>=0:
            value = item.text()
            if value != '':
                valeu = float(value)
            else:
                value = 0
            spinbox = QtGui.QDoubleSpinBox(self.table_memberDaily)
            spinbox.setValue(float(value))
            spinbox.setRange(0.0,8.0)
            spinbox.setSingleStep(0.5)
            self.table_memberDaily.setCellWidget(row,col,spinbox)
        if headerLabel.find(u'日期')>=0:
            calendar = myCalendarWidget(self.table_memberDaily)
            self.table_memberDaily.setRowHeight(row,200)
            self.table_memberDaily.setColumnWidth(col,250)
            self.table_memberDaily.setCellWidget(row,col,calendar)    
           
        
class myCalendarWidget(QtGui.QCalendarWidget):
    def __init__(self,parent=None):
        super(myCalendarWidget,self).__init__(parent)
        children = self.children()
        for child in children:
            child.installEventFilter(self)
    
    def eventFilter(self,widget,event):
        if event.type() == QtCore.QEvent.KeyPress:
            self.keyPressEvent(event)
        elif event.type() == QtCore.QEvent.MouseButtonPress:
            self.mousePressEvent(event)
        widget.event(event)
        return True

    def keyPressEvent(self,e):
        parent = self.parentWidget()
        parent.keyPressEvent(e)
        
    def mousePressEvent(self,e):
        button = e.button()
        if button == QtCore.Qt.LeftButton:
            parent = self.parentWidget()
            parent.mousePressEvent(e)
            
        

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
        return (newTaskDict,projectId,subprojectId,result==QtGui.QDialog.Accepted)
        


class newDailyDialog(ui_newDailyDialog.Ui_dialog):
    def __init__(self,parent=None,memberDict={},index=0):
        super(newDailyDialog,self).__init__(parent)
        self.setupUi(self)
        self.allMembers = memberDict
        idlist = self.allMembers.keys()
        idlist.sort()
        for memberId in idlist:
            memberName = self.allMembers[memberId][u'姓名']
            data = QtCore.QVariant(memberId)
            self.combo_name.addItem(memberName,data)
        self.combo_name.setCurrentIndex(index)
        for cate in [u'调休',u'请假',u'出差',u'其他']:
            self.combo_category.addItem(cate)
        date = QtCore.QDate.currentDate()
        self.date.setDate(date)
        
    @staticmethod
    def newDaily(parent=None,memberDict={},index=0):
        newDaily = newDailyDialog(parent,memberDict,index)
        result = newDaily.exec_()
        newDailyDict = {}
        index = newDaily.combo_name.currentIndex()
        memberId = unicode(newDaily.combo_name.itemData(index,QtCore.Qt.UserRole).toString())
        date = unicode(newDaily.date.date().toString('yyyy-MM-dd'))
        time  = unicode(str(newDaily.time.value()))
        print time
        cate = unicode(newDaily.combo_category.currentText())
        comment = unicode(newDaily.comment.toPlainText())
        newDailyDict[u'编号'] = memberId
        newDailyDict[u'日期'] = date
        newDailyDict[u'时长'] = time
        newDailyDict[u'事项'] = cate
        newDailyDict[u'备注'] = comment
        return (newDailyDict,memberId,result==QtGui.QDialog.Accepted)
        
        



class scheduleBar(QtGui.QWidget):
    def __init__(self,rect,startPos,endPos,curPos,color,progress,status,level,detail,showDetial,parent=None):
        super(QtGui.QWidget,self).__init__(parent)
        self.rect = rect
        self.startPos = startPos
        self.endPos = endPos
        self.curPos = curPos
        self.progress = progress
        self.status = status
        self.level = level
        self.color = color
        self.progressColor = color
        self.detail = detail
        self.showDetail = showDetial

        
    def setRect(self,rect):
        self.rect = rect
        
    def setStartPos(self,pos):
        self.startPos = pos
        
    def setEndPos(self,pos):
        self.endPos = pos
        
    def setColor(self,color):
        self.color = color
        
    def barColor(self):
        if self.level == 1:
            self.color = QtGui.QColor(120,168,255,255)
        elif self.level == 2:
            self.color = QtGui.QColor(242,157,82,255)
        else:
            self.color = QtGui.QColor(220,166,232,255)
            
    def progressBarColor(self):
        mult = 0.8
        red = self.color.red() * mult
        green = self.color.green() * mult
        blue = self.color.blue() * mult
        self.progressColor = QtGui.QColor(red,green,blue,255)
        
        
    def setProgress(self,progress):
        self.progress = progress
    
    def setLevel(self,level):
        self.level = level
        
    def setStatus(self,status):
        self.status = status

    def setShowDetial(self,show):
        self.showDetail = show
        
    def detailToString(self):
        s =u'完成度：{:.2%}   '.format(self.progress)
        for key in self.detail.keys():
            temp = key + ':' + self.detail[key] + ' '*3
            s= s + unicode(temp)
        return s
        
    def paintEvent(self,e):
        rectLeft = self.rect.left()
        rectWidth = self.rect.width()
        rectTop = self.rect.top()
        rectHeight = self.rect.height()
        barLeft = rectLeft + rectWidth*self.startPos
        barWidth = rectWidth * (self.endPos - self.startPos)
        if self.level == 1:
            yscale = 1
        elif self.level == 2:
            yscale = 0.9
        else:
            yscale = 0.8
        barHeight = rectHeight*0.8 * yscale
        barTop = rectTop + (rectHeight-barHeight)*0.5        
        bar = QtCore.QRect(barLeft,barTop,barWidth,barHeight)
        progressBarWidth = barWidth*(self.progress)
        progressBar = QtCore.QRect(barLeft,barTop,progressBarWidth,barHeight) 
        self.barColor()
        p = QtGui.QPainter()
        brush = QtGui.QBrush()
        pen = QtGui.QPen()
        p.begin(self)
        if self.level == 1:
            bgColor = QtGui.QColor(200,220,220,100)
        elif self.level == 2:
            bgColor = QtGui.QColor(190,210,210,120)
        else:
            bgColor = QtGui.QColor(180,200,200,140)
        pen.setColor(bgColor)
        pen.setStyle(QtCore.Qt.NoPen)        
        p.setPen(pen)
        brush.setColor(bgColor)
        brush.setStyle(QtCore.Qt.SolidPattern)
        p.setBrush(brush)
        p.drawRect(self.rect)       
        pen.setColor(QtCore.Qt.black)
        pen.setStyle(QtCore.Qt.SolidLine)
        p.setPen(pen)
        brush.setColor(self.color)
        p.setBrush(brush)
        p.drawRect(bar)
        self.progressBarColor()
        brush.setColor(self.progressColor)
        brush.setStyle(QtCore.Qt.SolidPattern)
        p.setBrush(brush)
        p.drawRect(progressBar)
        startLineTopx = bar.left()
        startLineTopy = self.rect.top()
        startLineBottomx = bar.left()
        startLineBottomy = self.rect.bottom()
        endLineTopx = endLineBottomx = bar.right()
        endLineTopy = self.rect.top()
        endLineBottomy = self.rect.bottom()
        pen.setColor(QtCore.Qt.black)
        pen.setStyle(QtCore.Qt.SolidLine)
        pen.setWidth(2)
        p.setPen(pen)
        todayPos = rectWidth * self.curPos + rectLeft
        pen.setColor(QtCore.Qt.darkGray)
        pen.setStyle(QtCore.Qt.SolidLine)
        pen.setWidth(2)
        p.setPen(pen)
        p.drawLine(todayPos,startLineTopy,todayPos,startLineBottomy)
        if self.showDetail:
            font = QtGui.QFont()
            font.setPixelSize(10)
            textPos = QtCore.QPoint(endLineTopx+10,endLineBottomy-5)
            pen.setColor(self.progressColor)
            p.setPen(pen)
            text = self.detailToString()
            p.drawText(textPos,text)
        p.end()


class nullItem(QtGui.QWidget):
    def __init__(self,rect,cur_pos,parent=None):
        self.rect = rect
        self.curPos = cur_pos
        super(QtGui.QWidget,self).__init__(parent)
        
    def paintEvent(self,e):
        rectWidth = self.rect.width()
        rectLeft = self.rect.left()
        startLineTopy = self.rect.top()
        startLineBottomy = self.rect.bottom()
        todayPos = rectWidth * self.curPos + rectLeft
        p = QtGui.QPainter()
        pen = QtGui.QPen()   
        p.begin(self)
        pen.setColor(QtCore.Qt.darkGray)
        pen.setStyle(QtCore.Qt.SolidLine)
        pen.setWidth(2)
        p.setPen(pen)    
        p.drawLine(todayPos,startLineTopy,todayPos,startLineBottomy)
        p.end()
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    path = sys.argv[0]
    cwd = os.path.dirname(path)
    #xmlPath = cwd + '''\department.xml'''
    manager = MemberClient()
    manager.show()
    app.exec_()