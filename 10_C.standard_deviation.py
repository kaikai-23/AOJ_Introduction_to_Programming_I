import math

while(1):
	sample_count = float(input())
	if sample_count == 0:
		break
	sample = list(map(float, input().split()))

	average = 0
	for x in sample:
		average += x
	average /= sample_count

	dispersion = 0
	for x in sample:
		dispersion += (x - average) ** 2
	dispersion /= sample_count


	standard_deviation = math.sqrt(dispersion)

	print(standard_deviation)
