#在这个模块里使用keras生成的模型
from keras.models import load_model
from keras.datasets import reuters
from utility.vectorization import vectorization
import numpy as np
model = load_model("./models/2020.12.15-16.36.37classification_1.h5")
(train_data, train_labels), (test_data, test_labels) = reuters.load_data(num_words=10000)

x_data = vectorization(test_data,10000)

predictions = model.predict(x_data)

print(predictions[0].shape, np.sum(predictions[0]),np.argmax(predictions[0]))
#--------------------------------------------------------------------------------------------

