# dictionary =  A cghangeable, unordered collection of unique key:value pairs fast because they use hashing, allow us to acces a value quickly


capitals = {"usa": "washinton DC", "india": "new Dehli", "china": "beijing", "russia": "moscow"}

# print(capitals["usa"])
print(capitals.get("jamaica"))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())
capitals.update({"germany": "Berlin"})
capitals.pop("china")
# capitals.clear()

for key, value in capitals.items():
    print(key,value)
