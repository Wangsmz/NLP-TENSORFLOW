from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
from utility.graphic import training_and_validation_loss
import time
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

network = models.Sequential()

network.add(layers.Dense(512,activation='relu',input_shape=(28*28,)))
network.add(layers.Dense(10,activation='softmax'))

network.compile(optimizer='rmsprop',loss='categorical_crossentropy',metrics=['accuracy'])

train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 25

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

history = network.fit(train_images,train_labels,epochs=5,batch_size=128)
test_loss, test_acc = network.evaluate(test_images, test_labels)

#保存模型文件
import os
current_file = str(os.path.basename(__file__)).split(".")[0]
model_path = "../models/"+str(time.strftime("%Y.%m.%d-%H.%M.%S"))+current_file+".h5"
network.save(model_path)