#!/usr/bin/env python3

# processes a file with numbers and prints out their ascii equivalent

with open('txt', 'r') as f:
	for i in f:
		print(chr(int(i)), end='')
