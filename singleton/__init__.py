__author__ = 'wangke'

from singleton.conf import Config, NewConfig

if __name__ == '__main__':
    conf1 = Config()
    print('实例第{0}次被初始化'.format(conf1.state))

    conf2 = Config()
    print('实例第{0}次被初始化'.format(conf2.state))

    conf3 = NewConfig()
    print('实例第{0}次被初始化'.format(conf3.state))
