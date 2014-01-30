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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_length

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

    def test_read_1 (self) :
        r = io.StringIO("")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == False)
        self.assertTrue(i ==  0)
        self.assertTrue(j == 0)

    def test_read_2 (self) :
        r = io.StringIO("345 678\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  345)
        self.assertTrue(j == 678)

    def test_read_3 (self) :
        r = io.StringIO("450 11\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  450)
        self.assertTrue(j == 11)

    # ------
    # length
    # ------

    def test_length_1 (self) :
        c = collatz_length(7)
        self.assertTrue(c == 17)

    def test_length_2 (self) :
        c = collatz_length(34)
        self.assertTrue(c == 14)

    def test_length_3 (self) :
        c = collatz_length(100)
        self.assertTrue(c == 26)

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

    def test_eval_5 (self) :
        v = collatz_eval(1, 3)
        self.assertTrue(v == 8)

    # -----
    # print
    # -----

    def test_print (self) :
        w = io.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertTrue(w.getvalue() == "1 10 20\n")

    def test_print_1 (self) :
        w = io.StringIO()
        collatz_print(w, 5, 6, 7)
        self.assertTrue(w.getvalue() == "5 6 7\n")

    def test_print_2 (self) :
        w = io.StringIO()
        collatz_print(w, 11, 1, 111)
        self.assertTrue(w.getvalue() == "11 1 111\n")

    def test_print_3 (self) :
        w = io.StringIO()
        collatz_print(w, 10, 67, 1)
        self.assertTrue(w.getvalue() == "10 67 1\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = io.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_1 (self) :
        r = io.StringIO("1 3\n1 6\n1 3\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 3 8\n1 6 9\n1 3 8\n")

    def test_solve_2 (self) :
        r = io.StringIO("10 1\n200 100\n210 201\n1000 900\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "10 1 20\n200 100 125\n210 201 89\n1000 900 174\n")

    def test_solve_3 (self) :
        r = io.StringIO("10 11\n10 11")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "10 11 15\n10 11 15\n")
# ----
# main
# ----

print("TestCollatz.py")
unittest.main()
print("Done.")
