# reduce() = apply a function to an iterable and reduce it to a single cumulative value

#perform function on first two elements and repeats process until 1 value remains

#reduce(function,iterable)

import functools

letters  = ["H","E","L","L","O"]
word = functools.reduce(lambda x,y:x + y,letters)
print(word)

# def red(cb,list):
#     val = None

#     for i in range(len(list)):
        
#         val = cb(i,i+1)

