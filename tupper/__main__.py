from argparse import ArgumentParser

from tupper.console_plotter import ConsolePlotter
from tupper.export_plotter import ExportPlotter
from tupper.solver import Solver


import tupper.constants

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

    ConsolePlotter(args.true, args.false).plot(args.k)

    if args.export:
        print("Exporting...")
        ep = ExportPlotter(filename=args.export)
        ep.export(args.k)
