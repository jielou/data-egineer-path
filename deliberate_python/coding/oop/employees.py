#redeisgn for avoiding diamond problem

# from hr import SalaryPolicy, CommissionPolicy, HourlyPolicy
# from productivity import ManagerRole, SalesRole,SecretaryRole,FactoryRole

from productivity import get_role
from hr import get_policy
from contacts import get_employee_address
from representations import AsDictionaryMixin

class _EmployeeDatabase:
    def __init__(self):
        self._employees = {
            1: {
                "name":"mary",
                "role":"manager"
            },
            2: {
                "name":"jack",
                "role":"secretary"
            },
            3: {
                "name":"kevin",
                "role":"sales"
            },
            4: {
                "name":"jane",
                "role":"factory"
            },
            5:{
                "name":"robin",
                "role":"secretary"
            },

        }
        # self.productivity = ProductivitySystem()
        # self.payroll = PayrollSystem()
        # self.employee_addresses = AddressBook()

    def employees(self):
        return [Employee(id_) for id_ in sorted(self._employees)]

    def get_employee_info(self, employee_id):
        info = self._employees.get(employee_id)
        if not info:
            raise ValueError("invliad employee_id")
        return info

employee_database = _EmployeeDatabase()

class Employee(AsDictionaryMixin):
    def __init__(self, id):
        self.id = id
        info = employee_database.get_employee_info(self.id)
        self.name = info.get("name")
        self.address = get_employee_address(self.id)
        self._employee_role = get_role(info.get("role"))
        self._payroll_policy = get_policy(self.id)

    def work(self, hours):
        duties = self._employee_role.work(hours)
        print(f"Employee {self.id} 0 {self.name}:")
        print(f"- {duties}")
        print("")
        self._payroll_policy.track_work(hours)

    def calculate_payroll(self):
        return self._payroll_policy.calculate_payroll()

    def apply_payroll_policy(self, new_policy):
        new_policy.apply_to_policy(self._payroll_policy)
        self._payroll_policy = new_policy


# composition
# class Manager(Employee, ManagerRole, SalaryPolicy):
#     def __init__(self, id, name, weekly_salary):
#         SalaryPolicy.__init__(self, weekly_salary)
#         super().__init__(id,name)

# class Secretary(Employee, SecretaryRole, SalaryPolicy):
#     def __init__(self, id, name, weekly_salary):
#         SalaryPolicy.__init__(self, weekly_salary)
#         super().__init__(id,name)

# class SalesPerson(Employee, SalesRole, CommissionPolicy):
#     def __init__(self, id,name, weekly_salary, commission):
#         CommissionPolicy.__init__(self, weekly_salary, commission)
#         super().__init__(id,name)

# class FactoryWorker(Employee, FactoryRole, HourlyPolicy):
#     def __init__(self, id,name, hours_worked, hour_rate):
#         HourlyPolicy.__init__(self, hours_worked, hour_rate)
#         super().__init__(id,name)

# class TemporarySecretary(Employee, SecretaryRole, HourlyPolicy):
#     def __init__(self, id,name, hours_worked, hour_rate):
#         HourlyPolicy.__init__(self, hours_worked, hour_rate)
#         super().__init__(id,name)





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

