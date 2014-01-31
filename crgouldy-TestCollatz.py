#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2014
# Glenn P. Downing
# -------------------------------

"""
To test the program:
    % python TestCollatz.py >& TestCollatz.out
    % chmod ugo+x TestCollatz.py
    % TestCollatz.py >& TestCollatz.out
"""

# -------
# imports
# -------

import io
import unittest

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_cycle_length

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
    def test_read1 (self) :
        r = io.StringIO("1 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  1)
        self.assertTrue(j == 1)
    def test_read2 (self) :
        r = io.StringIO("100 200\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i == 100)
        self.assertTrue(j == 200)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertTrue(v == 20)

    def test_eval_2 (self) :
        v = collatz_eval(132410, 274551)    
        self.assertTrue(v == 443)

    def test_eval_3 (self) :
        v = collatz_eval(651977, 512394)
        self.assertTrue(v == 509)

    def test_eval_4 (self) :
        v = collatz_eval(794826, 979308)
        self.assertTrue(v == 525)

    def test_eval_5 (self) :
        v = collatz_eval(73610, 153052)
        self.assertTrue(v ==  375)
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

    def test_solve1 (self) :
        r = io.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
    def test_solve2 (self) :
        r = io.StringIO("1 1\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 1 1\n")
    def test_solve3 (self) :
        r = io.StringIO("37898 41306\n71924 71823\n83774 39756\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "37898 41306 306\n71924 71823 219\n83774 39756 351\n")
        
    # ------------
    # cycle_length
    # ------------

    def test_cycle_length1 (self) :
        z = collatz_cycle_length(20)
        self.assertTrue(z == 8)
    def test_cycle_length2 (self) :
        z = collatz_cycle_length(9)
        self.assertTrue(z == 20)
    def test_cycle_length3 (self) :
        z = collatz_cycle_length(6)
        self.assertTrue(z == 9)
        

# ----
# main
# ----

print("TestCollatz.py")
unittest.main()
print("Done.")

