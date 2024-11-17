def percent(marks):
    p = ((marks[0] + marks[1] + marks[2] + marks[3])/400)*100
    return p

marks1 = [56, 87, 69, 90]
percentage1 = percent(marks1)

marks2 = [58, 80, 69, 34]
percentage2 = percent(marks2)

print(percentage1, percentage2)


def myNum(num1, num2):
    return num1+num2

s = myNum(8,32)
print (s)


def greet(name):
    gr = ("Hello, "+ name)
    return gr

a = greet("Piyu")
print(a)