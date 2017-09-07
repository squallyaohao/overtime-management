#File include declareation and denfinition of Class Department

import sys
import os.path
import xml.etree.cElementTree as ET


def initXML(path):
    #check if xml file exist,otherwise create one
    if os.path.exists(path):
        xmltree = ET.parse(path)
    else:
        root = ET.Element('Department')
        xmltree = ET.ElementTree(root) 
        memberList = ET.SubElement(root,'MemberList')
        projectList = ET.SubElement(root,'ProjectList')
        xmltree = ET.ElementTree(root)
        xmltree.write(path)

    

class Department():
    def __init__(self,*args):
        self.dataPath= ''
        self.depName = ''
        self.memberList = []
        self.projectList =[]        
        if len(args)!=0 :
            if len(args)>1:
                print 'More than one argument has been passed!'
            elif os.path.exists(args[0]) and os.path.getsize(args[0])>0 and os.path.splitext(args[0])[1]=='.xml':
                print 'start initialzie'
                self.dataPath = args[0]
                xmltree = ET.parse(self.dataPath)
                root = xmltree.getroot()
                try:
                    self.depName = root.get('depName')
                    print 'Department name: '+self.depName
                except AttributeError,e:
                    self.depName = ''
                    print 'Department name: '
                try:
                    for member in root.iter('member'):
                        name = member.get('name')
                        self.memberList.append(name)
                        print 'Department has member: '+name
                except AttributeError,e:
                    print e
                    self.memberList = []
                try:
                    for project in root.iter('project'):
                        pro = project.get('project-name')
                        self.projectList.append(pro)
                        print 'Department has project: '+ pro
                except AttributeError,e:
                    print e
                    self.projectList =[]                    
          
            elif os.path.exists(args[0]) and  os.path.splitext(args[0])[1]=='.xml' and os.path.getsize(args[0])==0:
                self.dataPath= args[0]
                self.depName = ''
                self.memberList = []
                self.projectList =[]
                initXML(self.dataPath)
                
            else:
                self.dataPath= args[0]
                self.depName = ''
                self.memberList = []
                self.projectList =[]                
                initXML(args[0])
                #print 'Invalid path passed!'
        else:
            print 'pleas pass the data file(*.xml)'
        
        
    def setDepName(self,name):
        self.depName = name
        xmltree = ET.parse(self.dataPath)
        root = xmltree.getroot()
        root.set('depName',name)
        xmltree.write(self.dataPath)
            
    
    def getDepName(self):
        return self.depName
    
    def addMember(self,member):
        self.memberList.append(member)
        xmltree = ET.parse(self.dataPath)
        memberList = xmltree.find('MemberList')
        newMember = ET.SubElement(memberList,'member')
        newMember.set('name',member)
        xmltree.write(self.dataPath)
        
    def deleteMember(self,name):
        try:
            self.memberList.remove(name)
        except ValueError,e:
            print e
        xmltree = ET.parse(self.dataPath)
        memberlist = xmltree.getroot().find('MemberList')
        for member in memberlist.findall('member'):
            if member.get('name') == name:
                memberlist.remove(member)
        xmltree.write(self.dataPath)
        
    
    def getAllMembers(self):
        return self.memberList

    
    def addProject(self,project):
        self.projectList.append(project)
        xmltree = ET.parse(self.dataPath)
        projectList = xmltree.find('ProjectList')
        newProject = ET.SubElement(projectList,'project')
        newProject.set('project-name',project)
        xmltree.write(self.dataPath)        
        
    def deleteProject(self,pro):
        try:
            self.projectList.remove(pro)
        except ValueError,e:
            print e
        xmltree = ET.parse(self.dataPath)
        projectlist = xmltree.getroot().find('ProjectList')
        for project in projectlist.findall('project'):
            if project.get('project-name') == pro:
                projectlist.remove(project)
        xmltree.write(self.dataPath)        
        
    def getAllProjects(self):
        return self.projectList
    
        

    