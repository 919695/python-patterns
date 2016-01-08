__author__ = 'wangke'
from builder.car import Director, BenzBuilder, AudiBuilder

if __name__ == '__main__':
    bb = BenzBuilder()
    Director.construct_builder(bb)
    car = bb.create_car()
    car.run()

    ba = AudiBuilder()
    Director.construct_builder(ba)
    car = ba.create_car()
    car.run()
