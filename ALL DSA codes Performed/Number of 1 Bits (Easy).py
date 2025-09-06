import sys

n = int(sys.argv[1])

def setBits(n):
	count = 0 
	while n:
		n &= (n - 1)
		count +=1
	return count
print(setBits(n))