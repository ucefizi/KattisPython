# Problem statement: https://open.kattis.com/problems/4thought

ops = ['*', '+', '-', '/']
prec = {"+": 0, "-": 0, "*": 1, "/": 1}
def parse(expression):
	stack = []
	for val in expression.split(' '):
		if val in ['-', '+', '*', '/']:
			op1 = stack.pop()
			op2 = stack.pop()
			if val == '-':
				result = op2 - op1
			if val == '+':
				result = op2 + op1
			if val == '*':
				result = op2 * op1
			if val == '/':
				result = op2 // op1
			stack.append(result)
		else:
			stack.append(int(val))
	return stack.pop()

def postfix(tokens):
	output = []
	stack = []
	for item in tokens:
		if item in ops:
			while stack and prec[stack[-1]] >= prec[item]:
				output.append(stack.pop())
			stack.append(item)
		elif item == "(":
			stack.append("(")
		elif item == ")":
			while stack and stack[-1] != "(":
				output.append(stack.pop())
		else:
			output.append(item)
	while stack:
		output.append(stack.pop())
	return ' '.join(output)


tab = []
for i in ops:
	for j in ops:
		for k in ops:
			tab.append('4 '+i+' 4 '+j+' 4 '+k+' 4')
for i, v in enumerate(tab):
	v += ' = ' + str(parse(postfix(v.split())))

dic = {}
for i in tab:
	x = i.split()
	try:
		dic[int(x[-1])] = i
	except KeyError:
		pass
for i in range(int(input())):
	n = int(input())
	if n > 256 or i < -60:
		print('no solution')
	else:
		try:
			print(dic[n])
		except KeyError:
			print('no solution')
