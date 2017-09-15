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

#overtime_varslist = ['overtime',('date','date'),('name','varchar(10)'),('project','varchar(20)'),('subproject','varchar(20)'),('duration','tinyint'),('meal','varchar(10)'),('description','varchar(50)')]
#members_varslist = ['members',('name','varchar(10)'),('id','int'),('department','varchar(10)'),('title','varchar(10)')] 
#project_varlist = ['project',('project','varchar(20)'),('start_date','date'),('finish_date','date'),('subprojects','varchar(500)'),('description','varchar(200)')]
#subproject_varslist = ['subproject',('subproject','varchar(20)'),('subproject_category','varchar(10)'),('project','varchar(20)'),('start_date','date'),('finish_date','date'),('tasks','varchar(500)'),('subproject_description','varchar(200)')]
#tasks_varslist = ['tasks',('task','varchar(50)'),('department','varchar(10)'),('project','varchar(20)'),('subproject','varchar(20)'),('start_date','date'),('finish_date','date'),('progress','float'),('members','varchar(200)'),('description','varchar(50)')]

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
    print statement
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
def sqlQuerysState(table='',condition={}):
    if len(condition.keys())>0:
        statement = "select * from " + table + " where "
        timequery = ''
        namequery = ''    
        projectquery = ''
        subprojectquery = ''
        #query date
        if condition.has_key('date'):
            timequery = "(date>'" + condition['date'][0] + "' or date='" + condition['date'][0] + "') and (date<'" + condition['date'][1] + "' or date='" + condition['date'][1] + "') and "
        
        #query name
        if condition.has_key('name'):
            if condition['name'] != '*':
                namequery = "name='" + condition['name'] + "' and "
            else:
                namequery = "name like '%' and "
        
        #query project
        if condition.has_key('project'): 
            if condition['project'] != '*':
                projectquery = "project='" + condition['project'] + "' and "
            else:
                projectquery = "project like '%' and "
        
        #query subproject
        if condition.has_key('subproject'): 
            if condition['subproject']!='*':
                subprojectquery = "subproject='" + condition['subproject'] + "' and "
            else:
                subprojectquery = "subproject like '%' and "
            
    
        statement = statement + timequery + namequery + projectquery + subprojectquery
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
#Test fuctions
#===================================================================================================

#generate a overtime list
def overtimesheet():
    memberlist = ('姚灏','孙林','王恒','苏里找','万涛涛','张磊','郑伟','张强')
    projectlist = ('郑州园博园','中国科技馆','滁州科技馆','大河生命馆','长江文明馆')
    meallist = (' ','米饭','水饺','肉丝面','鸡蛋面')
    varlist = []
    for i in range(10):
        date = '2017-7-' + str(random.randint(1,10))
        member = memberlist[random.randint(0,len(memberlist)-1)]
        project = projectlist[random.randint(0,len(projectlist)-1)]
        duration = str(random.randint(1,4))
        meal = meallist[random.randint(0,len(meallist)-1)]
        #because this *.py file has been declared using utf8 coding,so we need to decode every piece of chinese data using utf8
        #before we pass it to other functions to generate proper sql statement
        var = [date,member,project,duration,meal]
        varlist.append(var)
    return varlist



def initSQL(dbname='',table='',varlist=[]):
    #connect to local sql server
    conn = sql.connect(host='localhost',user ='root',passwd ='123456',db=dbname,charset='utf8')
    cur = conn.cursor()
    for var in varlist:
        s = sqlInsertState(table,var)
        cur.execute(s)      
    conn.commit()
    cur.close()
    conn.close()



    
        
def updateSQL(dbname='',table='',varlist=[]):
    conn = sql.connect(host='localhost',user ='root',passwd ='123456',db=dbname,charset='utf8')
    cur = conn.cursor()
    for var in varlist:
        var[3] = str(int(var[3])+10)
        var[4] = ' '
        s=sqlUpdateState(table,var)
        print s
        cur.execute(s)
    conn.commit()
    cur.close()
    conn.close()
    


def deleteSQL(dbname='',table='',condition={}):
    conn = sql.connect(host='localhost',user ='root',passwd ='123456',db=dbname,charset='utf8')
    cur = conn.cursor()
    statement = sqldeletState(table,condition)
    print statement
    cur.execute(statement)
    conn.commit()
    cur.close()
    conn.close()    




def querySQL(dbname='',table='',condition={}):
    conn = sql.connect(host='localhost',user ='root',passwd ='123456',db=dbname,charset='utf8')
    statement = sqlQuerysState(table, condition)
    print statement
    cur.execute(statement)
    conn.commit()
    data = cur.fetchone()
    while data is not None:
        print data
        data = cur.fetchone()
    cur.close()
    conn.close()



def querySQLPandas(dbname='',table='',condition={}):
    conn = sql.connect(host='localhost',user ='root',passwd ='123456',db=dbname,charset='utf8')
    statement = sqlQuerysState(table, condition)
    df = pd.read_sql(statement, conn, index_col='date')
    print df





if __name__=='__main__':
    #varlist = overtimesheet()
    #initSQL('myfirstdb','overtime',varlist)
    #updateSQL('myfirstdb','overtime',varlist)
    #con = {'date':'2017-07-09','name':'孙林'.decode('utf-8')}
    #deleteSQL('myfirstdb','overtime',con)
    #query_dict = {'date':['2017-07-08','2017-07-10']}
    #querySQL('myfirstdb','overtime',query_dict)
    #querySQLPandas('myfirstdb','overtime',query_dict)
    initDatabase()