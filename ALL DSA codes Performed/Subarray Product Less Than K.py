import sys

nums = [int(x) for x in sys.argv[1].split(',')]
k = int(sys.argv[2])

def numSubarrayProductLessThanK(nums, k):
	if k <=1:
		return 0

	prod = 1
	result = 0
	left = 0

	for right in range(len(nums)):
		prod *= nums[right]
		while prod >= k:
			prod //= nums[left]
			left += 1
		result += right - left + 1
	return result

print(numSubarrayProductLessThanK(nums, k))