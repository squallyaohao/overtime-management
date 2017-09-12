#coding=utf-8
#this file define the actual interface of the program and internal actions and slots

import sys
import os,os.path
import xlrd,xlwt
from xlutils import copy



def exportToExcel(path,list=[]):

    if os.path.exists(path):
        xlsrd = xlrd.open_workbook(filename=path)
        sheet = xlsrd.sheet_by_index(0)
        rows = sheet.nrows
        cols = sheet.ncols

        xlscopy = copy.copy(xlsrd)
        xlswt = xlscopy.get_sheet(0)
        for i in range(rows):
            for j in range(cols):
                xlswt.write(i,j,'')
        try:
            xlscopy.save(path)
        except IOError,e:
            return e
        
        

    xlswt = xlwt.Workbook(encoding='utf-8')
    sheet = xlswt.add_sheet('sheet0')
    for i,row in enumerate(list):
        for j,col in enumerate(row):
            sheet.write(i,j,col)      
            #print 'write row {0} col {1} vlaue: {2}'.format(str(i),str(j),col)
    try:
        xlswt.save(path)
        return 1
    except IOError,e:
        return e
        
        
        
        
                
 
 
if __name__ == '__main__':    
    exportToExcel(u'C:\\aa2.xlsx',[['a','b','c'],['d','e','f'],['g','h','l']])
        
        
        