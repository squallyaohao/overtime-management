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
                    print '部门名称：'.decode('utf-8') + root.get('depName')
                except AttributeError,e:
                    self.depName = ''
                    print '部门名称：'.decode('utf-8') 

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
        
        
    def setDepName(self,name):
        self.depName = name
        xmltree = ET.parse(self.dataPath)
        root = xmltree.getroot()
        root.set('depName',name.decode('utf-8'))
        xmltree.write(self.dataPath )
            
    
    def getDepName(self):
        print '部门名称： '.decode('utf-8') +self.depName.decode('utf-8')
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
        
    
    def getAllMembers(self):
        print '成员列表： '.decode('utf-8')
        for mem in self.memberList:
            print '\t'+mem.decode('utf-8')
        return self.memberList

    
    def addProject(self,project):
        if project not in self.projectList:
            self.projectList.add(project)          
            print '添加项目： '.decode('utf-8') + project.decode('utf-8')
        xmltree = ET.parse(self.dataPath)
        projectList = xmltree.find('ProjectList')
        projectList.clear()
        for pro in self.projectList:
            newProject = ET.SubElement(projectList,'project')
            newProject.set('project-name',pro.decode('utf-8'))
        xmltree.write(self.dataPath)   
        
    def deleteProject(self,pro):
        if pro in self.projectList:
            self.projectList.remove(pro)
        xmltree = ET.parse(self.dataPath)
        projectlist = xmltree.getroot().find('ProjectList')
        for project in projectlist.findall('project'):
            if project.get('project-name') == pro.decode('utf-8'):
                projectlist.remove(project)
        xmltree.write(self.dataPath)        
        
    def getAllProjects(self):
        print '项目列表： '.decode('utf-8')
        for pro in self.projectList:
            print '\t'+pro.decode('utf-8')
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
    
    a.setDepName('二维')
    a.addMember('姚灏')
    a.deleteMember('姚灏')
    a.addProject('中国科技馆')
    a.deleteProject('中国科技馆')

if __name__ == '__main__':
    #testIntializeDepartment('F:\Dev\overtime-management\department1.xml')
    testChangeDepartment('F:\Dev\overtime-management\department1.xml')