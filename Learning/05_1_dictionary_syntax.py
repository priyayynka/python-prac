myDict = {
    "Fast" : "In a Quick Manner",
    "Piyu" : "A Good Girl",
    "Marks" : [56, 89, 85],
    "anotherDict" : {'Piyu': 'Human'}
}

print(myDict['Fast'])
print(myDict['Piyu'])
myDict['Marks'] = [56, 25]
print(myDict['Marks'])
print(myDict['anotherDict']['Piyu'])