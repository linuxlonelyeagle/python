import pandas as pd
import numpy as np
data = pd.read_csv('./Training_LogInfo.csv')      # 主表
print(pd.pivot_table(data,index = ['LogInfo3','Idx'],values=['LogInfo1'],aggfunc= [np.sum, np.mean])) # index 就是层次字段，values 要显示的值
# 我们可以通过values 对 值进行挑选
print(pd.pivot_table(data,index = ['Idx'],values=['LogInfo2'],aggfunc=[np.sum]))





