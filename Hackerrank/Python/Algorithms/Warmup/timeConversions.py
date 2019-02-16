#timeConversions.py

from datetime import datetime

clock_time = input()

def time_conversions(clock_time):
	return datetime.strptime(clock_time, '%I:%M:%S%p').strftime('%H:%M:%S')

print(time_conversions(clock_time))
