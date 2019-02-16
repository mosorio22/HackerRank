#miniMaxSum

arr = list(map(int, input().rstrip().split()))

def mini_max_sum(array):
	global arr
	array = arr
	array.sort()
	#min
	min_val = 0
	for i in range(4):
		min_val = min_val + array[i]
	#max
	max_val = 0
	for i in range (1, 5):
		max_val = max_val + array[i]
	print(min_val, max_val)

mini_max_sum(arr)



