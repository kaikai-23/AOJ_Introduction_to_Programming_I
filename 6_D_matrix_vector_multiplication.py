n, m = map(int, input().split())

# n * m行列を用意
matrix = [[0 for _ in range(m)] for _ in range(n)]

# n * m行列を保存
for i in range(n):
	row = list(map(int, input().split()))
	for j in range(m):
		matrix[i][j] = row[j]

# print(matrix)

# m * 1行列を用意
arr = [0 for _ in range(m)]

# m * 1行列を保存
for k in range(m):
    arr[k] = int(input())

# print(arr)

# n * 1行列を用意
result = [0 for _ in range(n)]

# n * 1行列を保存
for i in range(n):
	for j in range(m):
		result[i] += matrix[i][j] * arr[j]

# print(result)

# 結果出力
for i in range(n):
	print(result[i])
