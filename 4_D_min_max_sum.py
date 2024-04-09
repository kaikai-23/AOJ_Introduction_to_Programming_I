n = int(input())
arr = [int(i) for i in input().split()]

# めちゃ小さい値を入れておく
max = -1000001
# めちゃ大きい値を入れておく
min = 1000001
sum = 0
for num in arr:
	sum += num
	if max < num:
		max = num
	if min > num:
		min = num

print(min, max, sum)
