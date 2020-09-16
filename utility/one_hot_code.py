
import string
import numpy as np
samples = ['concatenate is the operation of combining several vectors into one','China is a country with 56 nationnalities']

#单词级ont-hot编码。
#字典序号从零开始
token_index = {}
for sample in samples:
    for word in sample.split():
        if word not in token_index:
            token_index[word] = len(token_index)

#设定句子的最大长度
max_length = 5
#初始化
results = np.zeros(shape=(len(samples),max_length,max(token_index.values())+1))

#构造
for i,sample in enumerate(samples):
    for j,word in list(enumerate(sample.split()))[:max_length]:
            index = token_index.get(word)
            results[i,j,index] = 1
        




#字符级one-hot编码



