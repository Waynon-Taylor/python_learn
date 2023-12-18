#  if __name__ == "__main__"


# python interpreter sets "special variables", one of which is __name__
#python will assign the __name__ variable a value of "__main__" if it's

# import module_two

def hello(name):
    print("Hello {0}".format(name))
    
# print(module_two.__name__)

if __name__ == "__main__":
    hello("taylor")
    print(__name__)

print(__name__)


# for i in range(5):
#     for j in range(10):
#         pass


lst =  [[j for j in range(9)] for i in range(3)]
print(lst)
# 11Done22334455667788991010   
