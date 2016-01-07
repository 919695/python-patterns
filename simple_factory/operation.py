__author__ = 'wangke'

'''
简单工厂模式
模式特点：工厂根据条件产生不同功能的类。
程序实例：四则运算计算器，根据用户的输入产生相应的运算类，用这个运算类处理具体的运算。

---------------------------------------------

Operation 抽象基类
get_result 方法没有实现,在子类实现
factory 标记为类方法,该方法在类未实例化前就可以使用

'''


class Operation(object):
    def __init__(self):
        pass

    def get_result(self, op1, op2):
        pass


class OperationAdd(Operation):
    def get_result(self, op1, op2):
        return op1 + op2


class OperationSub(Operation):
    def get_result(self, op1, op2):
        return op1 - op2


class OperationMul(Operation):
    def get_result(self, op1, op2):
        return op1 * op2


class OperationDiv(Operation):
    def get_result(self, op1, op2):
        try:
            sum = op1 / op2
        except ZeroDivisionError:
            return 0
        return sum


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
