import sys

s = sys.argv[1]
t = sys.argv[2]

def isomorphicStrings(s, t):
	if len(s) != len(t):
		return False

	mapping_s_t = {}
	mapping_t_s = {}

	for char_s, char_t in zip(s,t):
		if (char_s in mapping_s_t and mapping_s_t[char_s] != char_t) or  (char_t in mapping_t_s and mapping_t_s[char_t] != char_s):
			return False
		mapping_s_t[char_s] = char_t
		mapping_t_s[char_t] = char_s
	return True

print("true" if isomorphicStrings(s, t) else "false");