#!/usr/bin/env python3
"""
Fibonacci Sequence

Create a program that generates Fibonacci numbers less than a limit and writes them to a file. The _Fibonacci_ sequence is a sequence in which each number is the sum of the two preceding ones: 

`0, 1, 1 (0+1), 2 (1+1), 3 (2+1), 5 (3+2), ...`

	- Use a function to generate Fibonacci numbers as a list
	- Use `with` statements for file operations
	- Handle potential file I/O errors with `try`/`except`
	- Use command-line arguments (via `argparse`) to specify the upper limit and output file name

Task: Generate the Fibonacci numbers less than 100 and write them to `fibonacci_100.txt`
"""
def fibnums_under(top_number):
	x = [0,1]

	while x[-1] + x[-2] < top_number:
		next_num = x[-1] + x[-2]
		x.append(next_num)
	return(x)	

if __name__ == "__main__":
    result = fibnums_under(100)

out_file= "fibonacci_100.txt"

with open(out_file, 'w') as f:
	print(f"The fibonacci numbers under 100:{result}", file = f)