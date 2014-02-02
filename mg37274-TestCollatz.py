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
    % ./TestCollatz.py >& TestCollatz.out
"""
from Collatz import collatz_solve, collatz_print, collatz_read, collatz_eval, collatz_makecycle
import unittest
import sys
from io import StringIO

class testit(unittest.TestCase):  
        def test_read_1 (self) :
                r = io.StringIO("1 10\n")
                a = [0, 0]
                b = collatz_read(r, a)
                i, j = a
                self.assertTrue(b == True)
                self.assertTrue(i ==  1)
                self.assertTrue(j == 10)

        def test_read_2 (self) :
                r = io.StringIO("100 200\n")
                a = [0, 0]
                b = collatz_read(r, a)
                i, j = a
                self.assertTrue(b == True)
                self.assertTrue(i ==  100)
                self.assertTrue(j == 200)

        def test_read_3 (self) :
                r = io.StringIO("100 200\n")
                a = [0, 0]
                b = collatz_read(r, a)
                i, j = a
                self.assertTrue(b == True)
                self.assertTrue(i ==  201)
                self.assertTrue(j == 210)

            # ----
            # makecycle
            # ----

        def test_makecycle_1 (self) :
                v = collatz_makecycle(4)
                self.assertTrue(v == 3)

        def test_makecycle_2 (self) :
                v = collatz_makecycle(17)
                self.assertTrue(v == 13)

        def test_makecycle_3 (self) :
                v = collatz_makecycle(256)
                self.assertTrue(v == 9)

        def test_makecycle_4 (self) :
                v = collatz_makecycle(1000)
                self.assertTrue(v == 112)

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

        def test_print_1 (self) :
                w = io.StringIO()
                collatz_print(w, 1, 10, 20)
                self.assertTrue(w.getvalue() == "1 10 20\n")
                
        def test_print_2 (self) :
                w = io.StringIO()
                collatz_print(w, 99, 100, 101)
                self.assertTrue(w.getvalue() == "99 100 101\n")
                
            # -----
            # solve
            # -----

        def test_solve_1 (self) :
                r = io.StringIO("1 10\n100 200\n201 210\n900 1000\n")
                w = io.StringIO()
                collatz_solve(r, w)
                self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

        def test_solve_2 (self) :
                r = io.StringIO("100 200\n1 10\n201 210\n900 1000\n")
                w = io.StringIO()
                collatz_solve(r, w)
                self.assertTrue(w.getvalue() == "100 200 125\n1 10 20\n201 210 89\n900 1000 174\n")
# ----
# main
# ----

print("TestCollatz.py")
unittest.main()
print("Done.")
