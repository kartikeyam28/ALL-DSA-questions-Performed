import sys

arr = [int(x) for x in sys.argv[1].split(',')]

def missingNum(arr):
	n = len(arr) + 1
	expected_sum = n *(n + 1) // 2
	actual_sum = sum(arr)
	return expected_sum - actual_sum

print(missingNum(arr))