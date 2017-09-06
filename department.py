#File include declareation and denfinition of Class Department

import sys
import os.path
import xml.etree.cElementTree as ET


class Department():
    def __init__(self,*args):
        if len(args)!=0 :
            if len(args)>1:
                print 'More than one argument has been passed!'
            elif os.path.exists(args[0]) and os.path.getsize(args[0])>0 and os.path.splitext(args[0])[1]=='.xml':
                self.dataPath = args[0]
                xmltree = ET.parse(self.dataPath)
                root = xmltree.getroot()
                self.depName = root.get('depName')
                try:
                    for member in root.find('memberList').findall('member'):
                        self.memberList.append(member.get('name'))
                    for project in root.find('projectList').findall('project'):
                        self.projectList.append(project.get('projectName'))
                except AttributeError,e:
                    self.memberList = []
                    self.projectList =[]                    
          
            elif os.path.exists(args[0]) and  os.path.splitext(args[0])[1]=='.xml' and os.path.getsize(args[0])==0:
                self.dataPath= args[0]
                self.depName = ''
                self.memberList = []
                self.projectList =[]
            
            else:
                print 'Invalid path passed!'
        else:
            print 'pleas pass the data file(*.xml)'
        
        
    def setDepName(self,name):
        self.depName = name
        try:
            xmltree = ET.parse(self.dataPath)
            root =xmltree.getroot()
            root.set('depName',name)
            xmltree.write(self.dataPath)
        except ET.ParseError,e:
            root = ET.Element('Department')
            root.set('depName',name)
            xmltree = ET.ElementTree(root)
            xmltree.write(self.dataPath)
            
    
    def getDepName(self):
        return self.depName
    
    def addMember(self,member):
        self.memberList.append(member)
        
    def deleteMember(self,member):
        try:
            self.memberList.remove(member)
        except ValueError,e:
            print e
    
    def getAllMembers(self):
        return self.memberList
    
    def addProject(self,pro):
        self.projectList.append(pro)
        
    def deleteProject(self,pro):
        try:
            self.projectList.remove(pro)
        except ValueError,e:
            print e
        
    def getAllProjects(self):
        return self.projectList
    
        

    