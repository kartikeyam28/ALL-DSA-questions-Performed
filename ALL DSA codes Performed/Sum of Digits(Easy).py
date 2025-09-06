import sys

n = int(sys.argv[1])

def sumOfDigits(n):
	return sum(int(digit) for digit in str(n))
print(sumOfDigits(n))