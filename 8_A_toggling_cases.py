str = input()

for char in str:
	if 'a' <= char and char <= 'z':
		print(chr(ord(char) + ord('A') - ord('a')), end="")
	elif 'A' <= char and char <= 'Z':
		print(chr(ord(char) - ord('A') + ord('a')), end="")
	else:
		print(char, end="")
print()
