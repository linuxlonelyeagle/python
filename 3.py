import pandas as pd
import numpy as np
model = pd.read_excel("./model.xls")

# 定义标准差标准化函数
def standardscaler(data):
    data = (data-data.mean())/data.std()
    return data
#自定义离差 标准化函数
def MINMAXScale(data):
    data = (data - data.min()) / (data.max() - data.min())
    return data
#自定义小数定标标准化函数
def Decimalscaler(data):
    data  = data/10**np.ceol(np.log10(data.abs().max()))
    return data


data1 = standardscaler(model['线损指标'])
print(data1)
data2 = standardscaler(model[' 告警类指标  '])
print(data2)
data3 = standardscaler(model['是否窃漏电'])
print(data3)
