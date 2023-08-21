students={"name":"khizar" ,"Roll No":"Fa20-bse-144","semester":"7th"}
students['city']="swabi"
print(students)
# Iterate through keys
for key in students:
    print(key)
# Iterate through Values
for value in students.values():
    print(value)

# key value pairs
for key,value in students.items():
    print(key+"         "+value)

# pop elements
students.pop("city")
print(students)
# pop item 
students.popitem()
print(students)
# clean items
students.clear()
print(students)