#diagonalDifference.py

#matrix = [row][column]

t = int(input())
arr = []
for e in range(t):
	e = list(map(int, input().split()))
	arr.append(e)


def diagonalDifference(matrix):
	global t
	#print(matrix)
	#first diagonal
	first = matrix[0][0]
	for i in range(t - 1):
		for j in range(t):
			if (j == i + 1):
				first = first + matrix[j][j]
				#print(first)
	#print(first)

	#second diagonal
	second = matrix[t-1][0]
	'''#print(second)
	#print(second)
	for i in range(t-1, 0, -1):
		#print(j)
		for j in range(t):
			if (j == i - 1):
				second = second + matrix[j][i-1]
				#print(matrix[i-1][j])
				#print(matrix[j][j])
				#print(second)
	#print(second)

	'''

	#reverse matrix...duh
	matrix.reverse()
	for i in range(t - 1):
		for j in range(t):
			if (j == i + 1):
				second = second + matrix[j][j]

	result = abs(first - second)
	return result	

print(diagonalDifference(arr))