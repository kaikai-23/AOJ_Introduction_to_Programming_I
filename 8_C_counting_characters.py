import sys

count_char = [0 for _ in range(26)]

input_str = sys.stdin.read()

for char in input_str:
	if 'a' <= char and char <= 'z':
		count_char[ord(char) - ord('a')] += 1
	elif 'A' <= char and char <= 'Z':
		count_char[ord(char) - ord('A')] += 1

for i in range(26):
	print((chr(i + ord('a'))), ":", count_char[i])

# コマンドDでターミナルから抜け出す想定になってる
