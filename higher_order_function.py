# higher order function = a function taht either: 1. accepts a function as an argument or 2.return a function
#(In python,  function are also treated  as objects)
 

from ast import Param


def loud(text):
    return text.upper()

def quiet(text):
     return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

hello(loud)
hello(quiet)
