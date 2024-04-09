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
	def get_top(self):
		return self.top

temp = list(map(int, input().split()))
dice = Dice(temp[0], temp[1], temp[2], temp[3], temp[4], temp[5])

order_list = input()
for order in order_list:
	if order == "S":
		dice.roll_south()
	elif order == "E":
		dice.roll_east()
	elif order == "N":
		dice.roll_north()
	else:
		dice.roll_west()

print(dice.get_top())
