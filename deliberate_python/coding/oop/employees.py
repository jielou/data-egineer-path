#redeisgn for avoiding diamond problem

from hr import SalaryPolicy, CommissionPolicy, HourlyPolicy
from productivity import ManagerRole, SalesRole,SecretaryRole,FactoryRole

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Manager(Employee, ManagerRole, SalaryPolicy):
    def __init__(self, id, name, weekly_salary):
        SalaryPolicy.__init__(self, weekly_salary)
        super().__init__(id,name)

class Secretary(Employee, SecretaryRole, SalaryPolicy):
    def __init__(self, id, name, weekly_salary):
        SalaryPolicy.__init__(self, weekly_salary)
        super().__init__(id,name)

class SalesPerson(Employee, SalesRole, CommissionPolicy):
    def __init__(self, id,name, weekly_salary, commission):
        CommissionPolicy.__init__(self, weekly_salary, commission)
        super().__init__(id,name)

class FactoryWorker(Employee, FactoryRole, HourlyPolicy):
    def __init__(self, id,name, hours_worked, hour_rate):
        HourlyPolicy.__init__(self, hours_worked, hour_rate)
        super().__init__(id,name)

class TemporarySecretary(Employee, SecretaryRole, HourlyPolicy):
    def __init__(self, id,name, hours_worked, hour_rate):
        HourlyPolicy.__init__(self, hours_worked, hour_rate)
        super().__init__(id,name)





# from abc import ABC, abstractmethod


# class Employee(ABC):
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
    
#     @abstractmethod
#     def calculate_payroll(self):
#         pass

# class SalaryEmployee(Employee):
#     def __init__(self, id, name, weekly_salary):
#         super().__init__(id, name)
#         self.weekly_salary = weekly_salary

#     def calculate_payroll(self):
#         return self.weekly_salary

# class HourlyEmployee(Employee):
#     def __init__(self, id, name, hours_worked, hour_rate):
#         super().__init__(id, name)
#         self.hours_worked = hours_worked
#         self.hour_rate = hour_rate

#     def calculate_payroll(self):
#         return self.hour_rate * self.hours_worked

# class ComissionEmployee(SalaryEmployee):
#     def __init__(self, id, name, weekly_salary, commission):
#         super().__init__(id, name, weekly_salary)
#         self.commission = commission

#     def calculate_payroll(self):
#         return super().calculate_payroll()+self.commission

# class Manager(SalaryEmployee):
#     def work(self, hours):
#         print()

# class Secretary(SalaryEmployee):
#     def work(self, hours):
#         print()

# class SalesPerson(ComissionEmployee):
#     def work(self, hours):
#         print(f"{self.name} expends for {hours} hours on the phone")

# class FactoryWorker(HourlyEmployee):
#     def work(self, hours):
#         print(f"{self.name} manufactures gadgets for {hours} hours")

# class TemporarySecretary(Secretary, HourlyEmployee):
#     # templorary secretary is secretary but works at hourly base
#     def __init__(self, id, name, hours_worked, hour_rate):
#         HourlyEmployee.__init__(self, id, name, hours_worked, hour_rate)

#     def calculate_payroll(self):
#         return HourlyEmployee.calculate_payroll(self)
#     #hourly


# print(TemporarySecretary.__mro__)

