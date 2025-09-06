import sys

s = sys.argv[1]

def FirstNonRepeating(s):

	freq = {}
	q = []
	result = []

	for ch in s:
		freq[ch] = freq.get(ch, 0) + 1
		q.append(ch)

		while q and freq[q[0]] > 1:
			q.pop(0)
		if q:
			result.append(q[0])
		else:
			result.append('#')
	return ''.join(result)
print(FirstNonRepeating(s))