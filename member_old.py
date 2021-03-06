#File include declareation and denfinition of Class Member and Leader
#coding=utf-8

import sys
import os,os.path
import codecs
import xml.etree.ElementTree as ET
import time
import department
import project
import mysql_utility
import MySQLdb as sql
from db_structure import *


depDict = {0:'三维动画',1:'投标动画',2:'二维动画',3:'平面设计',4:'编导'}

#Function used to initialize and xml file
#system use this xml file to store and restore user-related information
def initXML(path):
    root = ET.Element('Member')
    name = ET.SubElement(root,'Name')
    department = ET.SubElement(root,'Department')
    title = ET.SubElement(root,'Title')
    projectList = ET.SubElement(root,'ProjectList')
    xmltree = ET.ElementTree(root)
    xmltree.write(path)
        
        

#Definition of Member calss
#Member is the base class that contain bunch of basic attributes and methods that represent for a person in a department
class Member():
    def __init__(self,xmlPath):
        self.dataPath = ''
        self.name = ''
        self.department = '0'
        self.title = ''
        self.projectList = set([])
        self.overTimeInfo = ''
        if os.path.exists(xmlPath):
            if os.path.splitext(xmlPath)[1]=='.xml' and os.path.getsize(xmlPath)>0:
                self.dataPath = xmlPath
                xmltree = ET.parse(xmlPath)
                member = xmltree.getroot()

                #read name tag
                name = member.find('Name')
                try:
                    self.name = name.text
                except AttributeError,e:
                    self.name = ''
                
                dep = member.find('Department')
                try:
                    self.department = int(dep.text.encode('utf-8'))
                except AttributeError,e:
                    self.department = 0
                    
                #read title tag
                title = member.find('Title')
                try:
                    self.title = title.text.encode('utf-8')
                except AttributeError,e:
                    self.title = ''
                
                #read projects tags
                try:
                    for project in member.iter('Project'):
                        self.projectList.add(project.text.encode('utf-8'))
                except :
                    self.projectList = []
                    
            elif os.path.splitext(xmlPath)[1]=='.xml' and os.path.getsize(xmlPath)==0:
                initXML(xmlPath)
                self.dataPath = xmlPath
            else:
                raise IOError('Invalid xml path: '+xmlPath)
        else:
            if os.path.splitext(xmlPath)[1]=='.xml':
                initXML(xmlPath)
                self.dataPath = xmlPath
            else:
                raise IOError('Invalid xml path: '+xmlPath)
               
        
    def setName(self,name):
        self.name = name
        print name
        print '设置姓名: '.decode('utf-8') + self.name
        xmltree = ET.parse(self.dataPath)
        member = xmltree.getroot()
        nameTag = member.find('Name')
        nameTag.text = self.name
        xmltree.write(self.dataPath)
    
    def getName(self):
        print '成员名称： '.decode('utf-8') + self.name
        return self.name
    
    
    def setDepartment(self,dep):
        self.department = dep
        xmltree = ET.parse(self.dataPath)
        member = xmltree.getroot()
        depTag = member.find('Department')
        depTag.text = str(self.department)
        xmltree.write(self.dataPath)
        
    
    def getDepartment(self):
        #print '部门： '.decode('utf-8') + depDict[self.department].decode('utf-8')
        return self.department
        
        
    
    def setTitle(self,title):
        self.title = title
        print '设置职位: '.decode('utf-8')+ self.title.decode('utf-8')
        xmltree = ET.parse(self.dataPath)
        member = xmltree.getroot()
        titleTag = member.find('Title')
        titleTag.text = title.decode('utf-8')
        xmltree.write(self.dataPath)
    
    
    def getTitle(self):
        return self.title



    
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
    


    def tableQuery(self,table='',tableList=[]):
        tempDict = {}
        conn,cursor = self.connectToServer()
        query_statement = mysql_utility.sqlQueryState(table)
        cursor.execute(query_statement)
        conn.commit()
        result = cursor.fetchall()
        for row in result:
            tempDict[row[0]] = dict(zip(tableList[1:],row[1:]))
        return tempDict



    def getProjectsFromServer(self):
        self.projectDict = self.tableQuery(table='project',tableList=projectTableList)
        return self.projectDict
        
 
    
    def addProject(self,project):
        self.projectList.add(project)
        print '增加项目: '.decode('utf-8') + project.decode('utf-8')
        xmltree = ET.parse(self.dataPath)
        projectList = xmltree.getroot().find('ProjectList')
        projectList.clear()
        for pro in self.projectList:
            newproject = ET.SubElement(projectList,'Project')
            newproject.text = pro.decode('utf-8')
        xmltree.write(self.dataPath)
        
    
    
    def deleteProject(self,pro):
        if pro in self.projectList:
            self.projectList.remove(pro)
        xmltree = ET.parse(self.dataPath)
        projectList = xmltree.getroot().find('ProjectList')
        for project in projectList.iter('Project'):
            if project.text == pro.decode('utf-8'):
                projectList.remove(project)
        xmltree.write(self.dataPath)
    

    
    def applyOvertime(self,table='',varsList=[]):
        conn,cursor = self.connectToServer()
        query_statement = "select * from overtime where date='" + varsList[0] + "' and name='" + varsList[1] +"';"
        cursor.execute(query_statement)
        conn.commit()
        result = cursor.fetchall()
        if result is not None and len(result)>0:
            return 0
        else:
            insert_statement = mysql_utility.sqlInsertState(table,varsList)
            cursor.execute(insert_statement)
            conn.commit()
            cursor.close()
            conn.close()
            return 1
    
    
    def queryOvertime(self,table='',date=(),project=''):
        loginfile = open('hostname','r').read().split(' ')
        hostid = loginfile[0]
        database = loginfile[1]
        user = loginfile[2]
        pwd = loginfile[3]
        if hostid[:3] == codecs.BOM_UTF8:
            hostid = hostid[3:]
        conn = sql.connect(hostid,user,pwd,database,charset='utf8')
        cursor = conn.cursor()
        query_condition = {'date':date,'name':self.name,'project':project}
        querystatement = mysql_utility.sqlQuerysState(table,query_condition)
        cursor.execute(querystatement)
        conn.commit()
        result = cursor.fetchall()
        cursor.close()
        return result
    
    
    
    def updateServer(self,table,curTable=[]):
        conn,cursor = self.connectToServer()
        cursor = conn.cursor()
        for row in curTable:
            varsList = zip(overtimeTableList[2:],row[2:])
            conditionsList = zip(overtimeTableList[:2],row[:2])
            updatestatement = mysql_utility.sqlUpdateState(table,varsList,conditionsList)
            print updatestatement
            cursor.execute(updatestatement)
            conn.commit()        
        cursor.close()
        conn.close()
        return 1
            
        
            
    
    
 
#child class inherit from base class 'Member',add some more tools for leader to maintain department information
#for example leader can add or delete members and projects, query overtime information based on certain member,certain
#project,and certain time duration
class Leader(Member):
    def __init__(self,xmlPath):
        Member.__init__(self,xmlPath)
        self.depDataPath = ''
        xmltree = ET.parse(self.dataPath)
        member = xmltree.getroot()
        try:
            depdata = member.find('DepartmentData')
            self.depDataPath = depdata.text
        except AttributeError ,e:
            depdata = ET.SubElement(member, 'DepartmentData')
            dirname = os.path.dirname(self.dataPath)
            depxmlname = dirname + '\\department.xml'
            depdata.text = depxmlname
            self.depDataPath = depxmlname
            xmltree.write(self.dataPath) 
        
        
        
    def getDepartment(self):
        dep = department.Department(self.depDataPath)
        return dep
           
    
    def addDepMember(self,name):
        dep = self.getDepartment()
        dep.addMember(name)
    
    
    def deleteDepMember(self,name):
        dep = self.getDepartment()
        dep.deleteMember(name)
    
    
    def getAllDepMembers(self):
        dep = self.getDepartment()
        dep.getAllMembers()
    
    
    def addDepProject(self,pro):
        dep = self.getDepartment()
        dep.addProject(pro)
    
    
    def deleteDepProject(self,pro):
        dep = self.getDepartment()
        dep.deleteProject(pro)
    
    
    def getAllDepProjects(self):
        dep = self.getDepartment()
        dep.getAllProjects()
    
    
    def queryOvertime(self,timeduration=(),project='',member=(),):
        pass
    
        

#define test fuction
def testIntializeMember(path):
    member = Member(path)
    member.setName('Yao')
    member.setDepartment(0)
    member.setTitle('FX')
    member.addProject('ZY')
    member.addProject('ZGKJG')   
    
    return member


#define test fuction    
def testChangeMember(path):
    member = Member(path)
 
    member.setName('姚灏')
    member.setTitle('特效师')
    member.setDepartment(1)
    member.addProject('中国科技馆')
    member.addProject('遵义科技馆')
    member.addProject('滁州科技馆')
    
    #print member.getName()
    #print member.getTitle()
    #print member.getAllProjects()    
    
    return member


#define test fuction
def testLeaderInit(path):
    leader = Leader(path)
    leader.setName('万涛涛')
    leader.setTitle('三维主管')
    
    leader.addDepMember('姚灏')
    leader.addDepMember('孙林')
    leader.addDepMember('王恒')
    leader.addDepMember('王政')
    
    leader.addDepProject('遵义科技馆')
    leader.addDepProject('滁州科技馆')
    leader.addDepProject('中国科技馆')
    leader.addDepProject('鸟馆')
    leader.addDepProject('郑州科技馆')
    leader.addDepProject('单县科技馆')
    
    leader.addProject('遵义科技馆')
    leader.addProject('中国科技馆')
    
    return leader
    
    
#define test fuction
def testChangeLeader(path):
    leader = Leader(path)
    leader.addDepMember('苏里找')
    leader.addDepMember('姜峰')
    leader.addDepMember('郑伟')
    leader.deleteDepMember('姚灏')
    leader.deleteDepMember('孙林')
    
    leader.addDepProject('海门科技馆')
    leader.addDepProject('郑州科技馆')
    leader.deleteDepProject('遵义科技馆')
    
    leader.addProject('郑州科技馆')
    leader.addProject('单县科技馆')    
    leader.deleteProject('遵义科技馆')
    leader.deleteProject('中国科技馆')
    
    return leader
    


def testOvertime(path):
    member = testIntializeMember(path)
    member.setName('姚灏')
    member.applyOvertime(table='overtime',date='2017-9-20',duration='3',project='遵义科技馆',meal='米饭',description='')
    
    
    
        
