import math


class Employee:
    def __init__(self, name, last, pay):
        self.name = name
        self.last = last
        self.pay = pay
        self.tax = 1.04

    def fullname(self):
        full_name = f"{self.name} {self.last}"
        return full_name

    def greetings(self):
        print(f"Hi {self.name} {self.last}!")

    def email_id(self):
        email = f"{self.name}{self.last}@gmail.com"
        return email

    def tax_incre(self):
        self.tax += 0.06
        return self.tax

    def ftax(self):
        a = self.pay * self.tax
        return round(a)


class Developer(Employee):
    def __init__(self, name, last, pay, language):
        super().__init__(name, last, pay)
        self.language = language

    def lang(self):
        return self.language


class manager(Employee):

    def __init__(self, name, last, pay, employees=[]):
        super().__init__(name, last, pay)
        self.employees = employees

    def add(self, x):
        if x not in self.employees:
            self.employees.append(x)
            print(f"\n{x.fullname()} added successfully\n")
        else:
            print(f"\n{x.fullname()} already exists in your company\n")

    def remove(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            print(f"\n{emp.fullname()} removed successfully\n")
        else:
            print(f"\n{emp.fullname()} does not exists in your company\n")

    def lists(self):
        for i in self.employees:
            print(f"\n--> {i.fullname()} is in your company\n")

    def clear_data(self):
        self.employees.clear()
        print("\nyour employees data have been deleted\n")


# command format :object.function(value)
# This project will soon be released as a GUI application
a = Employee("panni", "pandaram", 100000)
b = Developer("poona", "mani", 100000, "python")
c = manager("sara", "pambu", 100000)
