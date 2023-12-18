# dictionary comprehention =  create dictionaries using an expression can replace  for loops and certain lambda functions

# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if conditional}
# dictionary = {key: if/else for (key,value) in iterable}
# dictionary = {key: function(value) for (key,value) in iterable}

cities_in_F =  {"New York":32, "Boston":75,"Los  Angles":100,"Chicago":50}

cities_in_C  =  {key:round((value - 32) * (5/9)) for (key,value) in cities_in_F.items() if  value != 32}
print(cities_in_C)

# ______

cities_temp  =  {key: "cold" if value >= 40 else "hot" for (key,value) in cities_in_F.items()}
print(cities_temp)


# _____________________
def check_temp(value):
    if value  >= 70:
        return "HOT"
    elif value >= 40:
        return "WARM"
    else:
        return "COLD"

cities =  {"New York":32, "Boston":75,"Los  Angles":100,"Chicago":50}
desc_cities ={key: check_temp(value) for (key,value) in cities.items()}

print(desc_cities)
