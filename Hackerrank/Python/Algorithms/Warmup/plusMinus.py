#plusMinus.py

n = int(input())
arr = list(map(int, input().rstrip().split()))

def plus_minus(nums):
	global n
	global arr
	nums = arr
	minus = 0
	plus = 0
	zero = 0 
	for i in range(n):
		if (nums[i] > 0):
			plus += 1
		elif (nums[i] < 0):
			minus += 1
		else:
			zero += 1
	print(plus/n)
	print(minus/n)
	print(zero/n)

plus_minus(arr)

