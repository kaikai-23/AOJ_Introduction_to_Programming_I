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


temp = list(map(int, input().split()))
dice_1 = Dice(temp[0], temp[1], temp[2], temp[3], temp[4], temp[5])

temp = list(map(int, input().split()))

flag = 0
for i in range(6):
	for _ in range(4):
		if (dice_1.top == temp[0]) and (dice_1.back == temp[1]) and (dice_1.right == temp[2]) and (dice_1. left == temp[3]) and (dice_1.front == temp[4]) and (dice_1.bottom == temp[5]):
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
	print("Yes")
else:
	print("No")
