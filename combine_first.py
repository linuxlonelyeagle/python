import pandas as pd
import numpy as np
dict1 = {'ID':[1,2,3,4,5,6,7,8,9],'System':['win10','win10',np.nan,'win10',np.nan,np.nan,'win7','win7','win8'],
'cpu':['i7','i5',np.nan,'i7',np.nan,np.nan,'i5','i5','i3']}
dict2 = {'ID':[1,2,3,4,5,6,7,8,9],'System':[np.nan,np.nan,'win7',np.nan,'win8','win7',
np.nan,np.nan,np.nan],'cpu':[np.nan,np.nan,'i3',np.nan,'i7','i5',np.nan,np.nan,np.nan]}

df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)

print(df1)
print(df2)
print(df1.combine_first(df2))