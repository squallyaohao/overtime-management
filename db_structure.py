#coding=utf-8


#tables header
membersTableList = [u'name',u'id',u'department',u'title'] 
projectTableList = [u'project',u'start_date',u'finish_date',u'subprojects',u'description']
subprojectTableList = [u'subproject',u'subproject_category',u'start_date',u'finish_date',u'tasks',u'subproject_description']
tasksTableList = [u'task',u'task_id',u'department',u'project',u'subproject',u'start_date',u'finish_date',u'progress',u'members',u'description']
overtimeTableList = [u'date',u'name',u'project',u'subproject',u'duration',u'meal',u'description']


#table values data sturcture
overtime_varslist = ['overtime',('date','date'),('name','varchar(10)'),('project','varchar(20)'),('subproject','varchar(20)'),('duration','tinyint'),('meal','varchar(10)'),('description','varchar(50)')]
members_varslist = ['members',('name','varchar(10)'),('id','int'),('department','varchar(10)'),('title','varchar(10)')] 
project_varlist = ['project',('project','varchar(20)'),('start_date','date'),('finish_date','date'),('subprojects','varchar(500)'),('description','varchar(200)')]
subproject_varslist = ['subproject',('subproject','varchar(20)'),('subproject_category','varchar(10)'),('project','varchar(20)'),('start_date','date'),('finish_date','date'),('tasks','varchar(500)'),('subproject_description','varchar(200)')]
tasks_varslist = ['tasks',('task','varchar(50)'),('department','varchar(10)'),('project','varchar(20)'),('subproject','varchar(20)'),('start_date','date'),('finish_date','date'),('progress','float'),('members','varchar(200)'),('description','varchar(50)')]

tableList = [overtime_varslist,members_varslist,project_varlist,tasks_varslist,subproject_varslist]