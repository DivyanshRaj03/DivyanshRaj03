class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        Person.__init__(self, name, age)
        self.employee_id = employee_id
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, dept):
        Employee.__init__(self, name, age, employee_id, salary)
        self.dept = dept

    def show_information(self):
        print(f"Manager: {self.name}")
        print(f"Age: {self.age}")
        print(f"ID: {self.employee_id}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.dept}")

manager = Manager("Divyansh", 19, "ADT25SOCB1656", 1000, "CSE")
manager.show_information()