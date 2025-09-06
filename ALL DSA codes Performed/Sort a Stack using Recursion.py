import sys

stack = [int(x) for x in sys.argv[1].split(',')]

def sortStack(stack):
	if len(stack) <= 1:
		return stack

	top = stack.pop()
	sortStack(stack)

	insert_sorted(stack, top)
	return stack
def insert_sorted(stack, element):
	if not stack or stack[-1] >= element:
		stack.append(element)
	else:
		top = stack.pop()
		insert_sorted(stack, element)
		stack.append(top)
print(",".join(map(str, sortStack(stack))))