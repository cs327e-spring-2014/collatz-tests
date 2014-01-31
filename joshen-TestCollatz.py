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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_eval_helper

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        r = io.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  1)
        self.assertTrue(j == 10)

    def test_read_2 (self) :
        r = io.StringIO("5 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i == 5)
        self.assertTrue(j == 1)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertTrue(v == 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertTrue(v == 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertTrue(v == 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertTrue(v == 174)

    # ----------------
    # additional tests
    # ----------------

    def test_eval_5 (self) :
        v = collatz_eval(39183, 479796)
        self.assertTrue(v == 449)

    def test_eval_6 (self) :
        v = collatz_eval(730399, 571879)
        self.assertTrue(v == 509)

    def test_eval_7 (self) :
        v = collatz_eval(913353, 441359)
        self.assertTrue(v == 525)

    def test_eval_8 (self) :
        v = collatz_eval(1, 1)
        self.assertTrue(v == 1)

    def test_eval_9 (self) :
        v = collatz_eval(1, 2)
        self.assertTrue(v == 2)

    def test_eval_10 (self) :
        v = collatz_eval(58758, 71526)
        self.assertTrue(v == 335)

    def test_eval_11 (self) :
        v = collatz_eval(772316, 741481)
        self.assertTrue(v == 468)

    def test_eval_12 (self) :
        v = collatz_eval(5, 1)
        self.assertTrue(v == 8)

    def test_eval_13 (self) :
        v = collatz_eval(45, 52)
        self.assertTrue(v == 105)

    # ------
    # helper
    # ------

    def test_eval_helper (self) :
        v = collatz_eval(1, 5)
        self.assertTrue(v == 8)

    # -----
    # print
    # -----

    def test_print (self) :
        w = io.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertTrue(w.getvalue() == "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = io.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

# ----
# main
# ----

print("TestCollatz.py")
unittest.main()
print("Done.")
