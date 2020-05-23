# import hr
# import employees
# import productivity
# import contacts

# further improvement

import json
from hr import calculate_payroll, LTDPolicy
from productivity import track
from employees import employee_database, Employee

# modify behavior in the runtime
employees = employee_database.employees()
sales_employee = employees[2]
ltd_policy = LTDPolicy()
sales_employee.apply_payroll_policy(ltd_policy)




# def print_dict(d):
#     print(json.dumps(d, indent=2))

# employees = employee_database.employees()

# track(employees, 40)
# calculate_payroll(employees)

# temp_secretary = Employee(5)
# print("temporary secretary:")
# print_dict(temp_secretary.to_dict())




# use mixin
# import json
# from employees import EmployeeDatabase

# def print_dict(d):
#     print(json.dumps(d, indent=2))

# for employee in EmployeeDatabase().employees():
#     print(employee.to_dict())


# flexible composition: policy based degisn
# from hr import PayrollSystem, HourlyPolicy
# from productivity import ProductivitySystem
# from employees import EmployeeDatabase


# productivity_system = ProductivitySystem()
# payroll_system = PayrollSystem()
# employee_database = EmployeeDatabase()
# employees = employee_database.employees()
# ## penalty for managers
# manager = employees[0]
# manager.payroll_policy = HourlyPolicy(55)

# productivity_system.track(employees, 40)
# payroll_system.calculate_payroll(employees)




# manager = employees.Manager(1, "John", 1500)
# manager.address = contacts.Address("121 Admin Road", "concord", "NH", "03301")
# secretary = employees.Secretary(1, "John", 1200)
# sales_guy = employees.SalesPerson(3, "Kevin", 1000, 250)
# factory_worker = employees.FactoryWorker(2, "Jane", 40,15)
# tempory_secretary = employees.TemporarySecretary(5, "Robin Williams", 40, 9)
# # generic_employee = hr.Employee(4, "Generic Employee")
# # Can't instantiate abstract class Employee with abstract methods calculate_payroll

# employees = [#generic_employee,
#              manager, secretary, sales_guy, factory_worker,tempory_secretary]

# productivity_system = productivity.ProductivitySystem()
# productivity_system.track(employees, 40)

# payroll_system = hr.PayrollSystem()
# payroll_system.calculate_payroll(employees)

# # try

