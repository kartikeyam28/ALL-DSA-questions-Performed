import sys

N = int(sys.argv[1])

def generateCode(N):
	result = []
	for i in range(2**N):
		gray_code = i ^ (i >>1)
		result.append(format(gray_code, f'0{N}b'))
	return result
print(",".join(map(str, generateCode(N))))