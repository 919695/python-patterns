__author__ = 'wangke'

'''
工厂方法模式
模式特点：定义一个用于创建对象的接口，让子类决定实例化哪一个类。这使得一个类的实例化延迟到其子类。
程序实例：基类雷锋类，派生出学生类和志愿者类，由这两种子类完成“学雷锋”工作。子类的创建由雷锋工厂的对应的子类完成。
'''

# 雷锋
class LeiFeng(object):
    def sweep(self):
        print("LeiFeng sweep")


# 学生
class Student(LeiFeng):
    def sweep(self):
        print("Student sweep")


# 志愿者
class Volenter(LeiFeng):
    def sweep(self):
        print("Volenter sweep")


# 雷锋创建者
class LeiFengFactory:
    @staticmethod
    def createLeiFeng():
        temp = LeiFeng()
        return temp


# 学生创建者
class StudentFactory(LeiFengFactory):
    @staticmethod
    def createLeiFeng():
        temp = Student()
        return temp


# 志愿者创建者
class VolenterFactory(LeiFengFactory):
    @staticmethod
    def createLeiFeng():
        temp = Volenter()
        return temp
