# List

grocery_list= ["apple","orange","banana"]

empty_list= ["milk","spinach","Grape"]

print('apple' in grocery_list)

print(grocery_list[-2])
print(grocery_list.index("orange"))
print(grocery_list[0:])
print(len(grocery_list))

grocery_list.append("kathirikai")
print(grocery_list)

grocery_list+= ["rice"]
print(grocery_list)

print('')

grocery_list.extend(empty_list)
print(grocery_list)

print('')

grocery_list.insert(1,"cake")
print(grocery_list)

print("")

grocery_list[1:2] = ["pepper", "onion"]
print(grocery_list)

print('')

grocery_list.remove("orange")
print(grocery_list)

print('')

grocery_list.remove("onion")
print(grocery_list)

print("")

grocery_list.pop()
print(grocery_list)

print('')

del grocery_list[0]
print(grocery_list)

print('')

grocery_list.sort()
print(grocery_list)

print("")

grocery_list.sort(key=str.lower)

nums = [1,2,3,6,5,2]
nums.reverse()
print(nums) 

nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

numsCopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print('')
print(numsCopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(type (nums))

#TUPLES

mytuple = tuple(('Agathiyan','25','Athlet'))
print(mytuple)

newtuple = list(mytuple)
newtuple.append('Great')
newlist = tuple(newtuple)
print(type(newlist))

