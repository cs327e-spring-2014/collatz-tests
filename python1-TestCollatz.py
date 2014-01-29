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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_cacheEval

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----
    
    
    def test_read_1(self) :
        r = io.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  1)
        self.assertTrue(j == 10)
    
    #reverse order
    def test_read_2 (self) :
        r = io.StringIO("999 111\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i == 999)
        self.assertTrue(j == 111)
    
    #same number    
    def test_read_3 (self) :
        r = io.StringIO("2222 2222\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i == 2222)
        self.assertTrue(j == 2222)
    
    #same number    
    def test_read_4 (self) :
        r = io.StringIO("1 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i == 1)
        self.assertTrue(j == 1)
    
    #full range
    def test_read_5 (self) :
        r = io.StringIO("1 999999\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i == 1)
        self.assertTrue(j == 999999)
        

    #---------
    #cacheEval
    #---------
    
    
    def test_cacheEval_1 (self) :
        v = collatz_cacheEval(251)
        self.assertTrue(v == 65)
    
    def test_cacheEval_2 (self) :
        v = collatz_cacheEval(87654)
        self.assertTrue(v == 164)
    
    def test_cacheEval_3 (self) :
        v = collatz_cacheEval(999999)
        self.assertTrue(v == 258)
    
    def test_cacheEval_4 (self) :
        v = collatz_cacheEval(837799)
        self.assertTrue(v == 524)

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
        
    #full range    
    def test_eval_5(self):
        v = collatz_eval(1, 999999)
        self.assertTrue(v == 525)
	
    #reverse order	
    def test_eval_6(self):
        v = collatz_eval(999, 111)
        self.assertTrue(v == 179)
		
    #same number
    def test_eval_7(self):
        v = collatz_eval(100, 100)
        self.assertTrue(v == 26)
		
    #test for 1	
    def test_eval_8(self):
        v = collatz_eval(1, 1)
        self.assertTrue(v == 1)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = io.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertTrue(w.getvalue() == "1 10 20\n")
    
    #full range    
    def test_print_2 (self) :
        w = io.StringIO()
        collatz_print(w, 1, 999999, 525)
        self.assertTrue(w.getvalue() == "1 999999 525\n")
    
    #reverse order    
    def test_print_3 (self) :
        w = io.StringIO()
        collatz_print(w, 999, 111, 179)
        self.assertTrue(w.getvalue() == "999 111 179\n")
        
    #same number    
    def test_print_4 (self) :
        w = io.StringIO()
        collatz_print(w, 100, 100, 26)
        self.assertTrue(w.getvalue() == "100 100 26\n")
    
    #number 1
    def test_print_5 (self) :
        w = io.StringIO()
        collatz_print(w, 1, 1, 1)
        self.assertTrue(w.getvalue() == "1 1 1\n")

    # -----
    # solve
    # -----
    
    
    def test_solve (self) :
        r = io.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
    
    #reverse order
    def test_solve_2 (self) :
        r = io.StringIO("8888 2222\n1 1\n100000 85000\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "8888 2222 262\n1 1 1\n100000 85000 333\n")
    
    #full range    
    def test_solve_3 (self) :
        r = io.StringIO("1 999999\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 999999 525\n")
        
    #same number    
    def test_solve_4 (self) :
        r = io.StringIO("10 10\n100 100\n1000 1000\n10000 10000\n100000 100000\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "10 10 7\n100 100 26\n1000 1000 112\n10000 10000 30\n100000 100000 129\n")
    
    #random numbers    
    def test_solve_5 (self) :
        r = io.StringIO("111 999\n4268 9877\n86 376\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "111 999 179\n4268 9877 262\n86 376 144\n")
# ----
# main
# ----

print("TestCollatz.py")
unittest.main()
print("Done.")
