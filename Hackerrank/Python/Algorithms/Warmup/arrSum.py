#arr_sum.py

n = int(input())
arr = list(map(int, input().rstrip().split()))

def arr_sum(arr):
	global n
	sum = 0
	for i in range(n):
		sum = sum + arr[i]
	return sum

print(arr_sum(arr))