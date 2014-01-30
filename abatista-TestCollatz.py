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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

<<<<<<< HEAD
    def test_read (self) :
=======
    def test_read_1 (self) :
>>>>>>> da6f4962140669c0bfdc6f721cb805195102671d
        r = io.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  1)
        self.assertTrue(j == 10)

<<<<<<< HEAD
    def test_read (self) :
=======
    def test_read_2 (self) :
>>>>>>> da6f4962140669c0bfdc6f721cb805195102671d
        r = io.StringIO("1000 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  1000)
        self.assertTrue(j == 10)

<<<<<<< HEAD
    def test_read (self) :
        r = io.StringIO("99999 5000\n")
=======
    def test_read_3 (self) :
        r = io.StringIO("-99999 5000\n")
>>>>>>> da6f4962140669c0bfdc6f721cb805195102671d
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
<<<<<<< HEAD
        self.assertTrue(i ==  99999)
        self.assertTrue(j == 5000)

    def test_read (self) :
=======
        self.assertTrue(i == -99999)
        self.assertTrue(j == 5000)

    def test_read_4 (self) :
>>>>>>> da6f4962140669c0bfdc6f721cb805195102671d
        r = io.StringIO("12345 6789\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i == 12345)
        self.assertTrue(j == 6789)

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
<<<<<<< HEAD
        v = collatz_eval(900, 1000)
        self.assertTrue(v == 174)
=======
        v = collatz_eval(32, 5)
        self.assertTrue(v == 112)

    def test_eval_5 (self) :
        v = collatz_eval(5, 32)
        self.assertTrue(v == 112)

    def test_eval_6 (self) :
        v = collatz_eval(34579, 40033)
        self.assertTrue(v == 324)

    def test_eval_7 (self) :
        v = collatz_eval(1045, 1294)
        self.assertTrue(v == 182)

>>>>>>> da6f4962140669c0bfdc6f721cb805195102671d

    # -----
    # print
    # -----

<<<<<<< HEAD
    def test_print (self) :
=======
    def test_print_1 (self) :
>>>>>>> da6f4962140669c0bfdc6f721cb805195102671d
        w = io.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertTrue(w.getvalue() == "1 10 20\n")

<<<<<<< HEAD
=======
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

>>>>>>> da6f4962140669c0bfdc6f721cb805195102671d
    # -----
    # solve
    # -----

<<<<<<< HEAD
    def test_solve (self) :
=======
    def test_solve_1 (self) :
>>>>>>> da6f4962140669c0bfdc6f721cb805195102671d
        r = io.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

<<<<<<< HEAD
=======
    def test_solve_2 (self) :
        r = io.StringIO("32 5\n5 32\n34579 40333\n1045 1294\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "32 5 112\n5 32 112\n34579 40333 324\n1045 1294 182\n")

    def test_solve_3 (self) :
        r = io.StringIO("19 6\n6 19\n10 9\n8 8\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "19 6 21\n6 19 21\n10 9 20\n8 8 4\n")

    def test_solve_4 (self) :
        r = io.StringIO("34556 40000\n1 9\n2 8\n5 5\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "34556 40000 324\n1 9 20\n2 8 17\n5 5 6\n")
>>>>>>> da6f4962140669c0bfdc6f721cb805195102671d
# ----
# main
# ----

print("TestCollatz.py")
unittest.main()
print("Done.")
