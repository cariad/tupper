""" Tests for the Solver class. """

import csv
import os
import unittest

from tupper.solver import Solver


class SolverTestCase(unittest.TestCase):
    """ Tests for the Solver class. """

    @classmethod
    def setUpClass(cls):
        cls.solver = Solver()
        this_dir = os.path.dirname(os.path.realpath(__file__))
        cls.data_dir = os.path.join(this_dir, "test_data")

    def test_samples(self):
        for filename in os.listdir(self.data_dir):
            filename = os.path.join(self.data_dir, filename)
            if not str.endswith(filename, ".csv"):
                continue
            self._test_file(filename)

    def _test_file(self, filename):
        with open(filename) as test_data:
            csv_reader = csv.reader(test_data)
            for row in csv_reader:
                self._test_coord(int(row[0]), int(row[1]), row[2] == "True")

    def _test_coord(self, x, y, expect):
        a = self.solver.solve(x, y)
        self.assertEqual(expect, a, f"Expected ({x}, {y}) to be {expect}.")


if __name__ == '__main__':
    unittest.main()
