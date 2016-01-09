# python-patterns
python设计模式示例,不是照搬静态语言对设计模式的实现,而是尽可能用python语言的特性去实现,有的模式甚至不需要去实现.

### 不需要实现的模式

+ 原型模式:直接使用python的系统函数copy.copy()
+ 单例模式:python的模块本身就是唯一存在,所以通过模块就可以完成单例模式

### 创建型

+ [简单工厂](simple_factory.py)
+ [抽象工厂](abstract_factory.py)
+ [建造者](builder.py)
+ [工厂方法](factory_method.py)

### 结构型

+ [适配器](adpater.py)
+ [桥接模式](brigde.py)
+ [组合模式](composite.py)

### 参考
+ <https://github.com/faif/python-patterns>
+ <https://github.com/wklken/py-patterns>
+ <http://www.cnblogs.com/wuyuegb2312/archive/2013/04/09/3008320.html>
+ <http://www.cnblogs.com/houleixx/archive/2008/02/23/1078877.html> (桥接模式)