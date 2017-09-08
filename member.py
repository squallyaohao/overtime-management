#File include declareation and denfinition of Class Member and Leader
#coding=utf-8

import sys
import os.path
import xml.etree.ElementTree as ET
import time
import department


#Function used to initialize and xml file
#system use this xml file to store and restore user-related information
def initXML(path):
    root = ET.Element('Member')
    name = ET.SubElement(root,'Name')
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
        self.title = ''
        self.projectList = set([])
        self.overTimeInfo = ''
        if os.path.exists(xmlPath):
            if os.path.splitext(xmlPath)[1]=='.xml' and os.path.getsize(xmlPath)>0:
                self.dataPath = xmlPath
                xmltree = ET.parse(xmlPath)
                member = xmltree.getroot()
                name = member.find('Name')
                try:
                    self.name = name.text.encode('utf-8')
                except AttributeError,e:
                    self.name = ''
                title = member.find('Title')
                try:
                    self.title = title.text.encode('utf-8')
                except AttributeError,e:
                    self.title = ''
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
        print '设置姓名: '.decode('utf-8') + self.name.decode('utf-8')
        xmltree = ET.parse(self.dataPath)
        member = xmltree.getroot()
        nameTag = member.find('Name')
        nameTag.text = self.name.decode('utf-8')
        xmltree.write(self.dataPath)
    
    def getName(self):
        print '成员名称： '.decode('utf-8') + self.name.decode('utf-8')
        return self.name
    
    
    def setTitle(self,title):
        self.title = title
        print '设置职位: '.decode('utf-8')+ self.title.decode('utf-8')
        xmltree = ET.parse(self.dataPath)
        member = xmltree.getroot()
        titleTag = member.find('Title')
        titleTag.text = title.decode('utf-8')
        xmltree.write(self.dataPath)
    
    
    def getTitle(self):
        print '职位： '.decode('utf-8') + self.title.decode('utf-8')
        return self.title
    
    
    def getAllProjects(self):
        print '项目列表： '.decode('utf-8')
        for pro in self.projectList:
            print '\t' + pro.decode('utf-8')
        return self.projectList
    
    
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
    
    
    def applyOvertime(self,date=time.time(),duration=0,project='',dinner='',description=''):
        pass
    
    
    def queryOvertime(self,data=time.time()):
        pass
    
    
 
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
            print self.depDataPath
            xmltree.write(self.dataPath)
        self.department = department.Department(self.depDataPath)
        
        
        
    def getDepartment(self):
        return self.department
        
    
    
    def addMember(self,name):
        self.department.addMember(name)
    
    
    def deleteMember(self,name):
        self.department.deleteMember(name)
    
    
    def getAllMembers(self):
        self.department.getAllMembers()
    
    
    def addProject(self,pro):
        self.department.addProject(pro)
    
    
    def deleteProject(self,pro):
        self.department.deleteProject(pro)
    
    
    def getAllProjects(self):
        self.department.getAllProjects()
    
    
    def queryOvertime(self,timeduration=(),project='',member=(),):
        pass
    
        


def testIntializeMember(path):
    a = Member(path)
    a.setName('Yao')
    a.setTitle('FX')
    a.addProject('ZY')
    a.addProject('ZGKJG')    
    
def testChangeMember(path):
    a = Member(path)
 
    a.setName('姚灏')
    a.setTitle('ANI')
    a.addProject('zgfdafa')
    a.addProject('中国科技馆')
    a.addProject('遵义科技馆')
    a.addProject('滁州科技馆')
    
    print a.getName()
    print a.getTitle()
    print a.getAllProjects()    

def testLeaderInit(path):
    leader = Leader(path)
    leader.setName('万涛涛')
    leader.setTitle('三维主管')
    
    leader.addMember(name)
    
    
        
if __name__ == '__main__':
    #testIntializeMember('F:\Dev\overtime-management\member1.xml')
    #testChangeMember('F:\Dev\overtime-management\member1.xml')
    testLeaderInit('F:\Dev\overtime-management\Leader.xml')
    