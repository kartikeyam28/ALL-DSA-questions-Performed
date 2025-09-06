n = int(input())
for i in range(2*n):
	if i<n:
		stars=n-i
		spaces=2*i
	else:
		j=i-n
		stars=j+1
		spaces=2*(n-j-1)
	line="*"*stars+' '*spaces+"*"*stars
	print(line)