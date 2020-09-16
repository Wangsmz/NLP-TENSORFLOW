"""
特殊方法属性（special method attribute）是Python类的一种属性，对Python而言具备特殊的含义。
虽然被定义为方法，但其实并不是打算直接当作方法使用的。通常特殊方法不会被直接调用，而是由Python
自动调用，以便对属于该类的对象的某种请求做出响应。
"""
class IteratorClass:

    def __init__(self,filepath):
        self.fileobject = open(filepath,'r',encoding='utf-8')

    #返回类的可读字符串表示
    def __str__(self):
        return "该类有特殊方法属性__getitem__，所以类对象可以被用作迭代器使用"

    #__getitem__使类具有迭代器功能。下面使用它实现读取文件的功能
    def __getitem__(self, index):
        line = self.fileobject.readline()

        if line == "":
            self.fileobject.close()
            raise IndexError

        else:
            return line

"""
上面的类可以作为读取文件的工具类。一下子读取整个文件，可能内存会吃不消，所以一行一行的读一般是我们采用的
方法，直接用这个类对象进行迭代比较方便。
"""
file_iterator = IteratorClass("..\\records\\error.txt")
print(file_iterator)

for line in file_iterator:
    print(line)

"""
解释上面的操作：
print(file_iterator)会输出一个字符串明着是因为类中定义了__str__特殊方法属性，是的对象直接可以被当作字符串
读出，实际上是python隐式调用了__str__

for line in file_iterator:这里直接把对象当作可迭代的是因为类中定义了特殊方法属性__getitem__，参数index
被使用，其实它只是for循环用来迭代的索引而已，即从0开始，1,2,3,4.....，也就是说每次迭代都是调用file_iterator.__getitem__(index)。这个函数内部由使用者自己定义，
这里的代码就是读取文件的一行，又因为将指针移到下一行是程序自己完成的不需要使用者来实现，所以迭代一次就读取了文件的一行，如果遇到了空行则视为读完了，则关闭文件，抛出异常，for循环能捕获这个异常，for循环终止
"""