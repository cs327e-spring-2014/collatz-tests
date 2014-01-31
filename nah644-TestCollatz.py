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

from Collatz import collatz_setCache, collatz_cycle, collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    def setUp(self):
        collatz_setCache()
        
    # ----
    # cycl
    # ----
    
    #Test if 0
    def test_cycl_1 (self) :
        v = collatz_cycle(0)
        self.assertTrue(v == 0)

    #Test if 1
    def test_cycl_2 (self) :
        v = collatz_cycle(1)
        self.assertTrue(v == 1)

    #Power of 2
    def test_cycl_3 (self) :
        v = collatz_cycle(8)
        self.assertTrue(v == 4)

    #Odd number
    def test_cycl_4(self) :
        v = collatz_cycle(3)
        self.assertTrue(v == 8)

    #TEST THE MAX
    def test_cycl_5 (self) :
        v = collatz_cycle(999999)
        self.assertTrue(v == 259)
    
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
    # eval
    # ----
    
    #Standard test
    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertTrue(v == 20)

    #Standard test
    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertTrue(v == 125)

    #Standard test
    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertTrue(v == 89)

    #Standard test
    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertTrue(v == 174)

    #Test range reversal
    def test_eval_5 (self) :
        v = collatz_eval(10, 1)
        self.assertTrue(v == 20)

    #Test single number range
    def test_eval_6 (self) :
        v = collatz_eval(2, 2)
        self.assertTrue(v == 2)

    #Test range reversal
    def test_eval_7 (self) :
        v = collatz_eval(1, 2)
        self.assertTrue(v == 2)

    #Test range reversal and half thing
    def test_eval_8 (self) :
        v = collatz_eval(1, 200)
        self.assertTrue(v == 125)

    #Reversal and range
    def test_eval_9 (self) :
        v = collatz_eval(4, 2)
        self.assertTrue(v == 8)

    #Make sure it's the same
    def test_eval_10 (self) :
        v = collatz_eval(4, 1)
        self.assertTrue(v == 8)

    # -----
    # print
    # -----

    def test_print (self) :
        w = io.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertTrue(w.getvalue() == "1 10 20\n")

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

#;_;
