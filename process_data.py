# -*- coding: utf-8 -*-
import  mysql.connector as connector
import string
import time
import numpy as np
import pandas as pd
from numpy.linalg import inv
from numpy import dot
time1 = time.time()
mysql = connector.connect(user='root',password = '00011122q', host = '127.0.0.1',buffered = True)
cursor = mysql.cursor()
use_database =  "use bigdata"
select_all_fine = "select * from table_1 where var1 is not null "
for i in range(2,69):
    select_all_fine +=" and var{} is not null" .format(i)
select_fine = []
module = "select * from table_1 where var{} is not null"
for i in range(1,69) :
     select_fine.append(module.format(i))
# print(select_fine)
# print(select_all_fine)
cursor.execute(use_database)
cursor.execute(select_all_fine)

# cursor.execute(select_fine[2])
# print(cursor.fetchall().__len__())
times =[]
var = [ []  for i in range(68)]
one = cursor.fetchone()
while one is not None:
             times.append(one[0])
             for i in range(2,70):
                    var[i-2].append(one[i])
             one = cursor.fetchone()

times_ = np.array(times)
var_ = np.array(var)
print(times_.shape)
print(var_.shape)

# 正规方程法
# var_ = var_.T
for i in range(68):
    X = var_[:, ]
    Y = var_[:, i][:, np.newaxis]
    print(X.shape)
    print(Y.shape)
    theta_n = dot(dot(inv(dot(X.T, X)), X.T), Y)  # theta = (X'X)^(-1)X'Y
    print i


# 批量梯度下降法
# theta_g = np.array([1.0]*67)  # 初始化theta
# theta_g = theta_g.reshape(67, 1)
# alpha = 0.1
# temp = theta_g
# J = pd.Series(np.arange(800, dtype=float))
# for k in range(800):
#     # theta j := theta j + alpha*(yi - h(xi))*xi
#     for i in range(67):
#             temp[i] = theta_g[i] + alpha * np.sum((Y - dot(X, theta_g)) * X[:,i]) / 150.
#
#     # J[i] = 0.5 * np.sum((Y - dot(X, theta_g)) ** 2)  # 计算损失函数值
#     theta_g = temp  # 更新theta
#     print(k)
# print theta_g


time2 = time.time()
print(time2-time1)
# print(str(time[0][0]))
# query = "select var67 from table_1 where ts = '{}'"
# s = query.format(time[0][0])
# var67 =np.empty(shape=(time.__len__(),1))
# for  i in range(time.__len__()):
#     cursor.execute(query.format(time[i][0]))
#     tem = cursor.fetchall()
#     var67[i][0] = tem[0][0]
#     print(i)
# print(var67)

# print(cursor.fetchall())
cursor.close()
mysql.close()