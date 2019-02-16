#grading.py

students = int(input())

grades = []

for _ in range(students):
	grades_item = int(input())
    grades.append(grades_item)

def grading(grades):
	new_val = 0
	#print(grades)
	for i in range(students):
		#print(i)
		if (grades[i] >= 38):
			if (int(round(grades[i]/5.0)*5.0) >= grades[i]):
				if ((int(round(grades[i]/5.0)*5.0)) - grades[i] < 3):
					grades[i] = int(round(grades[i]/5.0)*5.0)
		print(grades[i])
	return grades






grading(grades)
