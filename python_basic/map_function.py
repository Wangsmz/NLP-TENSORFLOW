#map的参数是函数和一个可迭代的对象。返回一个迭代器
def square(x):
    return x*x

a = list(map(square,[1,2,3,4,5,6,7,8]))
print(a)