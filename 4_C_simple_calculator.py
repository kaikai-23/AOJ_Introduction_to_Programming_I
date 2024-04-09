while(1):
	x, op, y = input().split()
	if op == '?':
		break
	x, y = int(x), int(y)
	if op == '+':
		print(x+y)
	elif op == '-':
		print(x-y)
	elif op == '*':
		print(x*y)
	elif op == '/':
		print(x//y)
