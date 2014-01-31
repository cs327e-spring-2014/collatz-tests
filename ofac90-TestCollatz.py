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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

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

    # ----
    # my READ unit tests
    # ----

    def test_read_1 (self) :          # Test 1.1...
        r = io.StringIO("3 4\n")
        a = [0, 0] # I'm thinking this is always initialized to 0s
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i == 3)
        self.assertTrue(j == 4)

    def test_read_2 (self) :          # Test 1.2...
        r = io.StringIO("13 26\n")
        a = [0, 0] # I'm thinking this is always initialized to 0s
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i == 13)
        self.assertTrue(j == 26)

    def test_read_3 (self) :          # Test 1.3...
        r = io.StringIO("12 98\n")
        a = [0, 0] # I'm thinking this is always initialized to 0s
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i == 12)
        self.assertTrue(j == 98)


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

    # ----
    # my EVAL unit tests
    # ----

    def test_eval_5 (self):
        v = collatz_eval(1031, 3013)     # some random test I'm trusting is right.
        self.assertTrue(v == 217)        # I looked into the class test repo to find it

    def test_eval_6 (self):              # Corner Case:
        v = collatz_eval(1000, 900)     # See that it works when numbers given in the
        self.assertTrue(v == 174)        # reverse order: big small


    def test_eval_7(self):               # Corner Case:
        v = collatz_eval(1, 1)           # Another good idea I found in class test
        self.assertTrue(v == 1)          # repo. Tests for the same number.

    def test_eval_8(self):               # Last one for good luck. Again, peeked at other
        v = collatz_eval(16097, 7366)    # ppl's results to make this test
        self.assertTrue(v == 276)

    # -----
    # print
    # -----

    def test_print (self) :
        w = io.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertTrue(w.getvalue() == "1 10 20\n")

    # ----
    # my PRINT unit tests
    # ----

    def test_print_1 (self) :
        w = io.StringIO()
        collatz_print(w, 10, 200, 125)
        self.assertTrue(w.getvalue() == "10 200 125\n")

    def test_print_2 (self) :
        w = io.StringIO()
        collatz_print(w, 201, 210, 89)
        self.assertTrue(w.getvalue() == "201 210 89\n")

    def test_print_3 (self) :
        w = io.StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assertTrue(w.getvalue() == "900 1000 174\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = io.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    # ----
    # my SOLVE unit tests
    # ----

    # Test values taken from other people's results
    #7195 8354 252
    #20101 9474 279
    #16097 7366 276
    #1273 28607 308
    def test_solve_1 (self) :
        r = io.StringIO("7195 8354\n20101 9474\n16097 7366\n1273 28607\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "7195 8354 252\n20101 9474 279\n16097 7366 276\n1273 28607 308\n")

    #20303 20564 243
    #35918 14489 324
    #16725 25391 282
    #67414 76227 325
    def test_solve_2 (self) :
        r = io.StringIO("20303 20564\n35918 14489\n16725 25391\n67414 76227\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "20303 20564 243\n35918 14489 324\n16725 25391 282\n67414 76227 325\n")

    #45914 93571 351
    #86459 96853 333
    #9096 11320 268
    #54818 48561 340
    def test_solve_3 (self) :
        r = io.StringIO("45914 93571\n86459 96853\n9096 11320\n54818 48561\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "45914 93571 351\n86459 96853 333\n9096 11320 268\n54818 48561 340\n")

# ----
# main
# ----

print("TestCollatz.py")
unittest.main()
print("Done.")
