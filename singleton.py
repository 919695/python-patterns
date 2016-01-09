__author__ = 'wangke'

'''
模式特点：保证类仅有一个实例，并提供一个访问它的全局访问点。
程序实例：实现一个唯一的配置文件,通过实例化次数统计来证实这个实例是唯一的
备注:python不需要特地去实现单例模式,因为python的模块本身就是单例模式
'''


class Config(object):
    __shared_state = {}

    def __init__(self):

        ''' 把类的属性赋值给实例属性来保证唯一 '''

        self.__dict__ = self.__shared_state
        try:
            self.state += 1
        except AttributeError:
            self.state = 1

    def __str__(self):
        return self.state


class NewConfig(Config):
    pass

if __name__ == '__main__':
    conf1 = Config()
    print('实例第{0}次被初始化'.format(conf1.state))

    conf2 = Config()
    print('实例第{0}次被初始化'.format(conf2.state))

    conf3 = NewConfig()
    print('实例第{0}次被初始化'.format(conf3.state))
