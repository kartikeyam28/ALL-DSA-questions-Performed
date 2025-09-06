import sys

nums = [int(x) for x in sys.argv[1].split(',')]

def nextPermutation(nums):
	n = len(nums)
	pivot = -1

	for i in range(n - 2, -1, -1):
		if nums[i] < nums[i + 1]:
			pivot = i
			break
	if pivot == -1:
		nums.reverse()
		return nums

	for j in range(n - 1, pivot, -1):
		if nums[j] > nums[pivot]:
			nums[pivot], nums[j] = nums[j], nums[pivot]
			break
	left = pivot + 1
	right = n - 1
	while left < right:
		nums[left], nums[right] = nums[right], nums[left]
		left += 1
		right -= 1
	return nums

print(",".join(map(str, nextPermutation(nums))))