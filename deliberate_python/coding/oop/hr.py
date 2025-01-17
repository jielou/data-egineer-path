
class _PayrollSystem:
    def __init__(self):
        self._employee_policies = {
            1:SalaryPolicy(3000),
            2:SalaryPolicy(1500),
            3:CommissionPolicy(1000,100),
            4:HourlyPolicy(15),
            5:HourlyPolicy(9)
        }

    def get_policy(self, emmployee_id):
        policy = self._employee_policies.get(emmployee_id)
        if not policy:
            raise ValueError("invliad role id")
        return policy

    def calculate_payroll(self, employees):
        print("calculating payroll")
        print("==================")
        for employee in employees:
            print(f"Payroll for: {employee.id}- {employee.name}")
            print(f"- Check Amount: {employee.calculate_payroll()}")
            if employee.address:
                print('Sent to: ')
                print(employee.address)
            print("")

class LTDPolicy:
    def __init__(self):
        self._base_policy = None
    
    def track_work(self, hours):
        self._check_base_policy()
        return self._base_policy.track_work(hours)

    def calculate_payroll(self):
        self._check_base_policy()
        base_salary = self._base_policy.calculate_payroll()
        return base_salary*0.6

    def apply_to_policy(self, base_policy):
        self._base_policy = base_policy

    def _check_base_policy(self):
        if not self._base_policy:
            raise RuntimeError("Base policy missing")




class PayrollPolicy:
    def __init__(self):
        self.hour_worked = 0
    
    def track_work(self, hours):
        self.hour_worked += hours

class SalaryPolicy(PayrollPolicy):
    def __init__(self, weekly_salary):
        super().__init__()
        self.weekly_salary = weekly_salary
    
    def calculate_payroll(self):
        return self.weekly_salary
    
class HourlyPolicy(PayrollPolicy):
    def __init__(self, hour_rate):
        super().__init__()
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hour_rate * self.hour_worked

class CommissionPolicy(SalaryPolicy):
    def __init__(self, weekly_salary, commission_per_sale):
        super().__init__( weekly_salary)
        self.commission_per_sale = commission_per_sale

    def commission(self):
        sales = self.hour_worked / 5
        return sales * self.commission_per_sale

    def calculate_payroll(self):
        return super().calculate_payroll()+self.commission()

_payroll_system = _PayrollSystem()

def get_policy(employee_id):
    return _payroll_system.get_policy(employee_id)

def calculate_payroll(employees):
    _payroll_system.calculate_payroll(employees)

