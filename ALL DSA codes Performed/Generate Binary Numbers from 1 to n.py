import sys

n = [int(x) for x in sys.argv[1].split(',')]

def generateBinaryNumbers(n):
	num = n[0]
	result = []
	for i in range(1, num + 1):
		result.append(bin(i)[2:])
	return result
print(",".join(map(str, generateBinaryNumbers(n))))