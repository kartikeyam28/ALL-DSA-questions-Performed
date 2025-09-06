import sys

num = [int(x) for x in sys.argv[1].split(',')]

def minOperations(num):
	n = len(num)
	ops = 0

	for i in range(n - 2):
		if num[i] == 0:

			num[i] ^= 1
			num[i + 1] ^= 1
			num[i + 2] ^= 1
			ops += 1

	if any(x == 0 for x in num):
		return -1

	return ops

print(minOperations(num))