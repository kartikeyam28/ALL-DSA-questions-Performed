import sys

arr = [int(x) for x in sys.argv[1].split(',')]
k = int(sys.argv[2])

def kthSmallest(arr, k):
	def quickselect(left, right, k_smallest):
		if left == right:
			return arr[left]

		pivot_index = partition(left, right)

		if k_smallest == pivot_index:
			return arr[k_smallest]
		elif k_smallest < pivot_index:
			return quickselect(left, pivot_index - 1, k_smallest)
		else:
			return quickselect(pivot_index + 1, right, k_smallest)

	def partition(left, right):
		pivot = arr[right]
		i = left
		for j in range(left, right):
			if arr[j] <= pivot:
				arr[i], arr[j] = arr[j], arr[i]
				i += 1
		arr[i], arr[right] = arr[right], arr[i]
		return i

	return quickselect(0, len(arr) - 1, k - 1)

print(kthSmallest(arr, k))