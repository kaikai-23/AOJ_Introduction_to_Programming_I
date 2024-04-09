while (1):
	cards = input()
	if cards == "-":
		break
	shuffle_count = int(input())


	for _ in range(shuffle_count):
		change_index = int(input())
		cards = cards[change_index:] + cards[:change_index]
	print(cards)
