#!/usr/bin/env python3

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

# -------
# imports
# -------

import io
import unittest
import random

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, cycleLength

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read_default (self) :
        r = io.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  1)
        self.assertTrue(j == 10)

    def test_read_extraSpacing (self):
        r = io.StringIO("  1   10 \n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  1)
        self.assertTrue(j == 10)

    def test_read_noLineBreak (self):
        r = io.StringIO("1 10")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  1)
        self.assertTrue(j == 10)

    def test_read_manyLineBreaks (self):
        r = io.StringIO("1 10\n\n\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  1)
        self.assertTrue(j == 10)

    def test_read_randomInts (self) :
        firstNum = random.randint(0, 1000000)
        secondNum = random.randint(0, 1000000)
        r = io.StringIO(str(firstNum) + " " + str(secondNum) + "\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  firstNum)
        self.assertTrue(j == secondNum)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10, {})
        self.assertTrue(v == 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200, {})
        self.assertTrue(v == 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210, {})
        self.assertTrue(v == 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000, {})
        self.assertTrue(v == 174)

    def test_eval_reverseOrder (self) :
        v = collatz_eval(1000, 900, {})
        self.assertTrue(v == 174)

    def test_eval_corner1 (self) :
        v = collatz_eval(1, 1, {})
        self.assertTrue(v == 1)

    def test_eval_corner2 (self) :
        v = collatz_eval(999999, 999999, {})
        self.assertTrue(v == 259)

    def test_eval_corner3 (self) :
        v = collatz_eval(1, 999999, {})
        self.assertTrue(v == 525)

    # ----
    # cycleLength
    # ----

    def test_cycleLength_1 (self) :
        cycle_length = cycleLength(5, {})
        self.assertTrue(cycle_length == 6)

    def test_cycleLength_2 (self) :
        cycle_length = cycleLength(20, {})
        self.assertTrue(cycle_length == 8)

    def test_cycleLength_corner1 (self) :
        cycle_length = cycleLength(1, {})
        self.assertTrue(cycle_length == 1)

    def test_cycleLength_corner2 (self) :
        cycle_length = cycleLength(999999, {})
        self.assertTrue(cycle_length == 259)


    # -----
    # print
    # -----

    def test_print_default (self) :
        w = io.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertTrue(w.getvalue() == "1 10 20\n")

    def test_print_randomInts (self) :
        w = io.StringIO()
        testInt1 = random.randint(0, 1000000)
        testInt2 = random.randint(0, 1000000)
        testInt3 = random.randint(0, 1000000)
        collatz_print(w, testInt1, testInt2, testInt3)
        self.assertTrue(w.getvalue() == str(testInt1) + " " + str(testInt2) + " " + str(testInt3) + "\n")

    # -----
    # solve
    # -----

    def test_solve_default (self) :
        r = io.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_reversed (self) :
        r = io.StringIO("10 1\n200 100\n210 201\n1000 900\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "10 1 20\n200 100 125\n210 201 89\n1000 900 174\n")

    def test_solve_corner(self):
       r = io.StringIO("1 1\n1 999999\n")
       w = io.StringIO()
       collatz_solve(r, w)
       self.assertTrue(w.getvalue() == "1 1 1\n1 999999 525\n")

    def test_solve_random1(self) :
        #Corner test 2 for test_solve
        r = io.StringIO("555 655\n4 5\n200000 300000\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "555 655 145\n4 5 6\n200000 300000 443\n")

    def test_solve_random2(self) :
        #Corner test 3 for test_solve
        r = io.StringIO("7 10\n10 7\n150000 10000\n11 17\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "7 10 20\n10 7 20\n150000 10000 375\n11 17 18\n")

# ----
# main
# ----

print("TestCollatz.py")
unittest.main()
print("Done.")
