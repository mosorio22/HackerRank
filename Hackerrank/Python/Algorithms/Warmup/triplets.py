#triplets.py

a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))

def triplet(a, b):
	a_score = 0
	b_score = 0
	for i in range(3):
		if (a[i] > b[i]):
			a_score += 1
		elif (b[i] > a[i]):
			b_score += 1
	print(a_score, end="")
	print(" ", end="")
	print(b_score)

triplet(a,b)
