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
