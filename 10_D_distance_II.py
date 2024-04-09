import math

n = int(input())

vector_x = list(map(float, input().split()))
vector_y = list(map(float, input().split()))

manhattan_distance = 0
for i in range(n):
	manhattan_distance += abs(vector_x[i] - vector_y[i])

print(manhattan_distance)

euclidean_distance = 0

for i in range(n):
	euclidean_distance += abs(vector_x[i] - vector_y[i])**2

euclidean_distance = math.sqrt(euclidean_distance)
print(euclidean_distance)

case_3 = 0
for i in range(n):
	case_3 += abs(vector_x[i] - vector_y[i])**3

case_3 = math.pow(case_3, 1 / 3)
print(case_3)

chessboard_distance = 0
for i in range(n):
	if abs(vector_x[i] - vector_y[i]) >= chessboard_distance:
		chessboard_distance = abs(vector_x[i] - vector_y[i])
print(chessboard_distance)
