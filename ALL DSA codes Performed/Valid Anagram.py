import sys

s = sys.argv[1]
t = sys.argv[2]

def isAnagram(s, t):
	return sorted(s) == sorted(t)
print("true" if isAnagram(s, t) else "false");