second = int(input())
minute = 0
hour = 0

while second >= 60:
	minute += 1
	second -= 60

while minute >= 60:
	hour += 1
	minute -= 60

print(str(hour) + ":" + str(minute) + ":" + str(second))

# 別解
# second = int(input())
# print(second//3600, (second%3600)//60, second%60, sep=":")
