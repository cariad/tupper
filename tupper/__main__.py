from argparse import ArgumentParser

from tupper.solver import Solver

import tupper.constants


class ConsolePlotter:
    def __init__(self, k, true_plot, false_plot, export_filename=None):
        self.k = k
        self.true_plot = true_plot
        self.false_plot = false_plot
        self.export_filename = export_filename

    def plot(self):
        solver = Solver(self.export_filename)
        for y in range(self.k, self.k+17):
            for x in range(105, -1, -1):
                if solver.solve(x, y):
                    print(self.true_plot, end='')
                else:
                    print(self.false_plot, end='')
            print()


if __name__ == '__main__':
    parser = ArgumentParser("Plots Tupper's Self-Referential Formula.")
    parser.add_argument("--k",
                        type=int,
                        default=tupper.constants.k,
                        help="the value k to plot (defaults to magic)")

    parser.add_argument("--true",
                        type=str,
                        default=u"\u2588",
                        help="string to write for truthy plots")

    parser.add_argument("--false",
                        type=str,
                        default=" ",
                        help="string to write for falsey plots")

    parser.add_argument("--export",
                        type=str,
                        nargs="?",
                        help="filename to export results to")

    args = parser.parse_args()

    ConsolePlotter(args.k, args.true, args.false, args.export).plot()
