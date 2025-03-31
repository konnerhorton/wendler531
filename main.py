from wendler531 import one_rep_max
from wendler531.units import Quantity
import numpy as np
def main():
    print("Hello from wendler531!")
    orm = one_rep_max.OneRepMax(235, 10)
    print(orm.mean)
    # print(orm.mean, orm.min, orm.max)
    # print([i for i in one_rep_max.lift_curve(func=one_rep_max.adams, weight=200)])


if __name__ == "__main__":
    main()
