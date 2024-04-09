while(1):
	num = int(input())
	if num == 0:
		break
	sum = 0
	while (num > 0):
		sum += num % 10
		num //= 10
	print(sum)
