import sys

A = int(sys.argv[1])
B = int(sys.argv[2])

def countSetBits(A, B):
	k = bin(B).count('1')
	X= 0

	for i in reversed(range(32)):
		if A &(1<< i) and k>0:
			X |= (1 << i)
			k -=1
	for i in range(32):
		if not (X & (1<<i)) and k > 0:
			X |= (1 << i)
			k -=1
	return X
print(countSetBits(A, B))