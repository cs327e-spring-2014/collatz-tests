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

from Collatz import collatz_read, collatz_single, collatz_eval, collatz_print, collatz_solve

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
        r = io.StringIO ("40 50\n")
        a = [0,0]
        b = collatz_read(r,a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i == 40)
        self.assertTrue(j == 50)

    def test_read_3 (self) :
        r = io.StringIO ("100 200\n")
        a = [0,0]
        b = collatz_read(r,a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i == 100)
        self.assertTrue(j == 200)

    def test_read_4 (self) :
        r = io.StringIO ("1234 5678")
        a = [0,0]
        b = collatz_read(r,a)
        i,j = a
        self.assertTrue(b == True)
        self.assertTrue(i == 1234)
        self.assertTrue(j == 5678)

    # ----
    # single
    # ----

    def test_single (self) :
        count = collatz_single (10)
        self.assertTrue(count == 7)

    def test_single (self) :
        count = collatz_single (1)
        self.assertTrue(count == 1)

    def test_single (self) :
        count = collatz_single (2)
        self.assertTrue(count == 2)
        
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
        v = collatz_eval (1, 2)
        self.assertTrue(v== 2)

    def test_eval_6 (self) :
        v = collatz_eval (1,1)
        self.assertTrue(v== 1)

    def test_eval_7 (self) :
        v = collatz_eval (50,100)
        self.assertTrue(v== 119)


    # -----
    # print
    # -----

    def test_print (self) :
        w = io.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertTrue(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :
        w = io.StringIO()
        collatz_print(w, 100, 200, 125)
        self.assertTrue(w.getvalue() == "100 200 125\n")

    def test_print_3 (self) :
        w = io.StringIO()
        collatz_print(w, 1, 2, 2)
        self.assertTrue(w.getvalue() == "1 2 2\n")

    def test_print_4 (self) :
        w = io.StringIO()
        collatz_print(w, 50, 100, 119)
        self.assertTrue(w.getvalue() == "50 100 119\n")


    # -----
    # solve
    # -----

    def test_solve (self) :
        r = io.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = io.StringIO("1 2\n50 100\n1 1\n")
        w = io.StringIO()
        collatz_solve(r,w)
        self.assertTrue(w.getvalue() == "1 2 2\n50 100 119\n1 1 1\n")

    def test_solve_3 (self) :
        r = io.StringIO("5 5\n")
        w = io.StringIO()
        collatz_solve(r,w)
        self.assertTrue(w.getvalue() == "5 5 6\n")

    def test_solve_4 (self) :
        r = io.StringIO("2 10\n")
        w = io.StringIO()
        collatz_solve(r,w)
        self.assertTrue(w.getvalue() == "2 10 20\n")

    def test_solve_5 (self) :
        r = io.StringIO("10 1\n")
        w = io.StringIO()
        collatz_solve(r,w)
        self.assertTrue(w.getvalue() == "10 1 20\n")

# ----
# main
# ----

print("TestCollatz.py")
unittest.main()
print("Done.")
