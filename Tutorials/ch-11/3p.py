class Employee:
    salary = 100000
    increment = 10

    @property
    def salaryAfterIncrement(self):
        return (self.increment/100)*self.salary + self.salary

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary-self.salary)/self.salary)*100

e = Employee()
print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 120000
print(e.increment)