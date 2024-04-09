str = input()
count_order = int(input())

for _ in range(count_order):
	order = list(input().split())
	if order[0] == "print":
		print(str[int(order[1]): int(order[2]) + 1])
	elif order[0] == "replace":
		str = str[: int(order[1])] + order[3] + str[int(order[2]) + 1:]
	elif order[0] == "reverse":
		str = str[: int(order[1])] + str[int(order[1]) : int(order[2]) + 1][:: -1] + str[int(order[2]) + 1:]
