# Name: William Gunn
# ID: weg375
# Date Created: 21 Jan 2013
# Date Last Modified: 30 Jan 2013

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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, second_opt, chk_cache, cache_insert, cycle_len

# Global
cache = []

# ----------
# make cache
# ----------
for i in range(1, 1000002):
        cache.append(0)

# -----------
# TestCollatz
# -----------

class TestCollatz (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        r = io.StringIO("1 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  1)
        self.assertTrue(j == 10)
        
    def test_read_2 (self) :
        r = io.StringIO("1 1\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  1)
        self.assertTrue(j == 1)
        
    def test_read_3 (self) :
        r = io.StringIO("100 10\n")
        a = [0, 0]
        b = collatz_read(r, a)
        i, j = a
        self.assertTrue(b == True)
        self.assertTrue(i ==  100)
        self.assertTrue(j == 10)
        
    # ------------
    # cycle length
    # ------------
    
    def test_cycle_len_1 (self) :
        l = [0, 1, 2, 8, 3, 6, 9, 17, 4, 20, 7]
        n = 1
        v = cycle_len(n)
        self.assertTrue(v == 1)
        
    def test_cycle_len_2 (self) :
        l = [0, 1, 2, 8, 3, 6, 9, 17, 4, 20, 7, 0]
        n = 10
        self.assertTrue(l[10] == 7)
        v = cycle_len(n)
        self.assertTrue(v == 7)
        
    def test_cycle_len_3 (self) :
        l = []
        for i in range(1, 202):
            l.append(0)
        n = 200
        v = cycle_len(n)
        self.assertTrue(v == 27)
        
    def test_cycle_len_4 (self) :
        n = 10
        v = cycle_len(n)
        self.assertTrue(v == 7)
    
    # -------------------
    # second optimization
    # -------------------
    
    def test_second_opt_1 (self):
        v = second_opt(1, 10)
        self.assertTrue(v == 5)
        
    def test_second_opt_2 (self):
        v = second_opt(1, 100)
        self.assertTrue(v == 50)
        
    def test_second_opt_3 (self):
        v = second_opt(70, 100)
        self.assertTrue(v == 70)
            
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
    # Added Tests
    def test_bckward (self) :
        v = collatz_eval(10, 1)
        self.assertTrue(v == 20)
		
    def test_corner_1 (self) :
        v = collatz_eval(1, 1)
        self.assertTrue(v == 1)

		

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = io.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertTrue(w.getvalue() == "1 10 20\n")

    def test_print_2 (self) :
        w = io.StringIO()
        collatz_print(w, 10, 20, 40)
        self.assertTrue(w.getvalue() == "10 20 40\n")
        
    def test_print_3 (self) :
        w = io.StringIO()
        collatz_print(w, 1, 1, 50)
        self.assertTrue(w.getvalue() == "1 1 50\n")
        
    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = io.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
        
    def test_solve_2 (self) :
        r = io.StringIO("10 1\n200 100\n201 210\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "10 1 20\n200 100 125\n201 210 89\n")
        
    def test_solve_3 (self) :
        r = io.StringIO("1 1\n200 201\n")
        w = io.StringIO()
        collatz_solve(r, w)
        self.assertTrue(w.getvalue() == "1 1 1\n200 201 27\n")
    # -----
    # cache
    # -----
    """
    def test_mk_cache_1 (self) :
        cache = mk_cache()
        self.assertTrue(cache[1000] == 0)
        
    def test_mk_cache_2 (self) :
        cache = mk_cache()
        self.assertTrue(cache[100000] == 0)
        
    def test_mk_cache_3 (self) :
        cache = mk_cache()
        self.assertTrue(cache[1000000] == 0)
    """
    def test_chk_cache_1 (self) :
        n = 3
        v = chk_cache(n)
        self.assertTrue(v == 8)
        
    def test_chk_cache_2 (self) :
        n = 2
        v = chk_cache(n)
        self.assertTrue(v == 2)
        
    def test_chk_cache_3 (self) :
        n = 1
        v = chk_cache(n)
        self.assertTrue(v == 1)
    
    # Can't Test from import due to global Variable    
    def test_cache_insert_1 (self) :
        n = 1
        v = 1
        global cache
        cache[n] = v
        self.assertTrue(cache[n] == 1)
     
    def test_cache_insert_2 (self) :
        n = 4
        v = 3
        global cache
        cache[n] = v
        self.assertTrue(cache[n] == 3)
        
    def test_cache_insert_3 (self) :
        n = 5
        v = 6
        global cache
        cache[n] = v
        self.assertTrue(cache[n] == 6)

# ----
# main
# ----

print("TestCollatz.py")
unittest.main()
print("Done.")
