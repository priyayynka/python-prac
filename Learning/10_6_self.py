class Employee:
    company = "Google"
    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

piyu = Employee()
piyu.salary = 100000
piyu.getSalary("Thanks!")  #Employee.getSalary(piyu)
piyu.greet() #Employee.greet()

