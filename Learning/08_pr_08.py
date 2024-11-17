# Multiplication table using function

def table(num):
    for i in range(1,11):
     output = print(f"{num} x {i} = {num*i}")
    return output

s = table(8)
print (s)