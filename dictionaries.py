#Dictionaries
car = {
    "Brand" : "Tesla",
    "Model" : "Model_3",
    "year" : 2024
 }

print(car)
print(type(car))
print(len(car))

# Access Item

print (car["Brand"])
print(car.get("year"))

# List all keys
print(car.keys())

# List all Values
print(car.values())

# List of key/value pairs as tuples
print(car.items())

# verify a key exists
print("Model" in car)

#change value
car["Brand"] = "Audi"
car.update({"price":100000})
print(car)

print("")

# Remove Items
print(car.pop("price"))
print(car)

# Delet and Clear
del car["year"]
print(car)

# copy Dictionaries

# car2 = car # create a reference
# print('')
# print("bad copy!")
# print(car)
# print(car2)

# car2["ev"] = "no"

# print(car)

# Nested dictionaries

athlet_1 = {
    "Name" : "Vishnu",
    "Age" : 23,
    "event" : "400 Meters"
}

athlet_2 = {
    "Name" : "Tholkappaian",
    "Age" : 20,
    "event" : "Boating"
}

Coach = {
    "Student 1" : athlet_1,
    "Student 2" : athlet_2
}
print('')
print(Coach)
print(Coach["Student 1"]["Name"])

# SETS

nums = {1,2,3,4,5,6}
print(nums)

print(type(nums))

# Add New Element

nums.add(8)
print(nums)

Numbers = {10,20,30,40,50,60}
nums.update(Numbers)
print(nums)
