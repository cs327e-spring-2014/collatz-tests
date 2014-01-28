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
    my command line call:
    % python TestCollatz.py
"""

# -------
# imports
# -------

import io
import unittest

from Collatz import collatz_read, collatz_eval, collatz_cycle_length, collatz_print, collatz_solve

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

    def test_read_2 (self) :
        r = io.StringIO("100 200\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  100)
        self.assertTrue(j == 200)
 
    def test_read_3 (self) :
        r = io.StringIO("201 210\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  201)
        self.assertTrue(j == 210)

    def test_read_4 (self) :
        r = io.StringIO("900 1000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  900)
        self.assertTrue(j == 1000)

    def test_read_5 (self) :
        r = io.StringIO("10 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  10)
        self.assertTrue(j == 1)

    def test_read_6 (self) :
        r = io.StringIO("1 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  1)
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

    def test_eval_5 (self) :
        v = collatz_eval(10, 1)
        self.assertTrue(v == 20)

    def test_eval_6 (self) :
        v = collatz_eval(1, 1)
        self.assertTrue(v == 1) 

    # -----
    # cycle length
    # -----

    def test_collatz_cycle_length_1 (self) :
        max = collatz_cycle_length(1, 10)
        self.assertTrue(max == 20)

    def test_collatz_cycle_length_2 (self) :
        max = collatz_cycle_length(100, 200)
        self.assertTrue(max == 125)

    def test_collatz_cycle_length_3 (self) :
        max = collatz_cycle_length(201, 210)
        self.assertTrue(max == 89)

    def test_collatz_cycle_length_4 (self) :
        max = collatz_cycle_length(900, 1000)
        self.assertTrue(max == 174)

    def test_collatz_cycle_length_6 (self) :
        max = collatz_cycle_length(1, 1)
        self.assertTrue(max == 1)
    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = io.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertTrue(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :
        w = io.StringIO()
        collatz_print(w, 100, 200, 125)
        self.assertTrue(w.getvalue() == "100 200 125\n")

    def test_print_3 (self) :
        w = io.StringIO()
        collatz_print(w, 201, 210, 89)
        self.assertTrue(w.getvalue() == "201 210 89\n")

    def test_print_4 (self) :
        w = io.StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assertTrue(w.getvalue() == "900 1000 174\n")

    def test_print_5 (self) :
        w = io.StringIO()
        collatz_print(w, 1, 1, 1)
        self.assertTrue(w.getvalue() == "1 1 1\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = io.StringIO("1 10\n100 200\n201 210\n900 1000\n10 1\n1 1\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n10 1 20\n1 1 1\n")

# ----
# main
# ----

print("TestCollatz.py")
unittest.main()
print("Done.")
