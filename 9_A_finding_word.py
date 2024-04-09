word = input()
count = 0
while (1):
	oneline = list(input().split())
	if oneline[0] == "END_OF_TEXT":
		print(count)
		break
	for i in range(len(oneline)):
		if oneline[i].lower() == word:
			count += 1
