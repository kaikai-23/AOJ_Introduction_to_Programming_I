r, c = map(int, input().split())

spreadsheet = [[0 for _ in range(c)] for _ in range(r)]

# 行の足し算
row_sum = [0 for _ in range(r)]

# 列の足し算
column_sum = [0 for _ in range(c)]

# 総合計
all_sum = 0

for i in range(r):
	row = list(map(int, input().split()))
	for j in range(c):
		spreadsheet[i][j] = row[j]
		row_sum[i] += row[j]
		column_sum[j] += row[j]
		all_sum += row[j]

for i in range(r+1):
	if i != r:
		for j in range(c+1):
			if j != c:
				print(spreadsheet[i][j], end=" ")
			else:
				print(row_sum[i])
	else:
		for j in range(c+1):
			if j != c:
				print(column_sum[j], end=" ")
			else:
				print(all_sum)
