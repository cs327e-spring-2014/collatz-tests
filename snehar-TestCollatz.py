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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_next_number, collatz_cycle_length

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

    def test_read_extra_space (self):
        r = io.StringIO("1 10 \n")
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

    def test_eval_5(self): #test small range
        v = collatz_eval (1, 2)
        self.assertTrue(v == 2)
        
    def test_eval_6(self): 
        v = collatz_eval (20,22) #test small numbers
        self.assertTrue(v == 16)

    def test_eval_7(self): #test same number
        v = collatz_eval (1, 1)
        self.assertTrue(v == 1)

    def test_eval_8(self): #test reverse
        v = collatz_eval (10,1)
        self.assertTrue(v == 20)

    def test_eval_9(self): #test smaller range
        v = collatz_eval (5, 10)
        self.assertTrue(v == 20)

    def test_eval_10(self): #test large numbers
        v = collatz_eval (1, 999999)
        self.assertTrue(v == 525)

    # -----
    # collatz_next_number
    # -----


    def test_next_number(self): #test for evens
        number = collatz_next_number(6)
        self.assertTrue(number == 3)
            
    def test_next_number(self): #test for odds
        number = collatz_next_number(3)
        self.assertTrue(number == 9)

    def test_next_number(self): #test for number 2
        number = collatz_next_number(2)
        self.assertTrue(number == 1)

    # -----
    # collatz_cycle_length
    # ----- 
      
    def test_collatz_cycle(self): #test that cycle length of a is 1
        a= collatz_cycle_length(1)
        self.assertTrue(a == 1)
    
    def test_collatz_cycle(self): #test that cycle length of 5 is 6
        a= collatz_cycle_length(5)
        self.assertTrue(a == 6)
        
    def test_collatz_cycle(self): #test that cycle length of 4 is 3
        a= collatz_cycle_length(4)
        self.assertTrue(a == 3)
    
    # -----
    # print
    # -----


    def test_print (self) :
        w = io.StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertTrue(w.getvalue() == "1 10 20\n")

    def test_print1 (self): #test smaller range
        w = io.StringIO()
        collatz_print(w, 1, 2, 4)
        self.assertTrue(w.getvalue() == "1 2 4\n")
    # -----
    # solve
    #---------

    def test_solve(self):
        r=io.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w= io.StringIO()
        collatz_solve(r,w)
        self.assertTrue(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_1(self): #with extra spaces
        r=io.StringIO("1 10 \n 100 200 \n 201 210 \n 900 1000 \n")
        w= io.StringIO()
        collatz_solve(r,w)
        self.assertTrue(w.getvalue()=="1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
        
    def test_solve_2(self): #extra numbers
        r=io.StringIO("1 10 30\n100 200 38\n201 210 76\n900 1000 11\n")
        w= io.StringIO()
        collatz_solve(r,w)
        self.assertTrue(w.getvalue()=="1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

print ("TestCollatz.py")        
unittest.main()
print("Done")
