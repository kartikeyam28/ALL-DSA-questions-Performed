import sys

expression = sys.argv[1]

def infixToPostfix(expression):
	precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
	result = []
	stack = []
	
	for char in expression:
		if char.isalnum():  # operand
			result.append(char)
		elif char in precedence:
			while (stack and stack[-1] != '(' and
				   ((precedence[char] < precedence[stack[-1]]) or
					(precedence[char] == precedence[stack[-1]] and char != '^'))):
				result.append(stack.pop())
			stack.append(char)
		elif char == '(':
			stack.append(char)
		elif char == ')':
			while stack and stack[-1] != '(':
				result.append(stack.pop())
			stack.pop()  # remove '('
	
	while stack:
		result.append(stack.pop())
	
	return ''.join(result)

print(infixToPostfix(expression))