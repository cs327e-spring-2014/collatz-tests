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

    def test_read_1 (self):
        r = StringIO.StringIO("100 200\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 100)
        self.assert_(a[1] == 200)
    
    def test_read_larger_initial_value (self):
        r = StringIO.StringIO("210 201\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 210)
        self.assert_(a[1] == 201)

    def test_read_same_value (self):
        r = StringIO.StringIO("2 2\n")
        a = [0, 0]
        b = collatz_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] == 2)
        self.assert_(a[1] == 2)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assert_(v == 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assert_(v == 125)

    def test_eval_larger_initial_value (self) :
        v = collatz_eval(210, 201)
        self.assert_(v == 89)

    def test_eval_4_same_value (self) :
        v = collatz_eval(2, 2)
        self.assert_(v == 2)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")

    def test_print_1 (self) :
        w = StringIO.StringIO()
        collatz_print(w, 100, 200, 125)
        self.assert_(w.getvalue() == "100 200 125\n")
    
    def test_print_larger_initial_value (self) :
        w = StringIO.StringIO()
        collatz_print(w, 210, 201, 89)
        self.assert_(w.getvalue() == "210 201 89\n")
    
    def test_print_same_value (self) : 
        w = StringIO.StringIO()
        collatz_print(w, 2, 2, 2)
        self.assert_(w.getvalue() == "2 2 2\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_1_larger_initial_values (self) :
        r = StringIO.StringIO("731 75\n384 174\n998 469\n875 729\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "731 75 171\n384 174 144\n998 469 179\n875 729 179\n")
 
    def test_solve_2_with_same_value (self) :
        r = StringIO.StringIO("1 1\n110 482\n451 997\n659 215\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n110 482 144\n451 997 179\n659 215 145\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("1 812\n739 812\n869 374\n506 95\n")
        w = StringIO.StringIO()
        collatz_solve(r, w)
        self.assert_(w.getvalue() == "1 812 171\n739 812 153\n869 374 171\n506 95 144\n")

# ----
# main
# ----

print "TestCollatz.py"
unittest.main()
print "Done."
