witdh, height, x, y, r = map(int, input().split())

if witdh < x+r or 0 > x-r:
	print("No")
elif height < y+r or 0 > y-r:
	print("No")
else:
	print("Yes")
