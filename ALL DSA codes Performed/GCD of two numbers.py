import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

def gcd(a, b):
	while b:
		a, b =b, a % b
	return a

print(gcd(a, b))