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

from Collatz import collatz_read, collatz_eval, collatz_len, collatz_print, collatz_solve

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

    def test_read_2 (self):
        r = io.StringIO("13381 19993\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  13381)
        self.assertTrue(j == 19993)
        
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
        s = collatz_eval(55, 113)
        self.assertTrue(s == 119)

    def test_eval_6 (self) :
        v = collatz_eval(211, 5994)
        self.assertTrue(v == 238)

    def test_eval_7 (self) :
        v = collatz_eval(1337, 1337)
        self.assertTrue(v == 45)

    # ----
    # len
    # ----
    
    def test_len_1(self):
        v = collatz_len(55)
        self.assertTrue(v == 113)

    def test_len_2(self):
        v = collatz_len(1337)
        self.assertTrue(v == 45)

    def test_len_3(self):
        v = collatz_len(128)
        self.assertTrue(v == 8)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = io.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertTrue(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :
        w = io.StringIO()
        collatz_print(w, 55, 56, 113)
        self.assertTrue(w.getvalue() == "55 56 113\n")

    def test_print_3 (self) :
        w = io.StringIO()
        collatz_print(w, 1, 291, 331)
        self.assertTrue(w.getvalue() == "1 291 331\n")

    def test_print_4 (self) :
        w = io.StringIO()
        collatz_print(w, 211, 5994, 238)
        self.assertTrue(w.getvalue() == "211 5994 238\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = io.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        s = io.StringIO("55 113\n211 5994\n")
        x = io.StringIO()
        collatz_solve(s, x)
        self.assertTrue(x.getvalue() == "55 113 119\n211 5994 238\n")

    def test_solve_3 (self) :
        t = io.StringIO("128 128\n")
        y = io.StringIO()
        collatz_solve(t, y)
        self.assertTrue(y.getvalue() == "128 128 8\n")

    def test_solve_4 (self) :        
        u = io.StringIO("128 129\n")
        z = io.StringIO()
        collatz_solve(u, z)
        self.assertTrue(z.getvalue() == "128 129 122\n")
# ----
# main
# ----

print("TestCollatz.py")
unittest.main()
print("Done.")
