import onnx
model = onnx.load("../onnx_files/keras-classification_1.onnx")
# 检查模型格式是否完整及正确
onnx.checker.check_model(model)
# 获取输入层层，包含层名称、维度信息
input = model.graph.input
#同理
output = model.graph.output
print(output)