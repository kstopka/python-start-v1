users = ['Krystian', "Marian", "Darek"]

data = ["Krystian", 30, True]

emptyList = []

# print("Krystian" in users)
# print("Krystian" in users[0])
# print("Krystian" in emptyList)
# print("Krystian" in data[0])
# print(users[-1])
# print(users.index("Marian"))
# print(users[0:2])
# print(users[1:3])
# print(users[-3:-1])


print(len(emptyList))
print(len(data))

users.append("Karol")
print(users)

users += ["Michał"]
print(users)

users.extend(["Bartek", "Zenon"])
print(users)

# users.extend(data)
# print(users)

users.insert(0, "Krzysiek")
print(users)

users[2:2] = ["Janek", "Maniek"]
print(users)

users[1:3] = ["Robert", "Tomek"]
print(users)

users.remove("Krzysiek")
print(users)

users.pop()
print(users)

del users[0]
print(users)

# del data
data.clear()
print(data)

users[1:1] = ["krystian"]
users.sort()
print(users)

users.sort(key=str.lower)
print(users)


nums = [2, 54, 21, 11, 693, 20]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

numsCopy = nums.copy()
myNums = list(nums)
myCopy = nums[:]


print(numsCopy)
print(myNums)
myCopy.sort()
print(myCopy)
print(nums)

print(type(nums))

myList = list([1, "Norbert", True])
print(myList)

# Tuples
myTuple = tuple(("Krystian", 20, True))

anotherTuple = (1, 2, 5, 7, 9, 55)

print(myTuple)
print(type(myTuple))
print(type(anotherTuple))

newList = list(myTuple)
newList.append("Eryk")
newTuple = tuple(newList)
print(newTuple)

(one, *two, hey) = anotherTuple

print(one)
print(two)
print(hey)


print(anotherTuple.count(5))
