import math

from decimal import Decimal, getcontext


class Solver:
    """ Solves Tupper's Self-Referential Formula for any given (x, y). """

    def __init__(self):
        self.ctx = getcontext()
        self.ctx.prec = 1000

    def solve(self, x, y):
        """ Solves the formula for (x, y). """
        fx = math.floor(x)
        fy = math.floor(y)

        exponent = (-17 * fx) - (fy % 17)
        raised = self.ctx.power(2, exponent)
        inner_rhs = (y // 17) * raised
        mod_rhs = inner_rhs % 2
        floor_rhs = math.floor(mod_rhs)
        return 0.5 < floor_rhs

    def x(self):
        for x in range(105, -1, -1):
            yield x

    def y(self, k):
        for y in range(k, k+17):
            yield y
