""""
生成器函数是内部有yield关键字的函数，因为python语言里面函数就是一个对象，
那么这种带yield关键字的函数就可以叫做生成器对象generator,
也可以叫它迭代器iterator。
"""

def generator():
    x = 0
    while x < 4:
        x += 1
        yield x
#你可以这样访问每一个元素
print(next(generator()))
#也可以这样
for i in generator():
    print(i)
print(list(generator()))
print(5 in generator())
"""
上面的输出表明生成器函数其实就是一个可迭代对象，或者叫迭代器，迭代的那个地点就在yield关键字处，每运行到
这个地方就返回yield所声明的那个对象，下次迭代就从这个地方下面继续运行，但是在循环体里面，直到不满足条件(比如这里就是不满足while条件)。
所以每次迭代使用上一个状态就行了，对内存消耗的非常小。如果这个函数你使用常规的做法最终返回一个序列，比如列表，你在while循环里每次添加一个值最终输出整个列表，假如你需要的是一个上百万大小的列表，那么内存将消耗的非常多
"""
def trail():
    x = 2
    while x < 100000:
        x = x*x
        yield x

for i in trail():
    print(i)