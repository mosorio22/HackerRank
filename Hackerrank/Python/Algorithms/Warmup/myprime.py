#This program should return the nth prime number. For example: if your program takes in the number 5, it shoul return the 5th prime number (11).
#bonus: return a list of all primes less than and equal to the nth prime number.

#Assumptions: n will always be less than 1000 and greater than 0. The 1000th prime number is 7919.

import math

def isprime(test):
    if test == 2: return True
    if test < 2 or test % 2 == 0: return False
    return not any(test % i == 0 for i in range(3, int(math.sqrt(test)) + 1, 2))

def prime(n):
	count = 0
	if (n == 0):
		raise ValueError("value should be at least 1")
	if (n > 1000):
		raise ValueError("value should be less than 1000")
	if (n == 1):
		return 2
	for i in range (1, 7920):
		if (isprime(i)):
			count += 1
		if (n == count):
			break
	return i


#print(prime(1000))
#print(prime(5))
#print(prime(12))
#print(prime(22))
#print(prime(0))
#print(prime(1020))

