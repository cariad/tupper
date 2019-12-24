import csv
from decimal import Decimal, getcontext


class Solver:
    """ Solves Tupper's Self-Referential Formula for any given (x, y). """

    def __init__(self, export_filename=None):
        self.export_filename = export_filename
        getcontext().prec = 1000

    def export(self, x, y, result):
        """ Appends the result to a CSV file. """
        with open(self.export_filename, mode="a+") as export_file:
            writer = csv.writer(export_file)
            writer.writerow([x, y, result])

    def solve(self, x, y):
        """ Solves the formula for (x, y). """
        yd = Decimal(y)
        res = ((yd // 17) * getcontext().power(2, -17 * x - yd % 17)) % 2 >= 1
        if self.export_filename:
            self.export(x, y, res)
        return res
