import  mysql.connector as connector

mysql = connector.connect(user='root',password = '00011122q', host = '127.0.0.1')
use_database =  "use bigdata"
set_local_infile = "set global local_infile = 'ON' "
create_table = "create table if not exists table_{} (ts datetime not null,id int not null,var1 double default null,var2 double default null,var3 double default null,var4 double default null,var5 double default null,var6 double default null, var7 double default null,var8 double default null,var9 double default null,var10 double default null,var11 double default null,var12 double default null,var13 double default null,var14 double default null,var15 double default null,var16 int default null,var17 double default null,var18 double default null,var19 double default null,var20 int default null,var21 double default null,var22 double default null,var23 double default null,var24 double default null,var25 double default null,var26 double default null,var27 double default null,var28 double default null,var29 double default null,var30 double default null,var31 double default null,var32 double default null,var33 double default null,var34 double default null,var35 double default null,var36 double default null,var37 double default null,var38 double default null,var39 double default null,var40 double default null,var41 double default null,var42 double default null,var43 double default null,var44 double default null,var45 double default null,var46 double default null,var47 int default null,var48 double default null,var49 double default null,var50 double default null,var51 double default null,var52 double default null,var53 bool default null,var54 double default null,var55 double default null,var56 double default null,var57 double default null,var58 double default null,var59 double default null,var60 double default null,var61 double default null,var62 double default null,var63 double default null,var64 double default null,var65 double default null,var66 bool default null,var67 double default null,var68 double default null)"
load_file = "load data local infile '/home/kai/Downloads/data/{}/201807~.csv' into table table_{} fields terminated by ',' OPTIONALLY ENCLOSED BY '\"' lines terminated by '\n' ignore 1 lines "
select_null ="select ts from table_{} where var{} is null "
cursor = mysql.cursor()
cursor.execute(use_database)
cursor.execute(set_local_infile)
for i in range(1,34):
    cursor.execute(create_table.format(i))
    cursor.execute(load_file.format(i,i))
    for k in range(1, 69):
        cursor.execute(select_null.format(i,k))
        tem = cursor.fetchall()  
        print('{} {}'.format(k, tem.__len__()))
