#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2014
# Glenn P. Downing
# -------------------------------

"""
To test the program:
    % python TestCollatz.py > TestCollatz.out
    % chmod ugo+x TestCollatz.py
    % TestCollatz.py > TestCollatz.out
"""

from Collatz import collatz_read, collatz_eval, CalcCycleLength, collatz_print, collatz_solve

import StringIO
import unittest


# Class defining various unit tests
class CollatzUnitTests(unittest.TestCase):
    # Read testing
    def test_read1(self):
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 1)
        self.assert_(a[1] == 10)

    def test_read2(self):
        r = StringIO.StringIO("550 160\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 550)
        self.assert_(a[1] == 160)

    def test_read3(self):
        r = StringIO.StringIO("1000000 12\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b == True)
        self.assert_(a[0] == 1000000)
        self.assert_(a[1] == 12)

    # Evaluation testing
    def test_eval_1(self):
        v = collatz_eval(1, 10)
        self.assert_(v == 20)

    def test_eval_2(self):
        v = collatz_eval(100, 200)
        self.assert_(v == 125)

    def test_eval_3(self):
        v = collatz_eval(201, 210)
        self.assert_(v == 89)

    def test_eval_4(self):
        v = collatz_eval(900, 1000)
        self.assert_(v == 174)

    def test_CalcCycleLength1(self):
        cycleLength = CalcCycleLength(545)
        self.assert_(cycleLength == 44)

    def test_CalcCycleLength2(self):
        cycleLength = CalcCycleLength(1)
        self.assert_(cycleLength == 1)

    def test_CalcCycleLength3(self):
        cycleLength = CalcCycleLength(989458)
        self.assert_(cycleLength == 197)

    def test_CalcCycleLength4(self):
        cycleLength = CalcCycleLength(12)
        self.assert_(cycleLength == 10)

    # Print testing
    def test_print1(self):
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print2(self):
        w = StringIO.StringIO()
        collatz_print(w, 550, 160, 144)
        self.assert_(w.getvalue() == "550 160 144\n")

    def test_print3(self):
        w = StringIO.StringIO()
        collatz_print(w, 1000000, 12, 525)
        self.assert_(w.getvalue() == "1000000 12 525\n")

    # Testing of the entire process
    def test_solve1(self):
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve2(self):
        r = StringIO.StringIO("469035 803823\n116388 233150\n296850 86292\n405396 868588\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "469035 803823 509\n116388 233150 443\n296850 86292 443\n405396 868588 525\n")

    def test_solve3(self):
        r = StringIO.StringIO("1 1\n53535 989898\n12345 987654\n98 45\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n53535 989898 525\n12345 987654 525\n98 45 119\n")


# Call the test
unittest.main()