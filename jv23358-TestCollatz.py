#!/usr/bin/env python

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2014
# Jesse Vo
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

from StringIO import StringIO
import unittest

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        r = StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  1)
        self.assertTrue(j == 10)

    def test_read_backwards (self) :
        r = StringIO("10 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i == 10)
        self.assertTrue(j == 1)

    def test_read_extra_space (self) :
        r = StringIO("1  10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i == 1)
        self.assertTrue(j == 10)

    def test_read_single (self) :
        r = StringIO("9 9\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i == 9)
        self.assertTrue(j == 9)

    def test_read_extra_num (self) :
        r = StringIO("1 10 20\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i == 1)
        self.assertTrue(j == 10)


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

    def test_eval_backwards (self) :
        v = collatz_eval(10, 1)
        self.assertTrue(v == 20)

    def test_eval_single (self) :
        v = collatz_eval(9, 9)
        self.assertTrue(v == 20)

    def test_eval_range (self) :
        v = collatz_eval(1,999999)
        self.assertTrue(v == 525)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertTrue(w.getvalue() == "1 10 20\n")

    def test_print_backwards (self) :
        w = StringIO()
        collatz_print(w, 10, 1, 20)
        self.assertTrue(w.getvalue() == "10 1 20\n")

    def test_print_single (self) :
        w = StringIO()
        collatz_print(w, 9, 9, 20)
        self.assertTrue(w.getvalue() == "9 9 20\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_backwards (self) :
        r = StringIO("10 1\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "10 1 20\n")

    def test_solve_single (self) :
        r = StringIO("9 9\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "9 9 20\n")

    def test_solve_extra_num (self) :
        r = StringIO("1 10 20\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n")

# ----
# main
# ----

print("TestCollatz.py")
unittest.main()
print("Done.")
