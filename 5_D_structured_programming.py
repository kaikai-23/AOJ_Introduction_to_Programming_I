n = int(input())

for i in range(1, n+1):
	if i % 3 == 0:
		print("", i, end="")
	else:
		j = i
		while (j > 0):
			if j % 10 == 3:
				print("", i, end="")
				break
			j //= 10
