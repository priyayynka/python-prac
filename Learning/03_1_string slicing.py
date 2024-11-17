greetings = "Good Morning, "
name = "Piyu"
# Concatenating two strings
c= (greetings + name)

print(c)

print(name[0])
print(name[3])

# name[3] = "d" --> Does not work

print(name[1:3])
print(name[:4]) #same as print(name[0:4])
print (name[1:]) #same as print(name[1:4])
print (name[-3:-1]) #same as print(name[1:3])


d= "piyuisthebest"
print(d[::3])