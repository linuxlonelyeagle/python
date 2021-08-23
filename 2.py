import pandas as pd
data1 = pd.read_csv('ele_loss.csv',encoding='gbk')
data2 = pd.read_csv('alarm.csv',encoding='gbk')
print(data1.shape)
print(data2.shape)
print(data1)
print(data2)
data3 = pd.concat([data1,data2],axis=1)    #   列连接
print(data3)
data3 = pd.concat([data1,data2],axis=0)     # 行连接
print(data3)
data3 = pd.merge(data1,data2,left_on=['ID','date'],right_on=['ID','date'],how = 'outer')
print(data3)
data3 = pd.merge(data1,data2,left_on=['ID','date'],right_on=['ID','date'],how = 'inner')
print(data3)





