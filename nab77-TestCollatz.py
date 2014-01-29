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

from Collatz import collatz_read, getCycleLength, collatz_eval, collatz_print, collatz_solve

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
        
    def test_eval_5 (self) :
        v = collatz_eval(861700, 78530)
        self.assert_(v == 525)

    # -----
    # get cycle length
    # Tests a function for finding the cycle length of an individual number
    # -----
    
    def testGetCycleLength1 (self):
        n = getCycleLength(1, 1)
        self.assert_(n == 1)

    def testGetCycleLength2 (self):
        n = getCycleLength(7, 1)
        self.assert_(n == 17)

    def testGetCycleLength3 (self):
        n = getCycleLength(9, 1)
        self.assert_(n == 20)

    def testGetCycleLength4 (self):
        n = getCycleLength(524288, 1)
        self.assert_(n == 20)

    def testGetCycleLength5 (self):
        n = getCycleLength(27, 1)
        self.assert_(n == 112)


    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve1 (self):
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve2 (self):
        r = StringIO.StringIO("73 54\n12 55\n69 5\n2 54\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "73 54 113\n12 55 113\n69 5 113\n2 54 112\n")

    def test_solve3 (self):
        r = StringIO.StringIO("325804 886708\n680226 342319\n699332 723677\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "325804 886708 525\n680226 342319 509\n699332 723677 504\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
