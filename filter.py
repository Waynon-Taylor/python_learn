#filter()  = creates a collection of elements from an iterable for which a function returns true

#filter(function,iterable)


friends = [("Rachel",19),
          ("Monica",18),
          ("Phoebe",17),
          ("joey",16)]

age = lambda data:data[1] >= 18
friends_of_age = list(filter(age,friends))
print(friends_of_age)
