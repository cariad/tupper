import csv

from tupper.solver import Solver

class ExportPlotter:
    def __init__(self, filename):
        self.filename = filename
        self.solver = Solver()

    def export(self, k):
        """ Appends the result to a CSV file. """
        with open(self.filename, mode="a+") as export_file:
            writer = csv.writer(export_file)
            for y in self.solver.y(k):
                for x in self.solver.x():
                    solution = self.solver.solve(x, y)
                    writer.writerow([x, y, solution])
