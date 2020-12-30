"""
abc.ABCMeta 可以像普通的class一样被继承，abc.ABCMeta派生的class可以被 issubclass()识别为抽象基类abc.ABCMeta的子类，但抽象基类ABCMeta不会出现在其子类的MRO（方法解析顺序）中。抽象基类中实现的方法也不
能被调用，用super()也不行。
抽象基类派生的类如果想要实例化，就必须先重新实现抽象基类中的方法，否则抽象基类的派生类会在实例化时报错。
"""
"""
1.简而言之，抽象基类相当于其他语言中的接口，不能被实例化，并且被implements后一定要实现接口里面的方法
2.在python中没有接口的概念，
"""
"""
1.指定抽象类的第一种方法

class interface(object):
    __metaclass__ = ABCMeta #指定这是一个抽象类
    @abstractmethod  #抽象方法
    def Lee(self):
        pass
2.指定抽象类的第二种方法
class A(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def greet(self):
        pass

"""
"""
抽象基类的抽象方法也可以实现，不影响实现类对它的实现，不过因为抽象基类不能实例化，所以要想使用它必须
把它同时装饰为类方法，然后用类名调用，其中第一个参数(名字习惯用cls,就像构造方法第一个参数习惯用self一样，不影响),指代的是调用它的类（可参见staticmethod_classmethod.py)
"""
import abc
class Human(metaclass=abc.ABCMeta):
    @classmethod
    @abc.abstractmethod
    def getName(cls):
        return "抽象基类的抽象方法被装饰为类方法，用类名直接调用"

    @abc.abstractmethod
    def getGender(self):
        pass

class Person1(Human):
    def __init__(s,name,gender):
        s.name = name
        s.gender = gender

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

person1 = Person1("Jack","male")
name = person1.getName()
print(name)
print(Human.getName())