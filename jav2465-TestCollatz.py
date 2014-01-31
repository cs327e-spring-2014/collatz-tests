#!/usr/bin/env python

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

import StringIO
import unittest
import random
from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_maxlength

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  1)
        self.assertTrue(j == 10)

    def test_read2 (self):
        r = StringIO.StringIO("1 1000000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  1)
        self.assertTrue(j == 1000000)
        

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
        v = collatz_eval(1, 1000000)
        self.assertTrue(v == 525)

    def test_eval_6 (self):
        v = collatz_eval(10, 1)
        self.assertTrue( v ==20)
    def test_eval7 (self):
        v = collatz_eval(1,1)
        self.assertTrue(v == 1)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertTrue(w.getvalue() == "1 10 20\n")

    # -----
    # max length function
    # -----
    def test_maxlength1(self):
        l = [1,2,3,7,4,5] 
        v =collatz_maxlength(l)
        self.assertTrue(v == 7)


    def test_maxlength2(self):
        l = [1000, 1, 5, 9, 2300]
        v =collatz_maxlength(l)
        self.assertTrue(v == 2300)

    def test_maxlength3(self):
        l = [1]
        v = collatz_maxlength(l)
        self.assertTrue(v==1)
    # -----
    # solve
    # -----
        
    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve2 (self):
        r = StringIO.StringIO("10 1\n200 100\n210 201\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "10 1 20\n200 100 125\n210 201 89\n900 1000 174\n")

# ----
# main
# ----

print("TestCollatz.py")
unittest.main()
print("Done.")
