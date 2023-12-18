# args
def add(*args):
    sum=0
    for num in args:
        sum += num
    return  sum


print(add(1,2,3,4,5))

#kwargs 

def hello(**kwargs):
    print(kwargs['first']  + " "  + kwargs['middle'] + " "+ kwargs['last'])


hello(first="Wayon", middle="Anthony", last="Taylor")
