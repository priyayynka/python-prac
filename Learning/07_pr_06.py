# Factorial of entered no. using for loop

num = int(input("Enter a no.: "))
factorial = 1
for i in range(1 , num+1) :
    factorial = factorial*i
print(f"The factorial of {num} is {factorial}")