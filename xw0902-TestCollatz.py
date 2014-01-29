#!/usr/bin/env python

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

from Collatz import collatz_read,_calc_cycle_length, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    # Normal test
    def test_read_1(self) :
        r = io.StringIO(unicode("1 10\n"))
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  1)
        self.assertTrue(j == 10)

    # Failure test- empty string
    def test_read_2 (self) :
        r = io.StringIO(unicode(""))
        a = [0, 0]
        b = collatz_read(r, a)
        self.assertTrue(b == False)
        
    # Corner test- same number
    def test_read_3 (self) :
        r = io.StringIO(unicode("1 1\n"))
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  1)
        self.assertTrue(j == 1)

    # Corner test- more than two numbers in a line
    def test_read_4 (self) :
        r = io.StringIO(unicode("1 10 50\n"))
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  1)
        self.assertTrue(j == 10)


    # ----
    # _calc_cycle_length
    # ----

    # Normal test #1
    def test_calc_1 (self) :
        cycle_length = _calc_cycle_length(5)
        self.assertTrue(cycle_length == 6)

    # Normal test #2
    def test_calc_2 (self) :
        cycle_length = _calc_cycle_length(20)
        self.assertTrue(cycle_length == 8)

    # Corner test- boundary case
    def test_calc_3 (self) :
        cycle_length = _calc_cycle_length(1)
        self.assertTrue(cycle_length == 1)

    
    # ----
    # eval
    # ----

    # Normal test #1
    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertTrue(v == 20)

    # Normal test #2
    def test_eval_2 (self) :
        v = collatz_eval(201, 210)
        self.assertTrue(v == 89)

    # Corner test- same number
    def test_eval_3 (self) :
        v = collatz_eval(1, 1)
        self.assertTrue(v == 1)
        
    # Corner test- reverse order
    def test_eval_4 (self) :
        v = collatz_eval(10, 1)
        self.assertTrue(v == 20)

    # -----
    # print
    # -----

    
    # Normal test #1
    def test_print_1 (self) :
        w = io.StringIO()
        collatz_print(w, 100, 200, 125)
        self.assertTrue(w.getvalue() == "100 200 125\n")

    # Normal test #2
    def test_print_2 (self) :
        w = io.StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assertTrue(w.getvalue() == "900 1000 174\n")

    # Corner test- same number    
    def test_print_3 (self) :
        w = io.StringIO()
        collatz_print(w, 1, 1, 1)
        self.assertTrue(w.getvalue() == "1 1 1\n")
    
    # Corner test- reverse order
    def test_print_4 (self) :
        w = io.StringIO()
        collatz_print(w, 10, 1, 20)
        self.assertTrue(w.getvalue() == "10 1 20\n")

    # -----
    # solve
    # -----

    # Normal test
    def test_solve_1 (self) :
        r = io.StringIO(unicode("1 10\n100 200\n201 210\n900 1000\n"))
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    # Corner test- same number
    def test_solve_2 (self) :
        r = io.StringIO(unicode("1 1\n9 9\n"))
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 1 1\n9 9 20\n")

    # Corner test- reverse order
    def test_solve_3 (self) :
        r = io.StringIO(unicode("10 1\n200 100\n"))
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "10 1 20\n200 100 125\n")

# ----
# main
# ----

print("TestCollatz.py")
unittest.main()
print("Done.")
