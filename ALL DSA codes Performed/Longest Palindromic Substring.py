import sys

s = sys.argv[1]

def longestPalindrome(s):
	n =  len(s)
	if n == 0:
		return 0

	max_len = 1

	for i in range(n):
		l, r = i, i
		while l >= 0 and r < n and s[l] == s[r]:
			max_len = max(max_len, r - l + 1)
			l -= 1
			r += 1

		l, r = i, i + 1
		while l >= 0 and r< n and s[l] == s[r]:
			max_len = max(max_len, r - l + 1)
			l -= 1
			r += 1
	return max_len

print(longestPalindrome(s))