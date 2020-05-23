class _ProductivitySystem:
    def __init__(self):
        self._roles = {
            "manager":ManagerRole,
            "secretary":SecretaryRole,
            "sales":SalesRole,
            "factory": FactoryRole
        }

    def get_role(self, role_id):
        role_type = self._roles.get(role_id)
        if not role_type:
            raise ValueError(f"invliad role id: {role_id}")
        return role_type()


    def track(self, employees, hours):
        print("Tracking Employee Productivity")
        print("==============================")
        for employee in employees:
            employee.work(hours)
            #result = employee.work(hours)
            #print(f"{employee.name}: {result}")
        print("")

#redegisn for avoiding diamond problem
class ManagerRole:
    def work(self, hours):
        return f"screams and yells for {hours} hours"

class SecretaryRole:
    def work(self, hours):
        return f"expends for {hours} hours doing office paperwork"

class SalesRole:
    def work(self, hours):
        return f"expends for {hours} hours on the phone"

class FactoryRole:
    def work(self, hours):
        return f"manufactures gadgets for {hours} hours"

# create singelton
_producticity_system = _ProductivitySystem()

def get_role(role_id):
    return _producticity_system.get_role(role_id)

def track(employees, hours):
    _producticity_system.track(employees, hours)