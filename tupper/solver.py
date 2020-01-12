import csv
import math

from decimal import Decimal, getcontext


class Solver:
    """ Solves Tupper's Self-Referential Formula for any given (x, y). """

    def __init__(self, export_filename=None):
        self.export_filename = export_filename
        self.ctx = getcontext()
        self.ctx.prec = 1000

    def export(self, x, y, result):
        """ Appends the result to a CSV file. """
        with open(self.export_filename, mode="a+") as export_file:
            writer = csv.writer(export_file)
            writer.writerow([x, y, result])

    def solve(self, x, y):
        """ Solves the formula for (x, y). """
        fx = math.floor(x)
        fy = math.floor(y)

        exponent = (-17 * fx) - (fy % 17)
        raised = self.ctx.power(2, exponent)
        inner_rhs = (y // 17) * raised
        mod_rhs = inner_rhs % 2
        floor_rhs = math.floor(mod_rhs)
        sol = 0.5 < floor_rhs

        if self.export_filename:
            self.export(x, y, sol)

        return sol
