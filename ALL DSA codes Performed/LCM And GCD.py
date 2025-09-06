import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

def lcmAndGcd(a, b):
	x, y = a, b
	while y:
		x, y = y, x % y
	gcd = x
	lcm = (a * b) // gcd
	return[lcm, gcd]
print(",".join(map(str, lcmAndGcd(a, b))))