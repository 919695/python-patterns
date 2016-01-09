__author__ = 'wangke'

from abc import ABCMeta, abstractmethod

"""
组合模式
模式特点:将对象组合成树状结构以表示`部分-整体`的层次结构 使得用户对单个对象和组合对象的使用具有一致性
程序实例:多个子部门构成了一家完整的公司
"""

# 抽象部件
class Component(object, metaclass=ABCMeta):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def add_department(self, department):
        pass

    @abstractmethod
    def remove_department(self, department):
        pass

# 子部件
class Leaf(Component):
    def add_department(self, department):
        pass

    def remove_department(self, department):
        pass

# 部件构建者
class Composite(Component):
    def __init__(self, name):
        self._name = name
        self.child_components = []

    def add_department(self, component):
        self.child_components.append(component)

    def remove_department(self, component):
        self.child_components.remove(component)

    def display(self, depth):
        print('-' * depth, self._name)
        for component in self.child_components:
            if isinstance(component, Composite):
                component.display(depth + 2)
            else:
                print('-' * (depth + 1), component._name)


if __name__ == '__main__':
    # 创建公司
    company = Composite('小葵科技')
    # 创建一级部门
    company.add_department(Leaf('总经办'))
    company.add_department(Leaf('技术部'))
    op = Composite('运营部')
    # 创建二级部门
    seo = Composite('SEO部')
    # 创建三级级部门
    seo.add_department(Leaf('外链部'))
    seo.add_department(Leaf('口碑部门'))
    op.add_department(seo)
    op.add_department(Leaf('外推部'))
    company.add_department(op)
    company.display(1)
