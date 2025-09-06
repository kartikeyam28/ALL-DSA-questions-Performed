import sys

Arr = [int(x) for x in sys.argv[1].split(',')]
N = int(sys.argv[2])
k = int(sys.argv[3])

def searchInsertK(Arr, N, k):
	left, right = 0, N - 1

	while left <= right:
		mid = (left + right) // 2
		if Arr[mid] == k:
			return mid
		elif Arr[mid] < k:
			left = mid + 1
		else:
			right = mid - 1
	return left

print(searchInsertK(Arr, N, k))