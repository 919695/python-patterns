__author__ = 'wangke'
from factory_methods.car import (LeiFengFactory, StudentFactory, VolenterFactory)

if __name__ == "__main__":
    lf = LeiFengFactory.createLeiFeng()
    lf.sweep()
    lf = StudentFactory.createLeiFeng()
    lf.sweep()
    lf = VolenterFactory.createLeiFeng()
    lf.sweep()
    pass
