__author__ = 'wangke'

from abc import ABCMeta, abstractmethod

'''
桥接模式
模式特点:将抽象部分与实现部分分离，使它们都可以独立的变化。
程序实例:不同的人可以驾驶不同的车在不同的路上行驶
'''

# 抽象车
class AbstractCar(object, metaclass=ABCMeta):
    def __str__(self):
        return '车'


class Bus(AbstractCar):
    def __str__(self):
        return '大巴车'


class Bicycler(AbstractCar):
    def __str__(self):
        return '自行车'


# 抽象路,路桥接了车,车就可以在路上行驶了
class AbstractRoad(object, metaclass=ABCMeta):
    def __init__(self, car):
        self._car = car

    @abstractmethod
    def run(self):
        pass

    def __str__(self):
        return '公路'


class Speedway(AbstractRoad):
    def run(self):
        print('{0}在{1}上行驶'.format(self._car, self))

    def __str__(self):
        return '高速公路'


class Street(AbstractRoad):
    def run(self):
        print('{0}在{1}上行驶', self._car, self)

    def __str__(self):
        return '街道'


# 抽象人,人桥接了路,路桥接了车,人就可以驾驶车在路上行驶了
class AbstractPeople(object, metaclass=ABCMeta):
    def __init__(self, road):
        self._road = road

    @abstractmethod
    def run(self):
        pass

    def __str__(self):
        return '人'


class Man(AbstractPeople):
    def run(self):
        print('{0}驾驶{1}在{2}上行驶'.format(self, self._road._car, self._road))
        pass

    def __str__(self):
        return '男人'


class Women(AbstractPeople):
    def run(self):
        print('{0}驾驶{1}在{2}上行驶'.format(self, self._road._car, self._road))
        pass

    def __str__(self):
        return '女人'


if __name__ == '__main__':
    # 自行车在高速公路上行驶
    car = Bicycler()
    road = Speedway(car)
    road.run()

    # 男人驾驶大巴车在街道上行驶
    car = Bus()
    road = Street(car)
    people = Man(road)
    people.run()
    pass
