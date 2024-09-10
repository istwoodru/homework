my_dict = {"Вячеслав" : 1984, "Михаил" : 2007,"Леонид" : 2023}
print("My dictionary:",my_dict)
print("Existing value:",my_dict["Леонид"])
print("Not existing value:",my_dict.get("Александр"))
my_dict.update({"Владимир" : 1983,"Геннадий" : 1988})
print("Deleted value:",my_dict["Геннадий"])
del my_dict["Геннадий"]
print("Modified dictionary:", my_dict)
my_set = {2,2,True,'War',True,'War'}
print("My set:", my_set)
my_set.add(False)
my_set.add(34)
my_set.remove(True)
print("Modified set:",my_set)










