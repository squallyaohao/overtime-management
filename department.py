#File include declareation and denfinition of Class Department
#coding=utf-8

import sys
import os,os.path
import codecs
import xml.etree.cElementTree as ET
import time
import mysql_utility
import MySQLdb as sql


depDict = {0:'三维动画',1:'投标动画',2:'二维动画',3:'平面设计',4:'编导'}


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
        
        
    def setDepName(self,dep):
        self.department = dep
        print dep
        xmltree = ET.parse(self.dataPath)
        department = xmltree.getroot()
        department.set('depName',str(self.department))
        xmltree.write(self.dataPath)
            
    
    def getDepName(self):
        return self.depName
    
    def addMember(self,member):
        if member not in self.memberList:
            self.memberList.add(member)
            print '添加成员： '.decode('utf-8') + member.decode('utf-8')
        xmltree = ET.parse(self.dataPath)
        memberList = xmltree.find('MemberList')
        memberList.clear()
        for mem in self.memberList:
            newMember = ET.SubElement(memberList,'member')
            newMember.set('name',mem.decode('utf-8'))
        xmltree.write(self.dataPath )
        
    def deleteMember(self,name):
        if name in self.memberList:
            self.memberList.remove(name)
        xmltree = ET.parse(self.dataPath)
        memberlist = xmltree.getroot().find('MemberList')
        for member in memberlist.findall('member'):
            if member.get('name') == name.decode('utf-8'):
                memberlist.remove(member)
        xmltree.write(self.dataPath)
        
    
    def getAllMembersFromServer(self,table=''):
        loginfile = open('hostname','r').read().split(' ')
        hostid = loginfile[0]
        database = loginfile[1]
        user = loginfile[2]
        pwd = loginfile[3]
        if hostid[:3] == codecs.BOM_UTF8:
            hostid = hostid[3:] 
        conn = sql.connect(hostid,user,pwd,database,charset='utf8')
        cursor = conn.cursor()
        query_statement = mysql_utility.sqlQuerysState(table)
        cursor.execute(query_statement)
        conn.commit()
        result = cursor.fetchall()
        if result is not None:
            memberlist = []
            for data in result:
                memberlist.append(data[1])
                print data[1]
        self.memberList = memberlist
        return self.memberList

    
    def addProject(self,projectdict):
        #if project not in self.projectList:
            #self.projectList.add(project)          
            #print '添加项目： '.decode('utf-8') + project.decode('utf-8')
        #xmltree = ET.parse(self.dataPath)
        #projectList = xmltree.find('ProjectList')
        #projectList.clear()
        #for pro in self.projectList:
            #newProject = ET.SubElement(projectList,'project')
            #newProject.set('project-name',pro.decode('utf-8'))
        #xmltree.write(self.dataPath)
        loginfile = open('hostname','r').read().split(' ')
        hostid = loginfile[0]
        database = loginfile[1]
        user = loginfile[2]
        pwd = loginfile[3]
        if hostid[:3] == codecs.BOM_UTF8:
            hostid = hostid[3:] 
        conn = sql.connect(hostid,user,pwd,database,charset='utf8')
        cursor = conn.cursor()
        project = projectdict.keys()[0]
        insert_statement = mysql_utility.sqlInsertState('project',[project,projectdict[project]])
        print insert_statement
        cursor.execute(insert_statement)
        conn.commit()
        cursor.close()
        return 1
            
             
        
    def deleteProject(self,projectdict):
        #if pro in self.projectList:
            #self.projectList.remove(pro)
        #xmltree = ET.parse(self.dataPath)
        #projectlist = xmltree.getroot().find('ProjectList')
        #for project in projectlist.findall('project'):
            #if project.get('project-name') == pro.decode('utf-8'):
                #projectlist.remove(project)
        #xmltree.write(self.dataPath)
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
        print delete_statment
        cursor.execute(delete_statment)
        conn.commit()
        cursor.close()
        return 1
        
    def getAllProjects(self):
        print '项目列表： '.decode('utf-8')
        for pro in self.projectList:
            print '\t'+pro.decode('utf-8')
        return self.projectList
        
        
    def getProjectsFromServer(self,table=''):
        projectDict = {}
        loginfile = open('hostname','r').read().split(' ')
        hostid = loginfile[0]
        database = loginfile[1]
        user = loginfile[2]
        pwd = loginfile[3]
        if hostid[:3] == codecs.BOM_UTF8:
            hostid = hostid[3:]    
        conn = sql.connect(hostid,user,pwd,database,charset='utf8')
        cursor = conn.cursor()
        query_statement = mysql_utility.sqlQuerysState(table)
        cursor.execute(query_statement)
        conn.commit()
        result = cursor.fetchall()
        if result is not None:
            for data in result:
                if projectDict.has_key(data[0]):
                    if data[1] is not None and len(data[1])>0:
                        projectDict[data[0]].append(data[1])
                    else:
                        projectDict[data[0]]=[]
                else:
                    if data[1] is not None and len(data[1])>0:
                        projectDict[data[0]]=[data[1]]
                    else:
                        projectDict[data[0]]=[]                
        cursor.close()
        conn.close()
        self.projectList = projectDict        
        xmltree = ET.parse(self.dataPath)
        projectList = xmltree.getroot().find('ProjectList')
        projectList.clear()
        for pro in self.projectList:
            newproject = ET.SubElement(projectList,'Project')
            newproject.set('project-name',pro)
            if len(self.projectList[pro])>0:
                for subpro in self.projectList[pro]:
                    subproject = ET.SubElement(newproject,'Subproject')
                    subproject.text = subpro
        xmltree.write(self.dataPath)
        return projectDict
    
    
    def updateServer(self,table='',l=[]): 
        pass
        


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