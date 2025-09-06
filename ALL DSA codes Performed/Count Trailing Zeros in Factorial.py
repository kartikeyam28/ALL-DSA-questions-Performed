import sys

n = int(sys.argv[1])

def countTrailingZeroes(n):
	count = 0
	while n >= 5:
		n//= 5
		count += n
	return count
print(countTrailingZeroes(n))