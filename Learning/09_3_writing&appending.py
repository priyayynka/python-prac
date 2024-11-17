#f = open('another.txt','w')
#f.write("Hello, how are you?")
#f.write("Hello, how are you?")
#f.write("Hello, how are you?") #can be written as many times as needed
#f.close()

f = open('another.txt','a')
f.write("appending currently")
f.close() # will keep on adding to the file as many times the program is run