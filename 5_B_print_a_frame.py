while (1):
	H, W = map(int, input().split())
	if H == 0 and W == 0:
		break
	for i in range(H):
		for k in range(W):
			if i == 0 or i == H-1 or k == 0 or k == W-1:
				print("#", end="")
			else:
				print(".", end="")
		print()
	print()
