
class PayrollSystem:
    def calculate_payroll(self, employees):
        print("calculating payroll")
        print("==================")
        for employee in employees:
            print(f"Payroll for: {employee.id}- {employee.name}")
            print(f"- Check Amount: {employee.calculate_payroll()}")
            print("")

class SalaryPolicy:
    def __init__(self, weekly_salary):
        self.weekly_salary = weekly_salary
    
    def calculate_payroll(self):
        return self.weekly_salary
    
class HourlyPolicy:
    def __init__(self, hours_worked, hour_rate):
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hour_rate * self.hours_worked

class CommissionPolicy(SalaryPolicy):
    def __init__(self, weekly_salary, commission):
        super().__init__( weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        return super().calculate_payroll()+self.commission


