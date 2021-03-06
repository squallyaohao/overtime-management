#File include declareation and denfinition of Class Department
#coding=utf-8

import sys
import os,os.path
import codecs
import xml.etree.cElementTree as ET
import time
import mysql_utility
import MySQLdb as sql
from db_structure import *


depDict = {0:'三维动画',1:'投标动画',2:'二维动画',3:'平面设计',4:'编导'}
#membersTableList = [u'id',u'department',u'title'] 
#projectTableList = [u'start_date',u'finish_date',u'subprojects',u'description']
#subprojectTableList = [u'subproject_category',u'start_date',u'finish_date',u'tasks',u'subproject_description']
#tasksTableList = [u'task_id',u'department',u'project',u'subproject',u'start_date',u'finish_date',u'progress',u'members',u'description']


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
                print 'start initialzie'
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
            self.tasksDict = {}
            self.allMembers = {}            
        
        
    def setDepName(self,dep):
        self.department = dep
        xmltree = ET.parse(self.dataPath)
        department = xmltree.getroot()
        department.set('depName',str(self.department))
        xmltree.write(self.dataPath)
            
    
    def getDepName(self):
        return self.depName
    
    
    def connectToServer(self):
        loginfile = open('hostname','r').read().split(' ')
        hostid = loginfile[0]
        database = loginfile[1]
        user = loginfile[2]
        pwd = loginfile[3]
        if hostid[:3] == codecs.BOM_UTF8:
            hostid = hostid[3:] 
        conn = sql.connect(hostid,user,pwd,database,charset='utf8')
        cursor = conn.cursor()
        return (conn,cursor)
    
    
    def tableInsert(self,table='',vars_list=[]):
        conn,cursor = self.connectToServer()
        insert_statement = mysql_utility.sqlInsertState(table,vars_list)
        print insert_statement
        cursor.execute(insert_statement)
        conn.commit()
        cursor.close()
        return 1

    
    def tableQuery(self,table='',tableList=[]):
        tempDict = {}
        conn,cursor = self.connectToServer()
        query_statement = mysql_utility.sqlQuerysState(table)
        cursor.execute(query_statement)
        conn.commit()
        result = cursor.fetchall()
        for row in result:
            tempDict[row[0]] = dict(zip(tableList[1:],row[1:]))
        return tempDict
    
    
        
        
    def deleteMember(self,name):
        if name in self.memberList:
            self.memberList.remove(name)
        xmltree = ET.parse(self.dataPath)
        memberlist = xmltree.getroot().find('MemberList')
        for member in memberlist.findall('member'):
            if member.get('name') == name.decode('utf-8'):
                memberlist.remove(member)
        xmltree.write(self.dataPath)
        
        
    
    def getMembersFromServer(self):
        self.allMembers = self.tableQuery(table='members', tableList=membersTableList)
        return self.allMembers


    def getProjectsFromServer(self):
        self.projectDict = self.tableQuery(table='project',tableList=projectTableList)
        return self.projectDict
    
    def getSubprojectFromServer(self):
        self.subprojectDict = self.tableQuery(table='subproject', tableList=subprojectTableList)
        return self.subprojectDict
    
    
    def getTasksFromeServer(self,table=''):
        self.tasksDict = self.tableQuery(table='tasks', tableList=tasksTableList)
        return self.tasksDict

    
    def addProject(self,project_vars=[]):
        success = self.tableInsert(table='project', vars_list=project_vars)
        if success:
             newProjectDict = dict(zip(projectTableList[1:], project_vars[1:]))
             return newProjectDict
        else:
             return 0        


    def addSubproject(self,subproject_vars=[]):
        success = self.tableInsert(table='subproject', vars_list=subproject_vars)
        return success
    

    def addTask(self,task_vars=[]):
        return 1
    
    
    def addMember(self,member=[]):
        success = self.tableInsert(table='members', vars_list=member)
        if success:
            newMemberDict = dict(zip(membersTableList[1:],member[1:]))
            return newMemberDict
        else :
            return 0            
    
        
    def deleteProject(self,projectdict):
        loginfile = open('hostname','r').read().split(' ')
        hostid = loginfile[0]
        database = loginfile[1]
        user = loginfile[2]
        pwd = loginfile[3]
        if hostid[:3] == codecs.BOM_UTF8:
            hostid = hostid[3:]
        conn = sql.connect(hostid,user,pwd,database,charset='utf8')
        cursor = conn.cursor()
        delete_statment = mysql_utility.sqldeletState('project',projectdict)
        project delete_statment
        cursor.execute(delete_statment)
        conn.commit()
        cursor.close()
        return 1
        
        
        
    def getAllProjects(self):
        project '项目列表： '.decode('utf-8')
        for pro in self.projectList:
            project '\t'+pro.decode('utf-8')
        return self.projectList
        
        

        
    def updateServer(self,table='',varsList=[],conditionsList=[]): 
        conn,cursor = self.connectToServer()
        update_statement = mysql_utility.sqlUpdateState(table, varsList,conditionsList)
        cursor.execute(update_statement)
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
        querystatement = mysql_utility.sqlQuerysState(table,query_condition)
        cursor.execute(querystatement)
        conn.commit()
        result = cursor.fetchall()
        cursor.close()
        return result


def testIntializeDepartment(path):
    a = Department(path)
    a.setDepName(0)
    a.addMember('姚灏')
    a.addMember('孙林')
    a.addMember('孙林')
    a.addProject('遵义科技馆')
    a.addProject('滁州科技馆')    
    a.addProject('滁州科技馆')
    a.getProjectsFromServer(table='project')
    
def testChangeDepartment(path):
    a = Department(path)
    
    a.setDepName('二维')
    a.addMember('姚灏')
    a.deleteMember('姚灏')
    a.addProject('中国科技馆')
    a.deleteProject('中国科技馆')

if __name__ == '__main__':
    testIntializeDepartment('F:\Dev\overtime-management\department1.xml')
    #testChangeDepartment('F:\Dev\overtime-management\department1.xml')