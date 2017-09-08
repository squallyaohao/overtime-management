#file containing definition of class Project
#coding=utf-8

import sys
import os.path
import xml.etree.ElementTree as ET

CATEGORY = dict({'ANI':0,'GAME':1,'TB':2})

class Project():
    def __init__(self):
        self.projectName = ''
        self.projectCategory = CATEGORY['ANI']
        self.projectDescrip = ''
        self.complete = True
        
    def setProjectName(self,name):
        pass
    
    
    def getProjectName(self):
        pass
    
    
    def setCategory(self,cat = CATEGORY['ANI']):
        pass
    
    
    def getCategory(self):
        pass
    
    
    def setComplete(self,value = True):
        pass
    
    
    def editDescrip(self,des):
        pass
    
    
    def getDescrip(self):
        pass
    
    

def textProjectInit():
    pro = Project()
    
    

if __name__=='__Main__':
    textProjectInit()