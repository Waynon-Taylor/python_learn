# exception = event detected during execution that
# that interrupt the flow of the program.

try:
    num1 = int(input("enter a number to divide :"))
    num2 = int(input("enter a number to divide by :"))
    result = num1 / num2
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero! idiot")
except ValueError as e:
    print(e)
    print("Enter only numbers plz")
except Exception as e:
    print(e)
    print("something went wrong :(")
else:
    print("all is good")
finally:
    print("closing all files")
