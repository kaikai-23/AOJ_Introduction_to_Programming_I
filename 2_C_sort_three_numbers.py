# 数字として配列に保存
arr = [int(n) for n in input().split()]

# 配列はリスト関数を使っても良し
# arr = list(map(int, input().split()))

i = 0
for _ in range(len(arr)-1):
	j = len(arr)-1
	while i < j:
		if arr[j-1] > arr[j]:
			arr[j], arr[j-1] = arr[j-1], arr[j]
		j -= 1
	i += 1

# join関数は配列から文字列への結合を行える
print(' '.join(map(str, arr)))
