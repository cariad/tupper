""" Tests for the Solver class. """

import csv
import os
import unittest

from solver import Solver


class SolverTestCase(unittest.TestCase):
    """ Tests for the Solver class. """

    @classmethod
    def setUpClass(cls):
        cls.solver = Solver()

    def test_samples(self):
        for filename in os.listdir("test_data"):
            self._test_file(os.path.join("test_data", filename))

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
