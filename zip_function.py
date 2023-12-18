# zip(iterable) = aggrefate elements from two or more iterables (list,tuples,set,ect.) create a zip ogbject  with paired elements stored in tuples for each element


username = ["Dude", "bro", "Mister"]
password = ("password", "abc123", "guest")
login_date = ["1/1/2021", "1/2/2021", "1/3/2021"]

users = dict(zip(username, password))
user_data = list(zip(username, password, login_date))
print(users)
print(user_data)
 