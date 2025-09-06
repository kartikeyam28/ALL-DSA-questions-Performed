import sys

nums = [int(x) for x in sys.argv[1].split(',')]
threshold = int(sys.argv[2])

def smallestDivisor(nums, threshold):
	left, right = 1, max(nums)

	while left < right:
		mid = (left + right)//2
		total = sum((num + mid - 1)// mid for num in nums)

		if total > threshold:
			left = mid + 1
		else:
			right = mid
	return left
print(smallestDivisor(nums, threshold))