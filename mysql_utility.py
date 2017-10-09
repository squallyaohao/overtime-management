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
def sqlInsertState1(table='',list=()):
    insert_statement = "insert into " + table + " values('"
    for value in list:
        insert_statement = insert_statement + value + "','"
    insert_statement = insert_statement[:-2] + ");" 
    return insert_statement


def sqlInsertState2(table='',varsdict={}):
    print varsdict
    insert_statement = "insert into " + table + "("
    sortedKey = varsdict.keys()
    sortedKey.sort()
    for key in sortedKey:
        insert_statement = insert_statement + key + ","
    insert_statement = insert_statement[:-1] + ") values('" 
    for key in sortedKey:
        insert_statement = insert_statement + varsdict[key] + "','"
    insert_statement = insert_statement[:-2] + ");"
    return insert_statement



#MySQL utility function
#given a table name and a list,generate update statement used to update old data into the table
#the list should contain a serial of data that match the format of the table 
#in this case list should be like ['date','name','project','duration','meal']
def sqlUpdateState(table='',varsList=[],conditionList=[]):
    statement = "update " + table + " set "
    for var in varsList:
        statement = statement + var[0] +"='" + var[1] + "', "
    statement = statement[:-2] + " where "
    for condition in conditionList:
        statement = statement + condition[0] + "='" + condition[1] + "' and "
    statement = statement[:-5] + ";"
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
    return statement




def sqlQueryState2(table='',columns=[],condition={}):
    columnList = ''
    for col in columns:
        columnList = columnList + col + ","
    columnList = columnList[:-1]
    if len(condition.keys())>0:
        statement = "select " + columnList + " from " + table + " where "
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
    return statement    




def sqlCreateTableStatement(name='',varlist=[]):
    statement = 'create table ' + name +'('
    for var in varlist:
        statement = statement + var[0] + ' ' + var[1] +','    
    statement = statement[:-1]+');'
    return statement



def initDatabase():
    conn = sql.connect(hostname,user,pwd,db,charset='utf8')
    cursor = conn.cursor()
    #===create header module table===
    #statement = sqlCreateTableStatement('proTabHeader',TableHeaderModule)
    #cursor.execute(statement)
    #conn.commit()
    #statement = sqlCreateTableStatement('subproTabHeader',TableHeaderModule)
    #cursor.execute(statement)
    #conn.commit()
    #statement = sqlCreateTableStatement('taskTabHeader',TableHeaderModule)
    #cursor.execute(statement)
    #conn.commit()
    #statement = sqlCreateTableStatement('memberTabHeader',TableHeaderModule)
    #cursor.execute(statement)
    #conn.commit()
    
    #===insert columns into header tables===
    #for headertable in [proTabHeader,subproTabHeader,taskTabHeader,memberTabHeader]:
        #table = headertable[0]
        #for column in headertable[1:]:
            #statement = sqlInsertState1(table,column)
            #cursor.execute(statement)
            #conn.commit()
    
    
    #===create project table===
    #varslist = []
    #for data in proTabHeader[1:]:
        #varslist.append([data[0],data[2]])
    #statement = sqlCreateTableStatement('project', varslist)
    #cursor.execute(statement)
    #conn.commit()
    
    #varslist = []
    #for data in subproTabHeader[1:]:
        #varslist.append([data[0],data[2]])
    #statement = sqlCreateTableStatement('subproject', varslist)
    #cursor.execute(statement)
    #conn.commit()    
    
    #varslist = []
    #for data in taskTabHeader[1:]:
        #varslist.append([data[0],data[2]])
    #statement = sqlCreateTableStatement('task', varslist)
    #cursor.execute(statement)
    #conn.commit()

    varslist = []
    for data in memberTabHeader[1:]:
        varslist.append([data[0],data[2]])
    statement = sqlCreateTableStatement('member', varslist)
    cursor.execute(statement)
    conn.commit()    
    
    
    cursor.close()
    conn.close()



def dropTables():
    conn = sql.connect(hostname,user,pwd,db,charset='utf8')
    cursor = conn.cursor()    
    tableList = [u'member']
    #tableList = [u'project',u'proTabHeader','subproject',u'subproTabHeader',u'task',u'taskTabHeader',u'member',u'memberTabHeader']
    for table in tableList:
        statement = "drop table if exists "+table+";"
        cursor.execute(statement)
        conn.commit()
    cursor.close()
    conn.close()


#===================================================================================================




if __name__=='__main__':
    dropTables()
    initDatabase()