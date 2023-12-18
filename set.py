# set = collection which is unordered, unindexed. no duplicate values


utensils = {"fork", "spoon","spoon", "knife"}
dishes ={"bowl","plate","cup","knife"}
# utensils.add("napkin")
# utensils.remove("spoon")
# utensils.clear()
# utensils.update(dishes)
dinner_table = utensils.union(dishes)
# print(utensils.difference(dishes))
print(utensils.intersection(dishes))

# for x in dinner_table:
#     print(x)
