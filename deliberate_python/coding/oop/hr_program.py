import hr
import employees
import productivity

manager = employees.Manager(1, "John", 1500)
secretary = employees.Secretary(1, "John", 1200)
sales_guy = employees.SalesPerson(3, "Kevin", 1000, 250)
factory_worker = employees.FactoryWorker(2, "Jane", 40,15)
tempory_secretary = employees.TemporarySecretary(5, "Robin Williams", 40, 9)
# generic_employee = hr.Employee(4, "Generic Employee")
# Can't instantiate abstract class Employee with abstract methods calculate_payroll

employees = [#generic_employee,
             manager, secretary, sales_guy, factory_worker,tempory_secretary]

productivity_system = productivity.ProductivitySystem()
productivity_system.track(employees, 40)

payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll(employees)

# try

