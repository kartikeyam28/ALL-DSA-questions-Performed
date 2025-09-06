import sys

nums = [int(x) for x in sys.argv[1].split(',')]

def missingNumber(nums):
	n =  len(nums)
	expected_sum = n * (n + 1) // 2
	actual_sum = sum(nums)
	return expected_sum - actual_sum

print(missingNumber(nums))