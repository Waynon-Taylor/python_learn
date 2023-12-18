# tuple = collection which is ordered and unchangeable used to group tohether related data.


student = ("bro",25,"male")
print(student.count("bro"))
print(student.index("male"))

for x in student:
    print(x)


if "male" in student:
    print("student is male")
