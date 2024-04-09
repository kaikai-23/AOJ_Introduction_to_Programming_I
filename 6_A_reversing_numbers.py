n = int(input())
arr = [int(x) for x in input().split()]

for i in reversed(range(n)):
	if i == 0:
		print(arr[i], end="")
	else:
		print(arr[i], end=" ")
print()

#別解
# n = int(input())
# arr = list(map(int, input().split()))

# arr.reverse()

# for i in range(n):
# 	if i == n-1:
# 		print(arr[i], end="")
# 	else:
# 		print(arr[i], end=" ")
# print()
