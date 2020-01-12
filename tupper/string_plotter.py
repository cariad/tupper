from tupper.solver import Solver

class StringPlotter:
    def __init__(self, true_mark, false_mark):
        self.true_mark = true_mark
        self.false_mark = false_mark
        self.solver = Solver()

    def row(self, y):
        """ Yields the marks for the specified row. """
        for x in self.solver.x():
            c = self.true_mark if self.solver.solve(x, y) else self.false_mark
            yield c

    def graph(self, k):
        """ Yields the marks for the entire graph. """
        for y in self.solver.y(k):
            for mark in self.row(y):
                yield mark
            yield "\n"
