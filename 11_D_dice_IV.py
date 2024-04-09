class Dice:
	def __init__(self, top, back, right, left, front, bottom):
		self.top = top
		self.back = back
		self.right = right
		self.left = left
		self.front = front
		self.bottom = bottom
	def roll_east(self):
		self.top, self.left, self.bottom, self.right = self.left, self.bottom, self.right, self.top
	def roll_north(self):
		self.top, self.front, self.bottom, self.back = self.back, self.top, self.front, self.bottom
	def roll_south(self):
		self.top, self.back, self.bottom, self.front = self.front, self.top, self.back, self.bottom
	def roll_west(self):
		self.top, self.left, self.bottom, self.right = self.right, self.top, self.left, self.bottom
	def rotate_clockwise(self):
		self.front, self.right, self.back, self.left = self.left, self.front, self.right, self.back
	def rotate_unclockwise(self):
		self.front, self.left, self.back, self.right = self.right, self.front, self.left, self.back
	def get_top(self):
		return self.top

def is_consistent_dice(dice_1: Dice, dice_2: Dice):
	flag = 0
	for i in range(6):
		for _ in range(4):
			if (dice_1.top == dice_2.top) and (dice_1.back == dice_2.back) and (dice_1.right == dice_2.right) and (dice_1. left == dice_2.left) and (dice_1.front == dice_2.front) and (dice_1.bottom == dice_2.bottom):
				flag = 1
			dice_1.rotate_clockwise()
		if i <= 2:
			dice_1.roll_north()
		elif i == 3:
			dice_1.roll_north()
			dice_1.roll_east()
		elif i == 4:
			dice_1.roll_west()
			dice_1.roll_west()
	if flag == 1:
		return True
	else:
		return False


n = int(input())

array = [[0 for _ in range(6)] for _ in range(n)]

for i in range(n):
	row = list(map(int, input().split()))
	for j in range(6):
		array[i][j] = row[j]

is_consistent = False

for i in range(n-1):
	for j in range(i+1, n):
		dice_1 = Dice(array[i][0], array[i][1], array[i][2], array[i][3], array[i][4], array[i][5])
		dice_2 = Dice(array[j][0], array[j][1], array[j][2], array[j][3], array[j][4], array[j][5])
		if is_consistent_dice(dice_1, dice_2) == True:
			is_consistent = True

if is_consistent == True:
	print("No")
else:
	print("Yes")
