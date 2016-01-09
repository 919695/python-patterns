__author__ = 'wangke'

'''
简单工厂模式
模式特点：工厂根据条件产生不同功能的类。
程序实例：四则运算计算器，根据用户的输入产生相应的运算类，用这个运算类处理具体的运算。
'''

# 产品基类
class Operation(object):
    def __init__(self):
        pass

    def get_result(self, op1, op2):
        pass


# Add产品类
class OperationAdd(Operation):
    def get_result(self, op1, op2):
        return op1 + op2


# Sub产品类
class OperationSub(Operation):
    def get_result(self, op1, op2):
        return op1 - op2


# Mul产品类
class OperationMul(Operation):
    def get_result(self, op1, op2):
        return op1 * op2


# Div产品类
class OperationDiv(Operation):
    def get_result(self, op1, op2):
        try:
            sum = op1 / op2
        except ZeroDivisionError:
            return 0
        return sum


# 产品工厂
class OperationFactory(object):
    @staticmethod
    def create(ch):
        if ch == '+':
            return OperationAdd()
        elif ch == '-':
            return OperationSub()
        elif ch == '*':
            return OperationMul()
        elif ch == '/':
            return OperationDiv()
        pass


if __name__ == '__main__':
    operatcion = OperationFactory.create('/')
    sum = operatcion.get_result(0, 0)
    print(sum)
