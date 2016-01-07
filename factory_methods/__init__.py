__author__ = 'wangke'

from factory_methods.car import AudiCarFactory, MercedesFactory

if __name__ == '__main__':
    # 客户找奥迪工厂生产A4轿车
    a4 = AudiCarFactory().create('a4')
    a4.run()

    # 客户找奔驰工厂生产GLK300汽车
    glk300 = MercedesFactory().create('glk300')
    glk300.run()
