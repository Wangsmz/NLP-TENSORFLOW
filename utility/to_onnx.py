import keras2onnx
import datetime
"""
1.对函数的参数进行解释
1.1 model:即是fit后的model,转化为onnx文件的原料
1.2 skeleton：即是模型的所属的框架
1.3
"""
def convert_to_onnx(model):
    onnx_model = keras2onnx.convert_keras(model, model.name)

    # Add metadata to the ONNX model.
    meta = onnx_model.metadata_props.add()
    meta.key = "creation_date"
    meta.value = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    meta = onnx_model.metadata_props.add()
    meta.key = "author"
    meta.value = 'wmingzhu'
    onnx_model.doc_string = 'reuters model'
    onnx_model.model_version = 3  # This must be an integer or long.
    keras2onnx.save_model(onnx_model,"../onnx_files/")
