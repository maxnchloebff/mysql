#coding:utf-8
import mysql.connector as connector
# import numpy as np
import re

# 首先预处理数据，由于数据中存在，，这样表示空值的数据，我们的操作是将这样的，，变为,\N, 这样有利于mysql load数据时的操作，不然空值会被自然设置为0
f = file('/home/kai/Downloads/data/001/201807.csv') #这里的路径是你csv存储的路径，绝对路径！
# f2 = file('/home/kai/Downloads/data/001/201807~.csv','w')
# for line in f:
#     f2.write(re.sub(r',,',r',\N,',line))
# f2.close()
# f.close()
#  下面是最标准的连接mysql的方法，user指的是用户名，之后是密码，buffered要职位true，host是localhost，故而是127.0.0.1
mysql = connector.connect(user='root', password='00011122q',buffered=True,host='127.0.0.1')
#  cursor 可理解为光标，在数据库中移动的光标，用于处理mysql命令，并且在cursor.feychall()中返回所查询的值
cursor = mysql.cursor()
# 创建bigdata数据库
cursor.execute("create database if not exists bigdata")
#声明使用bigdata
cursor.execute("use bigdata")
#打开这个模式，以便可以将外部文件数据load进如mysql
cursor.execute("set global local_infile = 'ON' ")
# 如果存在的话，删除table001
cursor.execute("drop table if exists table_001 ")
#创建一个新的table001，将默认值设置为null
cursor.execute("create table if not exists table_001 (ts datetime not null,id int not null,var1 double default null,var2 double default null,var3 double default null,var4 double default null,var5 double default null,var6 double default null, var7 double default null,var8 double default null,var9 double default null,var10 double default null,var11 double default null,var12 double default null,var13 double default null,var14 double default null,var15 double default null,var16 int default null,var17 double default null,var18 double default null,var19 double default null,var20 int default null,var21 double default null,var22 double default null,var23 double default null,var24 double default null,var25 double default null,var26 double default null,var27 double default null,var28 double default null,var29 double default null,var30 double default null,var31 double default null,var32 double default null,var33 double default null,var34 double default null,var35 double default null,var36 double default null,var37 double default null,var38 double default null,var39 double default null,var40 double default null,var41 double default null,var42 double default null,var43 double default null,var44 double default null,var45 double default null,var46 double default null,var47 int default null,var48 double default null,var49 double default null,var50 double default null,var51 double default null,var52 double default null,var53 bool default null,var54 double default null,var55 double default null,var56 double default null,var57 double default null,var58 double default null,var59 double default null,var60 double default null,var61 double default null,var62 double default null,var63 double default null,var64 double default null,var65 double default null,var66 bool default null,var67 double default null,var68 double default null) ")
#将外部csv文件load进入table_001中
# cursor.execute("load data local infile '/home/kai/Downloads/data/001/201807~.csv' into table table_001 fields terminated by ',' OPTIONALLY ENCLOSED BY '\"' lines terminated by '\n' ignore 1 lines ")
# 接下来挑选其中有null值的row，下面的select_null字符串代表了mysql中最为常见的选择命令，{}中是待填入的参数（1-68），下面这句话的意思就是从table001中选出var{}值为null的行，并返回他们这一行的ts值，返回的是一个list
select_null ="select ts from table_001 where var{} is null "
null_rows = []
for i in range(1,69):
    cursor.execute(select_null.format(i))
    tem = cursor.fetchall()#这是一个list，里面存放的是每一个var值为null的行的ts的值
    print('{} {}'.format(i,tem.__len__()) ) # 打印每一个tem中有多少行存在null值

cursor.close()
mysql.close()
