import tensorflow as tf
import pathlib
print(tf.__version__)
data_root = pathlib.Path.cwd()
print(data_root)

images_root = pathlib.Path("C:\\Users\\15216\\Desktop\\data\\dataset\\images1\\jpg")
#只选用buttercup这一种花
images_buttercup = pathlib.Path("C:\\Users\\15216\\Desktop\\data\\dataset\\images1\\jpg\\buttercup")
images_path_list = list(images_buttercup.glob('*'))
print(images_path_list[0],type(images_path_list[0]))
#将图片路径转为字符串形式
images_path_list = [str(path) for path in images_path_list]
print(images_path_list[0],type(images_path_list[0]))

label_list = [str(item.name) for item in images_root.glob('*')]
print(label_list)
#将类别编上号
label_dict = sorted({(tag,name) for tag,name in enumerate(label_list)},key=lambda x:x[0],reverse=False)
print(label_dict)

#构建图片路径数据集
imagepath_dataset = tf.data.Dataset.from_tensor_slices(images_buttercup)
#使用AUTOTUNE自动调节管道参数
AUTOTUNE = tf.data.experimental.AUTOTUNE

#构建图片数据的数据集
#images_dataset =

