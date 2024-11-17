# Multiplication Table using For Loop

num = int(input("Enter a no."))
for i in range(1,11):
    print( str(num) + "X" + str(i) + "=" + str(i*num) )
     #print(f"{num} x {i} = {num*i}")
    
 # Multiplication Table using While Loop   

num = int(input("Enter a no. "))
i = 1
while i < 11:
    print(f"{num} x {i} = {num*i}")
    i = i + 1