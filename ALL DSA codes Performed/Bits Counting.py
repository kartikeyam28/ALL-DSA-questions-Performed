import sys

n = int(sys.argv[1])

def countBits(n):
	ans = [0] * (n + 1)
	for i in range(1, n + 1):
		ans[i] = ans[i >> 1] + (i & 1)
	return ans
print(",".join(map(str, countBits(n))))