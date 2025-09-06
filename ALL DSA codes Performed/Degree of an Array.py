import sys

nums = [int(x) for x in sys.argv[1].split(',')]

def findShortestSubArray(nums):
	count = {}
	first_occurense = {}
	last_occurense = {}

	for index, num in enumerate(nums):
		if num not in count:
			count[num] = 1
			first_occurense[num] = index
			last_occurense[num] = index
		else:
			count[num] += 1
			last_occurense[num] = index

	degree = max(count.values())
	min_length = float('inf')
	for num in count:
		if count[num] == degree:
			length = last_occurense[num] - first_occurense[num] + 1
			if length < min_length:
				min_length = length

	return min_length
print(findShortestSubArray(nums))