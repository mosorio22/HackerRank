#revArr.py

arr_count = int(input())

arr = list(map(int, input().rstrip().split()))


def rev_arr(to_be_reversed):
	for i in range(arr_count-1,-1,-1):
		print(to_be_reversed[i], end=" ")

rev_arr(arr)




