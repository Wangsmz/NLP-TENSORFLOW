"""
with是从Python2.5引入的一个新的语法，它是一种上下文管理协议，目的在于从流程图中把 try,except 和finally 关键字和资源分配释放相关代码统统去掉，简化try….except….finlally的处理流程。

with通过__enter__方法初始化，然后在__exit__中做善后以及处理异常。

所以使用with处理的对象必须有__enter__()和__exit__()这两个方法。

其中__enter__()方法在语句体（with语句包裹起来的代码块）执行之前进入运行，__exit__()方法在语句体执行完毕退出后运行。

with 语句适用于对资源进行访问的场合，确保不管使用过程中是否发生异常都会执行必要的“清理”操作，释放资源，比如文件使用后自动关闭、线程中锁的自动获取和释放等。
"""
#------------------------
"""
with expression [as target]:
     body

参数说明：

expression：是一个需要执行的表达式；

target：是一个变量或者元组，存储的是expression表达式执行返回的结果，可选参数。
例:with open(file,mode,encoding) as f:
        body
"""
"""
with语句的工作原理：

紧跟with后面的语句会被求值，__enter__()方法被调用,返回一个对象，这个方法的返回值将被赋值给as
键字后面的变量，当with后面的代码块全部被执行完之后，将调用前面返回对象的__exit__()方法。

 with语句最关键的地方在于被求值对象必须有__enter__()和__exit__()这两个方法，那我们就可以通过自己实现这两方法来自定义with语句处理异常。

"""
class opened(object):
    def __init__(self,filename):
        self.handle=open(filename)
        print("Resource:%s"%filename)

    def __enter__(self):
        print("[enter%s]: Allocate resource."%self.handle)
        return self.handle#可以返回不同的对象

    def __exit__(self,exc_type,exc_value,exc_trackback):
        print("[Exit %s]: Free resource." %self.handle)
        if exc_trackback is None:
            print("[Exit %s]:Exited without exception."%self.handle)
            self.handle.close()
        else:
            print("[Exit %s]: Exited with exception raised."%self.handle)
        return False # 可以省略，缺省的None也是被看做是False


with opened('../testfiles/1.txt') as fp:
    print(fp.readlines())


"""
 with EXPR as VAR:
    BLOCK
其中EXPR可以是任意表达式；as VAR是可选的。其一般的执行过程是这样的：

执行EXPR，生成上下文管理器context_manager；
获取上下文管理器的__exit()__方法，并保存起来用于之后的调用；
调用上下文管理器的__enter__()方法；如果使用了as子句，则将__enter__()方法的返回值赋值给as子句中的VAR；
执行BLOCK中的表达式；
不管是否执行过程中是否发生了异常，执行上下文管理器的__exit__()方法，__exit__()方法负责执行“清理”工作，如释放资源等。如果执行过程中没有出现异常，或者语句体中执行了语句break/continue/return，则以None作为参数调用__exit__(None, None, None)；如果执行过程中出现异常，则使用sys.exc_info得到的异常信息为参数调用__exit__(exc_type, exc_value, exc_traceback)；
出现异常时，如果__exit__(type, value, traceback)返回False，则会重新抛出异常，让with之外的语句逻辑来处理异常，这也是通用做法；如果返回True，则忽略异常，不再对异常进行处理。
"""