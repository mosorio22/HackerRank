#strong_password

import math
import os
import random
import re
import sys

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

n = int(input())
password = input()


def strong_password(n, password):
	curr_count = 6
	has_num = False
	has_lower = False
	has_upper = False
	has_special = False
	while(has_num == False):
		for i in range(n)):
			if(curr_count == 0):
				break
			if(password[i].isdigit()):
				curr_count -= 1
				has_num = True

	while(has_lower == False):
		for i in range(len(n)):
			if(curr_count == 0):
				break
			if(password[i].islower()):
				curr_count -= 1
				has_lower = True
	
	while(has_upper == False):
		for i in range(len(n)):
			if(curr_count == 0):
				break
			if(password[i].isupper()):
				curr_count -= 1
				has_upper = True

	while(has_special == False):
		for i in range(len(n)):
			if(curr_count == 0):
				break
			if(password[i] in special_characters):
				curr_count -= 1
				has_special = True

	return curr_count


print(strong_password(n, password))