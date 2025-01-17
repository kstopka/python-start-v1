# Dictionaries
print("")
band = {
    'vocals': 'Plant',
    'guitar': "Page"
}


band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

# Access items
print(band["vocals"])
print(band.get("guitar"))

# list all keys
print(band.keys())

# list all values
print(band.values())

# list of key/value pairs as tuples
print(band.items())

# verify a key exist
print("guitar" in band)
print("trinagle" in band)

# change values
band["vocals"] = "Coverdale"
print(band)
band.update({"bass": "JPJ"})
print(band)

# remove items
print(band.pop("bass"))
print(band)


band["drums"] = "Bonham"
print(band)

print(band.popitem())  # tuple
print(band)

# delete and clear
band["drums"] = "Bonham"
print(band)
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2


# copy dictionaries

# print("Bad Copy!")
# band2 = band  # create reference
# print(band2)
# print(band)

# band2['drums'] = "Damian"
# print(band)

band2 = band.copy()
band2['drums'] = "Damian"
print(band)
print(band2)

# or use the dict() constructor function
band3 = dict(band)
print("good copy!")
print(band3)

# Nested dictionaries
member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}

band = {
    "member1": member1,
    "member2": member2,
}


print(band)
print(band["member1"])
print(band["member1"]["name"])

# Sets
nums = {1, 2, 3, 4}

nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# No duplicate allowed
nums = {1, 2, 2, 3, 4}
print(nums)

# True is a dupe of 1, False is a dupe of zero
nums = {1, True, 2, False, 3, 4, 0}
print(nums)


# check if a value is in a set

print(2 in nums)

# but you cannot refer to an element in the set with an index  position or a key

# Add  a new element to a set

nums.add(8)
print(nums)

# Add elements from one set  to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# You can use update  with lists, tuples, and dictionaries too.

# Merge  two sets to create a new set

one = {1, 2, 3}
two = {7, 8, 9}

myNewSet = one.union(two)
print(myNewSet)

# Keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 5}

one.intersection_update(two)
print(one)

# Keep everything except the duplicates
one = {1, 2, 3}
two = {2, 3, 5}

one.symmetric_difference_update(two)
print(one)
