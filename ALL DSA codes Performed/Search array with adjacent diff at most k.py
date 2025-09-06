import sys

arr = [int(x) for x in sys.argv[1].split(',')]
k = int(sys.argv[2])
x = int(sys.argv[3])

def findStepKeyIndex(arr, k, x):
	i = 0
	n = len(arr)

	while i < n:
		if arr[i] == x:
			return i

		jump = max(1, abs(arr[i] - x) // k)
		i += jump
	return -1

print(findStepKeyIndex(arr, k, x))