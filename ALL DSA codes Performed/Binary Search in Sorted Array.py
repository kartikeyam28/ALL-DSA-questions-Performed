import sys

arr = [int(x) for x in sys.argv[1].split(',')]
k = int(sys.argv[2])

def binarySearch(arr, k):
	left, right = 0, len(arr) - 1
	result = -1

	while left <= right:
		mid = (left + right) // 2

		if arr[mid] == k:
			result = mid
			right = mid - 1

		elif arr[mid] < k:
			left = mid + 1
		else:
			right = mid - 1
	return result

print(binarySearch(arr, k))