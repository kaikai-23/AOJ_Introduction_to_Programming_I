while(1) :
	x, y = map(int, input().split())
	if x == 0 and y == 0:
		break
	for _ in range(x):
		for _ in range(y):
			print('#', end="")
		print()
	print()
