import sys

arr = [int(x) for x in sys.argv[1].split(',')]

def findKRotation(arr):
	n = len(arr)
	low = 0
	high = n - 1

	while low <= high:
		if arr[low] <= arr[high]:
			return low

		mid =(low + high)//2
		next_idx = (mid + 1) % n
		prev_idx = (mid - 1 + n) % n

		if arr[mid] <= arr[next_idx] and arr[mid] <= arr[prev_idx]:
			return mid
		if arr[mid] >= arr[low]:
			low = mid +1
		else:
			high = mid - 1

	return 0
print(findKRotation(arr))