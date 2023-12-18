# sort() method =  used with list
# sorted()  function = usedwith iterables

num = [3,5,7,1,4,2]
animals =  ("bear","snake","dog","lion","cat","lizard")
num.sort(reverse=True)
sorted_animals=sorted(animals,reverse=True)

print(num)
print(sorted_animals)

students  = [("wayon","D",35),
            ("Alex","C",50),
            ("taylor","A",85)]


grade = lambda student_data:student_data[1]
students.sort(key=grade,reverse=True)
sorted_students=sorted(students,key=grade,reverse=True)

print(students)
print(sorted_students)
