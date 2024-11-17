mydict = {
    "Pankha" : "Fan",
    "Dabba" : "Box",
    "Vastu" : "Item"
}
print("Options are", mydict.keys())
a = input("Enter the Hindi Word\n")
#print("The meaning of your word is: ", mydict[a])

# Below line will not throw an error if the key value given is not present in the dictionary
print("The meaning of your word is: ", mydict.get(a))