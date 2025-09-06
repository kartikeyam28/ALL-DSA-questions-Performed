import sys

nums = [int(x) for x in sys.argv[1].split(',')]

def numSubarrayProductLessThanK(nums):
	k = 100
	result = []
	product = 1
	left = 0

	for right in range(len(nums)):
		product *= nums[right]
		while product >= k and left <= right:
			product /= nums[left]
			left += 1
		temp = []
		for i in range(right, left - 1, -1):
			temp.insert(0, nums[i])
			result.append(temp[:])
		return result

print("\n".join([",".join(map(str, row)) for row in numSubarrayProductLessThanK(nums)]))