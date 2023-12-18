#forloops
import time


# j = 0
# for i in range(50,100 + 1,3):
#     print(i)
#     j += 1

# print(j)


# for seconds in range(10,-1,-1):
#     print(seconds)
#     time.sleep(1)

# print("happy birthday!!!!!!")

rows = int(input("enter number of rows: "))
columns = int(input("enter number of columns: "))
symbol = input("enter number of symbol: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()
