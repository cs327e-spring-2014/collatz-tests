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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, cycle_length

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        r = io.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  1)
        self.assertTrue(j == 10)

    def test_read_2(self) :
        r = io.StringIO("100 200\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  100)
        self.assertTrue(j == 200)

    def test_read_3(self) :
        r = io.StringIO("900 1000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  900)
        self.assertTrue(j == 1000)


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

    def test_eval_5 (self):
        v = collatz_eval(100, 99)
        self.assertTrue(v == 26)

    def test_eval_6 (self):
        v = collatz_eval(1031, 3013)
        self.assertTrue(v == 217)

    # -----
    # cycle_length
    # -----

    def test_cycleLength_1(self) :
        cnt_list = cycle_length(5, 1, 5)
        self.assertTrue(cnt_list == 6)

    def test_cycleLenght_2(self) :
        cnt_list = cycle_length(10, 1, 10)
        self.assertTrue(cnt_list == 7)

    def test_cycleLength_3(self) :
        cnt_list = cycle_length(20, 1, 20)
        self.assertTrue(cnt_list == 8)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = io.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertTrue(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :
        w = io.StringIO()
        collatz_print(w, 20, 229, 125)
        self.assertTrue(w.getvalue()) == " 20 229 125\n "

    def test_print_3 (self) :
        w = io.StringIO()
        collatz_print(w, 11, 999, 179)
        self.assertTrue(w.getvalue()) == " 11 999 179\n "

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = io.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = io.StringIO("11 199\n20 229\n193 1111\n222 333\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "11 199 125\n20 229 125\n193 1111 179\n222 333 144\n")

    def test_solve_3 (self) :
        r = io.StringIO("1 5\n24 37\n1031 3013\n212 1212\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 5 8\n24 37 112\n1031 3013 217\n212 1212 182\n")

# ----
# main
# ----

print("TestCollatz.py")
unittest.main()
print("Done.")
