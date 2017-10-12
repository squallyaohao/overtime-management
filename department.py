#File include declareation and denfinition of Class Department
#coding=utf-8

import sys
import os,os.path
import codecs
import xml.etree.cElementTree as ET
import time,datetime
import mysql_utility
import MySQLdb as sql
from db_structure import *


depDict = {0:u'三维动画',1:u'投标动画',2:u'二维动画',3:u'平面设计',4:u'编导'}
memberstabHeader = [u'id',u'department',u'title'] 
projecttabHeader = [u'start_date',u'finish_date',u'subprojects',u'description']
subprojecttabHeader = [u'subproject_category',u'project',u'start_date',u'finish_date',u'tasks',u'subproject_description']
taskstabHeader = [u'department',u'project',u'subproject',u'start_date',u'finish_date',u'progress',u'members',u'description']


def initXML(path):
    root = ET.Element('Department')
    xmltree = ET.ElementTree(root) 
    memberList = ET.SubElement(root,'MemberList')
    projectList = ET.SubElement(root,'ProjectList')
    xmltree = ET.ElementTree(root)
    xmltree.write(path )

    

class Department(): 
    def __init__(self,*args):
        self.dataPath= ''
        self.depName = ''
        self.memberList = set([])
        self.projectList = set([])
        if len(args)!=0 :
            if len(args)>1:
                print 'More than one argument has been passed!'
            elif os.path.exists(args[0]) and os.path.getsize(args[0])>0 and os.path.splitext(args[0])[1]=='.xml':
                self.dataPath = args[0]
                xmltree = ET.parse(self.dataPath)
                root = xmltree.getroot()

                #get department name
                try:
                    self.depName = int(root.get('depName').encode('utf-8'))
                except AttributeError,e:
                    self.depName = 0


                #loop all member and get their names
                try:
                    for member in root.iter('member'):
                        name = member.get('name')
                        self.memberList.add(name.encode('utf-8'))
                        print '成员名称：'.decode('utf-8') + name
                except AttributeError,e:
                    print e
                    self.memberList = []
                
                #loop all projects and get their names
                try:
                    for project in root.iter('project'):
                        pro = project.get('project-name')
                        self.projectList.add(pro.encode('utf-8'))
                        print '项目名称: '.decode('utf-8') + pro
                except AttributeError,e:
                    print e
                    self.projectList =[]
          
            elif os.path.exists(args[0]) and  os.path.splitext(args[0])[1]=='.xml' and os.path.getsize(args[0])==0:
                self.dataPath= args[0]
                self.depName = ''
                self.memberList = set([])
                self.projectList = set([])   
                initXML(self.dataPath)
                
            else:
                self.dataPath= args[0]
                self.depName = ''
                self.memberList = set([])
                self.projectList = set([])                 
                initXML(args[0])
                #print 'Invalid path passed!'
        else:
            print 'pleas pass the data file(*.xml)'
            
            self.projectDict = {}
            self.subprojectDict = {}
            self.taskDict = {}
            self.allMembers = {}

            
        self.proTabHeader = self.getTableHeader(headertable='proTabHeader')
        self.subproTabHeader = self.getTableHeader(headertable='subproTabHeader')
        self.taskTabHeader = self.getTableHeader(headertable='taskTabHeader')
        self.memberTabHeader = self.getTableHeader(headertable='memberTabHeader')
        self.dailyTabHeader = self.getTableHeader(headertable='dailyTabHeader')

            
        self.getProjectsFromServer()
        self.getSubprojectFromServer()
        self.getTaskFromeServer()
        self.getMembersFromServer()
        self.getDailyFromServer()
        self.buildTreeHierarchy()



       
    def setDepName(self,dep):
        self.department = dep
        xmltree = ET.parse(self.dataPath)
        department = xmltree.getroot()
        department.set('depName',str(self.department))
        xmltree.write(self.dataPath)
            
    
    def getDepName(self):
        return self.depName
    
    
    def connectToServer(self):
        hostfile = os.path.dirname(self.dataPath)+'\\hostname'
        loginfile = open(hostfile,'r').read().split(' ')
        hostid = loginfile[0]
        database = loginfile[1]
        user = loginfile[2]
        pwd = loginfile[3]
        if hostid[:3] == codecs.BOM_UTF8:
            hostid = hostid[3:] 
        conn = sql.connect(hostid,user,pwd,database,charset='utf8')
        cursor = conn.cursor()
        return (conn,cursor)
    
    
    def tableInsert(self,table='',varsdict={}):
        conn,cursor = self.connectToServer()
        insert_statement = mysql_utility.sqlInsertState2(table,varsdict)
        cursor.execute(insert_statement)
        conn.commit()
        cursor.close()
        conn.close()
        return 1

    
    def queryServer(self,table='',tabHeader=[]):
        tempDict = {}
        conn,cursor = self.connectToServer()
        query_statement = mysql_utility.sqlQueryState(table)
        cursor.execute(query_statement)
        conn.commit()
        result = cursor.fetchall()
        if len(result) != 0:
            for row in result:
                tempDict[row[0]] = dict(zip(tabHeader,row))
        cursor.close()
        conn.close()
        return tempDict
    


    def queryServer2(self,table='',columns=[],condition={},tabHeader=[]):
        tempDict = {}
        conn,cursor = self.connectToServer()
        statement = mysql_utility.sqlQueryState2(table,columns, 
                                                condition)
        cursor.execute(statement)
        conn.commit()
        result = cursor.fetchall()
        if len(result) != 0:
            for row in result:
                tempDict[row[0]] = dict(zip(tabHeader,row))
        cursor.close()
        conn.close()
        return tempDict
    


    def checkNotExist(self,table='',condition={}):
        conn,cursor = self.connectToServer()
        statement = mysql_utility.sqlQueryState(table,condition)
        cursor.execute(statement)
        conn.commit()
        result = cursor.fetchall()
        if len(result) == 0:
            return 1
        else:
            return 0

        
    
    def updateServer(self,table='',varsList=[],conditionsList=[]): 
        conn,cursor = self.connectToServer()
        update_statement = mysql_utility.sqlUpdateState(table, varsList,conditionsList)
        #print update_statement
        cursor.execute(update_statement)
        conn.commit()
        cursor.close()
        conn.close()
        return 1



    def saveTable(self,table='',multiRow=[]):
        conn,cursor = self.connectToServer()
        headerLabels =''
        if table == u'project':
            headerLabels = self.proTabHeader
        elif table == u'subproject':
            headerLabels = self.subproTabHeader
        else:
            headerLabels = self.taskTabHeader
        for row in multiRow:
            varsList = zip(headerLabels,row)
            conditionList= varsList[0]
            statement = mysql_utility.sqlUpdateState(table, varsList, [conditionList])
            cursor.execute(statement)
            conn.commit()
            for key,value in varsList:
                if key.find(u'时间')>=0:
                    temp = value.split('-')
                    value = datetime.date(int(temp[0]),int(temp[1]),int(temp[2]))
                if table == u'project':
                    self.projectDict[varsList[0][1]][key]=value
                elif table == u'subproject':
                    self.subprojectDict[varsList[0][1]][key]=value
                else:
                    self.taskDict[varsList[0][1]][key]=value
        cursor.close()
        conn.close()

        
        
    def deleteMember(self,name):
        if name in self.memberList:
            self.memberList.remove(name)
        xmltree = ET.parse(self.dataPath)
        memberlist = xmltree.getroot().find('MemberList')
        for member in memberlist.findall('member'):
            if member.get('name') == name.decode('utf-8'):
                memberlist.remove(member)
        xmltree.write(self.dataPath)
        
    
    def getTableHeader(self,headertable=''):
        conn,cursor = self.connectToServer()
        statement = "select * from "+headertable+" order by columnIndex;" 
        cursor.execute(statement)
        conn.commit()
        result = cursor.fetchall()
        headerList = []
        for row in result:
            headerList.append(row[0])
        return headerList
    
        
    def getMembersFromServer(self):
        allMembers = self.queryServer(table='member', tabHeader=self.memberTabHeader)
        self.allMembers = {}
        for key in allMembers:
            if allMembers[key][u'部门'] == depDict[self.depName]:
                self.allMembers[key] = allMembers[key]
            
        return self.allMembers


    def getProjectsFromServer(self):
        self.projectDict = self.queryServer(table='project',tabHeader=self.proTabHeader)
        return self.projectDict

    
    def getSubprojectFromServer(self):
        self.subprojectDict = self.queryServer(table='subproject', tabHeader=self.subproTabHeader)
        return self.subprojectDict
    
    
    def getTaskFromeServer(self):
        self.taskDict = self.queryServer(table='task', tabHeader=self.taskTabHeader)
        return self.taskDict

    
    def getDailyFromServer(self):
        self.dailyDict = {}
        conn,cursor = self.connectToServer()
        query_statement = mysql_utility.sqlQueryState('daily')
        cursor.execute(query_statement)
        conn.commit()
        result = cursor.fetchall()
        for memberId in self.allMembers:
            self.dailyDict[memberId]={}
        if len(result) > 0:
            for row in result:
                date = row[1].isoformat() 
                daily = dict(zip(self.dailyTabHeader[2:], row[2:]))
                daily[self.dailyTabHeader[1]] = date
                self.dailyDict[row[0]][date] = daily    
                   
        cursor.close()
        conn.close()
        return self.dailyDict
    

    def buildTreeHierarchy(self):
        self.hierTree = {}
        for pro in self.projectDict.keys():
            self.hierTree[pro]={}
        for subpro in self.subprojectDict.keys():
            proKey = subpro[0:3]
            self.hierTree[proKey][subpro]=[]
        for task in self.taskDict.keys():
            proKey = task[0:3]
            subKey = task[0:6]
            self.hierTree[proKey][subKey].append(task)
        self.calcProgress()
        return self.hierTree


    def getHierTree(self):
        return self.hierTree



    def calcProgress(self):
        for pro in self.hierTree.keys():
            proProgress = 0.0
            subproList = self.hierTree[pro].keys()
            if len(subproList)>0:
                for subpro in subproList:
                    subproProgress= 0.0
                    taskList = self.hierTree[pro][subpro]
                    if len(taskList)>0:
                        for task in taskList:
                            progress = float(self.taskDict[task][u'完成度'])
                            subproProgress = subproProgress + progress
                        subproProgress = subproProgress / len(taskList)
                    self.subprojectDict[subpro][u'完成度']=str(subproProgress) 
                    proProgress = proProgress + subproProgress
                proProgress = proProgress/len(subproList)
            self.projectDict[pro][u'完成度']=u'{:.2f}'.format(proProgress)
            
    
    def updateProgress(self,projectId):
        proProgress = 0.0
        subproList = self.hierTree[projectId].keys()
        for subpro in subproList:
            subproProgress = 0.0
            taskList = self.hierTree[projectId][subpro]
            for task in taskList:
                progress = float(self.taskDict[task][u'完成度'])
                subproProgress = subproProgress + progress
            subproProgress = subproProgress / len(taskList)
            self.subprojectDict[subpro][u'完成度']=str(subproProgress) 
            proProgress = proProgress + subproProgress
        proProgress = proProgress/len(subproList)
        self.projectDict[projectId][u'完成度']=str(proProgress)        
        


    
    def addProject(self,project_vars={}):
        ok = self.checkNotExist('project',{u'项目名称':project_vars[u'项目名称']})
        if ok:
            totalProjects = len(self.projectDict.keys())
            projectId = '%03d'%(totalProjects + 1)
            project_vars[u'项目编号']=projectId
            success = self.tableInsert(table='project', varsdict=project_vars)
            if success:
                self.hierTree[projectId] = {}
                self.projectDict[projectId] = project_vars
                return (1,project_vars)
            else:
                return (2,project_vars)
        else:
            return (3,project_vars)


    def addSubproject(self,subproject_vars={},projectId=''):
        ok = self.checkNotExist('subproject',{u'展项名称':subproject_vars[u'展项名称'],u'项目名称':subproject_vars[u'项目名称']})
        if ok:
            totalSubproject = len(self.hierTree[projectId].keys())
            subprojectId = projectId + '%03d'%(totalSubproject+1)
            subproject_vars[u'展项编号'] = subprojectId
            success = self.tableInsert(table='subproject', varsdict=subproject_vars)
            if success:
                self.hierTree[projectId][subprojectId]=[]
                self.subprojectDict[subprojectId] = subproject_vars
                return (1,subproject_vars)
            else:
                return (2,subproject_vars)
        else:
            return (3,subproject_vars)


    def addTask(self,task_vars={},projectId='',subprojectId=''):
        ok = self.checkNotExist('task', {u'任务名称':task_vars[u'任务名称'],u'展项名称':task_vars[u'展项名称'],u'项目名称':task_vars[u'项目名称']})
        if ok:
            taskList = self.hierTree[projectId][subprojectId]
            totalTask = len(taskList)
            taskId = subprojectId+'%03d'%(totalTask+1)
            task_vars[u'任务编号'] = taskId
            success = self.tableInsert(table='task', varsdict=task_vars)
            if success:
                self.hierTree[projectId][subprojectId].append(taskId)
                self.taskDict[taskId] = task_vars
                return (1,task_vars)
            else:
                return (2,task_vars)
        else:
            return (3,task_vars)
        
    
    def addMember(self,member={}):
        ok = self.checkNotExist(table='member', condition=member)
        if ok:
            allmembers = self.queryServer(table='member', tabHeader=self.memberTabHeader)
            total = len(allmembers.keys())
            memberId = '%04d'%(total+ 1)
            member[u'编号'] = memberId
            for key in self.memberTabHeader:
                if member.has_key(key):
                    continue
                else:
                    member[key] = ''
            success = self.tableInsert(table='member', varsdict=member)
            if success:
                self.allMembers[memberId] = member
                print self.allMembers.keys()
                return (1,member)
            else :
                return (2,member)
        else:
            return (3,member)
    
        
    def deleteProject(self,projectId):
        conn,cursor = self.connectToServer()
        deleteDict = self.hierTree[projectId]
        del_statments = []
        del_statments.append(mysql_utility.sqldeletState(table='project', condition={u'项目编号':projectId}))
        for subproId in deleteDict.keys():
            del_statments.append(mysql_utility.sqldeletState(table='subproject', condition={u'展项编号':subproId}))
            for taskId in deleteDict[subproId]:
                del_statments.append(mysql_utility.sqldeletState(table='task', condition={u'任务编号':taskId}))
        for statement in del_statments:
            cursor.execute(statement)
            conn.commit()
        cursor.close()
        conn.close()
        self.hierTree.pop(projectId)
        self.projectDict.pop(projectId)
        return 1


    def deleteSubproject(self,subprojectId):
        conn,cursor = self.connectToServer()
        projectId = subprojectId[0:3]
        deleteDict = self.hierTree[projectId][subprojectId]
        del_statments = []
        del_statments.append(mysql_utility.sqldeletState(table='subproject', condition={u'展项编号':subprojectId}))
        for taskId in deleteDict:
            del_statments.append(mysql_utility.sqldeletState(table='task', condition={u'任务编号':taskId}))
        for statement in del_statments:
            cursor.execute(statement)
            conn.commit()
        cursor.close()
        conn.close()
        self.hierTree[projectId].pop(subprojectId)
        self.subprojectDict.pop(subprojectId)
        return 1



    def deleteTask(self,taskId):
        conn,cursor = self.connectToServer()
        projectId = taskId[0:3]
        subprojectId = taskId[0:6]
        del_statement = mysql_utility.sqldeletState(table='task', condition={u'任务编号':taskId})
        cursor.execute(del_statement)
        conn.commit()
        cursor.close()
        conn.close()
        self.hierTree[projectId][subprojectId].remove(taskId)
        self.taskDict.pop(taskId)
        return 1
        


    def assignTask(self,curmembers,member,taskId):
        curmembers = curmembers + member + ';'
        success = self.updateServer('task', [(u'参与人员',curmembers)], [(u'任务编号',taskId)])
        if success:
            self.taskDict[taskId][u'参与人员'] = curmembers
            memberId = unicode(member.split('(')[1].split(')')[0])
            memberName = unicode(member.split('(')[0])
            memberTask = self.allMembers[memberId][u'任务']
            if memberTask is not None:
                memberTask = memberTask + taskId + ';'
            else:
                memberTask = taskId + ';'
            self.allMembers[memberId][u'任务'] = memberTask
            success = self.updateServer('member',[(u'任务',memberTask)],[(u'编号',memberId)])
            return 1
        else :
            return 0
        
        
        
    def unassignTask(self,curmembers,member,taskId):
        curmembers = curmembers.replace(member+u';','')
        success = self.updateServer('task', [(u'参与人员',curmembers)], [(u'任务编号',taskId)])
        if success:
            self.taskDict[taskId][u'参与人员'] = curmembers
            memberId = member.split('(')[1].split(')')[0]
            memberName = member.split('(')[0]
            memberTask = self.allMembers[memberId][u'任务']
            memberTask = memberTask.replace(taskId+';','')
            self.allMembers[memberId][u'任务'] = memberTask
            success = self.updateServer('member',[(u'任务',memberTask)],[(u'编号',memberId)])
            return 1
        else:
            return 0

    

    def addNewDaily(self,newDailyDict={}): 
        conn,cursor = self.connectToServer()
        statment = mysql_utility.sqlInsertState2(table='daily', varsdict=newDailyDict)
        cursor.execute(statment)
        conn.commit()
        cursor.close()
        conn.close()
        return 1
     
    
    def delDaily(self,dailyDict={}):
        conn,cursor = self.connectToServer()
        statement = mysql_utility.sqldeletState(table='daily', condition=dailyDict)
        cursor.execute(statement)
        conn.commit()
        cursor.close()
        conn.close()
        return 1        


    def updateDaily(self,varsList=[],conditionList=[]):
        conn,cursor = self.connectToServer()
        statement = mysql_utility.sqlUpdateState(table='daily', varsList=varsList,conditionList=conditionList)
        print statement
        cursor.execute(statement)
        conn.commit()
        cursor.close()
        conn.close()
        return 1         
   
    
    def queryOvertime(self,table='',date=(),member='',project='',subproject=''):
        loginfile = open('hostname','r').read().split(' ')
        hostid = loginfile[0]
        database = loginfile[1]
        user = loginfile[2]
        pwd = loginfile[3]
        if hostid[:3] == codecs.BOM_UTF8:
            hostid = hostid[3:]
        conn = sql.connect(hostid,user,pwd,database,charset='utf8')
        cursor = conn.cursor()
        query_condition = {'date':date,'name':member,'project':project,'subproject':subproject}
        #query_condition = {'date':date,'name':member,'project':project}
        querystatement = mysql_utility.sqlQueryState(table,query_condition)
        cursor.execute(querystatement)
        conn.commit()
        result = cursor.fetchall()
        cursor.close()
        return result



