game_count = int(input())
player_1_point = 0
player_2_point = 0

for _ in range(game_count):
	player_1_card, player_2_card = input().split()
	# 他の言語であればstrcmpなどが使用できる
	if player_1_card < player_2_card:
		player_2_point += 3
	elif player_1_card > player_2_card:
		player_1_point += 3
	else:
		player_1_point += 1
		player_2_point += 1

print(player_1_point, player_2_point)
