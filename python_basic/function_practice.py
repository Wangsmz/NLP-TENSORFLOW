"""
1.如下面的函数所示，可以a:str，提示别人a参数的类型是str;这只是提示，如下所示，填入10，也不会报错，除非函数内部因为参数类型导致的错误
2.-> 类型。提示返回类型，这只是提示，如下所示提示返回列表，但是返回10并不会出错
"""
#以上叫做函数注解，可以叫做函数的元信息通过函数对象的_annotations_属性获得该信息
def getList(a:str) -> []:
    return 10
f = getList(10)
print(f)
print(getList.__annotations__)