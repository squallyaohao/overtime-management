#coding=utf-8


#tables header
membersTableList = [u'name',u'id',u'department',u'title'] 
projectTableList = [u'project',u'start_date',u'finish_date',u'subprojects',u'description']
subprojectTableList = [u'subproject',u'subproject_category',u'start_date',u'finish_date',u'tasks',u'subproject_description']
tasksTableList = [u'task',u'task_id',u'department',u'project',u'subproject',u'start_date',u'finish_date',u'progress',u'members',u'description']
overtimeTableList = [u'date',u'name',u'project',u'subproject',u'duration',u'meal',u'description']

projectTableHeader = [u'项目名称',u'起始时间',u'结束时间',u'展项列表',u'项目描述'] 
subprojectTableHeader =[u'展项名称',u'展项类型',u'起始时间',u'结束时间',u'任务列表',u'展项描述']
tasksTableHeader = [u'任务名称',u'起始时间',u'结束时间',u'完成进度',u'参与人员',u'任务描述']
#table values data sturcture




TableHeaderModule= [('columnLabel','varchar(20)'),('columnIndex','int'),('valueType','varchar(15)')]




proTabHeader = ['proTabHeader',
                      (u'项目编号' ,u'0' ,u'varchar(10)'),
                      (u'项目名称' ,u'1' ,u'varchar(20)'),
                      (u'起始时间' ,u'2' ,u'date'),
                      (u'结束时间' ,u'3' ,u'date'),
                      (u'项目经理' ,u'4' ,u'varchar(10)'),
                      (u'脚本负责' ,u'5' ,u'varchar(10)'), 
                      (u'平面负责' ,u'6' ,u'varchar(10)'),
                      (u'二维负责' ,u'7' ,u'varchar(10)'),
                      (u'三维负责' ,u'8' ,u'varchar(10)'),
                      (u'后期负责' ,u'9' ,u'varchar(10)'),
                      (u'软件负责' ,u'10',u'varchar(10)'),
                      (u'硬件负责' ,u'11',u'varchar(10)'),
                      (u'完成度'   ,u'12',u'float'),
                      (u'项目状态' ,u'13',u'varchar(10)'),
                      (u'项目说明' ,u'14',u'text'),]




subproTabHeader = ['subproTabHeader',
                         (u'展项编号' ,u'0' ,u'varchar(10)'),
                         (u'展项名称' ,u'1' ,u'varchar(20)'),
                         (u'项目名称' ,u'2' ,u'varchar(20)'),
                         (u'起始时间' ,u'3' ,u'date'),
                         (u'结束时间' ,u'4' ,u'date'),
                         (u'展项类型' ,u'5' ,u'varchar(10)'),
                         (u'脚本负责' ,u'6' ,u'varchar(10)'), 
                         (u'三维负责' ,u'7' ,u'varchar(10)'),
                         (u'后期负责' ,u'8' ,u'varchar(10)'),
                         (u'软件负责' ,u'9' ,u'varchar(10)'),
                         (u'硬件负责' ,u'10',u'varchar(10)'),
                         (u'完成度'   ,u'11',u'float'),
                         (u'展项状态' ,u'12',u'varchar(10)'),
                         (u'展项说明' ,u'13',u'text')]




taskTabHeader = ['taskTabHeader',
                   (u'任务编号' ,u'0' ,u'varchar(10)'),
                   (u'任务名称' ,u'1' ,u'varchar(20)'),
                   (u'项目名称' ,u'2' ,u'varchar(20)'),                   
                   (u'展项名称' ,u'3' ,u'varchar(20)'),
                   (u'起始时间' ,u'4' ,u'date'),
                   (u'结束时间' ,u'5' ,u'date'),
                   (u'完成度'   ,u'6' ,u'float'),
                   (u'参与人员' ,u'7' ,u'varchar(225)'),
                   (u'任务状态' ,u'8' ,u'varchar(10)'),
                   (u'任务说明' ,u'9' ,u'text')]




memberTabHeader = ['memberTabHeader',
                   (u'编号',u'0',u'varchar(10)'),
                   (u'姓名',u'1',u'varchar(10)'),
                   (u'部门',u'2',u'varchar(10)'),
                   (u'职务',u'3',u'varchar(10)'),
                   (u'任务',u'4',u'text')]
 



overtime_varslist = ['overtime',
                     ('date','date'),
                     ('name','varchar(10)'),
                     ('project','varchar(20)'),
                     ('subproject','varchar(20)'),
                     ('duration','tinyint'),
                     ('meal','varchar(10)'),
                     ('description','varchar(50)')]




members_varslist = ['members',
                    ('name','varchar(10)'),
                    ('id','int'),
                    ('department','varchar(10)'),
                    ('title','varchar(10)')] 




project_varlist = ['project',
                   ('project','varchar(20)'),
                   ('start_date','date'),
                   ('finish_date','date'),
                   ('subprojects','varchar(500)'),
                   ('description','varchar(200)')]




subproject_varslist = ['subproject',
                       ('subproject','varchar(20)'),
                       ('subproject_category','varchar(10)'),
                       ('project','varchar(20)'),
                       ('start_date','date'),('finish_date','date'),
                       ('tasks','varchar(500)'),
                       ('subproject_description','varchar(200)')]




tasks_varslist = ['tasks',
                  ('task','varchar(50)'),
                  ('department','varchar(10)'),
                  ('project','varchar(20)'),
                  ('subproject','varchar(20)'),
                  ('start_date','date'),
                  ('finish_date','date'),
                  ('progress','float'),
                  ('members','varchar(200)'),
                  ('description','varchar(50)')]





tableList = [overtime_varslist,members_varslist,project_varlist,tasks_varslist,subproject_varslist]