#!/usr/bin/env python3

# Cryptography
# ROT13 -> rotates by 13 characters
# e.g. running this with 'character' will give you 'punenpgre' and vice versa

import sys

def rot13(s: str):
	ans = ''
	for ss in s:
		c = ord(ss)	
		if (c > 64 and c < 91):
			ans += chr(c - 13 if c > 77 else c + 13)
		elif (c > 96 and c < 123):
			ans += chr(c - 13 if c > 109 else c + 13)
		else: ans += ss
	return ans

print(rot13(sys.argv[1]))