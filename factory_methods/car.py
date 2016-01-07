__author__ = 'wangke'

'''
工厂方法模式
模式特点：定义一个用于创建对象的接口，让子类决定实例化哪一个类。这使得一个类的实例化延迟到其子类。
程序实例：汽车类派生出奥迪汽车类和奔驰汽车类,工厂类派生出奥迪汽车工厂类和奔驰汽车工厂类,找哪个工厂生产什么型号的汽车由客户决定
'''

# 汽车
class Car(object):
    def __init__(self):
        self.engine = None
        self.brand = None

    def run(self):
        print('brand:{0} engine:{1} '.format(self.brand, self.engine))


# 奥迪A4汽车
class AudiA4Car(Car):
    def __init__(self):
        self.engine = 'A4发动机'
        self.brand = '奥迪'


# 奥迪A6汽车
class AudiA6Car(Car):
    def __init__(self):
        self.engine = 'A6发动机'
        self.brand = '奥迪'


# 奔驰GLK350
class MercedesGKL350Car(Car):
    def __init__(self):
        self.engine = 'GKL350发动机'
        self.brand = '奔驰'


# 奔驰GLK300
class MercedesGLK300Car(Car):
    def __init__(self):
        self.engine = 'GLK300发动机'
        self.brand = '奔驰'


# 汽车工厂
class CarFactory(object):
    def create(self, series):
        pass


# 奥迪汽车工厂
class AudiCarFactory(CarFactory):
    def create(self, series):
        if series.upper() == 'A4':
            return AudiA4Car()
        else:
            return AudiA6Car()


# 奔驰汽车工厂
class MercedesFactory(CarFactory):
    def create(self, series):
        if series.upper() == 'GLK300':
            return MercedesGLK300Car()
        else:
            return MercedesGKL350Car()
