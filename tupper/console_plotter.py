from tupper.string_plotter import StringPlotter

class ConsolePlotter:
    def __init__(self, true_mark, false_mark):
        self.sp = StringPlotter(true_mark, false_mark)

    def plot(self, k):
        for mark in self.sp.graph(k):
            print(mark, end='')
