__author__ = 'wangke'

from abc import ABCMeta, abstractmethod
from functools import wraps

'''
装饰器模式
模式特点:动态地为对象增加额外的职责
程序实例:给字符串增加样式
备注:python本身就支持装饰器的语法糖@,所以python在面向切面编程是非常方便的
'''


def make_bold(fn):
    @wraps(fn)
    def wraper():
        return '<b>{0}</b>'.format(fn())

    return wraper


def make_italic(fn):
    @wraps(fn)
    def wraper():
        return '<i>{0}</i>'.format(fn())

    return wraper


@make_italic
@make_bold
def text():
    return 'hello world!'


if __name__ == '__main__':
    res = text()
    print(res)
