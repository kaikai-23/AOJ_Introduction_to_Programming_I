str = input()
str = str*2
paragraph = input()


flag = 0
for i in range(len(str)):
	if paragraph[0] == str[i]:
		j = 0
		while i+j < len(str) and j < len(paragraph):
			if paragraph[j] != str[i+j]:
				break
			j += 1
		if j == len(paragraph):
			flag = 1
			break

if flag == 0:
	print("No")
else:
	print("Yes")
