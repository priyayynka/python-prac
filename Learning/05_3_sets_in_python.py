a = {3, 56, 78, 56, 98}

print(type(a))
print(a)

# Important: This syntax will create an empty dictionary and not an empty set
a = {}
print(type(a))

# An empty set can be created using the below syntax
b = set()
print(type(b))

# Adding values to an empty set
b.add(4)
b.add(5)
b.add(5)
b.add(5)
b.add(5) # Adding a value repeatedly does not change a set
b.add([4, 5, 6]) # List cannot be added to set cause list is not hashable
b.add((4, 5, 6))
b.add({4:5}) # Dictionary cannot be added to set cause dictionary is not hashable

# Length of the set
print(b)
print(len(b)) # Prints the length of this set

b.remove(5) # Removes the element 5 from the set
b.remove(15) # Throws an error as the element 15 is not present in the set
print(b) 

print(b.pop())