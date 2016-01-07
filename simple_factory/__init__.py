__author__ = 'wangke'

from simple_factory.operation import Operation

if __name__ == '__main__':
    operatcion = Operation.factory('/')
    sum = operatcion.get_result(0, 0)
    print(sum)
