import sys

arr = [int(x) for x in sys.argv[1].split(',')]

def missingNumber(arr):
	n = len(arr)

	for i in range(n):
		while 1 <= arr[i] <= n and arr[i] != arr[arr[i] - 1]:
			val = arr[i]
			arr[i], arr[val - 1] = arr[val - 1], arr[i]

	for i in range(n):
		if arr[i] != i + 1:
			return i + 1

	return n + 1
print(missingNumber(arr))