__author__ = 'wangke'

from abc import ABCMeta, abstractmethod

'''
适配器模式
模式特点:类的数据和行为都正确,但是接口不符时,将类转换成符合系统接口的类
'''


class Target(object, metaclass=ABCMeta):
    @abstractmethod
    def request(self):
        pass


class Adpatee(object):
    def get_request(self):
        return 'status 200'


class Adpater(Target):
    def __init__(self):
        self.__adpatee = Adpatee()

    def request(self):
       return self.__adpatee.get_request()


if __name__ == '__main__':
    adp = Adpater()
    res = adp.request()
    print(res)
