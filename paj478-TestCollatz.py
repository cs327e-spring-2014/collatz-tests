#!/usr/bin/env python

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

import StringIO
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
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)

     # Test same string
    def test_read_2 (self) :
       r = StringIO.StringIO("10 10\n")
       a = [0, 0]
       b = collatz_read(r, a)
       self.assert_(b == True)
       self.assert_(a[0] == 10)
       self.assert_(a[1] == 10)

    # Test reverse string
    def test_read_3 (self):
       r = StringIO.StringIO("200 100\n")
       a = [0, 0]
       b = collatz_read(r, a)
       self.assert_(b    == True)
       self.assert_(a[0] == 200)
       self.assert_(a[1] == 100)

    # Test extra spacing between inputs
    def test_read_4 (self):
      r = StringIO.StringIO("1  10\n")
      a = [0, 0]
      b = collatz_read(r, a)
      self.assert_(b == True)
      self.assert_(a[0] == 1)
      self.assert_(a[1] == 10)

    # Test extra spacing at end
    def test_read_5 (self):
      r = StringIO.StringIO("1 10   \n")
      a = [0, 0]
      b = collatz_read(r, a)
      self.assert_(b == True)
      self.assert_(a[0] == 1)
      self.assert_(a[1] == 10)

    # Test string input
    def test_read_string (self):
      r = StringIO.StringIO("Hi World!\n")
      a = [0, 0]
      b = collatz_read(r, a)
      self.assert_(b == False)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assert_(v == 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assert_(v == 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assert_(v == 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assert_(v == 174)

    # Testing reversed numbers
    def test_eval_rev (self) :
        v = collatz_eval(10, 1)
        self.assert_(v == 20)

    # Testing same numbers
    def test_eval_same (self) :
       v = collatz_eval(1, 1)
       self.assert_(v == 1)

    # Testing a non-positive int
    def test_eval_zero(self):
       v = collatz_eval(-1, 0)
       self.assert_(v == False)

    # Testing "corner"
    def test_eval_corner(self):
       v = collatz_eval(1, 999999)
       self.assert_(v == 525)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    # corner case
    def test_print_corner (self):
       w = StringIO.StringIO()
       collatz_print(w, 1, 999999, 525)
       self.assert_(w.getvalue() == "1 999999 525\n")

    # corner case
    def test_print_corner2 (self):
       w = StringIO.StringIO()
       collatz_print(w, 1, 1, 1)
       self.assert_(w.getvalue() == "1 1 1\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    # test corner cases
    def test_solve_corner(self):
       r = StringIO.StringIO("1 1\n1 999999\n")
       w = StringIO.StringIO()
       collatz_solve(r, w)
       self.assert_(w.getvalue() == "1 1 1\n1 999999 525\n")

    # test non-positive case
    def test_solve_zero(self):
       r = StringIO.StringIO("-1 1\n0 10\n")
       w = StringIO.StringIO()
       collatz_solve(r, w)
       self.assert_(w.getvalue() == False)

    # test string case
    def test_solve_string(self):
       r = StringIO.StringIO("Hi World\n")
       w = StringIO.StringIO()
       collatz_solve(r, w)
       self.assert_(w.getvalue() == False)

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
