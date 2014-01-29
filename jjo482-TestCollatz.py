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
    
    # -----
    # print
    # -----

    def test_print (self) :
        w = io.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertTrue(w.getvalue() == "1 10 20\n")
    
    def test_print_2 (self) :
        w = io.StringIO()
        collatz_print(w, 5, 10, 20)
        print(w.getvalue())
        self.assertTrue(w.getvalue() == "5 10 20\n")

    def test_print_3 (self) :
        w = io.StringIO()
        collatz_print(w, 1000, 900, 174)
        print(w.getvalue())
        self.assertTrue(w.getvalue() == "1000 900 174\n")
        
    def test_print_4 (self) :
        w = io.StringIO()
        collatz_print(w, 5000, 6000, 236)
        print(w.getvalue())
        self.assertTrue(w.getvalue() == "5000 6000 236\n")

    def test_print_5 (self) :  # corner test
        w = io.StringIO()
        collatz_print(w, 1, 1, 1)
        print(w.getvalue())
        self.assertTrue(w.getvalue() == "1 1 1\n")
    
    def test_print_55 (self): # corner test
        w = io.StringIO()
        collatz_print(w, 4, 4, 3)
        print(w.getvalue())
        self.assertTrue(w.getvalue() == "4 4 3\n")
    

    def test_print_6 (self) :  # whole range
        w = io.StringIO()
        collatz_print(w, 1, 1000000, 525)
        print(w.getvalue())
        self.assertTrue(w.getvalue() == "1 1000000 525\n")
    
    def test_print_7 (self) :  # other numbers
        w = io.StringIO()
        collatz_print(w, 420, 666, 145)
        print(w.getvalue())
        self.assertTrue(w.getvalue() == "420 666 145\n")
        
    def test_print_8 (self) :  # other numbers
        w = io.StringIO()
        collatz_print(w, 69, 420, 144)
        print(w.getvalue())
        self.assertTrue(w.getvalue() == "69 420 144\n")
    # -----
    # solve
    # -----
    # comment

    def test_solve (self) :
        r = io.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
        
    # Single line
    def test_solve_1 (self) :
        r = io.StringIO("1 10\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n")

    # Reverse solve
    def test_solve_2 (self) :
        r = io.StringIO("10 1\n200 100\n201 210\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "10 1 20\n200 100 125\n201 210 89\n")


# ----
# main
# ----

print("TestCollatz.py")
print("Done.")
unittest.main()
print("Done.")
