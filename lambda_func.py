
# lambda function =  function written in 1 line using lambda keyword  accepts any number,  but only has one Expression
# (think of it as a shortcut)
# (useful if needed for a short period of time, throw-away)


#lambda parameters:expression

multiply = lambda x,y:x*y
print(multiply(2,5))

age_check =  lambda age:True if age >= 18 else False
print(age_check(12))
