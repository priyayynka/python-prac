mydict = {
    "fast" : "in a quick manner",
    "piyu" : "a good girl",
    "marks" : [56, 89, 85],
    "anotherdict" : {'piyu': 'human'},
    1: 2
}

# Dictionary Methods
print(list(mydict.keys())) # Prints the keys of the dictionary
print(list(mydict.values())) # Prints the values of the dictionary
print(mydict.items()) # Prints the (key, value) for all the contents of the dictionary
print(mydict)
updatedict = {
     "Damon" : "LOML",
     "Stefan" : "cutiee",
     "Klaus" : "awwww",
     "Tyler" : "hottie",
     "Piyu" : "A Damon lover"
}
mydict.update(updatedict) # Updates the dictionary by adding key-value pairs from updatedict
print(mydict)

print(mydict.get("Piyu")) # Prints value associated with key "Piyu"
print(mydict["Piyu"]) # Prints value associated with key "Piyu"

# The difference between .get and [] syntax in Dictionaries
print(mydict.get("Piyu2")) # throws None as Piyu2 is not present in the dictionary
print(mydict["Piyu2"]) # throws an error as Piyu2 is not present in the dictionary
