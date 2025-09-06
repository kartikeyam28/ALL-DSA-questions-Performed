import sys

n = int(sys.argv[1])

def isPowerOfTwo(n):
	return n > 0 and(n & (n - 1)) == 0

print("true" if isPowerOfTwo(n) else "false");