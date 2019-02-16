#hourglassSum

import sys

input_arr = []

for _ in range(6):
	input_arr.append(list(map(int, input().rstrip().split())))

def hourglass_sum(ar):
	max_sum = -10000

	for i in range(6):
		for j in range(6):
			if (((j + 2) < 6) and ((i + 2) < 6)):
				result = ar[i][j] + ar[i][j+1] + ar[i][j+2] + ar[i+1][j+1] + ar[i+2][j] + ar[i+2][j+1] + ar[i+2][j+2]
				if (result > max_sum):
					max_sum = result
	return max_sum

print(hourglass_sum(input_arr))