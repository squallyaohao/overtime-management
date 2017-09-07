#File include declareation and denfinition of Class Department
#coding=utf-8

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
                    self.depName = root.get('depName').encode('utf-8')
                    print 'Department name: '+ root.get('depName')
                except AttributeError,e:
                    self.depName = ''
                    print 'Department name: '

                #loop all member and get their names
                try:
                    for member in root.iter('member'):
                        name = member.get('name')
                        self.memberList.add(name.encode('utf-8'))
                        print 'Department has member: '+name
                except AttributeError,e:
                    print e
                    self.memberList = []
                
                #loop all projects and get their names
                try:
                    for project in root.iter('project'):
                        pro = project.get('project-name')
                        self.projectList.add(pro.encode('utf-8'))
                        print 'Department has project: '+ pro
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
        
        
    def setDepName(self,name):
        self.depName = name
        xmltree = ET.parse(self.dataPath)
        root = xmltree.getroot()
        root.set('depName',name.decode('utf-8'))
        xmltree.write(self.dataPath )
            
    
    def getDepName(self):
        return self.depName.decode('utf-8')
    
    def addMember(self,member):
        member = member
        self.memberList.add(member)
        xmltree = ET.parse(self.dataPath)
        memberList = xmltree.find('MemberList')
        memberList.clear()
        for mem in self.memberList:
            newMember = ET.SubElement(memberList,'member')
            newMember.set('name',mem.decode('utf-8'))
            print 'add member: '+newMember.attrib['name']
        xmltree.write(self.dataPath )
        
    def deleteMember(self,name):
        try:
            self.memberList.remove(name)
        except ValueError,e:
            print e
        xmltree = ET.parse(self.dataPath)
        memberlist = xmltree.getroot().find('MemberList')
        for member in memberlist.findall('member'):
            if member.get('name') == name.decode('utf-8'):
                memberlist.remove(member)
        xmltree.write(self.dataPath)
        
    
    def getAllMembers(self):
        return self.memberList

    
    def addProject(self,project):
        self.projectList.add(project)          
        xmltree = ET.parse(self.dataPath)
        projectList = xmltree.find('ProjectList')
        projectList.clear()
        for pro in self.projectList:
            newProject = ET.SubElement(projectList,'project')
            newProject.set('project-name',pro.decode('utf-8'))
            print 'add project: '+newProject.attrib['project-name']
        xmltree.write(self.dataPath)   
        
    def deleteProject(self,pro):
        try:
            self.projectList.remove(pro)
        except ValueError,e:
            print e
        xmltree = ET.parse(self.dataPath)
        projectlist = xmltree.getroot().find('ProjectList')
        for project in projectlist.findall('project'):
            if project.get('project-name') == pro.decode('utf-8'):
                projectlist.remove(project)
        xmltree.write(self.dataPath)        
        
    def getAllProjects(self):
        return self.projectList
        


def testIntializeDepartment(path):
    a = Department(path)
    a.setDepName('三维')
    a.addMember('姚灏')
    a.addMember('孙林')
    a.addMember('孙林')
    a.addProject('遵义科技馆')
    a.addProject('滁州科技馆')    
    a.addProject('滁州科技馆')
    
def testChangeDepartment(path):
    a = Department(path)
    print a.getDepName()
    
    a.setDepName('二维')
    a.addMember('姚灏')
    print a.getAllMembers()
    a.deleteMember('姚灏')
    print a.getAllMembers()
    a.addProject('中国科技馆')
    print a.getAllProjects()
    a.deleteProject('中国科技馆')
    print a.getAllProjects()
    
if __name__ == '__main__':
    #testIntializeDepartment('D:\Dev\overtime-management\department1.xml')
    testChangeDepartment('D:\Dev\overtime-management\department1.xml')