students = ["hridey", "pranay", "abhi"]
students.sort()

print(students)

first_name = students[0]
first_name = first_name[:-1]
print(first_name)

long_name = ""
for name in students:
	if(len(name) > len(long_name)):
		long_name = name

print(long_name)