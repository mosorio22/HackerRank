#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the camelcase function below.

count = 1
s = input()
for i in range(len(s)):
	if s[i].isupper():
		count += 1
print(count)

