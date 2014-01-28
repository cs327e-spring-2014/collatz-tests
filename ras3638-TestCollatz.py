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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_eval_helper, collatz_eval_startLength

# -----------
# TestCollatz 
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        #Original test_read case given
        r = io.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i == 1)
        self.assertTrue(j == 10)

    def test_read_2 (self) :
        #Original test_read given
        r = io.StringIO("100 200\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i == 100)
        self.assertTrue(j == 200)

    def test_read_3 (self) :
        #Original test_read given
        r = io.StringIO("201 210\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i == 201)
        self.assertTrue(j == 210)

    def test_read_4 (self) :
        #Original test_read given
        r = io.StringIO("900 1000\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i == 900)
        self.assertTrue(j == 1000)

    def test_read_5 (self) :
        #Corner test 1 for test_read
        r = io.StringIO("999999 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i == 999999)
        self.assertTrue(j == 1)

    def test_read6 (self) :
        #Corner test 2 for test_read
        r = io.StringIO("1 2\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i == 1)
        self.assertTrue(j == 2)

    def test_read_7 (self) :
        #Corner test 3 for test_read case
        r = io.StringIO("99 100\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i == 99)
        self.assertTrue(j == 100)



    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        #Original test_eval given
        v = collatz_eval(1, 10)
        self.assertTrue(v == 20)

    def test_eval_2 (self) :
        #Original test_eval given
        v = collatz_eval(100, 200)
        self.assertTrue(v == 125)

    def test_eval_3 (self) :
        #Original test_eval given
        v = collatz_eval(201, 210)
        self.assertTrue(v == 89)

    def test_eval_4 (self) :
        #Original test_eval given
        v = collatz_eval(900, 1000)
        self.assertTrue(v == 174)

    def test_eval_5 (self) :
        #Corner test 1 for test_eval
        v = collatz_eval(999999, 1)
        self.assertTrue(v == 525)

    def test_eval_6 (self) :
        #Corner test 2 for test_eval
        v = collatz_eval(1, 2)
        self.assertTrue(v == 2)

    def test_eval_7 (self) :
        #Corner test 3 for test_eval
        v = collatz_eval(99, 100)
        self.assertTrue(v == 26)

    # -----
    # eval_helper
    # -----

    def test_eval_startLength1 (self) :
        #Corner test for test_eval_helper
        v = collatz_eval_startLength(1,20)
        self.assertTrue(v == 10)

    def test_eval_startLength2 (self) :
        #Corner test for test_eval_helper
        v = collatz_eval_startLength(3,6)
        self.assertTrue(v == 3)

    def test_eval_startLength3 (self) :
        #Corner test for test_eval_helper
        v = collatz_eval_startLength(100, 900)
        self.assertTrue(v == 450)
    # -----
    # eval_helper
    # -----

    def test_eval_helper1 (self) :
        #Corner test for test_eval_helper
        v = collatz_eval_helper(1,10)
        self.assertTrue(v == 20)

    def test_eval_helper2 (self) :
        #Corner test for test_eval_helper
        v = collatz_eval_helper(100,200)
        self.assertTrue(v == 125)

    def test_eval_helper3 (self) :
        #Corner test for test_eval_helper
        v = collatz_eval_helper(201, 210)
        self.assertTrue(v == 89)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        #Original test_print given
        w = io.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertTrue(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :
        #Original test_print given
        w = io.StringIO()
        collatz_print(w, 100, 200, 125)
        self.assertTrue(w.getvalue() == "100 200 125\n")

    def test_print_3 (self) :
        #Original test_print given
        w = io.StringIO()
        collatz_print(w, 201, 210, 89)
        self.assertTrue(w.getvalue() == "201 210 89\n")
        
    def test_print_4 (self) :
        #Original test_print given
        w = io.StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assertTrue(w.getvalue() == "900 1000 174\n")

    def test_print_5 (self) : 
        #Corner test 1 for test_print

        w = io.StringIO()
        collatz_print(w, 999999, 1, 525)
        self.assertTrue(w.getvalue() == "999999 1 525\n")

    def test_print_6 (self) : 
        #Corner test 2 for test_print
        
        w = io.StringIO()
        collatz_print(w, 1, 2, 2)
        self.assertTrue(w.getvalue() == "1 2 2\n")

    def test_print_7 (self) : 
        #Corner test 3 for test_print
        
        w = io.StringIO()
        collatz_print(w, 99, 100, 26)
        self.assertTrue(w.getvalue() == "99 100 26\n")
    

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        #Original test_solve given
        r = io.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")


    def test_solve_2 (self) :
        #Corner test 1 for test_solve
        r = io.StringIO("999999 1\n1 2\n99 100\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "999999 1 525\n1 2 2\n99 100 26\n")
        
    def test_solve_3(self) :
        #Corner test 2 for test_solve
        r = io.StringIO("555 655\n4 5\n200000 300000\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "555 655 145\n4 5 6\n200000 300000 443\n")

    def test_solve_4(self) :
        #Corner test 3 for test_solve
        r = io.StringIO("7 10\n10 7\n150000 10000\n11 17\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "7 10 20\n10 7 20\n150000 10000 375\n11 17 18\n")
        print("Done.")

# ----
# main
# ----

print("TestCollatz.py")
unittest.main()
