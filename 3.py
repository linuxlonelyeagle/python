import pandas as pd
LogInfo = pd.read_csv('Training_LogInfo.csv')
Userupdata = pd.read_csv('Training_Userupdate.csv')
data1 = LogInfo.groupby(LogInfo['Idx'])
data2 = Userupdata.groupby(Userupdata['Idx'])
data1.agg({'LogInfo3':pd.to_datetime})
data2.agg({'UserupdateInfo2':pd.to_datetime})
print('最早时间',data1['LogInfo3'].min())
print('最晚时间',data1['LogInfo3'].max())
print('最早时间',data2['UserupdateInfo2'].min())
print('最晚时间',data2['UserupdateInfo2'].max())
print('登陆次数',data1.size())   
print('更新次数',data2.size())













