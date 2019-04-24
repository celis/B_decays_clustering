#!/usr/bin/env python3

# std
import unittest

# 3rd
import numpy as np

# ours
from clusterking.util.testing import MyTestCase
from clusterking.scan.scanner import Scanner
from clusterking.data.data import Data


def func_zero(coeffs):
    return 0.


def func_identity(coeffs, x):
    return x


class TestScanner(MyTestCase):

    def test_set_spoints_grid(self):
        s = Scanner()
        s.set_spoints_grid({'c': [1, 2], 'a': [3], 'b': [1j, 1+1j]})
        self.assertAllClose(
            s.spoints,
            np.array([
                [3, 1j, 1],
                [3, 1j, 2],
                [3, 1+1j, 1],
                [3, 1+1j, 2],
            ])
        )

    def test_set_spoints_grid_empty(self):
        s = Scanner()
        s.set_spoints_grid({})
        self.assertEqual(len(np.squeeze(s.spoints)), 0)

    def test_set_spoints_equidist(self):
        s = Scanner()
        s.imaginary_prefix = "xxx"
        s.set_spoints_equidist({
            "a": (1, 2, 2),
            "xxxa": (3, 4, 2),
            "c": (1, 1, 1)
        })
        self.assertAllClose(
            s.spoints,
            np.array([
                [1+3j, 1],
                [1+4j, 1],
                [2+3j, 1],
                [2+4j, 1]
            ])
        )

    def test_run_zero(self):
        s = Scanner()
        d = Data()
        s.set_spoints_equidist({"a": (0, 1, 2)})
        s.set_dfunction(func_zero)
        s.run(d)


if __name__ == "__main__":
    unittest.main()
