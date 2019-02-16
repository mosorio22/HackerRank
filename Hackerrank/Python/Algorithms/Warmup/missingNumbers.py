#!/bin/python3

import math
import os
import random
import re
import sys
import collections

n = int(input())
arr = list(map(int, input().rstrip().split()))
m = int(input())
brr = list(map(int, input().rstrip().split())) 


# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
	a = collections.Counter(arr)
	b = collections.Counter(brr)
	result = sorted((b - a).keys())
	print(" ".join([str(x) for x in result]))


missingNumbers(arr, brr)
