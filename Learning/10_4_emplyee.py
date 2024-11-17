class Employee:
    company = "Google"
    

piyu = Employee()
priya = Employee()
piyu.salary = 300
priya.salary = 400

print(piyu.company)
print(priya.company)
Employee.company = "YouTube"
print(piyu.company)
print(priya.company)
print(piyu.salary)
print(priya.salary)