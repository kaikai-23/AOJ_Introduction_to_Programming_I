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
	
	def get_right(self, first_number, second_number):
		if first_number == self.bottom:
			self.roll_north()
			self.roll_north()
		elif first_number == self.left:
			self.roll_east()
		elif first_number == self.right:
			self.roll_west()
		elif first_number == self.front:
			self.roll_south()
		elif first_number == self.back:
			self.roll_north()
		
		if second_number == self.back:
			return self.right
		elif second_number == self.right:
			return self.front
		elif second_number == self.front:
			return self.left
		elif second_number == self.left:
			return self.back

temp = list(map(int, input().split()))
dice = Dice(temp[0], temp[1], temp[2], temp[3], temp[4], temp[5])
order_count = int(input())
for i in range(order_count):
	first_number, second_number = map(int, input().split())
	print(dice.get_right(first_number, second_number))
