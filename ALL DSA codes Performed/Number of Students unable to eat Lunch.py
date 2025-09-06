import sys

students = [int(x) for x in sys.argv[1].split(',')]
sandwiches = [int(x) for x in sys.argv[2].split(',')]

def countStudents(students, sandwiches):
	count0 = students.count(0)
	count1 = students.count(1)

	for sandwich in sandwiches:
		if sandwich == 0 and count0 > 0:
			count0 -= 1
		elif sandwich == 1 and count1 > 0:
			count1 -= 1
		else:
			break
	return count0 + count1

print(countStudents(students, sandwiches))