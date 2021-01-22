from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
from utility.graphic import training_and_validation_loss

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
print(train_images[0].shape)
# print(train_images[0])
from PIL import Image

img1 = Image.fromarray(train_images[0])
img1 = img1.resize((14,28))
img1.save("./minist1.jpg")
import numpy as np
array1 = np.array(img1)
# print(array1)
