#birthdayCandles.py

age = int(input())
candles = list(map(int, input().rstrip().split()))

def birthday_candles(candles):
	tallest = max(candles)
	count = 0
	for i in range(age):
		if (candles[i] == tallest):
			count += 1
	return count

print(birthday_candles(candles))
