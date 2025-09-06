def maxOnesAferflip(arr):
	total_ones = sum(arr)

	gain_array = [1 if x == 0 else -1 for x in arr]

	max_gain = curr_gain = gain_array[0]

	for i in range(1, len(gain_array)):
		curr_gain = max(gain_array[i], curr_gain + gain_array[i])
		max_gain = max(max_gain, curr_gain)

	return total_ones + max(0, max_gain)

n = int(input())
arr = list(map(int, input().split()))

print(maxOnesAferflip(arr))