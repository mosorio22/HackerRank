#This program should take in three (sub)strings and should replace each appearance of the second string in the first string to the third string.
#For example: stringChange(Hello, ell, hii) should return Hhiio.
#Assumptions: the second and third substrings should be of the same length.
import string

def stringChange(target, replaced, replacer):
	if (len(replaced) != len(replacer)):
		raise ValueError("both substrings should be of equal length")
	target = target.replace(replaced, replacer)
	return target



print(stringChange("Hello", "e", "i"))

print(stringChange("apple", "app", "red"))