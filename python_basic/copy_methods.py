"""
author: Mingdru,W
如果你想赋值一份对象，一般会面临以下几种情况
"""
import copy
#你想赋值一份列表
a = [1,2,3,4]
b = a
print(id(a),id(b))
b.append(5)
print(a)
#你会发现上面a和b指向同一个地址，所以改变b的值，a的值也被改变了。如果你不想这样，可以看下面
c = a[:]
d = list(a)
e = copy.copy(a)
c.append(6)
d.append(7)
e.append(8)
print(id(a),id(c),id(d),id(e),a,c,d,e)
"""
上面的输出地址和值都不一样，这说明这种复制，复制者和被复制者是独立的，他们使用不同的内存。但是如果被复制者中包含了子可变元素，
那么情况会怎样
"""
t = [[1,2,3],4,5,6]
t1 = t[:]
t2 = list(t)
t3 = copy.copy(t)
t1.append(7)
t2.append(8)
t3.append(9)
print(t,t1,t2,t3)
print(id(t),id(t1),id(t2),id(t3))
#上面的输出都不一样，这说明复制者和被复制者独立，互相不影响。但是要告诉你的是它们的可变子元素使用的却是同一个，下面给出示例
t[0].append(4)
print(t,t1,t2,t3)
print(id(t[0]),id(t1[0]))
#你会发现它们4个的第一个元素都变成了[1,2,3,4]。这说明它们的可变元素使用的是同一个。可以继续实验证明这点
t1[0].append(5)
print(t,t1,t2,t3)
t2[0].append(6)
print(t,t1,t2,t3)
t3[0].append(7)
print(t,t1,t2,t3)
#上面的拷贝称不上副本，因为你想要一个完全独立的新对象，它不会影响被拷贝的那个对象。此时可以使用copy.copy()，它是完全复制所有内容
p = [[1,2,3],4,5,6]
p1 = copy.deepcopy(p)
p1[0].append(4)
print(p,p1,id(p[0]),id(p1[0]))
#从上面的输出你可以知道p和p1是完全独立的，它们的第一个可变子元素当然也不一样

"""
上面讨论的所有内容都是基于列表的，即可变对象。那么对于像元组这种不可变得对象呢？ 很自然地，如果我是一名编程语言的设计者，对于不可变对象的
拷贝问题就可以简单处理了，因为既然不可变，就不用担心你拷贝过去拿去做什么，为了节省开销，无论怎么拷贝大家就用这一个对象。
"""
f = (1,2,3)
f1 = f
f2 = f[:]
f3 = tuple(f)
f4 = copy.copy(f)
f5 = copy.deepcopy(f)
print(id(f),id(f1),id(f2),id(f3),id(f4),id(f5))
#你会发现它们的地址都是一样的

#如果这个不可变的对象包含了可变的子元素，那么情况会怎样
g = ([1,2,3],4,5,6)
g1 = g
g2 = g[:]
g3 = tuple(g)
g4 = copy.copy(g)
g5 = copy.deepcopy(g)
g3[0].append(100)
print(g,g1,g2,g3,g4,g5)
print(id(g[0]),id(g1[0]),id(g2[0]),id(g5[0]))
#你会发现只有deepcopy的第一个元素，也就是[1,2,d]的地址是不一样的，剩下的都共用一个地址


"""
综上所有的内容可以用两句话概括：
1. 不可变的对象(包括它作为子元素）无论用什么拷贝方法，大家使用的其实是同一个对象
2. 可变的对象除了直接赋值外，其他的方法都可以做到赋值一份独立的版本。但是当它作为子元素时(无论是可变的还是不可变对象子元素)，只有deepcopy方法能实现赋值一份与它独立的内容
"""