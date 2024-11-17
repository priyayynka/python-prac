def summation(n):
    if n==1:
        return 1
    elif n==0:
        return 0
        
    return n + summation(n-1)


f=summation(7)
print(f)

