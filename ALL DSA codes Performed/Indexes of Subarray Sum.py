import sys

arr = [int(x) for x in sys.argv[1].split(',')]
target = int(sys.argv[2])

def subarraySum(arr, target):
	n = len(arr)
	left = 0
	curr_sum = 0

	for right in range(n):
		curr_sum += arr[right]

		while curr_sum > target and left <= right:
			curr_sum -= arr[left]
			left += 1

		if curr_sum == target:
			return[left +1, right + 1]

	return[-1]

print(",".join(map(str, subarraySum(arr, target))))