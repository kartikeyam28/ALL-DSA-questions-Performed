import sys

n = int(sys.argv[1])
k = int(sys.argv[2])

def distributeTicket(n, k):
	left = 1
	right = n
	turn = True

	while left < right:
		if turn:
			left = min(left + k, right)
		else:
			right = max(right - k, left)
		turn = not turn

	return left

print(distributeTicket(n, k))