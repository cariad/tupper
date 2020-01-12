""" Tests for the Solver class. """

import os
import unittest

import tupper.constants

from tupper.string_plotter import StringPlotter


class StringPlotterTestCase(unittest.TestCase):
    """ Tests for the StringPlotter class. """

    @classmethod
    def setUpClass(cls):
        cls.sp = StringPlotter("1", "0")
        this_dir = os.path.dirname(os.path.realpath(__file__))
        cls.data_dir = os.path.join(this_dir, "test_data")

    def _test_row(self, y, expect_row):
        for i, m in enumerate(self.sp.row(y)):
            e = expect_row[i]
            self.assertEqual(m, e, f"expected {e} but got {m} at #{i}")

    def test_row(self):
        y = tupper.constants.k
        filename = os.path.join(self.data_dir, "original.txt")
        with open(filename) as gold_graph:
            for expect_row in gold_graph:
                self._test_row(y, expect_row)
                y = y + 1

    def test_graph(self):
        y = tupper.constants.k
        filename = os.path.join(self.data_dir, "original.txt")

        expect_graph = ""

        with open(filename) as gold_graph:
            for expect_row in gold_graph:
                expect_graph = expect_graph + expect_row

        for i, m in enumerate(self.sp.graph(y)):
            e = expect_graph[i]
            self.assertEqual(m, e, f"expected {e} but got {m} at #{i}")

if __name__ == '__main__':
    unittest.main()
