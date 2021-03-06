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

from Collatz import collatz_read, cycle, collatz_eval, collatz_print, collatz_solve

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
    
    def test_read_extraspace (self) :
        r = io.StringIO("1  10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  1)
        self.assertTrue(j == 10)

    def test_read_nonewline(self) :
        r = io.StringIO("1 10")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  1)
        self.assertTrue(j == 10)
        
    # -----
    # cycle
    # -----
    def test_cycle_0 (self) :
        v = cycle(5)
        self.assertTrue(v == 6)
        
    def test_cycle_1 (self) :
        v = cycle(1)
        self.assertTrue(v == 1)
    
    def test_cycle_1 (self) :
        v = cycle(2)
        self.assertTrue(v == 2)
        
    # ----
    # eval
    # ----
    def test_eval_0 (self) :
        v = collatz_eval(1,5)
        self.assertTrue(v == 8)
        
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
        v = collatz_eval(5000, 6000)
        self.assertTrue(v == 236)
        
    def test_corner_case_1 (self) :
        v = collatz_eval(1, 1)
        self.assertTrue(v == 1)
        
    def test_corner_case_2 (self) :
        v = collatz_eval(1, 2)
        self.assertTrue(v == 2)
       
    def test_corner_case_3 (self) :
        v = collatz_eval(1,1000000)
        self.assertTrue(v == 525)
    
    # -----
    # print
    # -----

    def test_print (self) :
        w = io.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertTrue(w.getvalue() == "1 10 20\n")
        
    def test_print_2 (self) :
        w = io.StringIO()
        collatz_print(w, 910, 1000, 174)
        self.assertTrue(w.getvalue() == "910 1000 174\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = io.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

# ----
# main
# ----

print("TestCollatz.py")
unittest.main()
print("Done.")
