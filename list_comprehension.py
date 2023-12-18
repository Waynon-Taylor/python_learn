# list comprehension = a way to create a new list with less syntax can mimic certain lambda functions, easier to read.

# list =  [expression for item in iterable]
# list =  [expression for item in iterable if conditional]
# list =  [expression if/else for item in iterable]


# squares  = []
# for i in range(1,11):
#     squares.append(i*i)
# print(squares)

squares  = [i*i for i in range(1,11) if not(i*i >= 80)]
print(squares)


students =[100,90,80,70,60,50,40,30,0]
passed_students = list(filter(lambda x: x >= 60, students))
print(passed_students)

passed_students  = [i if i >= 60 else "failed" for i in students]
print(passed_students)
