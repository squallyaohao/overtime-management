#File include declareation and denfinition of Class Member and Leader

import sys
import os.path
import xml.etree.cElementTree as ET
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
        self.projectList = []
        self.overTimeInfo = ''
        if os.path.exists(xmlPath):
            if os.path.splitext(xmlPath)[1]=='.xml' and os.path.getsize(xmlPath)>0:
                self.dataPath = xmlPath
                xmltree = ET.parse(xmlPath)
                member = xmltree.getroot()
                name = member.find('Name')
                self.name = name.text
                title = member.find('Title')
                self.title = title.text
                try:
                    for project in member.iter('Project'):
                        self.projectList.append(project.text)
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
        xmltree = ET.parse(self.dataPath)
        member = xmltree.getroot()
        nameTag = member.find('Name')
        nameTag.text = name
        xmltree.write(self.dataPath)
    
    def getName(self):
        return self.name
    
    
    def setTitle(self,title):
        self.title = title
        xmltree = ET.parse(self.dataPath)
        member = xmltree.getroot()
        titleTag = member.find('Title')
        titleTag.text = title
        xmltree.write(self.dataPath)
    
    
    def getTitle(self):
        return self.title
    
    
    def getAllProjects(self):
        return self.projectList
    
    
    def addProject(self,pro):
        self.projectList.append(pro)
        xmltree = ET.parse(self.dataPath)
        projectList = xmltree.getroot().find('ProjectList')
        newproject = ET.SubElement(projectList,'Project')
        newproject.text = pro
        xmltree.write(self.dataPath)
        
    
    
    def deleteProject(self,pro):
        try:
            self.projectList.remove(pro)
        except ValueError,e:
            print e        
        xmltree = ET.parse(self.dataPath)
        projectList = xmltree.getroot().find('ProjectList')
        for project in projectList.iter('Project'):
            if project.text == pro:
                projectList.remove(project)
        xmltree.write(self.dataPath)
    
    
    def applyOvertime(self,date=time.time(),duration=0,project='',dinner='',description=''):
        pass
    
    
    def queryOvertime(self,data=time.time()):
        pass
    
    
    
    
    
#child class inheriet from base class 'Member',add some more tool for leader to maintain department information
#for example leader can add or delete member and project query overtime information based on certain member,certain
#project,and certain time duration
class Leader(Member):
    def __init__(self,xmlPath):
        Member.__init__(self,xmlPath)
        
        
    def getDepartment(self):
        pass
    
    
    def addMember(self):
        pass
    
    
    def deleteMember(self):
        pass
    
    
    def getAllMembers(self):
        pass
    
    
    def addProject(self,pro):
        pass
    
    
    def deleteProject(self,pro):
        pass
    
    
    def getAllProjects(self):
        pass
    
    
    def queryOvertime(self,timeduration=(),project='',member=(),):
        pass
    
        