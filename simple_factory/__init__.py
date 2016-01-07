__author__ = 'wangke'

from simple_factory.operation import OperationFactory

if __name__ == '__main__':
    operatcion = OperationFactory.create('/')
    sum = operatcion.get_result(0, 0)
    print(sum)
