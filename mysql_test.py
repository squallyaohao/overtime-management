#coding=utf-8
#this file is a test file
#in this py,we define some functions used to test connection between client and MySQL server 
#also,we do some simle manipulation to our database

import sys
import os.path
import pandas as pd
import xml.etree.ElementInclude as ET
import _mysql as sql
import _mysql_exceptions as sql_excep

def testSQL():
    conn = sql.connect(host='localhost',user ='yaohao',passwd ='123456',db='myfirstdb')
    print 'afdasfdasfa'
    return conn



if __name__=='__main__':
    testSQL()