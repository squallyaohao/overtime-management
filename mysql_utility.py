#coding=utf-8
#this file is a test file
#in this py,we define some functions used to test connection between client and MySQL server 
#also,we do some simle manipulation to our database

import sys
import os.path
import pandas as pd
import xml.etree.ElementInclude as ET
import MySQLdb as sql
import time
import random
from db_structure import *

#===================================================================================================
#Utility fuctions
#===================================================================================================
 
hostname = 'localhost'
db = 'myfirstdb'
user = 'root'
pwd = '123456' 


tableList = [overtime_varslist,members_varslist,project_varlist,tasks_varslist,subproject_varslist]

       
#MySQL utility function
#given a table name and a list,generate insert statement used to insert new data into the table
#the list should contain a serial of data that match the format of the table 
#in this case list should be like  ['date','name','project','duration','meal']
#we use utf-8 to encode our database,so make sure every element in the list should be a unicode string
def sqlInsertState(table='',list=[]):
    insert_statement = "insert into " + table + " values('"
    for value in list:
        insert_statement = insert_statement + value + "','"
    insert_statement = insert_statement[:-2] + ");" 
    return insert_statement



#MySQL utility function
#given a table name and a list,generate update statement used to update old data into the table
#the list should contain a serial of data that match the format of the table 
#in this case list should be like ['date','name','project','duration','meal']
def sqlUpdateState(table='',varsList='',conditionList=''):
    statement = "update " + table + " set "
    for var in varsList:
        statement = statement + var[0] +"='" + var[1] + "', "
    statement = statement[:-2] + " where "
    for condition in conditionList:
        statement = statement + condition[0] + "='" + condition[1] + "' and "
    statement = statement[:-5] + ";"
    #print statement
    return statement


#MySQL utility function
#given a table name and a dict,generate delete statement used to delte row or rows from the table
#the dict must contain 1-5 keys that represent the columns of the table 
#in this case list should be like  ['date','name','project','duration','meal']
def sqldeletState(table='',condition={}):
    statement = 'delete from ' + table + ' where '
    keys = condition.keys()
    for key in keys:
        statement = statement + key + "='" + condition[key] +"' and "
    statement = statement[:-5] + ';'
    return statement



#MySQL utility function
#def sqlQuerysState(table='',condition={}):
    #if len(condition.keys())>0:
        #statement = "select * from " + table + " where "
        #timequery = ''
        #namequery = ''    
        #projectquery = ''
        #subprojectquery = ''
        ##query date
        #if condition.has_key('date'):
            #timequery = "(date>'" + condition['date'][0] + "' or date='" + condition['date'][0] + "') and (date<'" + condition['date'][1] + "' or date='" + condition['date'][1] + "') and "
        
        ##query name
        #if condition.has_key('name'):
            #if condition['name'] != '*':
                #namequery = "name='" + condition['name'] + "' and "
            #else:
                #namequery = "name like '%' and "
        
        ##query project
        #if condition.has_key('project'): 
            #if condition['project'] != '*':
                #projectquery = "project='" + condition['project'] + "' and "
            #else:
                #projectquery = "project like '%' and "
        
        ##query subproject
        #if condition.has_key('subproject'): 
            #if condition['subproject']!='*':
                #subprojectquery = "subproject='" + condition['subproject'] + "' and "
            #else:
                #subprojectquery = "subproject like '%' and "
            
    
        #statement = statement + timequery + namequery + projectquery + subprojectquery
        #statement = statement[:-5] + ";"
    #else:
        #statement = "select * from " + table + ";"
    ##print statement
    #return statement
    


def sqlQueryState(table='',condition={}):
    if len(condition.keys())>0:
        statement = "select * from " + table + " where "
        for key in condition:
            if type(condition[key]) == type((1,2)) and len(condition[key]) == 2:
                statement = statement + "(" + key + ">'" + condition[key][0] + "' or " + key + "='" + condition[key][0] + \
                "') and (" + \
                key + "<'" + condition[key][1] + "' or "+ key + "='" + condition[key][1] + "') and "
            else:
                if condition[key] != '*':
                    statement = statement + key + "='" + condition[key] + "' and "
                else:
                    statement = statement + key + " like '%' and "
        statement = statement[:-5] + ";"
    else:
        statement = "select * from " + table + ";"    
    print statement
    return statement



def createTableStatement(name='',varlist=[]):
    statement = 'create table ' + name +'('
    for var in varlist:
        statement = statement + var[0] + ' ' + var[1] +','    
    statement = statement[:-1]+');'
    return statement

def initDatabase():
    conn = sql.connect(hostname,user,pwd,db,charset='utf8')
    cursor = conn.cursor()
    for table in tableList:
        statement = createTableStatement(table[0],table[1:])
        try:
            cursor.execute(statement)
            conn.commit()
            print 'create table' + table[0]
        except :
            continue    
    cursor.close()
    conn.close()



#===================================================================================================




if __name__=='__main__':
    #initDatabase()
    condition = {}
    condition['date'] = ('2010-01-01','2012-02-02')
    condition['count'] = ('1','2')
    condition['name'] = 'lee'
    condition['job'] = 'worker'
    table = 'test'
    statement = sqlQueryState(table,condition)
    print statement