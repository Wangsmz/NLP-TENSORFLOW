import os

from pypmml import Model

model = Model.load("./pmml_files/decision_tree1.pmml")

print(model.predict([[1, 2, 3, 1], [2, 4, 1, 5], [7, 8, 3, 6], [4, 8, 4, 7], [2, 5, 6, 9]]))



import tensorflow as tf

w = tf.Variable(1.0,name='weight')
b = tf.Variable(2.0,name='bias')
saver = tf.train.Saver({'weight1':b,'bias1':w})
with tf.Session() as sess:
    tf.global_variables_initializer().run()
    saver.save(sess,"./temp_files/test.ckpt")
from tensorflow.python.tools.inspect_checkpoint import print_tensors_in_checkpoint_file
print_tensors_in_checkpoint_file("./temp_files/test.ckpt",None,True)

