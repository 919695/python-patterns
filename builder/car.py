__author__ = 'wangke'

from abc import ABCMeta, abstractmethod

"""
建造者模式
模式特点:将一个复杂对象的构建与它的表示分离, 使得同样的构建过程可以创建不同的表示
        用户只需指定需要建造的类型, 不需要知道具体地建造过程和细节
        建造者模式是在当创建复杂对象的算法应该独立于该对象的组成部分以及它们的装配方式时适用的模式
程序实例:不同的汽车建造者可以建造出不同的汽车
"""

# 指挥者
class Director(object):
    @staticmethod
    def construct_builder(builder):
        builder.add_name()
        builder.add_brand()
        builder.add_engine()
        pass


# 汽车
class Car(object):
    def __init__(self):
        self.name = None
        self.brand = None
        self.engine = None

    def run(self):
        print('{0}汽车装载了{1}发动机在行驶...'.format(self.name, self.engine))


# 抽象建造者
class AbstractBuilder(object, metaclass=ABCMeta):
    @abstractmethod
    def add_name(self):
        pass

    @abstractmethod
    def add_brand(self):
        pass

    @abstractmethod
    def add_engine(self):
        pass

    @abstractmethod
    def create_car(self):
        pass


# 奔驰建造者
class BenzBuilder(AbstractBuilder):
    def __init__(self):
        self.__car = Car()

    def add_name(self):
        self.__car.name = 'GLK300'

    def add_brand(self):
        self.__car.brand = '奔驰'

    def add_engine(self):
        self.__car.engine = '超高速发动机'

    def create_car(self):
        return self.__car


# 奥迪建造者
class AudiBuilder(AbstractBuilder):
    def __init__(self):
        self.__car = Car()

    def add_name(self):
        self.__car.name = 'A4'

    def add_brand(self):
        self.__car.brand = '奥迪'

    def add_engine(self):
        self.__car.engine = '高速发动机'

    def create_car(self):
        return self.__car
