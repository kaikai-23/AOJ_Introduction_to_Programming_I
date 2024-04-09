n, m, l = map(int, input().split())

arr_1 = [[0 for _ in range(m)] for _ in range(n)]

arr_2 = [[0 for _ in range(l)] for _ in range(m)]

result_arr = [[0 for _ in range(l)] for _ in range(n)]

for i in range(n):
	row = list(map(int, input().split()))
	for j in range(m):
		arr_1[i][j] = row[j]

for i in range(m):
	row = list(map(int, input().split()))
	for j in range(l):
		arr_2[i][j] = row[j]

for i in range(n):
	for j in range(l):
		result = 0
		for k in range(m):
			result += arr_1[i][k] * arr_2[k][j]
		result_arr[i][j] = result

for i in range(n):
	for j in range(l):
		if j != l-1:
			print(result_arr[i][j], end=" ")
		else:
			print(result_arr[i][j])

