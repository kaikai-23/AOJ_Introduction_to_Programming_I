cards = [[0 for _ in range(13)] for _ in range(4)]

n = int(input())
for _ in range(n):
	mark, number = input().split()
	if mark == "S":
		cards[0][int(number)-1] = 1
	elif mark == "H":
		cards[1][int(number)-1] = 1
	elif mark == "C":
		cards[2][int(number)-1] = 1
	elif mark == "D":
		cards[3][int(number)-1] = 1

for i in range(4):
	for j in range(13):
		if cards[i][j] == 0:
			if i == 0:
				print("S", j+1)
			elif i == 1:
				print("H", j+1)
			elif i == 2:
				print("C", j+1)
			elif i == 3:
				print("D", j+1)
