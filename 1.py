import pandas as pd

def dropnullstd(data):
    beforelen = data.shape[1]
    colisnull = data.describe().loc['count'] == 0
    for i in range(len(colisnull)):
        if colisnull[i]:
            data.drop(colisnull.index[i],axis = 1, inplace = True)
    stdiszero = data.describe().loc['std'] == 0
    for i in range(len(stdiszero)):
        if stdiszero[i]:
            data.drop(stdiszero.index[i],axis = 1 ,inplace= True)
    afterlen = data.shape[1]
    print('剔除的列的数目为：',beforelen - afterlen)
    print('剔除后数据的形状为:',data.shape)

def main():
    data = pd.read_csv('Training_LogInfo.csv')
    print(data.ndim) #维度
    print(data.shape) #大小
    print(data.memory_usage) #占用的空间
    print(data.describe())    
    print(data.astype('category').describe())
    dropnullstd(data)    

main()

