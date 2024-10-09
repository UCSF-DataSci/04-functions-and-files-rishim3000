#!/usr/bin/env python3
"""
Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, and prints the largest prime number in the list. 

	- Use command-line arguments to specify the upper limit 
	- Implement a function to check if a number is prime
	- Import and use the Fibonacci generating function from problem 1 as a module

Task: Find the largest prime Fibonacci number less that 50000
"""

# You're on your own for this one. Good luck!

import argparse
import sys
from fibonnaci import fibnums_under

def prime_num(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
        return True
    
def max_prime_fib(x):
    prime_fibnum = []
    fibnums = fibnums_under(x)
    for i in fibnums:
        if prime_num(i):
            prime_fibnum.append(i)
    return(max(prime_fibnum))

if __name__ == "__main__":
    result = max_prime_fib(50000)
    print(f"The largest prime fibonacci number under 50000:{max_prime_fib(50000)}")